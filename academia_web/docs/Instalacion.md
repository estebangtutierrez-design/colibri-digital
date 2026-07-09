# Instalación — Lucas EGA Academy v1.0

## Requisitos

- Python 3.10+
- pip (gestor de paquetes)
- gcc y g++ (para ejecución de C/C++ en playground)
- SQLite 3.x (incluido con Python)
- Node.js (opcional, para ejecutar JavaScript server-side)

## Instalación

```bash
# 1. Clonar o copiar el proyecto
cd /ruta/a/academia_web

# 2. Crear entorno virtual
python3 -m venv venv

# 3. Activar entorno
source venv/bin/activate

# 4. Instalar dependencias
pip install flask flask-jwt-extended flask-cors bcrypt weasyprint

# 5. Inicializar base de datos
sqlite3 db/academy.db < schema.sql

# 6. Indexar capítulos para búsqueda
# (se hace automáticamente vía POST /api/init-index)

# 7. Crear usuario admin (opcional)
python3 -c "
import sqlite3, bcrypt
pw = bcrypt.hashpw('admin123'.encode(), bcrypt.gensalt()).decode()
conn = sqlite3.connect('db/academy.db')
conn.execute(\"INSERT INTO usuarios (nombre, email, password_hash, rol) VALUES ('Admin','admin@ega.com',?,'admin')\", (pw,))
conn.commit(); conn.close()
print('Admin creado: admin@ega.com / admin123')
"
```

## Ejecución

```bash
# Desarrollo
python3 server.py

# Producción (Gunicorn)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 server:app
```

## Variables de Entorno (opcional)

| Variable | Default | Descripción |
|----------|---------|-------------|
| FLASK_PORT | 5000 | Puerto del servidor |
| JWT_SECRET | (hardcodeado) | Secreto para tokens |
| DATABASE_PATH | db/academy.db | Ruta a SQLite |

## Verificación

```bash
curl http://localhost:5000/api/manifiestos | python3 -m json.tool
# Debería mostrar 15 cursos
```
