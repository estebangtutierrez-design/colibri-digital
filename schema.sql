CREATE TABLE IF NOT EXISTS divisiones (
    id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    subtitulo TEXT DEFAULT '',
    activa INTEGER DEFAULT 1
);

INSERT OR IGNORE INTO divisiones VALUES ('holding','Colibrí Digital','La Biblioteca Digital de América Latina',1);
INSERT OR IGNORE INTO divisiones VALUES ('academia','Lucas EGA Academy','Tecnología e Inteligencia Artificial',1);
INSERT OR IGNORE INTO divisiones VALUES ('legado','Legado Ancestral','Historia y Cultura de México',1);
INSERT OR IGNORE INTO divisiones VALUES ('historias','Historias de México','Leyendas, Misterios y Tradiciones',1);
INSERT OR IGNORE INTO divisiones VALUES ('esoterico','Mundo Esotérico','Espiritualidad y Bienestar',1);
INSERT OR IGNORE INTO divisiones VALUES ('infantil','Mundo Infantil','Juguetes, Ropa y Libros para Niños',1);
INSERT OR IGNORE INTO divisiones VALUES ('femenino','Mundo Femenino','Ropa, Cosméticos y Belleza para Mujer',1);
INSERT OR IGNORE INTO divisiones VALUES ('masculino','Mundo Masculino','Alto Rendimiento para el Hombre',1);

CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    token TEXT DEFAULT '',
    division_origen TEXT DEFAULT 'holding',
    suscripcion TEXT DEFAULT 'gratis',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (division_origen) REFERENCES divisiones(id)
);

CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT UNIQUE NOT NULL,
    titulo TEXT NOT NULL,
    descripcion TEXT DEFAULT '',
    division_id TEXT NOT NULL,
    categoria TEXT DEFAULT '',
    precio_fisico INTEGER DEFAULT 0,
    precio_pdf INTEGER DEFAULT 0,
    precio_audio INTEGER DEFAULT 0,
    precio_video INTEGER DEFAULT 0,
    precio_premium INTEGER DEFAULT 0,
    portada TEXT DEFAULT '',
    autor TEXT DEFAULT 'Colibrí Digital',
    activo INTEGER DEFAULT 1,
    url_afiliado TEXT DEFAULT '',
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (division_id) REFERENCES divisiones(id)
);

CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    cliente_nombre TEXT NOT NULL,
    cliente_email TEXT NOT NULL,
    cliente_telefono TEXT DEFAULT '',
    direccion TEXT DEFAULT '',
    ciudad TEXT DEFAULT '',
    estado TEXT DEFAULT '',
    cp TEXT DEFAULT '',
    items_json TEXT DEFAULT '[]',
    subtotal INTEGER DEFAULT 0,
    envio INTEGER DEFAULT 0,
    total INTEGER DEFAULT 0,
    formato TEXT DEFAULT 'fisico',
    metodo_pago TEXT DEFAULT 'transferencia',
    estatus TEXT DEFAULT 'pendiente',
    stripe_payment_id TEXT DEFAULT '',
    notas TEXT DEFAULT '',
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_pago TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE IF NOT EXISTS capturas_email (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    nombre TEXT DEFAULT '',
    origen TEXT DEFAULT 'holding',
    interes TEXT DEFAULT '',
    libro_gratis TEXT DEFAULT '',
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS admin_usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    rol TEXT DEFAULT 'admin',
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contenidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    division_id TEXT NOT NULL,
    tipo TEXT DEFAULT 'articulo',
    titulo TEXT NOT NULL,
    resumen TEXT DEFAULT '',
    contenido_texto TEXT DEFAULT '',
    contenido_html TEXT DEFAULT '',
    audio_url TEXT DEFAULT '',
    video_url TEXT DEFAULT '',
    autor TEXT DEFAULT '',
    etiquetas TEXT DEFAULT '',
    gratuito INTEGER DEFAULT 0,
    destacado INTEGER DEFAULT 0,
    fecha_publicacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (division_id) REFERENCES divisiones(id)
);

CREATE TABLE IF NOT EXISTS colecciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT DEFAULT '',
    division_id TEXT NOT NULL,
    productos_ids TEXT DEFAULT '',
    precio_coleccion INTEGER DEFAULT 0,
    portada TEXT DEFAULT '',
    activo INTEGER DEFAULT 1,
    FOREIGN KEY (division_id) REFERENCES divisiones(id)
);

CREATE TABLE IF NOT EXISTS progreso (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    curso_id TEXT NOT NULL,
    capitulo INTEGER DEFAULT 0,
    total INTEGER DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    UNIQUE(usuario_id, curso_id)
);

-- Admin user created by init_db()
