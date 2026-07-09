from flask import Blueprint, render_template, request, jsonify, session, current_app, redirect
import json

tienda_bp = Blueprint('tienda', __name__, template_folder='../../templates/tienda',
                      static_folder='../../static', static_url_path='/static')

@tienda_bp.route('/')
def index():
    db = current_app.config['get_db']()
    productos = db.execute("""SELECT p.*, d.nombre as division_nombre
                              FROM productos p JOIN divisiones d ON p.division_id = d.id
                              WHERE p.activo=1 ORDER BY p.division_id, p.titulo""").fetchall()
    db.close()
    return render_template('tienda/index.html', productos=productos)

@tienda_bp.route('/producto/<int:pid>')
def producto(pid):
    db = current_app.config['get_db']()
    p = db.execute("""SELECT p.*, d.nombre as division_nombre
                      FROM productos p JOIN divisiones d ON p.division_id = d.id
                      WHERE p.id=? AND p.activo=1""", (pid,)).fetchone()
    relacionados = db.execute("""SELECT * FROM productos WHERE division_id=? AND id!=? AND activo=1
                                 LIMIT 4""", (p['division_id'], pid)).fetchall() if p else []
    db.close()
    if not p:
        return redirect('/tienda')
    return render_template('tienda/producto.html', producto=p, relacionados=relacionados)

@tienda_bp.route('/api/carrito', methods=['GET','POST','PUT','DELETE'])
def api_carrito():
    carrito = session.get('carrito', [])
    db = current_app.config['get_db']()
    MAPA_FORMATOS = {'fisico':'precio_fisico','pdf':'precio_pdf','audio':'precio_audio','video':'precio_video','premium':'precio_premium'}
    if request.method == 'GET':
        total = 0
        for item in carrito:
            p = db.execute("SELECT * FROM productos WHERE id=?", (item['id'],)).fetchone()
            if p:
                col = MAPA_FORMATOS.get(item.get('formato', 'fisico'), 'precio_fisico')
                item['titulo'] = p['titulo']
                item['precio'] = p[col] or p['precio_fisico']
                item['subtotal'] = item['precio'] * item['cantidad']
                total += item['subtotal']
        envio = 0 if total >= current_app.config.get('ENVIO_GRATIS_DESDE', 500) else current_app.config.get('ENVIO_COSTO', 99)
        db.close()
        return jsonify(items=carrito, total=total, envio=envio, gran_total=total+envio)
    elif request.method == 'POST':
        data = request.get_json()
        libro_id = data.get('id')
        p = db.execute("SELECT * FROM productos WHERE id=? AND activo=1", (libro_id,)).fetchone()
        if p and p['url_afiliado']:
            db.close()
            return jsonify(error="Producto de afiliado. Compra directa en Amazon.", afiliado=True, url=p['url_afiliado']), 400
        formato = data.get('formato', 'fisico')
        cantidad = int(data.get('cantidad', 1))
        exists = next((c for c in carrito if c['id'] == libro_id and c.get('formato') == formato), None)
        if exists:
            exists['cantidad'] += cantidad
        else:
            carrito.append({'id': libro_id, 'formato': formato, 'cantidad': cantidad})
        session['carrito'] = carrito
        session.modified = True
        db.close()
        return jsonify(carrito=carrito, count=sum(c['cantidad'] for c in carrito))
    elif request.method == 'PUT':
        data = request.get_json()
        for item in carrito:
            if item['id'] == data.get('id'):
                item['cantidad'] = int(data.get('cantidad', 1))
                break
        session['carrito'] = carrito
        session.modified = True
        db.close()
        return jsonify(carrito=carrito)
    elif request.method == 'DELETE':
        data = request.get_json()
        lid = data.get('id') if data else None
        if lid:
            carrito = [c for c in carrito if c['id'] != lid]
        else:
            carrito = []
        session['carrito'] = carrito
        session.modified = True
        db.close()
        return jsonify(carrito=carrito)

@tienda_bp.route('/checkout')
def checkout():
    if not session.get('carrito'):
        return "Carrito vacío", 302
    return render_template('tienda/checkout.html')

@tienda_bp.route('/api/pedido', methods=['POST'])
def crear_pedido():
    data = request.get_json()
    carrito = session.get('carrito', [])
    if not carrito:
        return jsonify(error="Carrito vacío"), 400
    db = current_app.config['get_db']()
    MAPA_FORMATOS = {'fisico':'precio_fisico','pdf':'precio_pdf','audio':'precio_audio','video':'precio_video','premium':'precio_premium'}
    total = 0
    items = []
    for item in carrito:
        p = db.execute("SELECT * FROM productos WHERE id=?", (item['id'],)).fetchone()
        if p:
            col = MAPA_FORMATOS.get(item.get('formato', 'fisico'), 'precio_fisico')
            precio = p[col] or p['precio_fisico']
            subtotal = precio * item['cantidad']
            total += subtotal
            items.append({'id': p['id'], 'titulo': p['titulo'], 'formato': item.get('formato', 'fisico'), 'precio': precio, 'cantidad': item['cantidad'], 'subtotal': subtotal})
    envio = 0 if total >= current_app.config.get('ENVIO_GRATIS_DESDE', 500) else current_app.config.get('ENVIO_COSTO', 99)
    gran_total = total + envio
    db.execute("""INSERT INTO pedidos (cliente_nombre, cliente_email, cliente_telefono, direccion, ciudad, estado, cp,
                  items_json, subtotal, envio, total, metodo_pago, estatus)
                  VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
               (data['nombre'], data['email'], data.get('telefono',''), data.get('direccion',''),
                data.get('ciudad',''), data.get('estado',''), data.get('cp',''),
                json.dumps(items), total, envio, gran_total, data.get('metodo_pago','transferencia'), 'pendiente'))
    pid = db.execute("SELECT last_insert_rowid()").fetchone()[0]
    db.commit()
    db.close()
    session['carrito'] = []
    session.modified = True
    return jsonify(mensaje="Pedido creado", pedido_id=pid)

@tienda_bp.route('/gracias/<int:pid>')
def gracias(pid):
    db = current_app.config['get_db']()
    pedido = db.execute("SELECT * FROM pedidos WHERE id=?", (pid,)).fetchone()
    db.close()
    if not pedido:
        return "Pedido no encontrado", 404
    return render_template('tienda/gracias.html', pedido=pedido)
