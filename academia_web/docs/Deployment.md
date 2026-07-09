# Deployment — Lucas EGA Academy v1.0

## Opción 1: Servidor VPS (Recomendada)

```bash
# En el servidor:
git clone <repo> /var/www/academia
cd /var/www/academia

python3 -m venv venv
source venv/bin/activate
pip install flask flask-jwt-extended flask-cors bcrypt gunicorn

# Iniciar con Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 server:app --daemon
```

### Nginx (reverse proxy)

```nginx
server {
    listen 80;
    server_name academia.ega.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static/ {
        alias /var/www/academia/;
        expires 30d;
    }
}
```

## Opción 2: Docker

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install flask flask-jwt-extended flask-cors bcrypt gunicorn
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "server:app"]
```

```bash
docker build -t ega-academy .
docker run -d -p 5000:5000 --name academia ega-academy
```

## Backup

```bash
#!/bin/bash
# Respaldo diario
DATE=$(date +%Y%m%d)
mkdir -p /backups/academia
cp /var/www/academia/db/academy.db /backups/academia/db_$DATE.db
tar -czf /backups/academia/libros_$DATE.tar.gz /var/www/academia/libros/
tar -czf /backups/academia/assets_$DATE.tar.gz /var/www/academia/assets/
echo "Backup $DATE completado"
```

## Monitoreo

```bash
# Logs
tail -f /var/log/academia.log

# Procesos
ps aux | grep gunicorn

# Espacio
du -sh /var/www/academia/
```

## Seguridad

- Cambiar JWT_SECRET_KEY en producción
- Usar HTTPS con Certbot/Let's Encrypt
- Rate limiting en /api/auth/
- No exponer debug mode en producción
