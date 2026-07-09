# Base de Datos — Lucas EGA Academy v1.0

## Motor
- **SQLite 3.x** con WAL mode
- Archivo: `db/academy.db`
- Sin servidor externo, embebido en la app

## Tablas

### usuarios
| Columna | Tipo | Descripción |
|---------|------|-------------|
| id | INTEGER PK | Auto-increment |
| nombre | TEXT | Nombre completo |
| email | TEXT UNIQUE | Email (login) |
| password_hash | TEXT | bcrypt hash |
| rol | TEXT | 'alumno' o 'admin' |
| fecha_registro | TIMESTAMP | Default CURRENT_TIMESTAMP |
| ultimo_acceso | TIMESTAMP | Último login |
| racha_dias | INTEGER | Días consecutivos |
| puntos | INTEGER | Puntos totales |

### progreso
| Columna | Tipo | Descripción |
|---------|------|-------------|
| id | INTEGER PK | Auto-increment |
| usuario_id | INTEGER FK | → usuarios.id |
| curso_id | TEXT | Ej: "01_HTML5_LIBRO_MAESTRO" |
| capitulo | INTEGER | Último capítulo leído |
| total | INTEGER | Total capítulos (80) |
| porcentaje | REAL | 0.0 – 100.0 |
| completado | INTEGER | 0 o 1 |
| fecha_actualizacion | TIMESTAMP | Última actualización |
| UNIQUE | (usuario_id, curso_id) | Un progreso por curso |

### logros
| Columna | Tipo | Descripción |
|---------|------|-------------|
| id | INTEGER PK | Auto-increment |
| usuario_id | INTEGER FK | → usuarios.id |
| tipo | TEXT | Identificador del logro |
| nombre | TEXT | Nombre visible |
| icono | TEXT | Emoji del logro |
| fecha | TIMESTAMP | Fecha de obtención |

### foro_hilos
| Columna | Tipo | Descripción |
|---------|------|-------------|
| id | INTEGER PK | Auto-increment |
| usuario_id | INTEGER FK | → usuarios.id |
| titulo | TEXT | Título del hilo |
| contenido | TEXT | Mensaje inicial |
| curso_id | TEXT | Opcional, para filtrar |
| fecha | TIMESTAMP | Creación |

### foro_comentarios
| Columna | Tipo | Descripción |
|---------|------|-------------|
| id | INTEGER PK | Auto-increment |
| hilo_id | INTEGER FK | → foro_hilos.id |
| usuario_id | INTEGER FK | → usuarios.id |
| contenido | TEXT | Mensaje |
| fecha | TIMESTAMP | Creación |

### cursos
| Columna | Tipo | Descripción |
|---------|------|-------------|
| id | TEXT PK | ID del curso |
| nombre | TEXT | Nombre visible |
| nivel | INTEGER | 1-4 |

### capitulos_fts (Virtual Table FTS5)
| Columna | Tipo | Descripción |
|---------|------|-------------|
| curso_id | TEXT | ID del curso |
| modulo | TEXT | Módulo |
| titulo | TEXT | Título del capítulo |
| contenido | TEXT | Contenido completo |
| tokenize | 'unicode61' | Tokenizador español |

## Logros Automáticos

| Tipo | Condición | Icono |
|------|-----------|-------|
| primer_curso | 1 curso completado | 🎓 |
| cinco_cursos | 5 cursos completados | 📚 |
| diez_cursos | 10 cursos completados | 🏗️ |
| academia_completa | 15 cursos completados | 🏆 |
