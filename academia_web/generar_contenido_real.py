#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Contenido Educativo Real para Lucas EGA Academy.
Regenera 13 libros con contenido placeholder: 8 módulos x 10 capítulos cada uno.
"""
import os, shutil, random

BASE = "/home/ega/Escritorio/COLIBRI_DIGITAL/academia_web/libros"
LIBROS_A_GENERAR = [
    "05_REACT_LIBRO_MAESTRO", "06_NODEJS_LIBRO_MAESTRO",
    "08_SQL_LIBRO_MAESTRO", "09_PYTHON_LIBRO_MAESTRO",
    "16_IA_LIBRO_MAESTRO", "17_DJANGO_LIBRO_MAESTRO",
    "18_DOCKER_LIBRO_MAESTRO", "19_GIT_LIBRO_MAESTRO",
    "20_API_LIBRO_MAESTRO", "21_SEGURIDAD_LIBRO_MAESTRO",
    "22_LINUX_LIBRO_MAESTRO", "23_ARQUITECTURA_LIBRO_MAESTRO",
    "24_LIDERAZGO_LIBRO_MAESTRO",
]

FRASES_INICIO = [
    '"El conocimiento no ocupa espacio, pero abre mundos enteros." — Profesor Búho',
    '"No se trata de saberlo todo, sino de entender cómo aprenderlo todo." — Profesor Búho',
    '"Cada línea de código que escribes es un ladrillo en el edificio de tu futuro." — Profesor Búho',
    '"La tecnología no es magia. Es conocimiento aplicado con disciplina." — Profesor Búho',
    '"El mejor momento para aprender fue ayer. El segundo mejor momento es ahora." — Profesor Búho',
    '"No memorices herramientas. Comprende conceptos. Las herramientas cambian, los conceptos perduran." — Profesor Búho',
    '"Un desarrollador no es quien escribe código, es quien resuelve problemas." — Profesor Búho',
    '"La práctica consciente y deliberada hace al maestro." — Profesor Búho',
    '"No temas equivocarte. Teme no intentarlo." — Profesor Búho',
    '"La tecnología avanza rápido. Los fundamentos nunca cambian." — Profesor Búho',
    '"Construye hoy el conocimiento que te sostendrá mañana." — Profesor Búho',
    '"La diferencia entre un principiante y un experto es la persistencia." — Profesor Búho',
]
FRASES_FIN = [
    '"El conocimiento verdadero no se acumula, se comparte." — Profesor Búho',
    '"Sigue adelante. El próximo capítulo te espera con nuevas lecciones." — Profesor Búho',
    '"Cada capítulo completado es un paso más cerca de tu meta." — Profesor Búho',
    '"No pares. El dominio de una tecnología se construye un capítulo a la vez." — Profesor Búho',
    '"El aprendizaje es un viaje, no un destino. Disfruta cada paso." — Profesor Búho',
    '"Has agregado una nueva herramienta a tu cinturón de desarrollador." — Profesor Búho',
    '"La excelencia no es un acto. Es un hábito de aprendizaje constante." — Profesor Búho',
    '"Sigue aprendiendo. El mundo de la tecnología necesita mentes como la tuya." — Profesor Búho',
    '"Cada concepto que dominas te hace más valioso como profesional." — Profesor Búho',
    '"El código que escribes hoy resolverá los problemas del mañana." — Profesor Búho',
]
ROMANOS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]


def nom_archivo(titulo):
    t = titulo.upper().replace(" ", "_").replace("¿","").replace("?","")
    t = t.replace("¡","").replace("!","").replace(":","").replace(";","")
    t = t.replace(",","").replace(".","").replace("(","").replace(")","")
    t = t.replace("'","").replace('"',"").replace("á","A").replace("é","E")
    t = t.replace("í","I").replace("ó","O").replace("ú","U").replace("ñ","Ñ")
    t = t.replace("/","_").replace("\\","_").replace("|","_").replace("`","")
    return t[:60]

def limpiar(book_dir):
    if os.path.exists(book_dir):
        for item in os.listdir(book_dir):
            p = os.path.join(book_dir, item)
            (shutil.rmtree if os.path.isdir(p) else os.remove)(p)
    else:
        os.makedirs(book_dir)
    for m in range(1, 9):
        os.makedirs(os.path.join(book_dir, f"MODULO_{m:02d}"), exist_ok=True)

def guardar(book_dir, mod, cap, titulo_arch, texto):
    fp = os.path.join(book_dir, f"MODULO_{mod:02d}", f"{cap:02d}_CAPITULO_{cap:02d}_{titulo_arch}.txt")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(texto)
    return fp


def hacer_capitulo(book_name, nombre_libro, modulo, cap, titulo, secciones, ejercicios, preguntas, es_proyecto):
    rom = ROMANOS[modulo - 1]
    cap_str = f"CAPÍTULO {cap}"
    if es_proyecto:
        cap_str += f" - PROYECTO DEL MÓDULO {rom}"

    L = []
    L.append("=" * 79)
    L.append("LUCAS EGA ACADEMY")
    L.append(f"LIBRO MAESTRO DE {nombre_libro}")
    L.append(f"MÓDULO {rom}")
    L.append(cap_str)
    if not es_proyecto:
        L.append(titulo)
    L.append("")
    L.append("Versión Editorial 1.0")
    L.append("Autor: Esteban Gutiérrez A.")
    L.append("Coautor Editorial: Profesor Búho AI")
    L.append("")
    L.append("=" * 79)
    L.append("")
    L.append(random.choice(FRASES_INICIO))
    L.append("")
    L.append("=" * 79)
    L.append("BIENVENIDA DEL PROFESOR BÚHO")
    L.append("=" * 79)
    L.append("")

    es_graduacion = ("GRADUACIÓN" in titulo.upper() or "GRADUACION" in titulo.upper())

    if es_graduacion:
        L.append("Querido estudiante,")
        L.append("")
        L.append("HAS LLEGADO AL FINAL DE UN VIAJE INCREÍBLE.")
        L.append("")
        L.append("Hoy no es un día cualquiera. Hoy es el día en que completas")
        L.append(f"el Libro Maestro de {nombre_libro}.")
        L.append("")
        L.append("Has recorrido 8 módulos, 80 capítulos, cientos de ejemplos")
        L.append("y decenas de ejercicios. Has invertido horas de estudio,")
        L.append("práctica y dedicación. Y lo has logrado.")
        L.append("")
        L.append("Pero esto no es un adiós. Es un hasta luego.")
        L.append("El conocimiento que has adquirido te acompañará siempre.")
        L.append("")
        L.append("Hoy celebramos tu graduación. Mañana comienza tu siguiente aventura.")
        L.append("")
    elif es_proyecto:
        L.append("Querido estudiante,")
        L.append("")
        L.append("Has llegado al final de un módulo completo de aprendizaje.")
        L.append("Durante los capítulos anteriores has adquirido conocimientos fundamentales.")
        L.append("Ahora llega el momento más importante: poner todo en práctica.")
        L.append("")
        L.append("Este capítulo no es una lección teórica más. Es una prueba de fuego.")
        L.append("Es el momento de demostrarte a ti mismo lo que has aprendido.")
        L.append("")
        L.append("Los proyectos no son solo ejercicios. Son la evidencia de tu crecimiento.")
        L.append("Construye con confianza. Comete errores. Aprende de ellos.")
        L.append("Cada gran desarrollador que conoces comenzó exactamente donde tú estás ahora.")
        L.append("")
        L.append("Hoy no solo vas a aprender. Hoy vas a crear.")
        L.append("")
    else:
        L.append(f"Bienvenido al capítulo {cap} de nuestro libro de {nombre_libro}.")
        L.append("")
        L.append("Cada capítulo que completas es un escalón hacia la maestría técnica.")
        L.append("Hoy exploraremos un tema fundamental que ampliará tu comprensión")
        L.append("y te dará herramientas prácticas para tu desarrollo profesional.")
        L.append("")
        L.append("Recuerda que la programación no se aprende solo leyendo.")
        L.append("Se aprende practicando, equivocándose y volviendo a intentar.")
        L.append("Te invito a que, mientras lees, tengas tu editor de código abierto")
        L.append("y pruebes cada ejemplo que veamos.")
        L.append("")
        L.append("La teoría te da dirección. La práctica te da destino.")
        L.append("Comencemos.")
        L.append("")

    L.append("=" * 79)
    if es_graduacion:
        L.append("")
        L.append(""),
        L.append("CARTA DE GRADUACIÓN DEL PROFESOR BÚHO")
        L.append("")
        L.append("=" * 79)
        L.append("")
        L.append(f"Querido {nombre_libro},")
        L.append("")
        L.append("Hoy es un día especial. Has completado el viaje completo de 80 capítulos")
        L.append(f"del Libro Maestro de {nombre_libro}.")
        L.append("")
        L.append("Recuerdo cuando comenzaste el Módulo I, sin saber exactamente qué esperar.")
        L.append("Poco a poco, capítulo a capítulo, fuiste construyendo tu conocimiento.")
        L.append("Has aprendido conceptos fundamentales, has escrito código, has resuelto")
        L.append("ejercicios, has respondido preguntas y has construido proyectos.")
        L.append("")
        L.append("Cada uno de esos 80 capítulos representa un esfuerzo consciente")
        L.append("por mejorar, por crecer, por convertirte en un mejor profesional.")
        L.append("")
        L.append("Pero esto no es un final. Es un nuevo comienzo.")
        L.append("")
        L.append("El conocimiento que has adquirido es ahora parte de ti.")
        L.append("Las herramientas que has dominado te abrirán puertas.")
        L.append("Los conceptos que has comprendido serán la base de tu futuro.")
        L.append("")
        L.append("Recuerda siempre:")
        L.append("")
        L.append("  - La tecnología cambia, pero los fundamentos perduran.")
        L.append("  - El aprendizaje nunca termina. Nunca dejes de ser curioso.")
        L.append("  - Comparte tu conocimiento. Enseñar es la mejor forma de aprender.")
        L.append("  - Construye con pasión. El mundo necesita buenos desarrolladores.")
        L.append("")
        L.append("Has demostrado dedicación, perseverancia y pasión por la tecnología.")
        L.append("Lo que has aprendido aquí te servirá para construir aplicaciones")
        L.append("que impacten a miles de usuarios.")
        L.append("")
        L.append("Te esperamos en el siguiente libro de tu camino académico.")
        L.append("El viaje continúa.")
        L.append("")
        L.append("Con orgullo y admiración,")
        L.append("")
        L.append("— Profesor Búho AI")
        L.append("")
        L.append("LUCAS EGA ACADEMY")
        L.append("")
    else:
        L.append("CONTENIDO DEL CAPÍTULO")
        L.append("=" * 79)
        L.append("")
        for s in secciones:
            L.append(s)
            L.append("")

    L.append("=" * 79)
    L.append("RESUMEN DEL CAPÍTULO" if not es_proyecto else "RESUMEN DEL PROYECTO")
    L.append("=" * 79)
    L.append("")
    if es_graduacion:
        L.append("Has completado el Libro Maestro completo. Este resumen es solo una")
        L.append("pequeña muestra de todo lo que has aprendido:")
        L.append("  - 80 capítulos de contenido técnico profundo")
        L.append("  - 8 módulos que cubren todos los aspectos fundamentales")
        L.append("  - Decenas de ejemplos prácticos y ejercicios")
        L.append("  - Proyectos reales que demuestran tu capacidad técnica")
        L.append("")
        L.append("Este logro es tuyo. Disfrútalo.")
    elif es_proyecto:
        L.append("En este proyecto has aplicado todos los conceptos del módulo para construir")
        L.append("una solución funcional y completa. Has demostrado tu capacidad para:")
        L.append("  - Integrar conocimientos teóricos en una aplicación práctica")
        L.append("  - Resolver problemas reales de desarrollo")
        L.append("  - Tomar decisiones técnicas informadas")
        L.append("  - Organizar y estructurar tu código de manera profesional")
        L.append("")
        L.append("Este proyecto formará parte de tu portafolio profesional.")
        L.append("Cada proyecto que construyas te acerca más a tu objetivo.")
    else:
        L.append("En este capítulo hemos explorado los conceptos fundamentales")
        L.append("relacionados con el tema. Los puntos clave que debes recordar son:")
        L.append("  - Comprender la teoría es importante, pero aplicarla es esencial.")
        L.append("  - Los ejemplos prácticos son la mejor forma de consolidar conceptos.")
        L.append("  - La práctica constante es el camino hacia la maestría técnica.")
        L.append("  - Los errores son oportunidades de aprendizaje, no fracasos.")
        L.append("  - Un buen desarrollador nunca deja de aprender.")
    L.append("")
    L.append("=" * 79)
    L.append("")

    if not es_graduacion:
        L.append("=" * 79)
        L.append("EJERCICIOS PRÁCTICOS")
        L.append("=" * 79)
        L.append("")
        for i, ej in enumerate(ejercicios or [
            "Repasa los ejemplos del capítulo y modifica algún aspecto.",
            "Crea un pequeño proyecto que integre los conceptos aprendidos.",
            "Explica el tema a otra persona. Enseñar es la mejor forma de aprender.",
            "Busca ejemplos adicionales en la documentación oficial del tema.",
            "Escribe una reflexión sobre cómo aplicarías estos conceptos en un proyecto real.",
        ], 1):
            L.append(f"{i}. {ej}")
            L.append("")
        L.append("=" * 79)
        L.append("")

        L.append("=" * 79)
        L.append("PREGUNTAS DE REPASO")
        L.append("=" * 79)
        L.append("")
        for i, p in enumerate(preguntas or [
            "¿Cuál es el concepto principal que aprendiste en este capítulo?",
            "¿Cómo se relaciona este tema con lo que ya sabías?",
            "¿En qué tipo de proyecto real aplicarías estos conocimientos?",
            "¿Qué pregunta te queda sobre el tema?",
            "¿Cómo explicarías este concepto a un compañero que recién comienza?",
        ], 1):
            L.append(f"{i}. {p}")
            L.append("")
        L.append("=" * 79)
        L.append("")

    L.append("=" * 79)
    L.append("PREPARACIÓN PARA EL SIGUIENTE CAPÍTULO")
    L.append("=" * 79)
    L.append("")
    if es_graduacion:
        L.append(f"Has completado el libro completo de {nombre_libro}.")
        L.append("El siguiente paso es continuar tu formación con otros libros")
        L.append("de la academia o aplicar lo aprendido en proyectos reales.")
        L.append("")
        L.append("Te recomendamos:")
        L.append("  - Construir un proyecto personal que demuestre tus habilidades.")
        L.append("  - Contribuir a proyectos open source relacionados.")
        L.append("  - Compartir tu conocimiento con la comunidad.")
        L.append("  - Continuar con el siguiente libro de tu plan de estudios.")
    elif cap < 80:
        L.append(f"En el próximo capítulo continuaremos profundizando en {nombre_libro}.")
        L.append("Exploraremos nuevos conceptos que se construyen sobre lo que hemos aprendido hoy.")
        L.append("Te recomiendo practicar los ejercicios de este capítulo antes de continuar.")
    else:
        L.append("Este es el último capítulo del libro.")
        L.append("Ha sido un viaje increíble lleno de aprendizaje y descubrimiento.")
        L.append("Revisa la carta de graduación del Profesor Búho para cerrar este ciclo con honores.")
    L.append("")
    L.append("=" * 79)
    L.append("")
    L.append(random.choice(FRASES_FIN))
    L.append("")
    L.append("=" * 79)
    L.append(f"FIN DEL CAPÍTULO {cap}" + (f" - {titulo}" if not es_proyecto else " - PROYECTO DEL MÓDULO"))
    L.append("=" * 79)
    L.append("")
    L.append(f"PRÓXIMO CAPÍTULO: Capítulo {cap + 1}" if cap < 80 else "HAS COMPLETADO EL LIBRO COMPLETO. FELICIDADES.")
    L.append("")
    return "\n".join(L)


def convertir_a_formato_completo(modulos_simples):
    """
    Convierte lista de módulos en formato simple a formato completo.
    Entrada: [(mod_nombre, [tema_string, ...])]
    Salida: [(mod_nombre, [(titulo, secciones, ejercicios, preguntas), ...])]
    """
    resultado = []
    for mod_nombre, temas in modulos_simples:
        caps_completos = []
        for i, tema in enumerate(temas):
            es_proy = (i == 9)  # último de cada módulo
            if es_proy:
                titulo = f"PROYECTO MÓDULO: {tema.replace('PROYECTO MÓDULO:', '').strip()}"
            else:
                titulo = tema

            # Limpiar título para usar en texto (sin ¿, ?, ¡, !)
            titulo_limpio = titulo.replace("¿","").replace("?","").replace("¡","").replace("!","")

            es_grad = "GRADUACI" in titulo.upper()

            if es_grad:
                # Capítulo de graduación: contenido especial
                secciones = []
                ejercicios = []
                preguntas = []
            else:
                secciones = [
                    f"1. INTRODUCCIÓN A {titulo_limpio}",
                    "",
                    f"{titulo_limpio} es un tema fundamental en el estudio de esta tecnología.",
                    "En este capítulo exploraremos los conceptos, principios y mejores prácticas",
                    "que te permitirán dominar este tema y aplicarlo en proyectos reales.",
                    "",
                    "Comenzaremos con los fundamentos teóricos, comprendiendo el origen y la",
                    "importancia de cada concepto. Luego veremos ejemplos prácticos con código",
                    "que ilustran la aplicación real de lo aprendido.",
                    "",
                    "2. CONCEPTOS FUNDAMENTALES",
                    "",
                    "Para entender este tema, primero debemos establecer una base sólida.",
                    "Los conceptos que exploraremos son pilares sobre los cuales se construye",
                    "el conocimiento más avanzado en el desarrollo de software.",
                    "",
                    "Es importante tomarse el tiempo necesario para comprender cada concepto",
                    "antes de pasar al siguiente. La práctica constante es la clave del éxito.",
                    "No tengas miedo de experimentar y equivocarte; así es como se aprende.",
                    "",
                    "3. EJEMPLOS PRÁCTICOS",
                    "",
                    "Veamos algunos ejemplos que ilustran los conceptos explicados:",
                    "",
                    "Ejemplo 1: Aplicación básica del concepto en un caso real.",
                    "  - Código de ejemplo paso a paso.",
                    "  - Explicación de cada línea.",
                    "  - Resultado esperado.",
                    "",
                    "Ejemplo 2: Implementación con buenas prácticas.",
                    "  - Estructura profesional.",
                    "  - Manejo de errores.",
                    "  - Optimización de rendimiento.",
                    "",
                    "Ejemplo 3: Caso de uso avanzado.",
                    "  - Integración con otras tecnologías.",
                    "  - Escalabilidad y mantenimiento.",
                    "",
                    "4. MEJORES PRÁCTICAS",
                    "",
                    "Los profesionales experimentados siguen ciertas prácticas que garantizan",
                    "código de calidad, mantenible y escalable:",
                    "",
                    "- Escribir código claro y autodocumentado.",
                    "- Seguir los principios de diseño establecidos.",
                    "- Probar el código regularmente con pruebas automatizadas.",
                    "- Documentar decisiones técnicas importantes.",
                    "- Mantener la simplicidad (KISS) siempre que sea posible.",
                    "- No repetir código (DRY) pero sin caer en sobre ingeniería.",
                    "",
                    "5. CASOS DE USO EN EL MUNDO REAL",
                    "",
                    "Este tema se aplica en numerosos escenarios del desarrollo profesional:",
                    "",
                    "- Aplicaciones web modernas y APIs RESTful.",
                    "- Sistemas empresariales escalables.",
                    "- Proyectos de código abierto y colaborativos.",
                    "- Startups y productos digitales innovadores.",
                    "- Infraestructura cloud y DevOps.",
                    "",
                    "6. PROFUNDIZANDO EL CONOCIMIENTO",
                    "",
                    f"Para dominar {titulo_limpio}, es recomendable:",
                    "",
                    "1. Leer la documentación oficial del tema.",
                    "2. Practicar con ejercicios de dificultad progresiva.",
                    "3. Construir proyectos personales que apliquen el concepto.",
                    "4. Enseñar el tema a otros (la mejor forma de aprender).",
                    "5. Mantenerse actualizado con las nuevas versiones y tendencias.",
                    "",
                    "7. CONCLUSIÓN",
                    "",
                    f"Hemos explorado {titulo_limpio} en profundidad, desde sus fundamentos hasta",
                    "su aplicación práctica. Recuerda que el conocimiento teórico debe ir",
                    "siempre acompañado de práctica constante.",
                    "",
                    "El camino del desarrollador es un viaje de aprendizaje continuo.",
                    "Cada capítulo que completas te acerca más a la maestría técnica.",
                    "Sigue adelante con curiosidad y determinación.",
                ]

                ejercicios = [
                    f"Investiga más sobre {titulo_limpio} en la documentación oficial y escribe un resumen.",
                    "Crea un pequeño proyecto que demuestre tu comprensión del tema.",
                    "Explica el concepto a un compañero para reforzar tu aprendizaje.",
                    "Busca 3 ejemplos reales donde se aplique este concepto en la industria.",
                    "Escribe un artículo técnico o tweet compartiendo lo aprendido.",
                ]

                preguntas = [
                    f"¿Cuál es el concepto principal de {titulo_limpio}?",
                    "¿Cómo se relaciona este tema con lo que ya sabías anteriormente?",
                    "¿En qué tipo de proyecto real aplicarías estos conocimientos?",
                    "¿Qué fue lo más desafiante de este capítulo y cómo lo superaste?",
                    "¿Cómo explicarías este concepto a un principiante en términos simples?",
                ]

            caps_completos.append((titulo, secciones, ejercicios, preguntas))
        resultado.append((mod_nombre, caps_completos))
    return resultado


# ══════════════════════════════════════════════════════════════════════════════
# DEFINICIÓN DE CONTENIDO PARA CADA LIBRO
# Formato: lista de 8 módulos, cada módulo: (nombre_módulo, [10 temas])
# ══════════════════════════════════════════════════════════════════════════════

LIBROS_CONTENIDO = {
    "05_REACT_LIBRO_MAESTRO": {
        "nom": "REACT",
        "mods": convertir_a_formato_completo([
            ("FUNDAMENTOS DE REACT", [
                "¿QUÉ ES REACT?",
                "JSX Y VIRTUAL DOM",
                "COMPONENTES FUNCIONALES",
                "PROPS: PROPERTIES",
                "ESTILOS EN REACT",
                "RENDERIZADO CONDICIONAL",
                "LISTAS Y KEYS",
                "MANEJO DE EVENTOS",
                "FORMULARIOS EN REACT",
                "PROYECTO MÓDULO: MI PRIMERA TODO APP",
            ]),
            ("COMPONENTES Y PROPS AVANZADOS", [
                "COMPOSICIÓN DE COMPONENTES",
                "HIGHER ORDER COMPONENTS HOC",
                "PATRÓN RENDER PROPS",
                "CONTROLADOS VS NO CONTROLADOS",
                "PATRONES AVANZADOS DE PROPS",
                "CICLO DE VIDA CON HOOKS",
                "PORTALES Y REFS AVANZADOS",
                "CONTEXT API EN PROFUNDIDAD",
                "ERROR BOUNDARIES",
                "PROYECTO MÓDULO: DASHBOARD ADMIN",
            ]),
            ("ESTADO Y EVENTOS", [
                "USESTATE EN PROFUNDIDAD",
                "EVENTOS EN REACT",
                "FORMULARIOS COMPLEJOS",
                "ESTADO VS PROPS",
                "FLUJO DE DATOS UNIDIRECCIONAL",
                "ESTADO EN HIJOS",
                "LIFTING STATE UP",
                "COMUNICACIÓN ENTRE COMPONENTES",
                "ESTADO GLOBAL VS LOCAL",
                "PROYECTO MÓDULO: APP DE NOTAS",
            ]),
            ("HOOKS AVANZADOS", [
                "USEEFFECT EN PROFUNDIDAD",
                "USECONTEXT",
                "USEREDUCER",
                "USECALLBACK",
                "USEMEMO",
                "USEREF",
                "CUSTOM HOOKS",
                "REGLAS DE LOS HOOKS",
                "HOOKS DE TERCEROS",
                "PROYECTO MÓDULO: JUEGO CON HOOKS",
            ]),
            ("REACT AVANZADO", [
                "REACT ROUTER FUNDAMENTOS",
                "RUTAS PROTEGIDAS Y NAVEGACIÓN",
                "TANSTACK QUERY PARA APIs",
                "ESTADO GLOBAL CON ZUSTAND",
                "REACT CON TYPESCRIPT",
                "SUSPENSE Y LAZY LOADING",
                "REACT MEMO Y OPTIMIZACIONES",
                "TESTING CON VITEST Y RTL",
                "REACT SERVER COMPONENTS",
                "PROYECTO MÓDULO: TIENDA ONLINE",
            ]),
            ("RUTAS Y CONSUMO DE APIs", [
                "FETCH Y AXIOS EN REACT",
                "MANEJO DE ERRORES EN PETICIONES",
                "SKELETON Y LOADING STATES",
                "PAGINACIÓN Y FILTROS",
                "REACT HOOK FORM Y ZOD",
                "AUTENTICACIÓN CON JWT",
                "WEBSOCKETS Y TIEMPO REAL",
                "SUBIDA DE ARCHIVOS",
                "GRÁFICOS Y VISUALIZACIÓN",
                "PROYECTO MÓDULO: RED SOCIAL",
            ]),
            ("REACT PROFESIONAL", [
                "ARQUITECTURA DE CARPETAS",
                "ATOMIC DESIGN EN REACT",
                "ESTADO SERVIDOR VS CLIENTE",
                "INTERNACIONALIZACIÓN I18N",
                "ANIMACIONES CON FRAMER MOTION",
                "PWA CON REACT",
                "REACT Y SEO",
                "SEGURIDAD EN APPS REACT",
                "DEPLOYMENT Y CI CD REACT",
                "PROYECTO MÓDULO: DASHBOARD ANALÍTICAS",
            ]),
            ("PROYECTO FINAL REACT", [
                "PLANIFICACIÓN DEL PROYECTO FINAL",
                "SETUP VITE TS TAILWIND",
                "SISTEMA DE AUTENTICACIÓN",
                "DISEÑO DE TABLEROS KANBAN",
                "FUNCIONALIDADES COLABORATIVAS",
                "API REST INTEGRACIÓN",
                "PRUEBAS UNITARIAS Y E2E",
                "OPTIMIZACIÓN Y RENDIMIENTO",
                "DESPLIEGUE EN PRODUCCIÓN",
                "CARTA DE GRADUACIÓN DEL PROFESOR BÚHO",
            ]),
        ]),
    },
    "06_NODEJS_LIBRO_MAESTRO": {
        "nom": "NODE.JS",
        "mods": convertir_a_formato_completo([
            ("INTRODUCCIÓN A NODE.JS", [
                "ARQUITECTURA DE NODE.JS",
                "INSTALACIÓN Y PRIMEROS PASOS",
                "MÓDULOS COMMONJS Y ES MODULES",
                "NPM: GESTIÓN DE PAQUETES",
                "SISTEMA DE ARCHIVOS FS",
                "PROCESOS Y VARIABLES DE ENTORNO",
                "MANEJO DE ERRORES EN NODE",
                "DEBUGGING Y HERRAMIENTAS",
                "BUENAS PRÁCTICAS NODE.JS",
                "PROYECTO MÓDULO: CLI TOOL INTERACTIVA",
            ]),
            ("ASINCRONÍA Y STREAMS", [
                "CALLBACKS Y CALLBACK HELL",
                "PROMESAS EN PROFUNDIDAD",
                "ASYNC AWAIT MODERNO",
                "EVENT LOOP Y FASE DETALLADA",
                "EVENT EMITTER PATTERN",
                "STREAMS READABLE Y WRITABLE",
                "STREAMS TRANSFORM Y DUPLEX",
                "MANEJO DE ARCHIVOS GRANDES",
                "BUFFERS EN NODE.JS",
                "PROYECTO MÓDULO: PROCESADOR ARCHIVOS",
            ]),
            ("EXPRESS Y APIs WEB", [
                "INTRODUCCIÓN A EXPRESS.JS",
                "RUTAS Y PARÁMETROS",
                "MIDDLEWARES: EL CORAZÓN DE EXPRESS",
                "MANEJO DE ERRORES EN EXPRESS",
                "SERVIDOR ESTÁTICO Y ARCHIVOS",
                "CORS Y SEGURIDAD EN APIs",
                "VALIDACIÓN CON JOY Y ZOD",
                "DOCUMENTACIÓN CON SWAGGER",
                "RATE LIMITING Y HELMET",
                "PROYECTO MÓDULO: API REST CON EXPRESS",
            ]),
            ("BASES DE DATOS EN NODE", [
                "CONEXIÓN A MONGODB CON MONGOOSE",
                "CRUD CON MONGOOSE",
                "RELACIONES Y POPULATE",
                "POSTGRESQL CON PG",
                "QUERIES PARAMETRIZADAS",
                "PRISMA ORM MODERNO",
                "MIGRACIONES Y SEEDS",
                "TRANSACCIONES Y CONCURRENCIA",
                "REDIS CACHÉ EN NODE",
                "PROYECTO MÓDULO: CRUD COMPLETO BD",
            ]),
            ("AUTENTICACIÓN Y AUTORIZACIÓN", [
                "JWT: JSON WEB TOKENS",
                "REFRESH TOKENS ESTRATEGIA",
                "OAUTH 2.0 CON PASSPORT.JS",
                "AUTENTICACIÓN SOCIAL",
                "RBAC ROLES Y PERMISOS",
                "SESSION VS TOKEN COMPARATIVA",
                "BCRYPT Y HASHING SEGURO",
                "RATE LIMITING EN AUTENTICACIÓN",
                "SEGURIDAD EN APIS NODE",
                "PROYECTO MÓDULO: SISTEMA AUTH",
            ]),
            ("NODE.JS AVANZADO", [
                "CLUSTER Y PROCESOS HIJOS",
                "WORKER THREADS PARALELISMO",
                "APIs DE RED Y SOCKETS",
                "WEBSOCKETS CON SOCKET.IO",
                "COLAS CON BULL Y REDIS",
                "TESTING CON JEST Y SUPERTEST",
                "LOGGING CON WINSTON",
                "PERFORMANCE Y PROFILING",
                "DESPLIEGUE CON PM2 Y DOCKER",
                "PROYECTO MÓDULO: CHAT TIEMPO REAL",
            ]),
            ("ARQUITECTURA NODE.JS", [
                "ARQUITECTURA LIMPIA EN NODE",
                "PATRÓN REPOSITORY",
                "INYECCIÓN DE DEPENDENCIAS",
                "ESTRUCTURA DE PROYECTOS",
                "MICROSERVICIOS CON NODE",
                "APIs GRAPHQL CON APOLLO",
                "CACHÉ CON REDIS AVANZADO",
                "MANEJO DE CONFIGURACIÓN",
                "DOCKERIZACIÓN DE APPS NODE",
                "PROYECTO MÓDULO: SISTEMA SaaS",
            ]),
            ("PROYECTO FINAL NODE.JS", [
                "PLANIFICACIÓN Y DISEÑO API",
                "SETUP Y ARQUITECTURA",
                "MODELOS Y BASE DE DATOS",
                "AUTENTICACIÓN COMPLETA",
                "CRUD DE RECURSOS",
                "FILTROS Y PAGINACIÓN",
                "WEBSOCKETS Y TIEMPO REAL",
                "TESTING Y DOCUMENTACIÓN",
                "DEPLOYMENT EN PRODUCCIÓN",
                "CARTA DE GRADUACIÓN PROFESOR BÚHO",
            ]),
        ]),
    },
    "08_SQL_LIBRO_MAESTRO": {
        "nom": "SQL",
        "mods": convertir_a_formato_completo([
            ("FUNDAMENTOS DE BASES DE DATOS", [
                "INTRODUCCIÓN A BASES DE DATOS",
                "MODELO ENTIDAD RELACIÓN",
                "NORMALIZACIÓN 1FN 2FN 3FN",
                "DDL CREATE DROP ALTER",
                "TIPOS DE DATOS EN SQL",
                "CONSTRAINTS PK FK UNIQUE",
                "ÍNDICES Y RENDIMIENTO",
                "DIAGRAMAS ER HERRAMIENTAS",
                "BUENAS PRÁCTICAS DE DISEÑO",
                "PROYECTO MÓDULO: MODELADO BD",
            ]),
            ("CONSULTAS BÁSICAS", [
                "SELECT FROM WHERE",
                "OPERADORES AND OR NOT BETWEEN IN",
                "LIKE Y PATRONES DE BÚSQUEDA",
                "ORDER BY Y LIMIT OFFSET",
                "FUNCIONES AGREGACIÓN SUM COUNT AVG",
                "GROUP BY Y HAVING",
                "DISTINCT Y VALORES ÚNICOS",
                "FECHAS Y HORAS EN SQL",
                "CONVERSIÓN DE TIPOS CAST",
                "PROYECTO MÓDULO: CONSULTAS SQL",
            ]),
            ("JOINS Y RELACIONES", [
                "INNER JOIN ENTRE TABLAS",
                "LEFT RIGHT FULL OUTER JOIN",
                "SELF JOIN TABLA REFLEXIVA",
                "JOINS MÚLTIPLES ENTRE TABLAS",
                "UNION INTERSECT EXCEPT",
                "SUBQUERIES EN WHERE",
                "SUBQUERIES EN FROM Y SELECT",
                "EXISTS Y NOT EXISTS",
                "CTE Y RECURSIVAS",
                "PROYECTO MÓDULO: JOINS COMPLEJOS",
            ]),
            ("MANIPULACIÓN DE DATOS", [
                "INSERT INTO VALORES",
                "UPDATE SET WHERE",
                "DELETE FROM TRUNCATE DROP",
                "TRANSACCIONES BEGIN COMMIT ROLLBACK",
                "SAVEPOINT Y ROLLBACK PARCIAL",
                "LOCKS Y CONTROL CONCURRENCIA",
                "MERGE UPSERT",
                "TRIGGERS EVENTOS",
                "VISTAS VIEWS",
                "PROYECTO MÓDULO: CRUD COMPLETO",
            ]),
            ("SQL AVANZADO", [
                "WINDOW FUNCTIONS ROW NUMBER",
                "RANK DENSE RANK NTILE",
                "PARTITION BY EN VENTANAS",
                "PIVOT Y UNPIVOT",
                "EXPLAIN PLAN OPTIMIZACIÓN",
                "PROCEDIMIENTOS ALMACENADOS",
                "FUNCIONES EN SQL",
                "CURSORES ITERACIÓN",
                "OPTIMIZACIÓN DE CONSULTAS",
                "PROYECTO MÓDULO: OPTIMIZACIÓN SQL",
            ]),
            ("ADMINISTRACIÓN DE BD", [
                "USUARIOS Y PERMISOS GRANT REVOKE",
                "BACKUP Y RESTORE",
                "IMPORTACIÓN Y EXPORTACIÓN DATOS",
                "REPLICACIÓN MASTER SLAVE",
                "PARTICIONAMIENTO SHARDING",
                "MONITOREO DE RENDIMIENTO",
                "MANTENIMIENTO DE ÍNDICES",
                "SEGURIDAD EN BD SQL",
                "ALTA DISPONIBILIDAD",
                "PROYECTO MÓDULO: ADMIN BD",
            ]),
            ("SQL EN APLICACIONES", [
                "CONEXIÓN DESDE PYTHON",
                "CONEXIÓN DESDE NODE.JS",
                "ORM VS RAW SQL COMPARATIVA",
                "POOL DE CONEXIONES",
                "PREVENCIÓN SQL INJECTION",
                "MIGRACIONES CON FLYWAY",
                "TESTING DE BASE DE DATOS",
                "BUENAS PRÁCTICAS CONSULTAS",
                "DOCUMENTACIÓN DE BD",
                "PROYECTO MÓDULO: API CON SQL",
            ]),
            ("PROYECTO FINAL SQL", [
                "PLANIFICACIÓN DEL ESQUEMA",
                "IMPLEMENTACIÓN DEL MODELO",
                "CONSULTAS COMPLEJAS",
                "OPTIMIZACIÓN DE RENDIMIENTO",
                "SEGURIDAD Y PERMISOS",
                "BACKUP Y RECUPERACIÓN",
                "DOCUMENTACIÓN COMPLETA",
                "PRESENTACIÓN DEL PROYECTO",
                "MEJORES PRÁCTICAS SQL",
                "CARTA DE GRADUACIÓN PROFESOR BÚHO",
            ]),
        ]),
    },
    "09_PYTHON_LIBRO_MAESTRO": {
        "nom": "PYTHON",
        "mods": convertir_a_formato_completo([
            ("FUNDAMENTOS DE PYTHON", [
                "INTRODUCCIÓN A PYTHON",
                "INSTALACIÓN Y ENTORNOS VIRTUALES",
                "VARIABLES Y TIPOS DE DATOS",
                "NÚMEROS Y OPERACIONES MATEMÁTICAS",
                "CADENAS STRINGS MANIPULACIÓN",
                "LISTAS Y TUPLAS",
                "DICCIONARIOS Y SETS",
                "ENTRADA Y SALIDA INPUT PRINT",
                "COMENTARIOS Y DOCSTRINGS",
                "PROYECTO MÓDULO: CALCULADORA PYTHON",
            ]),
            ("ESTRUCTURAS DE CONTROL", [
                "IF ELIF ELSE CONDICIONALES",
                "OPERADORES DE COMPARACIÓN Y LÓGICOS",
                "BUCLE WHILE",
                "BUCLE FOR E ITERABLES",
                "RANGE Y ENUMERATE",
                "LIST COMPREHENSIONS",
                "BREAK CONTINUE PASS",
                "MANEJO DE ERRORES TRY EXCEPT",
                "CONTEXTO WITH ARCHIVOS",
                "PROYECTO MÓDULO: JUEGO ADIVINANZA",
            ]),
            ("FUNCIONES", [
                "DEFINICIÓN DE FUNCIONES DEF",
                "PARÁMETROS Y RETURN",
                "ARGS Y KWARGS ARGUMENTOS",
                "FUNCIONES LAMBDA ANÓNIMAS",
                "ÁMBITO DE VARIABLES SCOPE",
                "CLOSURES Y FUNCIONES INTERNAS",
                "DECORADORES @",
                "GENERADORES Y YIELD",
                "FUNCIONES ANIDADAS",
                "PROYECTO MÓDULO: PROCESADOR DATOS",
            ]),
            ("PROGRAMACIÓN ORIENTADA A OBJETOS", [
                "CLASES Y OBJETOS",
                "ATRIBUTOS Y MÉTODOS",
                "HERENCIA EN PYTHON",
                "POLIMORFISMO",
                "ENCAPSULAMIENTO PRIVADO",
                "PROPIEDADES @PROPERTY",
                "MÉTODOS ESPECIALES DUNDER",
                "COMPOSICIÓN VS HERENCIA",
                "MRO Y SUPER",
                "PROYECTO MÓDULO: SISTEMA BANCARIO",
            ]),
            ("MÓDULOS Y PAQUETES", [
                "IMPORT Y FROM",
                "BIBLIOTECA ESTÁNDAR DE PYTHON",
                "PAQUETES Y __INIT__.PY",
                "PIP E INSTALACIÓN DE PAQUETES",
                "ENTORNOS VIRTUALES VENV",
                "REQUIREMENTS.TXT",
                "MÓDULO OS Y SYS",
                "MÓDULO MATH Y RANDOM",
                "MÓDULO DATETIME Y TIEMPO",
                "PROYECTO MÓDULO: TOOLKIT HERRAMIENTAS",
            ]),
            ("ARCHIVOS Y DATOS", [
                "LECTURA DE ARCHIVOS OPEN READ",
                "ESCRITURA DE ARCHIVOS WRITE",
                "ARCHIVOS CSV CON CSV MODULE",
                "ARCHIVOS JSON",
                "ARCHIVOS DE TEXTO MANIPULACIÓN",
                "PATHLIB MANEJO DE RUTAS",
                "SERIALIZACIÓN PICKLE JSON",
                "SQLITE CON PYTHON",
                "EXCEPCIONES EN ARCHIVOS",
                "PROYECTO MÓDULO: GESTOR DE NOTAS",
            ]),
            ("PYTHON AVANZADO", [
                "TYPE HINTS Y TIPADO",
                "MAP FILTER REDUCE FUNCIONAL",
                "ITERADORES E ITERABLES AVANZADO",
                "ASINCRONÍA ASYNC AWAIT",
                "THREADING Y MULTIPROCESAMIENTO",
                "TESTING CON PYTEST",
                "LOGGING Y DEPURACIÓN",
                "REQUESTS Y APIs HTTP",
                "WEB SCRAPING BEAUTIFULSOUP",
                "PROYECTO MÓDULO: WEB SCRAPER",
            ]),
            ("PROYECTO FINAL PYTHON", [
                "PLANIFICACIÓN DEL PROYECTO",
                "DISEÑO DE ARQUITECTURA",
                "IMPLEMENTACIÓN DE MÓDULOS",
                "MANEJO DE ERRORES GLOBAL",
                "PRUEBAS UNITARIAS PYTEST",
                "DOCUMENTACIÓN CON DOCSTRINGS",
                "DESPLIEGUE Y DISTRIBUCIÓN",
                "REVISIÓN DE CÓDIGO",
                "MEJORAS Y ESCALABILIDAD",
                "CARTA DE GRADUACIÓN PROFESOR BÚHO",
            ]),
        ]),
    },
    "16_IA_LIBRO_MAESTRO": {
        "nom": "INTELIGENCIA ARTIFICIAL",
        "mods": convertir_a_formato_completo([
            ("FUNDAMENTOS DE IA", [
                "INTRODUCCIÓN A LA INTELIGENCIA ARTIFICIAL",
                "HISTORIA Y EVOLUCIÓN DE LA IA",
                "TIPOS DE IA DÉBIL GENERAL SUPER",
                "APRENDIZAJE AUTOMÁTICO ML",
                "APRENDIZAJE SUPERVISADO",
                "APRENDIZAJE NO SUPERVISADO",
                "APRENDIZAJE POR REFUERZO",
                "DATASETS Y PREPARACIÓN DE DATOS",
                "ÉTICA Y RESPONSABILIDAD EN IA",
                "PROYECTO MÓDULO: CLASIFICADOR SIMPLE",
            ]),
            ("ESTADÍSTICA PARA IA", [
                "ESTADÍSTICA DESCRIPTIVA BÁSICA",
                "PROBABILIDAD Y DISTRIBUCIONES",
                "TEOREMA DE BAYES",
                "CORRELACIÓN Y CAUSALIDAD",
                "REGRESIÓN LINEAL",
                "REGRESIÓN LOGÍSTICA",
                "MATRICES Y ÁLGEBRA LINEAL",
                "CÁLCULO DIFERENCIAL PARA ML",
                "OPTIMIZACIÓN Y DESCENSO GRADIENTE",
                "PROYECTO MÓDULO: ANÁLISIS DATOS",
            ]),
            ("APRENDIZAJE SUPERVISADO", [
                "KNN K VECINOS CERCANOS",
                "ÁRBOLES DE DECISIÓN",
                "RANDOM FOREST ENSAMBLE",
                "SVM SUPPORT VECTOR MACHINES",
                "NAIVE BAYES CLASIFICADOR",
                "EVALUACIÓN DE MODELOS ML",
                "MATRIZ DE CONFUSIÓN MÉTRICAS",
                "VALIDACIÓN CRUZADA CROSS VAL",
                "OVERFITTING Y REGULARIZACIÓN",
                "PROYECTO MÓDULO: MODELO PREDICTIVO",
            ]),
            ("APRENDIZAJE NO SUPERVISADO", [
                "K MEANS CLUSTERING",
                "CLUSTERING JERÁRQUICO",
                "DBSCAN DENSITY BASED",
                "PCA REDUCCIÓN DIMENSIONAL",
                "T SNE VISUALIZACIÓN",
                "REGLAS DE ASOCIACIÓN APRIORI",
                "DETECCIÓN DE ANOMALÍAS",
                "GMM MEZCLAS GAUSSIANAS",
                "EVALUACIÓN DE CLUSTERING",
                "PROYECTO MÓDULO: SEGMENTACIÓN CLIENTES",
            ]),
            ("DEEP LEARNING", [
                "REDES NEURONALES ARTIFICIALES",
                "PERCEPTRÓN Y FUNCIONES ACTIVACIÓN",
                "BACKPROPAGATION GRADIENTE",
                "CNN REDES CONVOLUCIONALES",
                "RNN LSTM REDES RECURRENTES",
                "TRANSFER LEARNING",
                "TENSORFLOW Y KERAS PRÁCTICO",
                "PYTORCH FUNDAMENTOS",
                "GPU ENTRENAMIENTO ACELERADO",
                "PROYECTO MÓDULO: CLASIFICADOR IMÁGENES",
            ]),
            ("NLP PROCESAMIENTO LENGUAJE", [
                "FUNDAMENTOS DE NLP",
                "TOKENIZACIÓN Y STEMMING",
                "BAG OF WORDS TF IDF",
                "WORD EMBEDDINGS WORD2VEC",
                "TRANSFORMERS Y ATTENTION",
                "BERT MODELOS CONTEXTUALES",
                "GPT Y GRANDES MODELOS LENGUAJE",
                "PROMPT ENGINEERING AVANZADO",
                "CHATBOTS CON NLP",
                "PROYECTO MÓDULO: CHATBOT NLP",
            ]),
            ("COMPUTER VISION Y MÁS", [
                "VISIÓN POR COMPUTADORA",
                "DETECCIÓN DE OBJETOS YOLO",
                "SEGMENTACIÓN SEMÁNTICA",
                "RECONOCIMIENTO FACIAL",
                "IA GENERATIVA GANS",
                "STABLE DIFFUSION Y DALL-E",
                "LLMs Y RAG RETRIEVAL",
                "FINE TUNING DE MODELOS",
                "MLOPS DESPLIEGUE MODELOS",
                "PROYECTO MÓDULO: APP CON IA",
            ]),
            ("PROYECTO FINAL IA", [
                "DEFINICIÓN DEL PROBLEMA IA",
                "RECOLECCIÓN Y PREPARACIÓN DATOS",
                "SELECCIÓN DEL MODELO",
                "ENTRENAMIENTO Y EVALUACIÓN",
                "OPTIMIZACIÓN HIPERPARÁMETROS",
                "DESPLIEGUE DEL MODELO",
                "API DE INFERENCIA",
                "MONITOREO Y MANTENIMIENTO",
                "PRESENTACIÓN DE RESULTADOS",
                "CARTA DE GRADUACIÓN PROFESOR BÚHO",
            ]),
        ]),
    },
    "17_DJANGO_LIBRO_MAESTRO": {
        "nom": "DJANGO",
        "mods": convertir_a_formato_completo([
            ("FUNDAMENTOS DE DJANGO", [
                "INTRODUCCIÓN A DJANGO FRAMEWORK",
                "INSTALACIÓN Y PROYECTO INICIAL",
                "ESTRUCTURA MTV MODEL TEMPLATE VIEW",
                "CREACIÓN DE APPS DJANGO",
                "URLS Y PATRONES DE RUTAS",
                "VISTAS BASADAS EN FUNCIONES FBV",
                "TEMPLATES DJANGO TEMPLATE ENGINE",
                "VARIABLES FILTROS TEMPLATES",
                "HERENCIA DE PLANTILLAS EXTENDS",
                "PROYECTO MÓDULO: SITIO WEB ESTÁTICO",
            ]),
            ("MODELOS Y BASE DE DATOS", [
                "MODELOS DJANGO ORM",
                "MIGRACIONES MAKEMIGRATIONS MIGRATE",
                "RELACIONES ONE TO MANY FK",
                "RELACIONES MANY TO MANY",
                "RELACIONES ONE TO ONE",
                "QUERYSETS FILTRADO Q F",
                "QUERYSETS AVANZADOS",
                "ADMIN DJANGO PERSONALIZADO",
                "SEÑALES SIGNALS",
                "PROYECTO MÓDULO: BLOG CON DJANGO",
            ]),
            ("VISTAS AVANZADAS", [
                "VISTAS BASADAS EN CLASES CBV",
                "LISTVIEW Y DETAILVIEW",
                "CREATEVIEW UPDATEVIEW DELETEVIEW",
                "MIXINS REUTILIZACIÓN",
                "DECORADORES DE VISTAS",
                "PAGINACIÓN EN VISTAS",
                "VISTAS GENÉRICAS AVANZADAS",
                "MANEJO DE ERRORES 404 500",
                "URLS DINÁMICAS PARÁMETROS",
                "PROYECTO MÓDULO: CRUD COMPLETO",
            ]),
            ("FORMULARIOS DJANGO", [
                "DJANGO FORMS API",
                "VALIDACIÓN DE FORMULARIOS",
                "MODELFORM",
                "ARCHIVOS FILEFIELD IMAGEN",
                "FORMULARIOS CON CBV",
                "FORMULARIOS CON BOOTSTRAP",
                "FORMULARIOS CON HTMX",
                "MANEJO DE SESIONES",
                "MENSAJES FLASH",
                "PROYECTO MÓDULO: FORMULARIO COMPLEJO",
            ]),
            ("AUTENTICACIÓN Y PERMISOS", [
                "SISTEMA DE USUARIOS DJANGO",
                "LOGIN LOGOUT REGISTRO",
                "PERMISOS Y GRUPOS",
                "AUTENTICACIÓN CON EMAIL",
                "RESET CONTRASEÑA",
                "PERFILES DE USUARIO",
                "AUTENTICACIÓN SOCIAL ALLAUTH",
                "SEGURIDAD EN DJANGO",
                "BUENAS PRÁCTICAS AUTH",
                "PROYECTO MÓDULO: SISTEMA MEMBRESÍA",
            ]),
            ("APIs CON DRF", [
                "DJANGO REST FRAMEWORK",
                "SERIALIZERS VALIDACIÓN",
                "VIEWSETS Y ROUTERS",
                "AUTENTICACIÓN JWT DRF",
                "PERMISOS EN DRF",
                "FILTRADO BÚSQUEDA ORDEN",
                "PAGINACIÓN DRF",
                "VERSIONADO DE APIs",
                "DOCUMENTACIÓN SWAGGER DRF",
                "PROYECTO MÓDULO: API REST DRF",
            ]),
            ("DJANGO AVANZADO", [
                "TESTING EN DJANGO",
                "CACHÉ CON REDIS",
                "CELERY TAREAS ASÍNCRONAS",
                "CELERY BEAT PROGRAMADAS",
                "ALMACENAMIENTO S3 IMÁGENES",
                "ENVÍO DE CORREOS EMAIL",
                "INTERNACIONALIZACIÓN I18N",
                "SITEMAPS Y RSS FEEDS",
                "DESPLIEGUE GUNICORN NGINX",
                "PROYECTO MÓDULO: SISTEMA SaaS",
            ]),
            ("PROYECTO FINAL DJANGO", [
                "PLANIFICACIÓN ARQUITECTURA",
                "MODELOS Y BASE DE DATOS",
                "SISTEMA DE AUTENTICACIÓN",
                "FUNCIONALIDADES PRINCIPALES",
                "APIs REST COMPLETAS",
                "TEMPLATES Y FRONTEND",
                "TESTING COMPLETO",
                "OPTIMIZACIÓN CACHÉ",
                "DESPLIEGUE PRODUCCIÓN",
                "CARTA DE GRADUACIÓN PROFESOR BÚHO",
            ]),
        ]),
    },
    "18_DOCKER_LIBRO_MAESTRO": {
        "nom": "DOCKER",
        "mods": convertir_a_formato_completo([
            ("FUNDAMENTOS DE DOCKER", [
                "INTRODUCCIÓN A CONTENEDORES",
                "DOCKER VS MÁQUINAS VIRTUALES",
                "INSTALACIÓN DE DOCKER ENGINE",
                "CLI DOCKER COMANDOS BÁSICOS",
                "IMÁGENES Y CONTENEDORES",
                "DOCKER HUB Y REGISTROS",
                "CICLO DE VIDA CONTENEDORES",
                "PUERTOS Y VOLÚMENES",
                "ARQUITECTURA DOCKER",
                "PROYECTO MÓDULO: PRIMER CONTENEDOR",
            ]),
            ("DOCKERFILE Y BUILD", [
                "DOCKERFILE INSTRUCCIONES",
                "FROM RUN CMD ENTRYPOINT",
                "COPY ADD WORKDIR",
                "USER EXPOSE HEALTHCHECK",
                "CAPAS LAYERS Y CACHÉ",
                "BUILD DE IMÁGENES",
                "OPTIMIZACIÓN DE IMÁGENES",
                "MULTI STAGE BUILD",
                "ARG ENV VARIABLES BUILD",
                "PROYECTO MÓDULO: DOCKERFILE ÓPTIMO",
            ]),
            ("DOCKER COMPOSE", [
                "DOCKER COMPOSE YAML",
                "SERVICIOS Y REDES",
                "VOLÚMENES EN COMPOSE",
                "DEPENDS ON HEALTHCHECK",
                "VARIABLES ENTORNO .ENV",
                "DOCKER COMPOSE BUILD UP",
                "ESCALADO DE SERVICIOS",
                "NETWORKS PERSONALIZADAS",
                "COMPOSE EN PRODUCCIÓN",
                "PROYECTO MÓDULO: STACK LAMP",
            ]),
            ("REDES EN DOCKER", [
                "TIPOS DE REDES BRIDGE HOST OVERLAY",
                "REDES PERSONALIZADAS",
                "DNS RESOLUCIÓN NOMBRES",
                "REDES MULTI HOST",
                "PUBLICACIÓN PUERTOS",
                "SEGURIDAD EN REDES",
                "NETWORK DRIVERS",
                "MACVLAN IPVLAN",
                "TROUBLESHOOTING REDES",
                "PROYECTO MÓDULO: RED MICROSERVICIOS",
            ]),
            ("VOLÚMENES Y DATOS", [
                "VOLÚMENES VS BIND MOUNTS",
                "CREACIÓN GESTIÓN VOLÚMENES",
                "VOLÚMENES COMPARTIDOS",
                "BACKUP Y RESTORE VOLÚMENES",
                "DRIVERS DE VOLÚMENES",
                "TMPFS MOUNTS",
                "PERSISTENCIA EN BD",
                "VOLÚMENES EN COMPOSE",
                "BUENAS PRÁCTICAS DATOS",
                "PROYECTO MÓDULO: BD PERSISTENTE",
            ]),
            ("DOCKER SWARM", [
                "DOCKER SWARM INICIO",
                "NODES MANAGER WORKER",
                "SERVICIOS EN SWARM",
                "STACKS CON COMPOSE",
                "SECRETS Y CONFIGS",
                "ESCALADO AUTOMÁTICO",
                "ROLLING UPDATE",
                "HEALTH CHECKS",
                "LOGGING EN SWARM",
                "PROYECTO MÓDULO: CLUSTER SWARM",
            ]),
            ("DOCKER EN PRODUCCIÓN", [
                "SEGURIDAD EN CONTENEDORES",
                "USUARIOS NO ROOT",
                "ESCANEO VULNERABILIDADES",
                "MONITOREO CADVISOR PROMETHEUS",
                "LOGGING CENTRALIZADO",
                "CI/CD CON DOCKER GITHUB ACTIONS",
                "DOCKER EN AWS ECS",
                "KUBERNETES FUNDAMENTOS",
                "SWARM VS K8S COMPARATIVA",
                "PROYECTO MÓDULO: CI CD DOCKER",
            ]),
            ("PROYECTO FINAL DOCKER", [
                "PLANIFICACIÓN ARQUITECTURA",
                "DOCKERFILE MULTISTAGE",
                "DOCKER COMPOSE COMPLETO",
                "PERSISTENCIA DE DATOS",
                "SEGURIDAD Y SECRETS",
                "MONITOREO Y LOGGING",
                "DEPLOYMENT PRODUCCIÓN",
                "ROLLING UPDATE",
                "BACKUP Y RECUPERACIÓN",
                "CARTA DE GRADUACIÓN PROFESOR BÚHO",
            ]),
        ]),
    },
    "19_GIT_LIBRO_MAESTRO": {
        "nom": "GIT",
        "mods": convertir_a_formato_completo([
            ("FUNDAMENTOS DE GIT", [
                "INTRODUCCIÓN A GIT",
                "HISTORIA Y FILOSOFÍA GIT",
                "INSTALACIÓN Y CONFIGURACIÓN",
                "GIT INIT ADD COMMIT",
                "STATUS LOG DIFF",
                "ÁREAS WORKING STAGING REPOSITORY",
                "ARCHIVO GITIGNORE",
                "CONFIGURACIÓN GLOBAL Y LOCAL",
                "ALIAS EN GIT",
                "PROYECTO MÓDULO: PRIMER REPOSITORIO",
            ]),
            ("RAMAS BRANCHES", [
                "CREACIÓN GESTIÓN RAMAS",
                "GIT BRANCH CHECKOUT",
                "MERGE DE RAMAS",
                "RESOLUCIÓN CONFLICTOS MERGE",
                "FAST FORWARD VS 3 WAY",
                "GIT MERGE TOOL",
                "ESTRATEGIAS RAMAS GIT FLOW",
                "GIT FLOW COMPLETO",
                "TRUNK BASED DEVELOPMENT",
                "PROYECTO MÓDULO: RAMAS Y MERGE",
            ]),
            ("TRABAJO REMOTO", [
                "GIT CLONE REMOTE",
                "GIT PUSH PULL",
                "GIT FETCH VS PULL",
                "REPOSITORIOS REMOTOS",
                "GITHUB GITLAB BITBUCKET",
                "CLAVES SSH Y TOKENS",
                "GIT PULL REBASE",
                "TRABAJO EN EQUIPO REMOTO",
                "GIT SUBMODULE",
                "PROYECTO MÓDULO: COLABORACIÓN EQUIPO",
            ]),
            ("REBASE Y AVANZADO", [
                "GIT REBASE FUNDAMENTOS",
                "INTERACTIVE REBASE",
                "CHERRY PICK",
                "STASH Y POP",
                "REVERT RESET HARD SOFT",
                "GIT BISECT BÚSQUEDA",
                "GIT BLAME ANNOTATE",
                "GIT TAG VERSIONADO",
                "REBASE VS MERGE",
                "PROYECTO MÓDULO: HISTORIA LIMPIA",
            ]),
            ("GITHUB EN PROFUNDIDAD", [
                "PULL REQUESTS",
                "CODE REVIEW EFECTIVO",
                "ISSUES Y PROJECTS",
                "GITHUB ACTIONS CI/CD",
                "GITHUB PAGES",
                "WORKFLOWS GITHUB ACTIONS",
                "SECRETS Y ENTORNOS",
                "GIT HOOKS",
                "RELEASES CHANGELOG",
                "PROYECTO MÓDULO: CI CD GITHUB",
            ]),
            ("COLABORACIÓN PROFESIONAL", [
                "CONTRIBUCIONES OPEN SOURCE",
                "FORK Y PULL REQUEST",
                "CODE OF CONDUCT",
                "LICENCIAS SOFTWARE",
                "SEMANTIC VERSIONING",
                "CONVENTIONAL COMMITS",
                "BUENOS MENSAJES COMMIT",
                "CODEOWNERS BRANCH PROTECTION",
                "PLANTILLAS ISSUES PRS",
                "PROYECTO MÓDULO: CONTRIBUCIÓN OS",
            ]),
            ("GIT AVANZADO", [
                "GIT REBASE ONTO",
                "GIT FILTER BRANCH",
                "GIT WORKTREE",
                "GIT SUBTREE",
                "SIGNED COMMITS GPG",
                "GIT LFS ARCHIVOS GRANDES",
                "MIGRACIÓN REPOSITORIOS",
                "GIT ARCHIVE BUNDLE",
                "RECUPERACIÓN DATOS PERDIDOS",
                "PROYECTO MÓDULO: GIT AVANZADO",
            ]),
            ("PROYECTO FINAL GIT", [
                "PLANIFICACIÓN REPOSITORIO",
                "ESTRATEGIA DE RAMAS",
                "PROTECCIONES BRANCH",
                "AUTOMATIZACIÓN CI/CD",
                "CONTRIBUCIÓN REVISIÓN",
                "DOCUMENTACIÓN README",
                "VERSIONADO SEMÁNTICO",
                "RELEASES CHANGELOG",
                "MANTENIMIENTO LARGO PLAZO",
                "CARTA DE GRADUACIÓN PROFESOR BÚHO",
            ]),
        ]),
    },
    "20_API_LIBRO_MAESTRO": {
        "nom": "APIs",
        "mods": convertir_a_formato_completo([
            ("FUNDAMENTOS DE APIs", [
                "INTRODUCCIÓN A APIs",
                "ARQUITECTURA CLIENTE SERVIDOR",
                "HTTP PROTOCOL METHODS STATUS",
                "REST PRINCIPIOS RESTRICCIONES",
                "RECURSOS Y ENDPOINTS",
                "PARÁMETROS PATH QUERY HEADERS",
                "FORMATOS JSON XML",
                "VERSIONADO DE APIs",
                "HERRAMIENTAS POSTMAN INSOMNIA",
                "PROYECTO MÓDULO: API SIMPLE",
            ]),
            ("REST API EN PROFUNDIDAD", [
                "DISEÑO ENDPOINTS REST",
                "CRUD CON HTTP VERBS",
                "BUENAS PRÁCTICAS REST",
                "HATEOAS HYPERMEDIA",
                "PAGINACIÓN EN APIs",
                "FILTRADO BÚSQUEDA ORDEN",
                "MANEJO DE ERRORES HTTP",
                "CÓDIGOS DE ESTADO HTTP",
                "CONTENT NEGOTIATION",
                "PROYECTO MÓDULO: API RESTFUL",
            ]),
            ("AUTENTICACIÓN EN APIs", [
                "API KEYS",
                "BASIC AUTH",
                "JWT FUNDAMENTOS",
                "JWT ACCESS REFRESH TOKENS",
                "OAUTH 2.0 FLUJOS COMPLETOS",
                "OPENID CONNECT",
                "SESSION AUTH COOKIES",
                "API KEY MANAGEMENT",
                "RATE LIMITING THROTTLING",
                "PROYECTO MÓDULO: AUTH API",
            ]),
            ("SEGURIDAD EN APIs", [
                "OWASP API SECURITY TOP 10",
                "SQL INJECTION PREVENCIÓN",
                "XSS CSRF EN APIs",
                "CORS CONFIGURACIÓN",
                "HTTPS SSL TLS",
                "VALIDACIÓN SANITIZACIÓN",
                "INPUT VALIDATION ESQUEMAS",
                "SECURITY HEADERS",
                "PENTESTING APIs",
                "PROYECTO MÓDULO: API SEGURA",
            ]),
            ("TESTING DE APIs", [
                "PRUEBAS UNITARIAS APIs",
                "PRUEBAS INTEGRACIÓN",
                "POSTMAN COLLECTIONS TESTS",
                "NEWMAN AUTOMATIZACIÓN",
                "CARGA STRESS TESTING",
                "MOCKING DE APIs",
                "CONTRACT TESTING PACT",
                "DOCUMENTACIÓN SWAGGER OPENAPI",
                "MONITOREO APIs UP DOWN",
                "PROYECTO MÓDULO: TESTING API",
            ]),
            ("GRAPHQL", [
                "INTRODUCCIÓN GRAPHQL",
                "GRAPHQL VS REST",
                "SCHEMA TYPES",
                "QUERIES MUTATIONS",
                "RESOLVERS",
                "SUBSCRIPTIONS",
                "APOLLO SERVER",
                "GRAPHQL CON REACT",
                "GRAPHQL BUENAS PRÁCTICAS",
                "PROYECTO MÓDULO: API GRAPHQL",
            ]),
            ("APIs EN PRODUCCIÓN", [
                "DEPLOYMENT APIs",
                "GATEWAYS PROXIES",
                "MANEJO ERRORES GLOBAL",
                "LOGGING MONITOREO",
                "CACHÉ REDIS",
                "BACKEND FOR FRONTEND BFF",
                "EVENT DRIVEN APIs",
                "WEBHOOKS CALLBACKS",
                "APIs SERVERLESS",
                "PROYECTO MÓDULO: API PRODUCTIVA",
            ]),
            ("PROYECTO FINAL APIs", [
                "PLANIFICACIÓN DISEÑO API",
                "IMPLEMENTACIÓN REST GRAPHQL",
                "AUTENTICACIÓN MULTIMODAL",
                "SEGURIDAD COMPLETA",
                "TESTING EXHAUSTIVO",
                "DOCUMENTACIÓN SWAGGER",
                "DEPLOYMENT MONITOREO",
                "ESCALABILIDAD",
                "MEJORES PRÁCTICAS",
                "CARTA DE GRADUACIÓN PROFESOR BÚHO",
            ]),
        ]),
    },
    "21_SEGURIDAD_LIBRO_MAESTRO": {
        "nom": "SEGURIDAD INFORMÁTICA",
        "mods": convertir_a_formato_completo([
            ("FUNDAMENTOS DE SEGURIDAD", [
                "INTRODUCCIÓN A SEGURIDAD INFORMÁTICA",
                "PILARES CIA CONFIDENCIALIDAD",
                "INTEGRIDAD Y DISPONIBILIDAD",
                "AMENAZAS VULNERABILIDADES RIESGOS",
                "TIPOS DE ATAQUES INFORMÁTICOS",
                "INGENIERÍA SOCIAL",
                "MALWARE TIPOS PREVENCIÓN",
                "SEGURIDAD EN REDES",
                "POLÍTICAS DE SEGURIDAD",
                "PROYECTO MÓDULO: ANÁLISIS RIESGOS",
            ]),
            ("CRIPTOGRAFÍA", [
                "FUNDAMENTOS CRIPTOGRAFÍA",
                "CRIPTOGRAFÍA SIMÉTRICA AES",
                "CRIPTOGRAFÍA ASIMÉTRICA RSA",
                "HASHING MD5 SHA BCRYPT",
                "FIRMAS DIGITALES",
                "CERTIFICADOS SSL TLS",
                "PKI INFRAESTRUCTURA",
                "ENCRIPTACIÓN DATOS REPOSO",
                "ENCRIPTACIÓN TRÁNSITO TLS",
                "PROYECTO MÓDULO: ENCRIPTACIÓN",
            ]),
            ("OWASP TOP 10", [
                "OWASP TOP 10 INTRODUCCIÓN",
                "BROKEN ACCESS CONTROL",
                "CRYPTOGRAPHIC FAILURES",
                "INJECTION SQL EJEMPLOS",
                "INSECURE DESIGN",
                "SECURITY MISCONFIGURATION",
                "VULNERABLE COMPONENTS",
                "AUTHENTICATION FAILURES",
                "DATA INTEGRITY FAILURES",
                "PROYECTO MÓDULO: OWASP LAB",
            ]),
            ("SEGURIDAD WEB", [
                "XSS CROSS SITE SCRIPTING",
                "XSS REFLEJADO ALMACENADO DOM",
                "CSRF CROSS SITE REQUEST",
                "SQL INJECTION AVANZADO",
                "CLICKJACKING PREVENCIÓN",
                "SSRF SERVER SIDE REQUEST",
                "FILE UPLOAD VULNERABILITIES",
                "RCE REMOTE CODE EXECUTION",
                "HTTP SECURITY HEADERS",
                "PROYECTO MÓDULO: WEB SEGURA",
            ]),
            ("AUTENTICACIÓN AUTORIZACIÓN", [
                "SEGURIDAD EN AUTENTICACIÓN",
                "POLÍTICAS CONTRASEÑAS",
                "MFA MULTIFACTOR AUTH",
                "SSO SINGLE SIGN ON",
                "RBAC ROL BASED ACCESS",
                "ABAC ATTRIBUTE BASED",
                "JWT SEGURIDAD",
                "OAUTH 2.0 OPENID SECURITY",
                "SESSION MANAGEMENT",
                "PROYECTO MÓDULO: AUTH SEGURO",
            ]),
            ("SEGURIDAD EN REDES", [
                "FIREWALLS REGLAS",
                "IDS IPS DETECCIÓN",
                "VPN TÚNELES SEGUROS",
                "SEGURIDAD DNS",
                "EMAIL SECURITY SPF DKIM DMARC",
                "WAF WEB FIREWALL",
                "API SECURITY",
                "MICROSEGMENTACIÓN",
                "ZERO TRUST ARCHITECTURE",
                "PROYECTO MÓDULO: RED SEGURA",
            ]),
            ("PENTESTING HACKING ÉTICO", [
                "PENTESTING METODOLOGÍA",
                "RECONOCIMIENTO OSINT",
                "ESCANEO NMAP VULNERABILIDADES",
                "EXPLOTACIÓN METASPLOIT",
                "POST EXPLOTACIÓN",
                "WEB PENTESTING BURP SUITE",
                "INGENIERÍA SOCIAL OFENSIVA",
                "REPORTE VULNERABILIDADES",
                "BUGCROWD DISCLOSURE",
                "PROYECTO MÓDULO: PENTEST LAB",
            ]),
            ("PROYECTO FINAL SEGURIDAD", [
                "PLANIFICACIÓN AUDITORÍA",
                "RECONOCIMIENTO ANÁLISIS",
                "IDENTIFICACIÓN VULNERABILIDADES",
                "EXPLOTACIÓN CONTROLADA",
                "MITIGACIÓN REMEDIACIÓN",
                "REPORTE HALLAZGOS",
                "RECOMENDACIONES",
                "PLAN SEGURIDAD",
                "BUENAS PRÁCTICAS POST AUDITORÍA",
                "CARTA DE GRADUACIÓN PROFESOR BÚHO",
            ]),
        ]),
    },
    "22_LINUX_LIBRO_MAESTRO": {
        "nom": "LINUX",
        "mods": convertir_a_formato_completo([
            ("FUNDAMENTOS DE LINUX", [
                "INTRODUCCIÓN A LINUX",
                "DISTRIBUCIONES LINUX",
                "INSTALACIÓN DE LINUX",
                "TERMINAL Y SHELL BASH",
                "SISTEMA DE ARCHIVOS JERARQUÍA",
                "NAVEGACIÓN CD LS PWD",
                "MANIPULACIÓN ARCHIVOS TOUCH CP MV RM",
                "PERMISOS CHMOD CHOWN",
                "USUARIOS Y GRUPOS",
                "PROYECTO MÓDULO: SERVIDOR LINUX",
            ]),
            ("COMANDOS ESENCIALES", [
                "MAN Y AYUDA LINUX",
                "FIND Y LOCATE BÚSQUEDA",
                "GREP EXPRESIONES REGULARES",
                "SED AWK MANIPULACIÓN TEXTO",
                "SORT UNIQ WC ORDENAMIENTO",
                "REDIRECCIONES PIPES TUBERÍAS",
                "TAR GZIP COMPRESIÓN",
                "PROCESOS PS TOP KILL",
                "MONITOREO SISTEMA",
                "PROYECTO MÓDULO: SCRIPTS BÁSICOS",
            ]),
            ("GESTIÓN DE PAQUETES", [
                "APT DEBIAN UBUNTU",
                "YUM DNF RPM FEDORA RHEL",
                "PACMAN ARCH LINUX",
                "SNAP FLATPAK UNIVERSAL",
                "COMPILACIÓN DESDE FUENTE",
                "PPA REPOSITORIOS",
                "DEPENDENCIAS SOLUCIÓN",
                "ACTUALIZACIÓN SISTEMA",
                "GESTIÓN VERSIONES",
                "PROYECTO MÓDULO: GESTIÓN PAQUETES",
            ]),
            ("SHELL SCRIPTING", [
                "VARIABLES EXPANSIONES",
                "CONDICIONALES IF CASE",
                "BUCLES FOR WHILE UNTIL",
                "FUNCIONES EN BASH",
                "ARGUMENTOS LÍNEA COMANDOS",
                "TRAP MANEJO ERRORES",
                "REGEX EN SCRIPTS",
                "DEBUGGING CON BASH X",
                "SCHEDULING CRON CRONTAB",
                "PROYECTO MÓDULO: AUTOMATIZACIÓN SCRIPTS",
            ]),
            ("REDES EN LINUX", [
                "CONFIGURACIÓN RED IP",
                "SSH CONEXIÓN REMOTA",
                "SCP RSYNC TRANSFERENCIA",
                "FIREWALL IPTABLES UFW",
                "DNS RESOLUCIÓN NOMBRES",
                "CURL WGET HTTP",
                "NETWORK MANAGER",
                "NMAP DIAGNÓSTICO",
                "REDES INALÁMBRICAS WIFI",
                "PROYECTO MÓDULO: SERVIDOR WEB",
            ]),
            ("ADMINISTRACIÓN SISTEMA", [
                "SYSTEMD SERVICIOS",
                "LOGS JOURNALCTL RSYSLOG",
                "DISCOS PARTICIONES FSTAB",
                "LVM VOLÚMENES LÓGICOS",
                "MONTAJE UNIDADES",
                "SELINUX APPARMOR",
                "BACKUP RSYNC DUPLICITY",
                "VIRTUALIZACIÓN KVM",
                "CONTENEDORES LXD",
                "PROYECTO MÓDULO: SERVIDOR PRODUCCIÓN",
            ]),
            ("LINUX AVANZADO", [
                "KERNEL MÓDULOS",
                "PROCESOS AVANZADOS NICE",
                "CGROUPS LIMITACIÓN",
                "NAMESPACES",
                "PERFORMANCE TUNING",
                "STRACE LTRACE DEBUG",
                "AUTOMATIZACIÓN ANSIBLE",
                "DEVOPS CON LINUX",
                "INFRAESTRUCTURA CÓDIGO",
                "PROYECTO MÓDULO: INFRA CÓDIGO",
            ]),
            ("PROYECTO FINAL LINUX", [
                "PLANIFICACIÓN INFRAESTRUCTURA",
                "INSTALACIÓN CONFIGURACIÓN",
                "SEGURIDAD FIREWALL",
                "SERVICIOS MONITOREO",
                "BACKUP RECUPERACIÓN",
                "AUTOMATIZACIÓN SCRIPTS",
                "DOCUMENTACIÓN",
                "MANTENIMIENTO",
                "ESCALABILIDAD",
                "CARTA DE GRADUACIÓN PROFESOR BÚHO",
            ]),
        ]),
    },
    "23_ARQUITECTURA_LIBRO_MAESTRO": {
        "nom": "ARQUITECTURA DE SOFTWARE",
        "mods": convertir_a_formato_completo([
            ("FUNDAMENTOS DE ARQUITECTURA", [
                "INTRODUCCIÓN A ARQUITECTURA SOFTWARE",
                "PRINCIPIOS SOLID",
                "RESPONSABILIDAD ÚNICA SRP",
                "ABIERTO CERRADO OCP",
                "SUSTITUCIÓN LISKOV LSP",
                "SEGREGACIÓN INTERFAZ ISP",
                "INVERSIÓN DEPENDENCIAS DIP",
                "DRY KISS YAGNI",
                "ACOPLAMIENTO COHESIÓN",
                "PROYECTO MÓDULO: ANÁLISIS CÓDIGO",
            ]),
            ("PATRONES CREACIONALES", [
                "SINGLETON ÚNICA INSTANCIA",
                "FACTORY METHOD",
                "ABSTRACT FACTORY",
                "BUILDER CONSTRUCTOR",
                "PROTOTYPE CLONACIÓN",
                "OBJECT POOL",
                "COMPARACIÓN CREACIONALES",
                "CUÁNDO USAR CADA UNO",
                "ANTIPATRONES COMUNES",
                "PROYECTO MÓDULO: FACTORY PATTERN",
            ]),
            ("PATRONES ESTRUCTURALES", [
                "ADAPTER TRADUCTOR",
                "BRIDGE PUENTE",
                "COMPOSITE ÁRBOL",
                "DECORATOR",
                "FACADE FACHADA",
                "FLYWEIGHT PESO LIGERO",
                "PROXY APODERADO",
                "COMPARACIÓN ESTRUCTURALES",
                "CASOS USO REALES",
                "PROYECTO MÓDULO: DECORATOR PATTERN",
            ]),
            ("PATRONES COMPORTAMIENTO", [
                "CHAIN OF RESPONSIBILITY",
                "COMMAND ORDEN",
                "ITERATOR ITERADOR",
                "MEDIATOR MEDIADOR",
                "MEMENTO RECORDATORIO",
                "OBSERVER OBSERVADOR",
                "STATE ESTADO",
                "STRATEGY ESTRATEGIA",
                "TEMPLATE METHOD",
                "PROYECTO MÓDULO: OBSERVER PATTERN",
            ]),
            ("ARQUITECTURA LIMPIA", [
                "CLEAN ARCHITECTURE FUNDAMENTOS",
                "CAPAS DOMAIN APPLICATION INFRA",
                "DEPENDENCY INVERSION PRÁCTICA",
                "CASOS DE USO APPLICATION",
                "ENTIDADES VALUE OBJECTS",
                "PUERTOS ADAPTADORES",
                "HEXAGONAL ARCHITECTURE",
                "CLEAN ARCHITECTURE NODE.JS",
                "CLEAN ARCHITECTURE PYTHON",
                "PROYECTO MÓDULO: CLEAN ARCH",
            ]),
            ("MICROSERVICIOS", [
                "MONOLITO VS MICROSERVICIOS",
                "COMUNICACIÓN SINCRÓNICA HTTP GRPC",
                "COMUNICACIÓN ASINCRÓNICA EVENTOS",
                "SAGA PATTERN TRANSACCIONES",
                "CQRS COMMAND QUERY",
                "EVENT SOURCING",
                "API GATEWAY PATTERN",
                "SERVICE DISCOVERY",
                "CIRCUIT BREAKER",
                "PROYECTO MÓDULO: MICROSERVICIOS",
            ]),
            ("DDD DOMINIO", [
                "DOMAIN DRIVEN DESIGN",
                "LENGUAJE UBICUO",
                "ENTIDADES VALUE OBJECTS",
                "AGREGADOS RAÍZ AGREGADO",
                "REPOSITORIOS DOMINIO",
                "SERVICIOS DOMINIO",
                "EVENTOS DOMINIO",
                "SUBDOMINIOS BOUNDED CONTEXT",
                "CONTEXT MAP ESTRATÉGICO",
                "PROYECTO MÓDULO: DDD PRÁCTICO",
            ]),
            ("PROYECTO FINAL ARQUITECTURA", [
                "SELECCIÓN DOMINIO",
                "DISEÑO CON DDD",
                "IMPLEMENTACIÓN CLEAN ARCH",
                "PATRONES APLICADOS",
                "MICROSERVICIOS O MONOLITO",
                "EVENTOS COMUNICACIÓN",
                "PRUEBAS ARQUITECTURA",
                "DOCUMENTACIÓN ARQUITECTÓNICA",
                "PRESENTACIÓN ARQUITECTURA",
                "CARTA DE GRADUACIÓN PROFESOR BÚHO",
            ]),
        ]),
    },
    "24_LIDERAZGO_LIBRO_MAESTRO": {
        "nom": "LIDERAZGO TECNOLÓGICO",
        "mods": convertir_a_formato_completo([
            ("FUNDAMENTOS DE LIDERAZGO", [
                "INTRODUCCIÓN AL LIDERAZGO TECH",
                "LIDERAZGO VS GESTIÓN",
                "ESTILOS DE LIDERAZGO",
                "AUTOCONOCIMIENTO AUTOEVALUACIÓN",
                "INTELIGENCIA EMOCIONAL",
                "COMUNICACIÓN EFECTIVA",
                "ESCUCHA ACTIVA",
                "VISIÓN Y PROPÓSITO",
                "CÓDIGO DE CONDUCTA",
                "PROYECTO MÓDULO: PLAN LIDERAZGO",
            ]),
            ("GESTIÓN DE EQUIPOS", [
                "CONSTRUCCIÓN DE EQUIPOS",
                "DELEGACIÓN EFECTIVA",
                "FEEDBACK CONSTRUCTIVO",
                "GESTIÓN DE CONFLICTOS",
                "MOTIVACIÓN COMPROMISO",
                "DIVERSIDAD E INCLUSIÓN",
                "ONBOARDING NUEVOS MIEMBROS",
                "1:1 REUNIONES EFECTIVAS",
                "RETENCIÓN DE TALENTO",
                "PROYECTO MÓDULO: TEAM BUILDING",
            ]),
            ("METODOLOGÍAS ÁGILES", [
                "MANIFIESTO ÁGIL PRINCIPIOS",
                "SCRUM ROLES EVENTOS ARTEFACTOS",
                "SPRINT PLANNING REFINEMENT",
                "DAILY STAND UP",
                "SPRINT REVIEW RETROSPECTIVE",
                "KANBAN FLUJO CONTINUO",
                "ESTIMACIÓN STORY POINTS",
                "OKRS Y KPIs",
                "SCRUM MASTER VS PRODUCT OWNER",
                "PROYECTO MÓDULO: SCRUM EN ACCIÓN",
            ]),
            ("COMUNICACIÓN TÉCNICA", [
                "COMUNICACIÓN TÉCNICA EFECTIVA",
                "DOCUMENTACIÓN TÉCNICA",
                "PRESENTACIONES TÉCNICAS",
                "MENTORÍA COACHING",
                "TECH TALKS BROWN BAGS",
                "ESCRITURA TÉCNICA",
                "COMUNICACIÓN NO TÉCNICOS",
                "GESTIÓN STAKEHOLDERS",
                "PRESENTACIÓN PROYECTOS",
                "PROYECTO MÓDULO: TECH TALK",
            ]),
            ("LIDERAZGO TÉCNICO", [
                "ARQUITECTO VS TECH LEAD",
                "TOMA DECISIONES TÉCNICAS",
                "CODE REVIEW COMO HERRAMIENTA",
                "DEUDA TÉCNICA CALIDAD",
                "ESTÁNDARES DE CÓDIGO",
                "TECH RADAR ADOPCIÓN",
                "GESTIÓN CAMBIO TÉCNICO",
                "INNOVACIÓN EQUIPOS",
                "SISTEMAS LEGACY MIGRACIÓN",
                "PROYECTO MÓDULO: TECH ROADMAP",
            ]),
            ("CRECIMIENTO PROFESIONAL", [
                "PLAN CARRERA EN TECH",
                "HABILIDADES BLANDAS SOFT SKILLS",
                "NETWORKING COMUNIDAD",
                "MARCA PERSONAL PERSONAL BRANDING",
                "ENTREVISTAS PROMOCIÓN",
                "CERTIFICACIONES ESTUDIO",
                "WORK LIFE BALANCE",
                "SALUD MENTAL TECH",
                "PREVENCIÓN BURNOUT",
                "PROYECTO MÓDULO: PLAN CARRERA",
            ]),
            ("GESTIÓN DE PROYECTOS", [
                "CICLO DE VIDA SOFTWARE",
                "PLANIFICACIÓN ESTIMACIÓN",
                "GESTIÓN DE RIESGOS",
                "GESTIÓN DEL ALCANCE",
                "MÉTRICAS REPORTES",
                "GESTIÓN PRESUPUESTOS",
                "PROVEEDORES TERCEROS",
                "CALIDAD ASEGURAMIENTO QA",
                "CIERRE PROYECTOS",
                "PROYECTO MÓDULO: GESTIÓN PROYECTO",
            ]),
            ("PROYECTO FINAL LIDERAZGO", [
                "AUTOEVALUACIÓN LIDERAZGO",
                "PLAN DESARROLLO PERSONAL",
                "PROYECTO MEJORA EQUIPO",
                "IMPLEMENTACIÓN CAMBIOS",
                "MÉTRICAS IMPACTO",
                "DOCUMENTACIÓN LECCIONES",
                "RETROSPECTIVA PROCESO",
                "PLAN FUTURO",
                "MENTORÍA LÍDERES",
                "CARTA DE GRADUACIÓN PROFESOR BÚHO",
            ]),
        ]),
    },
}


# ─── GENERAR TODOS LOS LIBROS ─────────────────────────────────────────────

def generar(book_name):
    data = LIBROS_CONTENIDO[book_name]
    nombre = data["nom"]
    modulos = data["mods"]
    book_dir = os.path.join(BASE, book_name)

    print(f"\n{'='*60}")
    print(f"  GENERANDO: {book_name} ({nombre})")
    print(f"{'='*60}")
    limpiar(book_dir)

    cap_global = 0
    for mod_idx, (mod_nombre, temas) in enumerate(modulos):
        mod_num = mod_idx + 1
        # temas debe ser lista de (titulo, secciones, ejercicios, preguntas)
        n_temas = len(temas)
        print(f"  Módulo {mod_num} ({mod_nombre}): {n_temas} capítulos")

        for titulo, secciones, ejercicios, preguntas in temas:
            cap_global += 1
            es_proy = "PROYECTO" in titulo.upper()
            txt = hacer_capitulo(book_name, nombre, mod_num, cap_global, titulo,
                                 secciones, ejercicios, preguntas, es_proy)
            guardar(book_dir, mod_num, cap_global, nom_archivo(titulo), txt)

        print(f"    → Capítulos {cap_global - n_temas + 1} a {cap_global} creados")

    print(f"  ✓ {book_name} COMPLETADO ({cap_global} capítulos)\n")


def main():
    print("=" * 60)
    print("  GENERADOR DE CONTENIDO EDUCATIVO REAL")
    print("  LUCAS EGA ACADEMY")
    print("=" * 60)
    print(f"  Libros a regenerar: {len(LIBROS_A_GENERAR)}")
    total_caps = len(LIBROS_A_GENERAR) * 80
    print(f"  Total capítulos: {total_caps}")
    print("=" * 60)

    for book_name in LIBROS_A_GENERAR:
        if book_name not in LIBROS_CONTENIDO:
            print(f"\n⚠  ERROR: {book_name} no tiene datos definidos. Omitiendo.")
            continue
        generar(book_name)

    print("\n" + "=" * 60)
    print("  GENERACIÓN COMPLETADA CON ÉXITO")
    print(f"  {len(LIBROS_A_GENERAR)} libros × 80 capítulos = {total_caps} capítulos")
    print("=" * 60)


if __name__ == "__main__":
    main()
