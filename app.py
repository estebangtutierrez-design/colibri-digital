from flask import Flask, g, session
from werkzeug.security import generate_password_hash
import sqlite3, os, json

from config import BASE, DB, SECRET_KEY, DIVISIONES

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
    init_db()
    app.config['DIVISIONES'] = DIVISIONES
    app.config['DB'] = DB

    app.jinja_env.filters['from_json'] = lambda x: json.loads(x) if isinstance(x, str) else (x or [])

    from blueprints.holding.routes import holding_bp
    from blueprints.academia.routes import academia_bp
    from blueprints.legado.routes import legado_bp
    from blueprints.historias.routes import historias_bp
    from blueprints.esoterico.routes import esoterico_bp
    from blueprints.holding.routes import holding_bp
    from blueprints.academia.routes import academia_bp
    from blueprints.legado.routes import legado_bp
    from blueprints.historias.routes import historias_bp
    from blueprints.esoterico.routes import esoterico_bp
    from blueprints.infantil.routes import infantil_bp
    from blueprints.femenino.routes import femenino_bp
    from blueprints.masculino.routes import masculino_bp
    from blueprints.tienda.routes import tienda_bp
    from blueprints.api.routes import api_bp

    app.register_blueprint(holding_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(academia_bp, url_prefix='/academia')
    app.register_blueprint(legado_bp, url_prefix='/legado')
    app.register_blueprint(historias_bp, url_prefix='/historias')
    app.register_blueprint(esoterico_bp, url_prefix='/esoterico')
    app.register_blueprint(infantil_bp, url_prefix='/infantil')
    app.register_blueprint(femenino_bp, url_prefix='/femenino')
    app.register_blueprint(masculino_bp, url_prefix='/masculino')
    app.register_blueprint(tienda_bp, url_prefix='/tienda')

    def get_db():
        conn = sqlite3.connect(DB)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA foreign_keys=ON")
        return conn

    app.config['get_db'] = get_db

    @app.context_processor
    def inject_globals():
        carrito = session.get('carrito', [])
        count = sum(c.get('cantidad', 1) for c in carrito) if carrito else 0
        return dict(
            divs=DIVISIONES,
            moneda_sym='$',
            carrito_count=count
        )

    @app.teardown_appcontext
    def close_db(exception):
        if hasattr(g, 'db'):
            g.db.close()

    return app

def init_db():
    from werkzeug.security import generate_password_hash
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA journal_mode=WAL")
    schema_path = os.path.join(BASE, 'schema.sql')
    if os.path.exists(schema_path):
        with open(schema_path) as f:
            conn.executescript(f.read())
    admin = conn.execute("SELECT id FROM admin_usuarios WHERE email='admin@colibri.mx'").fetchone()
    if not admin:
        conn.execute("INSERT INTO admin_usuarios (email, password_hash, rol) VALUES (?,?,?)",
                     ('admin@colibri.mx', generate_password_hash('admin123'), 'superadmin'))
    # Add token column if upgrading old DB
    try:
        conn.execute("ALTER TABLE usuarios ADD COLUMN token TEXT DEFAULT ''")
    except:
        pass

    for sfile in ['seed_productos.sql', 'seed_data.sql']:
        spath = os.path.join(BASE, sfile)
        if os.path.exists(spath):
            with open(spath) as f:
                conn.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
