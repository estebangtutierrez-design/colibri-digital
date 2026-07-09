# Política de Backup — Lucas EGA Academy v1.0

## ¿Qué se respalda?

| Componente | Ruta | Frecuencia |
|------------|------|------------|
| Base de datos | `db/academy.db` | Diario |
| Libros (contenido) | `libros/` | Semanal |
| Assets | `assets/` | Mensual |
| Configuración | `server.py`, `schema.sql` | En cada cambio |

## Script de Backup Automático

```bash
#!/bin/bash
# /usr/local/bin/backup_academia.sh

BACKUP_DIR="/backups/academia"
DATE=$(date +%Y%m%d_%H%M%S)
ACADEMIA_DIR="/var/www/academia"
RETENTION_DAYS=30

mkdir -p $BACKUP_DIR/{db,libros,assets,full}

# 1. Backup de base de datos
sqlite3 $ACADEMIA_DIR/db/academy.db ".backup $BACKUP_DIR/db/db_$DATE.sqlite"

# 2. Backup de libros
tar -czf $BACKUP_DIR/libros/libros_$DATE.tar.gz \
  -C $ACADEMIA_DIR libros/

# 3. Backup de assets
tar -czf $BACKUP_DIR/assets/assets_$DATE.tar.gz \
  -C $ACADEMIA_DIR assets/

# 4. Backup completo (semanal: domingos)
if [ $(date +%u) -eq 7 ]; then
  tar -czf $BACKUP_DIR/full/full_$DATE.tar.gz \
    -C $ACADEMIA_DIR \
    --exclude=__pycache__ \
    --exclude=venv \
    --exclude=.git \
    .
fi

# 5. Limpiar backups antiguos
find $BACKUP_DIR -name "*.sqlite" -mtime +$RETENTION_DAYS -delete
find $BACKUP_DIR -name "*.tar.gz" -mtime +$RETENTION_DAYS -delete

echo "✅ Backup $DATE completado"
```

### Programar en cron

```bash
sudo crontab -e

# Backup diario a las 3 AM
0 3 * * * /usr/local/bin/backup_academia.sh >> /var/log/backup.log 2>&1
```

## Restauración

```bash
# Restaurar base de datos
sqlite3 db/academy.db ".restore /backups/academia/db/db_20260701.sqlite"

# Restaurar libros
tar -xzf /backups/academia/libros/libros_20260701.tar.gz -C /var/www/academia/

# Restaurar completo
tar -xzf /backups/academia/full/full_20260701.tar.gz -C /var/www/academia/
```

## Verificación

```bash
# Verificar integridad de la DB
sqlite3 db/academy.db "PRAGMA integrity_check;"

# Verificar número de libros
ls libros/*_LIBRO_MAESTRO/ | wc -l
# Debería ser 15
```
