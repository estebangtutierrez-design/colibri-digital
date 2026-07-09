from flask import Blueprint, render_template, request, jsonify, current_app

infantil_bp = Blueprint('infantil', __name__, template_folder='../../templates/infantil',
                        static_folder='../../static', static_url_path='/static')

@infantil_bp.route('/')
def index():
    db = current_app.config['get_db']()
    productos = db.execute("""SELECT * FROM productos WHERE division_id='infantil'
                              AND activo=1 ORDER BY categoria, titulo LIMIT 12""").fetchall()
    db.close()
    return render_template('infantil/index.html', productos=productos)

@infantil_bp.route('/tienda')
def tienda():
    db = current_app.config['get_db']()
    categorias = db.execute("""SELECT DISTINCT categoria FROM productos
                               WHERE division_id='infantil' AND activo=1""").fetchall()
    productos = db.execute("""SELECT * FROM productos WHERE division_id='infantil'
                              AND activo=1 ORDER BY categoria, titulo""").fetchall()
    db.close()
    return render_template('infantil/tienda.html', productos=productos, categorias=[c['categoria'] for c in categorias])

@infantil_bp.route('/capturar-email', methods=['POST'])
def capturar_email():
    data = request.get_json()
    db = current_app.config['get_db']()
    db.execute("INSERT OR IGNORE INTO capturas_email (email, nombre, origen, interes) VALUES (?,?,?,?)",
               (data.get('email'), data.get('nombre', ''), 'infantil', data.get('interes', '')))
    db.commit()
    db.close()
    return jsonify(mensaje="¡Bienvenido! Recibirás contenido infantil exclusivo.")
