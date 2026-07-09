import os
from flask import Blueprint, render_template, redirect, current_app, send_from_directory

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ACADEMIA_WEB = os.path.join(BASE, 'academia_web')

academia_bp = Blueprint('academia', __name__, template_folder='../../templates/academia',
                        static_folder='../../static', static_url_path='/static')


@academia_bp.route('/')
def index():
    return send_from_directory(ACADEMIA_WEB, 'index.html')


@academia_bp.route('/cursos')
def cursos():
    return send_from_directory(ACADEMIA_WEB, 'index.html')


@academia_bp.route('/libros')
def libros():
    db = current_app.config['get_db']()
    productos = db.execute("""SELECT * FROM productos WHERE division_id='academia'
                              AND activo=1 ORDER BY categoria, titulo""").fetchall()
    db.close()
    return render_template('academia/libros.html', productos=productos)


LIBRO_MAP = {
    'LGA-HTML5': '01_HTML5_LIBRO_MAESTRO',
    'LGA-CSS3': '02_CSS3_LIBRO_MAESTRO',
    'LGA-JS': '03_JAVASCRIPT_LIBRO_MAESTRO',
    'LGA-TS': '04_TYPESCRIPT_LIBRO_MAESTRO',
    'LGA-REACT': '05_REACT_LIBRO_MAESTRO',
    'LGA-NODE': '06_NODEJS_LIBRO_MAESTRO',
    'LGA-PHP': '07_PHP_LIBRO_MAESTRO',
    'LGA-SQL': '08_SQL_LIBRO_MAESTRO',
    'LGA-PYTHON': '09_PYTHON_LIBRO_MAESTRO',
    'LGA-JAVA': '10_JAVA_LIBRO_MAESTRO',
    'LGA-C': '11_C_LIBRO_MAESTRO',
    'LGA-CPP': '12_CPLUSPLUS_LIBRO_MAESTRO',
    'LGA-CSHARP': '13_CSHARP_LIBRO_MAESTRO',
    'LGA-GO': '14_GO_LIBRO_MAESTRO',
    'LGA-RUBY': '15_RUBY_LIBRO_MAESTRO',
    'LGA-IA': '16_IA_LIBRO_MAESTRO',
    'LGA-DJANGO': '17_DJANGO_LIBRO_MAESTRO',
    'LGA-DOCKER': '18_DOCKER_LIBRO_MAESTRO',
    'LGA-GIT': '19_GIT_LIBRO_MAESTRO',
    'LGA-API': '20_API_LIBRO_MAESTRO',
    'LGA-SEGURIDAD': '21_SEGURIDAD_LIBRO_MAESTRO',
    'LGA-LINUX': '22_LINUX_LIBRO_MAESTRO',
    'LGA-ARQUITECTURA': '23_ARQUITECTURA_LIBRO_MAESTRO',
    'LGA-LIDERAZGO': '24_LIDERAZGO_LIBRO_MAESTRO',
    'LGA-VSCODE': '25_VSCODE_LIBRO_MAESTRO',
    'LGA-TERMINAL': '26_TERMINAL_LIBRO_MAESTRO',
    'LGA-REDES': '27_REDES_LIBRO_MAESTRO',
    'LGA-BP': '28_BUENAS_PRACTICAS_LIBRO_MAESTRO',
    'LGA-GITAV': '29_GIT_LIBRO_MAESTRO',
    'LGA-TYPESCRIPT': '30_TYPESCRIPT_LIBRO_MAESTRO',
    'LGA-VUE': '31_VUE_LIBRO_MAESTRO',
    'LGA-ANGULAR': '32_ANGULAR_LIBRO_MAESTRO',
    'LGA-BOOTSTRAP': '33_BOOTSTRAP_LIBRO_MAESTRO',
    'LGA-TAILWIND': '34_TAILWIND_LIBRO_MAESTRO',
    'LGA-EXPRESS': '35_EXPRESS_LIBRO_MAESTRO',
    'LGA-LARAVEL': '36_LARAVEL_LIBRO_MAESTRO',
    'LGA-FLASK': '37_FLASK_LIBRO_MAESTRO',
    'LGA-SPRING': '38_JAVA_SPRING_LIBRO_MAESTRO',
    'LGA-ASPNET': '39_ASPNET_LIBRO_MAESTRO',
    'LGA-GRAPHQL': '40_GRAPHQL_LIBRO_MAESTRO',
    'LGA-MICROSVC': '41_MICROSERVICIOS_LIBRO_MAESTRO',
    'LGA-AUTH': '42_AUTENTICACION_LIBRO_MAESTRO',
    'LGA-MYSQL': '43_MYSQL_LIBRO_MAESTRO',
    'LGA-POSTGRES': '44_POSTGRESQL_LIBRO_MAESTRO',
    'LGA-MONGODB': '45_MONGODB_LIBRO_MAESTRO',
    'LGA-REDIS': '46_REDIS_LIBRO_MAESTRO',
    'LGA-FIREBASE': '47_FIREBASE_LIBRO_MAESTRO',
    'LGA-RUST': '48_RUST_LIBRO_MAESTRO',
    'LGA-KOTLIN': '49_KOTLIN_LIBRO_MAESTRO',
    'LGA-SWIFT': '50_SWIFT_LIBRO_MAESTRO',
    'LGA-DART': '51_DART_LIBRO_MAESTRO',
    'LGA-POO': '52_POO_LIBRO_MAESTRO',
    'LGA-ALGORITMOS': '53_ALGORITMOS_LIBRO_MAESTRO',
    'LGA-ANDROID': '54_ANDROID_LIBRO_MAESTRO',
    'LGA-FLUTTER': '55_FLUTTER_LIBRO_MAESTRO',
    'LGA-RN': '56_REACT_NATIVE_LIBRO_MAESTRO',
    'LGA-PROMPT': '57_PROMPT_ENGINEERING_LIBRO_MAESTRO',
    'LGA-OPENAI': '58_OPENAI_LIBRO_MAESTRO',
    'LGA-GEMINI': '59_GEMINI_LIBRO_MAESTRO',
    'LGA-CLAUDE': '60_CLAUDE_LIBRO_MAESTRO',
    'LGA-RAG': '61_RAG_LIBRO_MAESTRO',
    'LGA-AGENTES': '62_AGENTES_IA_LIBRO_MAESTRO',
    'LGA-REDES-SEC': '63_REDES_SEGURIDAD_LIBRO_MAESTRO',
    'LGA-PENTEST': '64_PENTESTING_LIBRO_MAESTRO',
    'LGA-AWS': '65_AWS_LIBRO_MAESTRO',
    'LGA-AZURE': '66_AZURE_LIBRO_MAESTRO',
    'LGA-GCP': '67_GCP_LIBRO_MAESTRO',
    'LGA-K8S': '68_KUBERNETES_LIBRO_MAESTRO',
    'LGA-DEVOPS': '69_DEVOPS_LIBRO_MAESTRO',
    'LGA-UNITY': '70_UNITY_LIBRO_MAESTRO',
    'LGA-UNREAL': '71_UNREAL_LIBRO_MAESTRO',
    'LGA-GODOT': '72_GODOT_LIBRO_MAESTRO',
    'LGA-IA-JUEGOS': '73_IA_JUEGOS_LIBRO_MAESTRO',
    'LGA-ARDUINO': '74_ARDUINO_LIBRO_MAESTRO',
    'LGA-RPI': '75_RASPBERRY_PI_LIBRO_MAESTRO',
    'LGA-IOT': '76_IOT_LIBRO_MAESTRO',
    'LGA-PANDAS': '77_PANDAS_LIBRO_MAESTRO',
    'LGA-POWERBI': '78_POWER_BI_LIBRO_MAESTRO',
    'LGA-BIGDATA': '79_BIG_DATA_LIBRO_MAESTRO',
    'LGA-PROY-N1': '80_PROYECTO_N1_LIBRO_MAESTRO',
    'LGA-PROY-N2': '81_PROYECTO_N2_LIBRO_MAESTRO',
    'LGA-PROY-N3': '82_PROYECTO_N3_LIBRO_MAESTRO',
    'LGA-PROY-N4': '83_PROYECTO_N4_LIBRO_MAESTRO',
    'LGA-PROY-N5': '84_PROYECTO_N5_LIBRO_MAESTRO',
    'LGA-PROY-N6': '85_PROYECTO_N6_LIBRO_MAESTRO',
    'LGA-PROY-N7': '86_PROYECTO_N7_LIBRO_MAESTRO',
    'LGA-PROY-N8': '87_PROYECTO_N8_LIBRO_MAESTRO',
    'LGA-PROY-N9': '88_PROYECTO_N9_LIBRO_MAESTRO',
    'LGA-PROY-N10': '89_PROYECTO_N10_LIBRO_MAESTRO',
    'LGA-PROY-N11': '90_PROYECTO_N11_LIBRO_MAESTRO',
    'LGA-PROY-N12': '91_PROYECTO_N12_LIBRO_MAESTRO',
}


@academia_bp.route('/ruta-html5')
def ruta_html5():
    from flask import redirect as rd
    return rd('/academia/lector.html?libro=01_HTML5_LIBRO_MAESTRO')


@academia_bp.route('/clase/<sku>')
def clase(sku):
    from flask import redirect as rd
    libro = LIBRO_MAP.get(sku)
    if not libro:
        return rd('/tienda/')
    return rd(f'/academia/lector.html?libro={libro}')


@academia_bp.route('/<path:filename>')
def archivos(filename):
    return send_from_directory(ACADEMIA_WEB, filename)
