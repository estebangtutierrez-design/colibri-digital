from flask import Blueprint, render_template, request, jsonify, current_app

femenino_bp = Blueprint('femenino', __name__, template_folder='../../templates/femenino',
                        static_folder='../../static', static_url_path='/static')

@femenino_bp.route('/')
def index():
    db = current_app.config['get_db']()
    productos = db.execute("""SELECT * FROM productos WHERE division_id='femenino'
                              AND activo=1 ORDER BY categoria, titulo LIMIT 12""").fetchall()
    db.close()
    return render_template('femenino/index.html', productos=productos)

@femenino_bp.route('/tienda')
def tienda():
    db = current_app.config['get_db']()
    categorias = db.execute("""SELECT DISTINCT categoria FROM productos
                               WHERE division_id='femenino' AND activo=1""").fetchall()
    productos = db.execute("""SELECT * FROM productos WHERE division_id='femenino'
                              AND activo=1 ORDER BY categoria, titulo""").fetchall()
    db.close()
    return render_template('femenino/tienda.html', productos=productos, categorias=[c['categoria'] for c in categorias])

@femenino_bp.route('/capturar-email', methods=['POST'])
def capturar_email():
    data = request.get_json()
    db = current_app.config['get_db']()
    db.execute("INSERT OR IGNORE INTO capturas_email (email, nombre, origen, interes) VALUES (?,?,?,?)",
               (data.get('email'), data.get('nombre', ''), 'femenino', data.get('interes', '')))
    db.commit()
    db.close()
    return jsonify(mensaje="¡Bienvenida! Recibirás contenido femenino exclusivo.")
