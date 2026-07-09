# Lucas EGA Academy — Arquitectura

## Visión General

```
academia_web/
├── server.py           # Servidor Flask (API + Static)
├── schema.sql          # Esquema de base de datos
├── db/academy.db       # SQLite (WAL mode, FK activas)
├── manifest.json       # PWA manifest
├── sw.js               # Service Worker
├── style.css           # Tema oscuro GitHub-like
├── app.js              # Utilidades JS compartidas
├── index.html          # Landing + auth + cursos
├── lector.html         # Lector de libros
├── playground.html     # Editor multi-lenguaje
├── foro.html           # Foro comunitario
├── perfil.html         # Dashboard alumno
├── certificado.html    # Diploma
├── assets/             # 7 imágenes PNG
├── libros/             # 15 cursos (1,200 .txt)
├── manifiestos/        # 15 JSON de navegación
├── templates/admin/    # Admin panel HTML
├── docs/               # Documentación
└── generar_manifiestos.py  # Build tool
```

## Stack Tecnológico

| Componente    | Tecnología             |
|---------------|------------------------|
| Backend       | Flask 3.x (Python)     |
| Auth          | JWT (flask-jwt-extended) + bcrypt |
| Base de Datos | SQLite (WAL)           |
| Frontend      | HTML + CSS + Vanilla JS|
| PWA           | Service Worker + Manifest |
| Búsqueda      | SQLite FTS5            |
| Caché Offline | Cache API (Service Worker) |

## Flujo de Datos

```
Navegador → Flask Static (HTML/CSS/JS)
         → API REST (JSON)
         → SQLite
         → Sistema de Archivos (libros/)
```

## Estructura de la DB

### usuarios
- id, nombre, email, password_hash, rol, fecha_registro, ultimo_acceso, racha_dias, puntos

### progreso
- id, usuario_id, curso_id, capitulo, total, porcentaje, completado, fecha_actualizacion
- UNIQUE(usuario_id, curso_id)

### logros
- id, usuario_id, tipo, nombre, icono, fecha

### foro_hilos / foro_comentarios
- Hilos con usuario_id, titulo, contenido, curso_id
- Comentarios con hilo_id, usuario_id, contenido

### capitulos_fts
- Virtual table FTS5 para búsqueda global

## Sistema de Niveles

| Nivel | Cursos | Rol |
|-------|--------|-----|
| 🟢 N1 | HTML5, CSS3, JavaScript | Fundamentos |
| 🔵 N2 | TypeScript, React | Front-End |
| 🟣 N3 | Node.js, PHP, SQL | Full Stack |
| 🟠 N4 | Python, Java, C, C++, C#, Go, Ruby | Profesional |

## Gamificación

- 100 puntos por curso completado
- Logros: 1, 5, 10, 15 cursos
- Rachas por días consecutivos
- Leaderboard global
