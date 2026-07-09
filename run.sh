#!/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"
python3 -m venv venv 2>/dev/null
source venv/bin/activate 2>/dev/null
pip install -q -r requirements.txt 2>/dev/null
python3 -c "from app import create_app, init_db; init_db(); app = create_app(); app.run(host='0.0.0.0', port=5000, debug=True)"
