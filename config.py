import os

BASE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE, 'db', 'colibri.db')
SECRET_KEY = os.environ.get('COLIBRI_SECRET', 'colibri-ecosystem-dev-key')
STRIPE_KEY = os.environ.get('STRIPE_SECRET_KEY', '')

MONEDA = 'MXN'
MONEDA_SYM = '$'
ENVIO_GRATIS_DESDE = 500
ENVIO_COSTO = 99

ADMIN_EMAIL = 'admin@colibri.mx'
ADMIN_PASS = 'admin123'

DIVISIONES = {
    'holding': {
        'nombre': 'Colibrí Digital',
        'subtitulo': 'La Biblioteca Digital de América Latina',
        'lema': 'Todos los caminos llevan a Colibrí',
        'color_primario': '#1a1a2e',
        'color_secundario': '#d4a574',
        'color_fondo': '#f8f6f3',
        'emoji': '📚',
        'url': '/'
    },
    'academia': {
        'nombre': 'Lucas EGA Academy',
        'subtitulo': 'Tecnología e Inteligencia Artificial',
        'lema': 'Aprende. Construye. Innova.',
        'color_primario': '#0d1117',
        'color_secundario': '#f0883e',
        'color_fondo': '#161b22',
        'emoji': '💻',
        'url': '/academia'
    },
    'legado': {
        'nombre': 'Legado Ancestral',
        'subtitulo': 'Historia y Cultura de México',
        'lema': 'La memoria de nuestros pueblos',
        'color_primario': '#2d1810',
        'color_secundario': '#c4956a',
        'color_fondo': '#f5efe8',
        'emoji': '🌿',
        'url': '/legado'
    },
    'historias': {
        'nombre': 'Historias de México',
        'subtitulo': 'Leyendas, Misterios y Tradiciones',
        'lema': 'Donde el misterio cobra vida',
        'color_primario': '#0a0a0a',
        'color_secundario': '#8b0000',
        'color_fondo': '#1a1a1a',
        'emoji': '🌙',
        'url': '/historias'
    },
    'esoterico': {
        'nombre': 'Mundo Esotérico',
        'subtitulo': 'Espiritualidad y Bienestar',
        'lema': 'Conecta con tu esencia',
        'color_primario': '#1a0a2e',
        'color_secundario': '#9b59b6',
        'color_fondo': '#f8f4fc',
        'emoji': '🔮',
        'url': '/esoterico'
    },
    'infantil': {
        'nombre': 'Mundo Infantil',
        'subtitulo': 'Juguetes, Ropa y Libros para Niños',
        'lema': 'Imaginación sin límites',
        'color_primario': '#ff6b9d',
        'color_secundario': '#45b7d1',
        'color_fondo': '#fff5f7',
        'emoji': '🧸',
        'url': '/infantil'
    },
    'femenino': {
        'nombre': 'Mundo Femenino',
        'subtitulo': 'Ropa, Cosméticos y Belleza para Mujer',
        'lema': 'Brilla a tu manera',
        'color_primario': '#e91e63',
        'color_secundario': '#f5a623',
        'color_fondo': '#fff5f8',
        'emoji': '💄',
        'url': '/femenino'
    },
    'masculino': {
        'nombre': 'Mundo Masculino',
        'subtitulo': 'Alto Rendimiento para el Hombre',
        'lema': 'Fuerza, rendimiento, estilo',
        'color_primario': '#1a237e',
        'color_secundario': '#ff5722',
        'color_fondo': '#f5f5f5',
        'emoji': '💪',
        'url': '/masculino'
    }
}
