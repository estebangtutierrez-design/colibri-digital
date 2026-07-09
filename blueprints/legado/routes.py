from flask import Blueprint, render_template, request, jsonify, current_app

legado_bp = Blueprint('legado', __name__, template_folder='../../templates/legado',
                      static_folder='../../static', static_url_path='/static')

@legado_bp.route('/')
def index():
    return render_template('legado/index.html')

@legado_bp.route('/biblioteca')
def biblioteca():
    db = current_app.config['get_db']()
    libros = db.execute("""SELECT * FROM productos WHERE division_id='legado'
                           AND activo=1 ORDER BY titulo""").fetchall()
    contenidos = db.execute("""SELECT * FROM contenidos WHERE division_id='legado'
                               AND gratuito=1 ORDER BY fecha_publicacion DESC LIMIT 10""").fetchall()
    db.close()
    return render_template('legado/biblioteca.html', libros=libros, contenidos=contenidos)

@legado_bp.route('/capturar-email', methods=['POST'])
def capturar_email():
    data = request.get_json()
    db = current_app.config['get_db']()
    db.execute("INSERT OR IGNORE INTO capturas_email (email, nombre, origen, interes) VALUES (?,?,?,?)",
               (data.get('email'), data.get('nombre', ''), 'legado', data.get('interes', '')))
    db.commit()
    db.close()
    return jsonify(mensaje="Recibirás nuestra guía gratuita de plantas medicinales.")
