# API Reference — Lucas EGA Academy v1.0

Base URL: `http://localhost:5000/api`

## Autenticación

### POST /api/auth/register
```
Body: {"nombre": str, "email": str, "password": str}
Response: {"token": str, "usuario": {id, nombre, email, rol}}
```

### POST /api/auth/login
```
Body: {"email": str, "password": str}
Response: {"token": str, "usuario": {id, nombre, email, rol}}
```

### GET /api/auth/me
```
Headers: Authorization: Bearer <token>
Response: {"usuario": {id, nombre, email, rol, puntos, racha_dias}, "logros": [...]}
```

## Progreso

### GET /api/progreso
```
Headers: Authorization: Bearer <token>
Response: {"progreso": [{curso_id, capitulo, total, porcentaje, completado}, ...]}
```

### POST /api/progreso
```
Headers: Authorization: Bearer <token>
Body: {"curso_id": str, "capitulo": int, "total": int}
Response: {"porcentaje": float, "completado": int, "puntos": int, "logros": [str]}
```

### GET /api/progreso/<curso_id>
```
Headers: Authorization: Bearer <token>
Response: {capitulo, total, porcentaje, completado}
```

## Cursos

### GET /api/manifiestos
```
Response: [{id, nombre, nivel}, ...]  (15 cursos)
```

### GET /api/manifiestos/<id>
```
Response: {id, nombre, nivel, modulos: [{nombre, capitulos: [{archivo, titulo}]}]}
```

## Ejecución de Código

### POST /api/ejecutar
```
Body: {"codigo": str, "lenguaje": str}
Lenguajes: python, javascript, c, cpp, sql, html
Response: {"stdout": str, "stderr": str, "codigo": int}
```

## Foro

### GET /api/foro/hilos[?curso=<id>]
```
Response: [{id, titulo, autor_nombre, fecha, num_comentarios, curso_id}]
```

### POST /api/foro/hilos
```
Headers: Authorization: Bearer <token>
Body: {"titulo": str, "contenido": str, "curso_id": str|null}
Response: {"id": int, "mensaje": str}
```

### GET /api/foro/hilos/<id>
```
Response: {hilo: {titulo, contenido, autor_nombre, fecha}, comentarios: [{contenido, autor_nombre, fecha}]}
```

### POST /api/foro/comentarios
```
Headers: Authorization: Bearer <token>
Body: {"hilo_id": int, "contenido": str}
Response: {"mensaje": str}
```

## Gamificación

### GET /api/leaderboard
```
Response: [{nombre, puntos, cursos_completados, racha_dias}] (top 50)
```

## Búsqueda

### GET /api/buscar?q=<query>
```
Response: {"resultados": [{curso_id, modulo, titulo, preview}]}
```

## Admin

### GET /api/admin/estadisticas
```
Headers: Authorization: Bearer <token> (admin)
Response: {total_usuarios, total_progreso, cursos_completados, total_hilos, total_logros}
```

### GET /api/admin/usuarios
```
Headers: Authorization: Bearer <token> (admin)
Response: [{id, nombre, email, rol, cursos_iniciados, cursos_completados}]
```

### GET /api/admin/progreso
```
Headers: Authorization: Bearer <token> (admin)
Response: [{curso_id, capitulo, porcentaje, completado, usuario_nombre}]
```

## Utilidades

### POST /api/init-index
```
Inicia indexación FTS5 en segundo plano
Response: {"mensaje": str}
```
