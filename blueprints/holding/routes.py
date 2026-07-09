from flask import Blueprint, render_template, request, jsonify, current_app, session, redirect, url_for
from werkzeug.security import check_password_hash
from functools import wraps

holding_bp = Blueprint('holding', __name__, template_folder='../../templates/holding',
                       static_folder='../../static', static_url_path='/static')

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('admin_id'):
            return redirect(url_for('holding.admin_login'))
        return f(*args, **kwargs)
    return decorated

@holding_bp.route('/')
def index():
    return render_template('holding/index.html')

@holding_bp.route('/biblioteca')
def biblioteca():
    db = current_app.config['get_db']()
    contenidos = db.execute("""
        SELECT c.*, d.nombre as division_nombre
        FROM contenidos c JOIN divisiones d ON c.division_id = d.id
        WHERE c.gratuito=1 ORDER BY c.fecha_publicacion DESC LIMIT 20
    """).fetchall()
    productos = db.execute("""
        SELECT p.*, d.nombre as division_nombre
        FROM productos p JOIN divisiones d ON p.division_id = d.id
        WHERE p.activo=1 ORDER BY p.created DESC LIMIT 12
    """).fetchall()
    db.close()
    return render_template('holding/biblioteca.html', contenidos=contenidos, productos=productos)

@holding_bp.route('/capturar-email', methods=['POST'])
def capturar_email():
    data = request.get_json()
    db = current_app.config['get_db']()
    db.execute("INSERT OR IGNORE INTO capturas_email (email, nombre, origen, interes) VALUES (?,?,?,?)",
               (data.get('email'), data.get('nombre', ''), data.get('origen', 'holding'), data.get('interes', '')))
    db.commit()
    db.close()
    return jsonify(mensaje="¡Gracias! Te enviaremos contenido exclusivo.")

@holding_bp.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        data = request.form
        db = current_app.config['get_db']()
        admin = db.execute("SELECT * FROM admin_usuarios WHERE email=?", (data.get('email'),)).fetchone()
        db.close()
        if admin and check_password_hash(admin['password_hash'], data.get('password', '')):
            session['admin_id'] = admin['id']
            session['admin_rol'] = admin['rol']
            return redirect(url_for('holding.dashboard'))
        return render_template('admin/login.html', error="Credenciales inválidas")
    return render_template('admin/login.html')

@holding_bp.route('/admin/logout')
def admin_logout():
    session.pop('admin_id', None)
    session.pop('admin_rol', None)
    return redirect(url_for('holding.admin_login'))

@holding_bp.route('/admin/dashboard')
@admin_required
def dashboard():
    db = current_app.config['get_db']()
    stats = {
        'visitantes': db.execute("SELECT COUNT(*) FROM capturas_email").fetchone()[0],
        'pedidos': db.execute("SELECT COUNT(*) FROM pedidos").fetchone()[0],
        'ingresos': db.execute("SELECT COALESCE(SUM(total),0) FROM pedidos WHERE estatus IN ('confirmado','enviado','entregado')").fetchone()[0],
        'productos': db.execute("SELECT COUNT(*) FROM productos WHERE activo=1").fetchone()[0],
        'por_division': {}
    }
    for div in ['academia','legado','historias','esoterico']:
        stats['por_division'][div] = {
            'productos': db.execute("SELECT COUNT(*) FROM productos WHERE division_id=? AND activo=1", (div,)).fetchone()[0],
            'pedidos': 0
        }
    pedidos = db.execute("""SELECT * FROM pedidos ORDER BY fecha DESC LIMIT 20""").fetchall()
    db.close()
    return render_template('admin/dashboard.html', stats=stats, pedidos=pedidos)

@holding_bp.route('/leer/<int:cid>')
def leer_contenido(cid):
    db = current_app.config['get_db']()
    c = db.execute("SELECT c.*, d.nombre as division_nombre FROM contenidos c JOIN divisiones d ON c.division_id = d.id WHERE c.id=? AND c.gratuito=1", (cid,)).fetchone()
    db.close()
    if not c:
        return redirect(url_for('holding.biblioteca'))
    return render_template('holding/leer.html', contenido=c)


@holding_bp.route('/api/divisiones')
def api_divisiones():
    db = current_app.config['get_db']()
    rows = db.execute("SELECT * FROM divisiones WHERE activa=1").fetchall()
    db.close()
    return jsonify([dict(r) for r in rows])
