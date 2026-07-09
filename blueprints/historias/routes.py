from flask import Blueprint, render_template, request, jsonify, current_app

historias_bp = Blueprint('historias', __name__, template_folder='../../templates/historias',
                         static_folder='../../static', static_url_path='/static')

@historias_bp.route('/')
def index():
    return render_template('historias/index.html')

@historias_bp.route('/leyendas')
def leyendas():
    db = current_app.config['get_db']()
    contenidos = db.execute("""SELECT * FROM contenidos WHERE division_id='historias'
                               AND gratuito=1 ORDER BY fecha_publicacion DESC LIMIT 20""").fetchall()
    db.close()
    return render_template('historias/leyendas.html', contenidos=contenidos)

@historias_bp.route('/biblioteca')
def biblioteca():
    db = current_app.config['get_db']()
    libros = db.execute("""SELECT * FROM productos WHERE division_id='historias'
                           AND activo=1 ORDER BY titulo""").fetchall()
    db.close()
    return render_template('historias/biblioteca.html', libros=libros)
