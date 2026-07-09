from flask import Blueprint, render_template, request, jsonify, current_app

esoterico_bp = Blueprint('esoterico', __name__, template_folder='../../templates/esoterico',
                         static_folder='../../static', static_url_path='/static')

@esoterico_bp.route('/')
def index():
    return render_template('esoterico/index.html')

@esoterico_bp.route('/tienda')
def tienda():
    db = current_app.config['get_db']()
    productos = db.execute("""SELECT * FROM productos WHERE division_id='esoterico'
                              AND activo=1 ORDER BY categoria, titulo""").fetchall()
    db.close()
    return render_template('esoterico/tienda.html', productos=productos)

@esoterico_bp.route('/capturar-email', methods=['POST'])
def capturar_email():
    data = request.get_json()
    db = current_app.config['get_db']()
    db.execute("INSERT OR IGNORE INTO capturas_email (email, nombre, origen, interes) VALUES (?,?,?,?)",
               (data.get('email'), data.get('nombre', ''), 'esoterico', data.get('interes', '')))
    db.commit()
    db.close()
    return jsonify(mensaje="Recibirás contenido espiritual exclusivo.")
