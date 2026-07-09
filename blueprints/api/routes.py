import os, random, json, hashlib, secrets
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash

api_bp = Blueprint('api', __name__, url_prefix='/api')

MENSAJES_BASE = [
    "Sigue así, cada capítulo te acerca a tu meta. 🦉",
    "La práctica constante es el camino a la maestría. ¡No te detengas!",
    "Recuerda: los errores son oportunidades de aprendizaje. 💪",
    "Estoy orgulloso de tu progreso. Sigue adelante. 🚀",
    "Cada concepto que dominas te hace más fuerte como profesional.",
    "La disciplina vence al talento. Tu constancia es admirable.",
    "No compitas con otros, compite con tu yo de ayer.",
    "El conocimiento verdadero se construye paso a paso. Bien hecho.",
    "Tu dedicación me inspira, querido alumno. 🌟",
    "Los grandes desarrolladores no nacen, se hacen. Tú estás en camino.",
    "La tecnología cambia, pero los fundamentos perduran. Domínalos.",
    "Un capítulo a la vez. Así se construyen los expertos.",
    "La curiosidad es tu mejor herramienta. Sigue preguntando.",
    "Has llegado lejos. Pero el mejor aprendizaje está por venir.",
    "No temas equivocarte. Teme no intentarlo. ¡Sigue!",
    "El esfuerzo de hoy es el éxito de mañana.",
    "Practica, falla, aprende, repite. Ese es el ciclo del maestro.",
    "Tu progreso demuestra tu compromiso. Sigue así.",
    "La excelencia no es un acto, es un hábito. Lo estás formando.",
    "Confía en el proceso. Cada capítulo suma.",
]

MENSAJES_AVANZADO = [
    "Estás alcanzando niveles superiores. Tu esfuerzo se nota. 🔥",
    "El dominio técnico se construye con constancia. Vas por buen camino.",
    "Ya tienes una base sólida. Ahora a profundizar.",
    "Los expertos alguna vez fueron principiantes que nunca se rindieron.",
    "Tu progreso avanzado demuestra verdadera dedicación. 👏",
]

MENSAJES_FINAL = [
    "¡Felicidades! Has completado un libro completo. Eres increíble. 🎉",
    "Has llegado al final. Pero esto es solo el comienzo de tu viaje.",
    "LIBRO COMPLETADO. Toma un momento para celebrar tu logro. 🏆",
    "Eres oficialmente un estudiante avanzado. El mundo es tuyo. 🌍",
    "Has completado 80 capítulos. Eso es disciplina de élite.",
]

def generar_token():
    return secrets.token_hex(32)

@api_bp.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos requeridos"}), 400
    nombre = data.get('nombre', '').strip()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    if not nombre or not email or not password:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400
    if len(password) < 4:
        return jsonify({"error": "La contraseña debe tener al menos 4 caracteres"}), 400
    db = current_app.config['get_db']()
    exists = db.execute("SELECT id FROM usuarios WHERE email=?", (email,)).fetchone()
    if exists:
        db.close()
        return jsonify({"error": "El email ya está registrado"}), 400
    token = generar_token()
    db.execute("INSERT INTO usuarios (nombre, email, password_hash, token) VALUES (?,?,?,?)",
               (nombre, email, generate_password_hash(password), token))
    db.commit()
    usuario = {"id": db.execute("SELECT last_insert_rowid()").fetchone()[0], "nombre": nombre, "email": email}
    db.close()
    return jsonify({"token": token, "usuario": usuario})

@api_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos requeridos"}), 400
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    if not email or not password:
        return jsonify({"error": "Email y contraseña requeridos"}), 400
    db = current_app.config['get_db']()
    user = db.execute("SELECT id, nombre, email, password_hash FROM usuarios WHERE email=?", (email,)).fetchone()
    if not user or not check_password_hash(user['password_hash'], password):
        db.close()
        return jsonify({"error": "Credenciales inválidas"}), 401
    token = generar_token()
    db.execute("UPDATE usuarios SET token=? WHERE id=?", (token, user['id']))
    db.commit()
    db.close()
    return jsonify({"token": token, "usuario": {"id": user['id'], "nombre": user['nombre'], "email": user['email']}})

from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        auth = request.headers.get('Authorization', '')
        if auth.startswith('Bearer '):
            token = auth[7:]
        if not token:
            return jsonify({"error": "Token requerido"}), 401
        db = current_app.config['get_db']()
        user = db.execute("SELECT id, nombre, email FROM usuarios WHERE token=?", (token,)).fetchone()
        db.close()
        if not user:
            return jsonify({"error": "Token inválido"}), 401
        return f(user, *args, **kwargs)
    return decorated

@api_bp.route('/progreso', methods=['POST'])
@token_required
def guardar_progreso(user):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Datos requeridos"}), 400
    curso_id = data.get('curso_id', '')
    capitulo = data.get('capitulo', 0)
    total = data.get('total', 0)
    if not curso_id:
        return jsonify({"error": "curso_id requerido"}), 400
    db = current_app.config['get_db']()
    existing = db.execute("SELECT id FROM progreso WHERE usuario_id=? AND curso_id=?",
                          (user['id'], curso_id)).fetchone()
    if existing:
        db.execute("UPDATE progreso SET capitulo=?, total=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
                   (capitulo, total, existing['id']))
    else:
        db.execute("INSERT INTO progreso (usuario_id, curso_id, capitulo, total) VALUES (?,?,?,?)",
                   (user['id'], curso_id, capitulo, total))
    db.commit()
    db.close()
    return jsonify({"ok": True})

@api_bp.route('/progreso/<curso_id>', methods=['GET'])
@token_required
def obtener_progreso(user, curso_id):
    db = current_app.config['get_db']()
    p = db.execute("SELECT capitulo, total FROM progreso WHERE usuario_id=? AND curso_id=?",
                   (user['id'], curso_id)).fetchone()
    db.close()
    if p:
        return jsonify({"capitulo": p['capitulo'], "total": p['total']})
    return jsonify({"capitulo": 0, "total": 0})

@api_bp.route('/buho/mensaje', methods=['GET'])
@token_required
def mensaje_buho(user):
    db = current_app.config['get_db']()
    progresos = db.execute("SELECT capitulo, total FROM progreso WHERE usuario_id=?", (user['id'],)).fetchall()
    db.close()

    if not progresos:
        m = "Bienvenido a Lucas EGA Academy. Elige tu primer libro y comienza tu viaje. 🦉"
        return jsonify({"mensaje": m})

    max_pct = max((p['capitulo'] / max(p['total'], 1)) * 100 for p in progresos) if progresos else 0

    if max_pct >= 100:
        pool = MENSAJES_FINAL
    elif max_pct >= 60:
        pool = MENSAJES_AVANZADO
    else:
        pool = MENSAJES_BASE
    m = random.choice(pool)
    return jsonify({"mensaje": f"🦉 {m}"})
