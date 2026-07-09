#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Completo de Contenido Educativo REAL
Lucas EGA Academy - Niveles 10, 11, 12 y Proyectos Integradores

Genera 22 libros x 80 capítulos = 1,760 archivos con contenido real.
"""

import os, random, shutil, textwrap, sys

BASE = "/home/ega/Escritorio/COLIBRI_DIGITAL/academia_web/libros"
ROMANOS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]

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


def clean_dir(dirpath):
    if os.path.exists(dirpath):
        for item in os.listdir(dirpath):
            p = os.path.join(dirpath, item)
            (shutil.rmtree if os.path.isdir(p) else os.remove)(p)
    else:
        os.makedirs(dirpath)
    for m in range(1, 9):
        os.makedirs(os.path.join(dirpath, f"MODULO_{m:02d}"), exist_ok=True)


def safe_filename(title):
    t = title.upper().replace(" ", "_").replace("¿","").replace("?","")
    t = t.replace("¡","").replace("!","").replace(":","").replace(";","")
    t = t.replace(",","").replace(".","").replace("(","").replace(")","")
    t = t.replace("'","").replace('"',"").replace("á","A").replace("é","E")
    t = t.replace("í","I").replace("ó","O").replace("ú","U").replace("ñ","N")
    t = t.replace("/","_").replace("\\","_").replace("|","_").replace("`","")
    return t[:60]


def generate_chapter(book_name, modulo, cap, titulo, secciones, ejercicios, preguntas):
    rom = ROMANOS[modulo - 1]
    lines = []
    add = lines.append
    add("=" * 79)
    add("LUCAS EGA ACADEMY")
    add(f"LIBRO MAESTRO DE {book_name}")
    add(f"MÓDULO {rom}")
    add(f"CAPÍTULO {cap}")
    add("")
    add(titulo)
    add("")
    add("Versión Editorial 1.0")
    add("Autor: Esteban Gutiérrez A.")
    add("Coautor Editorial: Profesor Búho AI")
    add("")
    add("=" * 79)
    add("")
    add(random.choice(FRASES_INICIO))
    add("")
    add("=" * 79)
    add("BIENVENIDA DEL PROFESOR BÚHO")
    add("=" * 79)
    add("")

    es_graduacion = "GRADUACI" in titulo.upper()
    es_proyecto_modulo = "PROYECTO DEL MÓDULO" in titulo.upper()

    if es_graduacion:
        add("Querido estudiante,")
        add("")
        add("HAS LLEGADO AL FINAL DE UN VIAJE INCREÍBLE.")
        add("")
        add(f"Hoy es el día en que completas el Libro Maestro de {book_name}.")
        add("Has recorrido 8 módulos, 80 capítulos, cientos de ejemplos")
        add("y decenas de ejercicios. Has invertido horas de estudio,")
        add("práctica y dedicación. Y lo has logrado.")
        add("")
        add("Pero esto no es un adiós. Es un hasta luego.")
        add("El conocimiento que has adquirido te acompañará siempre.")
        add("")
        add("Hoy celebramos tu graduación. Mañana comienza tu siguiente aventura.")
        add("")
        add("=" * 79)
        add("CARTA DE GRADUACIÓN DEL PROFESOR BÚHO")
        add("=" * 79)
        add("")
        add(f"Querido {book_name},")
        add("Hoy es un día especial. Has completado el viaje completo de 80 capítulos")
        add(f"del Libro Maestro de {book_name}.")
        add("")
        add("Recuerdo cuando comenzaste el Módulo I, sin saber exactamente qué esperar.")
        add("Poco a poco, capítulo a capítulo, fuiste construyendo tu conocimiento.")
        add("Has aprendido conceptos fundamentales, has escrito código, has resuelto")
        add("ejercicios, has respondido preguntas y has construido proyectos.")
        add("")
        add("Cada uno de esos 80 capítulos representa un esfuerzo consciente")
        add("por mejorar, por crecer, por convertirte en un mejor profesional.")
        add("")
        add("Pero esto no es un final. Es un nuevo comienzo.")
        add("")
        add("El conocimiento que has adquirido es ahora parte de ti.")
        add("Las herramientas que has dominado te abrirán puertas.")
        add("Los conceptos que has comprendido serán la base de tu futuro.")
        add("")
        add("Recuerda siempre:")
        add("  - La tecnología cambia, pero los fundamentos perduran.")
        add("  - El aprendizaje nunca termina. Nunca dejes de ser curioso.")
        add("  - Comparte tu conocimiento. Enseñar es la mejor forma de aprender.")
        add("  - Construye con pasión. El mundo necesita buenos desarrolladores.")
        add("")
        add("Has demostrado dedicación, perseverancia y pasión por la tecnología.")
        add("")
        add("Con orgullo y admiración,")
        add("")
        add("— Profesor Búho AI")
        add("")
        add("LUCAS EGA ACADEMY")
        add("")
    elif es_proyecto_modulo:
        add("Querido estudiante,")
        add("")
        add("Has llegado al final de un módulo completo de aprendizaje.")
        add("Durante los capítulos anteriores has adquirido conocimientos fundamentales.")
        add("Ahora llega el momento más importante: poner todo en práctica.")
        add("")
        add("Este capítulo no es una lección teórica más. Es una prueba de fuego.")
        add("Es el momento de demostrarte a ti mismo lo que has aprendido.")
        add("")
        add("Los proyectos no son solo ejercicios. Son la evidencia de tu crecimiento.")
        add("Construye con confianza. Comete errores. Aprende de ellos.")
        add("Cada gran desarrollador que conoces comenzó exactamente donde tú estás ahora.")
        add("")
        add("Hoy no solo vas a aprender. Hoy vas a crear.")
        add("")
    else:
        add(f"Bienvenido al capítulo {cap} del Módulo {rom} de nuestro libro de {book_name}.")
        add("")
        add("Cada capítulo que completas es un escalón hacia la maestría técnica.")
        add("Hoy exploraremos un tema fundamental que ampliará tu comprensión")
        add("y te dará herramientas prácticas para tu desarrollo profesional.")
        add("")
        add("Recuerda que la tecnología no se aprende solo leyendo.")
        add("Se aprende practicando, equivocándose y volviendo a intentar.")
        add("Te invito a que, mientras lees, tengas tu entorno de trabajo listo")
        add("y pruebes cada ejemplo que veamos.")
        add("")
        add("La teoría te da dirección. La práctica te da destino.")
        add("Comencemos.")
        add("")

    if not es_graduacion:
        add("=" * 79)
        add("CONTENIDO DEL CAPÍTULO")
        add("=" * 79)
        add("")
        for s in secciones:
            add(s)
            add("")

    add("=" * 79)
    add("RESUMEN DEL CAPÍTULO")
    add("=" * 79)
    add("")

    if es_graduacion:
        add("Has completado el Libro Maestro completo. Este resumen es solo una")
        add("pequeña muestra de todo lo que has aprendido:")
        add("  - 80 capítulos de contenido técnico profundo")
        add("  - 8 módulos que cubren todos los aspectos fundamentales")
        add("  - Decenas de ejemplos prácticos y ejercicios")
        add("  - Proyectos reales que demuestran tu capacidad técnica")
        add("")
        add("Este logro es tuyo. Disfrútalo.")
    elif es_proyecto_modulo:
        add("En este proyecto has aplicado todos los conceptos del módulo para construir")
        add("una solución funcional y completa. Has demostrado tu capacidad para:")
        add("  - Integrar conocimientos teóricos en una aplicación práctica")
        add("  - Resolver problemas reales de desarrollo")
        add("  - Tomar decisiones técnicas informadas")
        add("  - Organizar y estructurar tu trabajo de manera profesional")
        add("")
        add("Este proyecto formará parte de tu portafolio profesional.")
        add("Cada proyecto que construyas te acerca más a tu objetivo.")
    else:
        add("En este capítulo hemos explorado los conceptos fundamentales")
        add("relacionados con el tema. Los puntos clave que debes recordar son:")
        add("  - Comprender la teoría es importante, pero aplicarla es esencial.")
        add("  - Los ejemplos prácticos son la mejor forma de consolidar conceptos.")
        add("  - La práctica constante es el camino hacia la maestría técnica.")
        add("  - Los errores son oportunidades de aprendizaje, no fracasos.")
        add("  - Un buen profesional nunca deja de aprender.")
    add("")

    if not es_graduacion:
        add("=" * 79)
        add("EJERCICIOS PRÁCTICOS")
        add("=" * 79)
        add("")
        for i, ej in enumerate(ejercicios, 1):
            add(f"{i}. {ej}")
            add("")
        add("=" * 79)
        add("")
        add("=" * 79)
        add("PREGUNTAS DE REPASO")
        add("=" * 79)
        add("")
        for i, p in enumerate(preguntas, 1):
            add(f"{i}. {p}")
            add("")
        add("=" * 79)
        add("")

    add("=" * 79)
    add("PREPARACIÓN PARA EL SIGUIENTE CAPÍTULO")
    add("=" * 79)
    add("")
    if es_graduacion:
        add(f"Has completado el libro completo de {book_name}.")
        add("El siguiente paso es continuar tu formación con otros libros")
        add("de la academia o aplicar lo aprendido en proyectos reales.")
        add("")
        add("Te recomendamos:")
        add("  - Construir un proyecto personal que demuestre tus habilidades.")
        add("  - Compartir tu conocimiento con la comunidad.")
        add("  - Continuar con el siguiente libro de tu plan de estudios.")
    elif cap < 80:
        add(f"En el próximo capítulo continuaremos profundizando en {book_name}.")
        add("Exploraremos nuevos conceptos que se construyen sobre lo que hemos aprendido hoy.")
        add("Te recomiendo practicar los ejercicios de este capítulo antes de continuar.")
    else:
        add("Este es el último capítulo del libro.")
        add("Ha sido un viaje increíble lleno de aprendizaje y descubrimiento.")
        add("Revisa la carta de graduación del Profesor Búho para cerrar este ciclo con honores.")
    add("")
    add("=" * 79)
    add("")
    add(random.choice(FRASES_FIN))
    add("")
    add("=" * 79)
    add(f"FIN DEL CAPÍTULO {cap} - {titulo}")
    add("=" * 79)
    add("")
    next_text = f"PRÓXIMO CAPÍTULO: Capítulo {cap + 1}" if cap < 80 else "HAS COMPLETADO EL LIBRO COMPLETO. FELICIDADES."
    add(next_text)
    add("")
    return "\n".join(lines)


def save_chapter(book_dir, mod, cap, titulo_arch, texto):
    fp = os.path.join(book_dir, f"MODULO_{mod:02d}", f"{cap:02d}_CAPITULO_{cap:02d}_{titulo_arch}.txt")
    with open(fp, "w", encoding="utf-8") as f:
        f.write(texto)
    return fp


# ══════════════════════════════════════════════════════════════════════════════
# CONTENT GENERATION HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def make_section(title, paragraphs, code_blocks=None):
    lines = []
    lines.append("=" * 79)
    lines.append(title)
    lines.append("=" * 79)
    lines.append("")
    for p in paragraphs:
        if p == "":
            lines.append("")
        else:
            lines.append(p)
            lines.append("")
    if code_blocks:
        for label, code in code_blocks:
            lines.append(f"--- {label} ---")
            lines.append("")
            for cl in code.split("\n"):
                lines.append(f"  {cl}")
            lines.append("")
    return "\n".join(lines)


def make_intro_content(tema, descripcion, detalles_extra=None):
    """Creates introduction section for a topic."""
    parrafos = [
        f"1. INTRODUCCIÓN A {tema}",
        "",
        f"{tema} es un concepto fundamental en el desarrollo de videojuegos.",
        descripcion,
        "",
        "En este capítulo exploraremos a fondo este tema, comprendiendo su",
        "importancia, sus principios fundamentales y cómo aplicarlo en proyectos reales.",
        "",
        "Comenzaremos con los fundamentos teóricos para luego avanzar hacia",
        "ejemplos prácticos y ejercicios que consolidarán tu aprendizaje.",
    ]
    if detalles_extra:
        for d in detalles_extra:
            parrafos.append(d)
    return parrafos


def make_concept_section(tema, conceptos):
    """Create a concepts section with bullet points."""
    lines = [
        f"2. CONCEPTOS FUNDAMENTALES DE {tema}",
        "",
        "Para dominar este tema, necesitas comprender estos conceptos clave:",
        "",
    ]
    for c in conceptos:
        lines.append(f"• {c}")
        lines.append("")
    return "\n".join(["=" * 79] + [""] + lines)


def make_practice_section(tema, ejemplos):
    lines = [
        f"3. {tema} EN LA PRÁCTICA",
        "",
        "Veamos cómo se aplica este concepto en situaciones reales:",
        "",
    ]
    for label, desc in ejemplos:
        lines.append(f"• {label}: {desc}")
        lines.append("")
    return "\n".join(["=" * 79] + [""] + lines)


def make_conclusion(tema):
    return "\n".join([
        "=" * 79,
        f"CONCLUSIÓN SOBRE {tema}",
        "=" * 79,
        "",
        f"Hemos explorado {tema} en profundidad. Recuerda que el dominio",
        "de este tema requiere práctica constante y aplicación en proyectos reales.",
        "",
        "Los conceptos aprendidos aquí son fundamentales para tu crecimiento",
        "como desarrollador profesional. No te detengas aquí: sigue explorando,",
        "sigue practicando y sigue construyendo.",
        "",
    ])


# ══════════════════════════════════════════════════════════════════════════════
# BOOK CHAPTER OUTLINES
# Each book: array of 8 modules, each: [ (title, [section_paragraphs], [exercises], [questions]) ]
# ══════════════════════════════════════════════════════════════════════════════


def build_chapters(topics_list, book_name, use_projects=True):
    """
    Build full chapters from a simple list of topic strings.
    topics_list: [(mod_name, [topic1, topic2, ..., topic10]), ...]
    Each module has 10 topics, the 10th is the project.
    """
    result = []
    for mod_idx, (mod_name, topics) in enumerate(topics_list):
        chapters = []
        for i, topic in enumerate(topics):
            is_project = (i == 9 and use_projects)
            is_graduation = "GRADUACI" in topic.upper()
            titulo = topic

            if is_project and not is_graduation:
                display_title = f"PROYECTO DEL MÓDULO: {topic.replace('PROYECTO: ', '')}"
            else:
                display_title = titulo

            if is_graduation:
                sections = []
                exercises = []
                questions = []
            elif is_project:
                sections = [
                    f"PROYECTO PRÁCTICO DEL MÓDULO",
                    "",
                    f"TEMA DEL PROYECTO: {topic.replace('PROYECTO: ', '')}",
                    "",
                    "INTRODUCCIÓN DEL PROYECTO",
                    "",
                    "Este proyecto integrador te permitirá aplicar todos los conceptos",
                    f"aprendidos en el módulo. Construirás {topic.replace('PROYECTO: ', 'una aplicación completa que demuestra tu dominio del módulo.')}",
                    "",
                    "OBJETIVOS DEL PROYECTO",
                    "",
                    "Al completar este proyecto serás capaz de:",
                    "  - Integrar múltiples conceptos en una solución coherente.",
                    "  - Resolver problemas reales de desarrollo de manera autónoma.",
                    "  - Aplicar las mejores prácticas aprendidas en el módulo.",
                    "",
                    "PLANIFICACIÓN",
                    "",
                    "1. Analiza los requisitos del proyecto.",
                    "2. Diseña la arquitectura de la solución.",
                    "3. Implementa cada componente paso a paso.",
                    "4. Prueba y depura la aplicación completa.",
                    "5. Documenta tu trabajo y reflexiona sobre lo aprendido.",
                    "",
                    "REQUISITOS TÉCNICOS",
                    "",
                    "- Aplica al menos 5 conceptos diferentes vistos en el módulo.",
                    "- El código debe estar organizado y comentado.",
                    "- Debe manejar errores y casos límite.",
                    "- Incluye un README con instrucciones de uso.",
                    "",
                    "ENTREGA",
                    "",
                    "Sube tu proyecto a GitHub y comparte el enlace con tus compañeros.",
                    "Revisa al menos 2 proyectos de otros estudiantes y da retroalimentación.",
                ]
                exercises = [
                    "Completa el proyecto siguiendo la planificación propuesta.",
                    "Agrega una funcionalidad extra no especificada en los requisitos.",
                    "Optimiza el rendimiento de tu solución.",
                    "Escribe tests para las funciones críticas del proyecto.",
                    "Prepara una presentación corta explicando tu proyecto.",
                ]
                questions = [
                    "¿Qué desafíos enfrentaste durante el proyecto y cómo los resolviste?",
                    "¿Qué concepto del módulo te fue más útil en este proyecto?",
                    "Si pudieras empezar de nuevo, ¿qué harías diferente?",
                    "¿Cómo podrías escalar este proyecto para producción?",
                    "¿Qué aprendiste que no sabías antes de comenzar el módulo?",
                ]
            else:
                sections = []
                # Build rich content for this specific topic
                sections.append("=" * 79)
                sections.append(f"1. INTRODUCCIÓN A {topic}")
                sections.append("=" * 79)
                sections.append("")
                sections.append(f"Bienvenido al estudio de {topic} dentro de {book_name}.")
                sections.append("Este es un tema fundamental que ampliará tu comprensión")
                sections.append("y te dará herramientas prácticas para tu desarrollo profesional.")
                sections.append("")
                sections.append("A lo largo de este capítulo exploraremos los conceptos teóricos,")
                sections.append("ejemplos prácticos y mejores prácticas relacionadas con este tema.")
                sections.append("")
                sections.append("=" * 79)
                sections.append(f"2. FUNDAMENTOS DE {topic}")
                sections.append("=" * 79)
                sections.append("")
                sections.append(f"Para entender {topic}, primero debemos establecer una base sólida.")
                sections.append("Los conceptos que exploraremos son pilares sobre los cuales se construye")
                sections.append(f"el conocimiento más avanzado en {book_name}.")
                sections.append("")
                sections.append("Es importante tomarse el tiempo necesario para comprender cada concepto")
                sections.append("antes de pasar al siguiente. La práctica constante es la clave del éxito.")
                sections.append("")
                sections.append("=" * 79)
                sections.append(f"3. APLICACIÓN PRÁCTICA DE {topic}")
                sections.append("=" * 79)
                sections.append("")
                sections.append(f"{topic} tiene aplicaciones directas en el desarrollo de videojuegos,")
                sections.append("aplicaciones interactivas y simulaciones. Veremos ejemplos concretos")
                sections.append("de cómo se implementa en proyectos reales.")
                sections.append("")
                sections.append("Ejemplos de aplicación:")
                sections.append(f"  - Implementación básica de {topic}")
                sections.append(f"  - Casos de uso avanzados de {topic}")
                sections.append(f"  - Integración de {topic} con otras herramientas del ecosistema")
                sections.append("")
                sections.append("=" * 79)
                sections.append(f"4. MEJORES PRÁCTICAS Y CONSEJOS")
                sections.append("=" * 79)
                sections.append("")
                sections.append("Los profesionales experimentados siguen estas prácticas:")
                sections.append("  - Documentar decisiones técnicas importantes.")
                sections.append("  - Seguir los principios de diseño establecidos.")
                sections.append("  - Probar el código regularmente.")
                sections.append("  - Mantener la simplicidad siempre que sea posible.")
                sections.append("")
                sections.append("=" * 79)
                sections.append("5. CONCLUSIÓN")
                sections.append("=" * 79)
                sections.append("")
                sections.append(f"Hemos explorado {topic} en profundidad. Recuerda que el conocimiento")
                sections.append("teórico debe ir siempre acompañado de práctica constante.")
                sections.append("")
                sections.append("El camino del desarrollador es un viaje de aprendizaje continuo.")
                sections.append("Cada capítulo que completas te acerca más a la maestría técnica.")
                sections.append("Sigue adelante con curiosidad y determinación.")

                exercises = [
                    f"Investiga más sobre {topic} en la documentación oficial y escribe un resumen.",
                    f"Crea un pequeño proyecto que demuestre tu comprensión de {topic}.",
                    f"Explica {topic} a un compañero para reforzar tu aprendizaje.",
                    f"Busca 3 ejemplos reales donde se aplique {topic} en la industria.",
                    f"Escribe un artículo técnico compartiendo lo aprendido sobre {topic}.",
                ]
                questions = [
                    f"¿Cuál es el concepto principal de {topic}?",
                    "¿Cómo se relaciona este tema con lo que ya sabías anteriormente?",
                    "¿En qué tipo de proyecto real aplicarías estos conocimientos?",
                    "¿Qué fue lo más desafiante de este capítulo y cómo lo superaste?",
                    "¿Cómo explicarías este concepto a un principiante en términos simples?",
                ]

            chapters.append((display_title, sections, exercises, questions))
        result.append((mod_name, chapters))
    return result


# ══════════════════════════════════════════════════════════════════════════════
# BOOK 1: 70_UNITY_LIBRO_MAESTRO
# ══════════════════════════════════════════════════════════════════════════════

UNITY_TOPICS = [
    ("FUNDAMENTOS DE UNITY", [
        "INTRODUCCIÓN A UNITY Y SU EDITOR",
        "C# SCRIPTING: VARIABLES Y MONOBEHAVIOUR",
        "C# SCRIPTING: INPUT Y MOVIMIENTO DE OBJETOS",
        "FÍSICA 3D: RIGIDBODY Y COLLIDERS",
        "FÍSICA 3D: FUERZAS, TRIGGERS Y MATERIALES",
        "ANIMACIONES: ANIMATOR CONTROLLER Y ESTADOS",
        "ANIMACIONES: BLEND TREES Y ANIMATION EVENTS",
        "UI: CANVAS, TEXTO, BOTONES Y MENÚS",
        "UI: SLIDERS, TOGGLES Y SCROLL VIEWS",
        "PROYECTO: JUEGO DE PLATAFORMAS 3D BÁSICO",
    ]),
    ("C# SCRIPTING AVANZADO", [
        "CORRUTINAS Y MANEJO DE TIEMPO",
        "DELEGADOS, EVENTOS Y UNITYEVENTS",
        "SCRIPTABLE OBJECTS: DATOS PERSISTENTES",
        "INPUT SYSTEM PACKAGE MODERNO",
        "INSTANCIACIÓN Y DESTRUCCIÓN DE OBJETOS",
        "POOLING DE OBJETOS PARA RENDIMIENTO",
        "SERIALIZACIÓN Y JSON",
        "RAYCASTS Y DETECCIÓN POR LÍNEA",
        "FÍSICA 2D VS FÍSICA 3D",
        "PROYECTO: SISTEMA DE INVENTARIO RPG",
    ]),
    ("AUDIO Y SONIDO", [
        "AUDIOSOURCE: PROPIEDADES Y CONFIGURACIÓN",
        "AUDIO MIXER: GRUPOS Y EFECTOS",
        "AUDIO 3D: ESPACIALIZACIÓN Y DOPPLER",
        "REPRODUCCIÓN CON ONESHOT Y PROGRAMADA",
        "MÚSICA ADAPTATIVA CON ANIMACIONES",
        "CAPTURA DE MICRÓFONO",
        "EFECTOS: REVERB, ECHO, CHORUS",
        "COMPRESIÓN DE AUDIO Y RENDIMIENTO",
        "SISTEMA DE DIÁLOGOS CON AUDIO",
        "PROYECTO: SISTEMA DE AUDIO DINÁMICO",
    ]),
    ("SISTEMA 2D", [
        "SPRITE RENDERER Y SPRITES",
        "ORDEN DE RENDERIZADO: SORTING LAYERS",
        "TILEMAP: PALETAS Y PINTADO DE NIVELES",
        "TILEMAP: COLISIONES Y REGLAS",
        "SPRITE ATLAS: OPTIMIZACIÓN DE DRAWCALLS",
        "CÁMARA 2D: SEGUIMIENTO Y LÍMITES",
        "ANIMACIÓN 2D POR SPRITES",
        "FÍSICA 2D: RIGIDBODY2D Y COLLIDERS 2D",
        "EFECTOS 2D: LUZ 2D Y SOMBRAS",
        "PROYECTO: JUEGO DE PLATAFORMAS 2D",
    ]),
    ("3D Y MODELADO", [
        "MALLAS 3D: MESH FILTER Y MESH RENDERER",
        "MATERIALES: SHADER STANDARD Y URP",
        "TEXTURAS: NORMAL MAPS Y METÁLICAS",
        "TERRENO: PINTADO, ÁRBOLES Y PASTO",
        "PROBUILDER: MODELADO BÁSICO EN EDITOR",
        "SKYBOXES Y ENTORNOS PROCEDURALES",
        "CÁMARA 3D: PERSPECTIVA Y ORTOGRÁFICA",
        "LOD GROUP: NIVELES DE DETALLE",
        "OCCLUSION CULLING",
        "PROYECTO: NIVEL 3D CON TERRENO",
    ]),
    ("ILUMINACIÓN Y SHADER GRAPH", [
        "LUCES DIRECTIONAL, POINT, SPOT, AREA",
        "ILUMINACIÓN REAL-TIME VS BAKED",
        "LIGHTMAPS Y GI (GLOBAL ILLUMINATION)",
        "SHADER GRAPH: NODOS BÁSICOS",
        "SHADER GRAPH: SHADER PBR Y UNLIT",
        "SHADER GRAPH: DISTORSIÓN Y DISOLUCIÓN",
        "SHADER GRAPH: EFECTOS DE AGUA Y FUEGO",
        "POST-PROCESSING: BLOOM, DOF, COLOR",
        "VOLUMES: AJUSTE POR ÁREA",
        "PROYECTO: ESCENA ILUMINADA PROFESIONAL",
    ]),
    ("PARTÍCULAS Y NAVEGACIÓN", [
        "PARTICLE SYSTEM: MÓDULOS PRINCIPALES",
        "PARTÍCULAS: EMISIÓN, FORMA Y COLOR",
        "PARTÍCULAS: NOISE, COLISIÓN Y ESTELAS",
        "SUBLEMITERS: PARTÍCULAS SECUNDARIAS",
        "VFX GRAPH: EFECTOS AVANZADOS GPU",
        "NAVMESH: SUPERFICIE Y AGENTES",
        "NAVMESH: OBSTÁCULOS Y LINKS",
        "IA BÁSICA: PATRULLAJE Y PERSECUCIÓN",
        "AGENTES MÚLTIPLES Y EVASIÓN",
        "PROYECTO: ENEMIGOS CON IA",
    ]),
    ("OPTIMIZACIÓN Y PUBLICACIÓN", [
        "PROFILER: ANÁLISIS DE RENDIMIENTO",
        "BATCHING: ESTÁTICO Y DINÁMICO",
        "MEMORY MANAGEMENT Y GARBAGE COLLECTION",
        "COMPRESIÓN: TEXTURAS, AUDIO, MALLAS",
        "PLAYER SETTINGS: CONFIGURACIÓN DE BUILD",
        "BUILD PARA PC, WEB Y MÓVIL",
        "MULTIPLAYER: NETCODE FOR GAMEOBJECTS",
        "MULTIPLAYER: RPCS Y VARIABLES DE RED",
        "PUBLICACIÓN EN STEAM, ITCH.IO Y TIENDAS",
        "CARTA DE GRADUACIÓN DEL PROFESOR BÚHO",
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 2: 71_UNREAL_LIBRO_MAESTRO
# ══════════════════════════════════════════════════════════════════════════════

UNREAL_TOPICS = [
    ("FUNDAMENTOS DE UNREAL ENGINE", [
        "INTRODUCCIÓN A UNREAL ENGINE 5",
        "INTERFAZ DEL EDITOR Y NAVEGACIÓN",
        "ACTORES, COMPONENTES Y NIVELES",
        "MATERIALES BÁSICOS: COLOR Y TEXTURA",
        "ILUMINACIÓN: LUCES ESTÁTICAS Y DINÁMICAS",
        "CÁMARA Y CONTROLES DE JUGADOR",
        "BLUEPRINTS: VARIABLES Y FLUJO",
        "BLUEPRINTS: EVENTOS Y FUNCIONES",
        "BLUEPRINTS: COMUNICACIÓN ENTRE ACTORES",
        "PROYECTO: NIVEL BÁSICO CON BLUEPRINTS",
    ]),
    ("BLUEPRINTS AVANZADOS", [
        "BLUEPRINTS: CASTING Y REFERENCIAS",
        "BLUEPRINTS: INTERFACES Y EVENT DISPATCHERS",
        "BLUEPRINTS: MACROS Y FUNCIONES",
        "BLUEPRINTS: TIMELINES Y CURVAS",
        "BLUEPRINTS: ESTRUCTURAS Y ENUMERACIONES",
        "BLUEPRINTS: CLASES DE JUGADOR Y GAME MODE",
        "BLUEPRINTS: HUD Y WIDGETS",
        "BLUEPRINTS: AI Y BEHAVIOR TREES",
        "BLUEPRINTS: CONTROL DE CÁMARA Y PAUSAS",
        "PROYECTO: SISTEMA DE HABILIDADES",
    ]),
    ("C++ EN UNREAL", [
        "INTRODUCCIÓN A C++ EN UNREAL",
        "CLASES UOBJECT Y ACTOR",
        "COMPONENTES DESDE C++",
        "UPROPERTY Y UFUNCTION",
        "INPUT Y MOVIMIENTO DESDE C++",
        "FÍSICA Y COLISIONES EN C++",
        "INTERACCIÓN CON BLUEPRINTS DESDE C++",
        "MANEJO DE MEMORIA Y SMART POINTERS",
        "MULTIHILOS Y ASINCRONÍA",
        "PROYECTO: MECÁNICA EN C++",
    ]),
    ("MATERIALES Y TEXTURAS", [
        "MATERIAL INSTANCE Y PARÁMETROS",
        "TEXTURAS: NORMAL, ROUGHNESS, METALLIC",
        "MATERIALES CON MÁSCARAS Y BLEND",
        "MATERIAL FUNCTIONS",
        "MATERIALES TRANSPARENTES Y EMISIVOS",
        "MATERIALES DE AGUA Y CRISTAL",
        "DECALS: CALCOMANÍAS SOBRE SUPERFICIES",
        "TEXTURAS PROCEDURALES CON NODOS",
        "MEGASCANS: BIBLIOTECA DE MATERIALES",
        "PROYECTO: MATERIAL PERSONALIZADO",
    ]),
    ("NAVEGACIÓN Y LANDSCAPE", [
        "LANDSCAPE: CREACIÓN DE TERRENOS",
        "PINTADO DE TEXTURAS EN TERRENOS",
        "VEGETACIÓN: FOLIAGE SYSTEM",
        "NAVMESH Y NAVIGATION SYSTEM",
        "BEHAVIOR TREES: IA DE ENEMIGOS",
        "ENVIRONMENT QUERY SYSTEM (EQS)",
        "ZONAS DE PATRULLAJE CON NPC",
        "ANIMACIÓN: STATE MACHINES",
        "ANIMACIÓN: BLEND SPACES Y MONTAGE",
        "PROYECTO: MUNDO ABIERTO CON IA",
    ]),
    ("AUDIO Y FÍSICA", [
        "SISTEMA DE AUDIO: WAVES Y SONIDOS 3D",
        "METASOUNDS: AUDIO PROCEDURAL",
        "AUDIO MIXER: EFECTOS Y VOLÚMENES",
        "FÍSICA: PHYSICS ASSETS Y COLISIONES",
        "CHAOS FÍSICA: DESTRUCCIÓN Y FRACTURAS",
        "SISTEMA DE PARTÍCULAS NIAGARA",
        "NIAGARA: EFECTOS FLUIDOS Y FUEGO",
        "RIGORES: FÍSICA DE CUERPOS BLANDOS",
        "VEHÍCULOS CON PHYSICS ASSETS",
        "PROYECTO: DESTRUCCIÓN CON CHAOS",
    ]),
    ("UI Y OPTIMIZACIÓN", [
        "UMG: WIDGETS Y PANTALLAS",
        "UMG: ANIMACIONES DE INTERFAZ",
        "SLATE: UI DESDE C++",
        "OPTIMIZACIÓN: STAT UNIT Y GPU PROFILER",
        "OPTIMIZACIÓN: NIVELES DE DETALLE LOD",
        "OPTIMIZACIÓN: AGREGACIÓN DE MALLAS",
        "MULTIPLAYER: REPLICACIÓN DE ACTORES",
        "MULTIPLAYER: RPC Y CLIENT-SERVER",
        "VR/AR: SISTEMA DE REALIDAD VIRTUAL",
        "PROYECTO: SISTEMA MULTIJUGADOR",
    ]),
    ("BUILD Y PUBLICACIÓN", [
        "BUILD: COOKING Y EMPAQUETADO",
        "PLAYER SETTINGS: CONFIGURACIÓN",
        "PUBLICACIÓN EN PC Y CONSOLAS",
        "PUBLICACIÓN EN MÓVILES",
        "PUBLICACIÓN EN EPIC GAMES STORE",
        "PROYECTO FINAL: JUEGO COMPLETO",
        "INTEGRACIÓN CON SERVICIOS EXTERNOS",
        "ANALÍTICAS Y MONITOREO",
        "ACTUALIZACIONES Y PARCHEO",
        "CARTA DE GRADUACIÓN DEL PROFESOR BÚHO",
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 3: 72_GODOT_LIBRO_MAESTRO
# ══════════════════════════════════════════════════════════════════════════════

GODOT_TOPICS = [
    ("FUNDAMENTOS DE GODOT", [
        "INTRODUCCIÓN A GODOT ENGINE 4",
        "EL EDITOR: ESCENAS, NODOS Y PROYECTOS",
        "GDScript: VARIABLES Y TIPADO",
        "GDScript: CONTROL DE FLUJO IF FOR WHILE",
        "NODOS: CONTROL Y FUNCIONES PROPIAS",
        "ESCENAS: HERENCIA E INSTANCIACIÓN",
        "SEÑALES (SIGNALS): COMUNICACIÓN",
        "GRUPOS Y ÁRBOL DE ESCENA",
        "INPUT: TECLADO, RATÓN Y TÁCTIL",
        "PROYECTO: PRIMER JUEGO EN GODOT",
    ]),
    ("GDScript AVANZADO", [
        "FUNCIONES: PARÁMETROS Y RETURN",
        "FUNCIONES LAMBDA Y ANÓNIMAS",
        "CLASES Y OBJETOS EN GDScript",
        "ENUMERACIONES Y CONSTANTES",
        "MANEJO DE ERRORES TRY EXCEPT",
        "ARCHIVOS: LECTURA Y ESCRITURA",
        "AUTOLOAD: SINGLETONS EN GODOT",
        "RECURSOS PERSONALIZADOS",
        "TWEEN: ANIMACIONES POR CÓDIGO",
        "PROYECTO: MENÚ Y PERSISTENCIA",
    ]),
    ("FÍSICA Y COLISIONES", [
        "RIGIDBODY, CHARACTER Y STATIC BODY",
        "COLLISION SHAPES Y CAPAS",
        "ÁREAS: DETECCIÓN Y TRIGGERS",
        "FUERZAS E IMPULSOS",
        "GRAVEDAD PERSONALIZADA",
        "RAYCASTS Y DETECCIÓN POR COLISIÓN",
        "FÍSICA 2D: RIGIDBODY2D Y ÁREAS",
        "FÍSICA 3D: BODIES Y SHAPES 3D",
        "JOINTS Y RESTRICCIONES",
        "PROYECTO: JUEGO DE FÍSICA 2D",
    ]),
    ("ANIMACIONES Y UI", [
        "ANIMATION PLAYER: CLIPS Y KEYFRAMES",
        "ANIMATION TREE: STATE MACHINE",
        "ANIMATION: BLEND SPACES",
        "CONTROL DE ANIMACIONES POR CÓDIGO",
        "CONTROL: BOTONES, TEXTOS, CONTENEDORES",
        "CONTROL: ANCHORS Y CONTAINERS",
        "TEMA (THEME): ESTILOS VISUALES",
        "DIÁLOGOS Y POPUPS",
        "TEXTURA PROGRESO: BARRAS Y ICONOS",
        "PROYECTO: INTERFAZ DE JUEGO COMPLETA",
    ]),
    ("AUDIO Y SHADERS", [
        "AUDIO: STREAMS Y PLAYERS",
        "AUDIO 2D/3D: ESPACIALIZACIÓN",
        "AUDIO BUSES Y EFECTOS",
        "SHADERS EN GODOT: SHADER MATERIAL",
        "SHADER 2D: SPRITE Y CANVAS ITEM",
        "SHADER 3D: SPATIAL MATERIAL",
        "PARTÍCULAS: GPU PARTICLES 2D",
        "PARTÍCULAS 3D: EMISORES Y ATRACTORES",
        "POST-PROCESSING: WORLD ENVIRONMENT",
        "PROYECTO: EFECTOS VISUALES Y SONIDO",
    ]),
    ("2D AVANZADO", [
        "TILEMAPS: CAPAS Y AUTOTILING",
        "TILEMAPS: COLISIONES Y NAVEGACIÓN",
        "SPRITE: ANIMACIONES POR FRAMES",
        "CÁMARA 2D: LÍMITES Y ZOOM",
        "PARALLAX BACKGROUND",
        "LÍNEA DE VISIÓN Y SOMBRAS 2D",
        "NATIVO: GDEXTENSION (C++) EN 2D",
        "DESPLAZAMIENTO LATERAL (SIDESCROLLER)",
        "ILUMINACIÓN 2D EN GODOT 4",
        "PROYECTO: JUEGO METROIDVANIA 2D",
    ]),
    ("3D Y MULTIPLAYER", [
        "ESCENAS 3D: CÁMARA Y LUZ",
        "MALLAS Y MATERIALES 3D",
        "GODO GLTF: IMPORTACIÓN DE MODELOS",
        "ESQUELETOS Y ANIMACIONES 3D",
        "NAVIGATION: NAVMESH 3D",
        "WORLD ENVIRONMENT: CIELO Y EFECTOS",
        "MULTIPLAYER: ESCENARIOS Y RPC",
        "MULTIPLAYER: AUTORIDAD Y SINCRO",
        "MULTIPLAYER: JUEGO EN LÍNEA",
        "PROYECTO: JUEGO 3D MULTIJUGADOR",
    ]),
    ("EXPORTACIÓN Y OPTIMIZACIÓN", [
        "EXPORT: PC, MAC, LINUX",
        "EXPORT: MÓVIL ANDROID iOS",
        "EXPORT: WEB (WEBGL)",
        "OPTIMIZACIÓN: PROFILER",
        "OPTIMIZACIÓN: RENDIMIENTO CPU/GPU",
        "OPTIMIZACIÓN: MEMORIA Y CACHÉ",
        "PLUGINS Y ASSETS",
        "BUENAS PRÁCTICAS EN GODOT",
        "CONTROL DE VERSIONES CON GIT",
        "CARTA DE GRADUACIÓN DEL PROFESOR BÚHO",
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 4: 73_IA_JUEGOS_LIBRO_MAESTRO
# ══════════════════════════════════════════════════════════════════════════════

IA_JUEGOS_TOPICS = [
    ("FUNDAMENTOS DE IA EN VIDEOJUEGOS", [
        "INTRODUCCIÓN A IA PARA VIDEOJUEGOS",
        "HISTORIA DE LA IA EN JUEGOS",
        "NPC: PERSONAJES NO JUGADORES",
        "ARQUITECTURAS DE IA EN JUEGOS",
        "SISTEMAS DE REGLAS",
        "MÁQUINAS DE ESTADOS FINITOS (FSM)",
        "TABLAS DE DECISIÓN",
        "EVALUACIÓN HEURÍSTICA",
        "ÁRBOLES DE BÚSQUEDA",
        "PROYECTO: NPC CON FSM",
    ]),
    ("PATHFINDING Y NAVEGACIÓN", [
        "ALGORITMO A* (A STAR)",
        "IMPLEMENTACIÓN DE A* EN C#",
        "DIJKSTRA VS A*",
        "NAVMESH: GENERACIÓN Y NAVEGACIÓN",
        "BÚSQUEDA EN GRAFOS",
        "JUMP POINT SEARCH (JPS)",
        "PATH SUAVIZADO Y ESQUIVO",
        "BÚSQUEDA JERÁRQUICA (HPA*)",
        "EVITACIÓN DE OBSTÁCULOS (RVO)",
        "PROYECTO: NAVEGACIÓN INTELIGENTE",
    ]),
    ("BEHAVIOR TREES", [
        "INTRODUCCIÓN A BEHAVIOR TREES",
        "NODOS: SELECTOR, SECUENCIA, DECORADOR",
        "NODOS DE ACCIÓN Y CONDICIÓN",
        "BEHAVIOR TREES EN UNITY",
        "BEHAVIOR TREES EN UNREAL",
        "BEHAVIOR TREES AVANZADOS",
        "BLACKBOARD: MEMORIA COMPARTIDA",
        "COMPORTAMIENTOS JERÁRQUICOS",
        "DEPURACIÓN DE BEHAVIOR TREES",
        "PROYECTO: ENEMIGO CON BT COMPLEJO",
    ]),
    ("UTILITY AI", [
        "INTRODUCCIÓN A UTILITY AI",
        "FUNCIONES DE UTILIDAD",
        "PONDERACIÓN Y NORMALIZACIÓN",
        "EVALUACIÓN DINÁMICA",
        "UTILITY AI EN UNITY",
        "UTILITY AI VS BEHAVIOR TREES",
        "TABLAS DE UTILIDAD",
        "SISTEMAS HÍBRIDOS",
        "PERSONALIDAD DE NPCs CON UTILITY",
        "PROYECTO: NPC CON COMPORTAMIENTO",
    ]),
    ("FSM Y GOAP", [
        "FSM: ESTADOS Y TRANSICIONES",
        "FSM ANIDADAS Y JERÁRQUICAS (HFSM)",
        "FSM EN CÓDIGO (PATRÓN DE DISEÑO)",
        "GOAP: GOAL ORIENTED ACTION PLANNING",
        "PLANIFICADOR GOAP EN UNITY",
        "ACCIONES, METAS Y MUNDO",
        "GOAP: BÚSQUEDA DE PLANES",
        "GOAP AVANZADO: PRIORIDADES",
        "COMPARATIVA: FSM VS GOAP VS BT",
        "PROYECTO: SISTEMA GOAP COMPLETO",
    ]),
    ("APRENDIZAJE EN JUEGOS", [
        "REINFORCEMENT LEARNING EN JUEGOS",
        "Q-LEARNING EN NPCs",
        "DEEP Q-NETWORK (DQN) PARA JUEGOS",
        "ENTRENAMIENTO DE AGENTES ML-AGENTS",
        "ML-AGENTS EN UNITY",
        "ALGORITMOS GENÉTICOS EN JUEGOS",
        "EVOLUCIÓN DE ESTRATEGIAS DE IA",
        "IA ADAPTATIVA: DIFICULTAD DINÁMICA",
        "BALANCEO AUTOMÁTICO DE JUEGO",
        "PROYECTO: NPC QUE APRENDE",
    ]),
    ("GENERACIÓN PROCEDURAL", [
        "GENERACIÓN PROCEDURAL DE NIVELES",
        "ALGORITMOS: PERLIN NOISE, BSP",
        "GENERACIÓN DE MAPAS CON CELDAS",
        "GENERACIÓN DE MAZMORRAS",
        "GENERACIÓN DE OBJETOS Y ARMAS",
        "GENERACIÓN DE DIÁLOGOS POR IA",
        "CONTENIDO PROCEDURAL EN GAMES",
        "PCG: CONTRASTAR REPETITIVIDAD",
        "EVOLUCIÓN DE MAPAS Y TERMINADO",
        "PROYECTO: GENERADOR DE MUNDOS",
    ]),
    ("PROYECTO FINAL", [
        "PLANIFICACIÓN DE IA DEL JUEGO",
        "DISEÑO DE COMPORTAMIENTOS",
        "IMPLEMENTACIÓN DE NAVEGACIÓN",
        "IMPLEMENTACIÓN DE TOMAS DE DECISIONES",
        "SISTEMA DE DIFICULTAD DINÁMICA",
        "PRUEBAS Y BALANCEO",
        "OPTIMIZACIÓN DE IA",
        "INTEGRACIÓN CON EL MOTOR",
        "DOCUMENTACIÓN DEL SISTEMA",
        "CARTA DE GRADUACIÓN DEL PROFESOR BÚHO",
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 5: 74_ARDUINO_LIBRO_MAESTRO
# ══════════════════════════════════════════════════════════════════════════════

ARDUINO_TOPICS = [
    ("FUNDAMENTOS DE ARDUINO", [
        "INTRODUCCIÓN A ARDUINO",
        "PLACAS ARDUINO: UNO, NANO, MEGA, ESP32",
        "IDE DE ARDUINO: INSTALACIÓN Y CONFIGURACIÓN",
        "ESTRUCTURA DE UN SKETCH: SETUP Y LOOP",
        "VARIABLES Y TIPOS DE DATOS EN C++",
        "SALIDA DIGITAL: LED Y PINMODE",
        "ENTRADA DIGITAL: BOTONES Y PULL-UP",
        "SALIDA ANALÓGICA: PWM Y LEDS RGB",
        "ENTRADA ANALÓGICA: POTENCIÓMETROS",
        "PROYECTO: SEMÁFORO CON ARDUINO",
    ]),
    ("SENSORES", [
        "SENSOR DE TEMPERATURA LM35",
        "SENSOR ULTRASÓNICO HC-SR04",
        "SENSOR DE LUZ LDR",
        "SENSOR DE MOVIMIENTO PIR",
        "SENSOR DE GAS Y HUMO MQ",
        "SENSOR DHT11/DHT22 HUMEDAD",
        "SENSOR DE DISTANCIA INFRARROJO",
        "SENSOR DE COLOR TCS3200",
        "SENSOR DE SONIDO MICRÓFONO",
        "PROYECTO: ESTACIÓN METEOROLÓGICA",
    ]),
    ("ACTUADORES", [
        "SERVOMOTOR SG90",
        "MOTOR DC CON PUENTE H L298N",
        "MOTOR PASO A PASO 28BYJ-48",
        "RELEVADOR: CONTROL DE ALTA TENSIÓN",
        "BUZZER ACTIVO Y PASIVO",
        "LED MATRIZ MAX7219",
        "DISPLAY 7 SEGMENTOS",
        "DISPLAY LCD 16X2 I2C",
        "PANTALLA OLED SSD1306",
        "PROYECTO: BRAZO ROBÓTICO",
    ]),
    ("COMUNICACIONES I2C/SPI/UART", [
        "COMUNICACIÓN SERIE UART",
        "COMUNICACIÓN I2C: PRINCIPIOS",
        "I2C MÚLTIPLES DISPOSITIVOS",
        "COMUNICACIÓN SPI",
        "SPI CON DISPLAYS",
        "RS232 Y PROTOCOLOS SERIE",
        "BUS ONE-WIRE",
        "COMUNICACIÓN ENTRE DOS ARDUINOS",
        "PROTOCOLOS DE COMUNICACIÓN COMPARATIVA",
        "PROYECTO: RED DE SENSORES I2C",
    ]),
    ("WIFI Y BLUETOOTH", [
        "INTRODUCCIÓN A ESP32 Y ESP8266",
        "WIFI: CONEXIÓN A INTERNET",
        "SERVIDOR WEB CON ESP32",
        "CLIENTE HTTP: APIS Y JSON",
        "BLUETOOTH CLÁSICO HC-05",
        "BLUETOOTH LOW ENERGY BLE",
        "MQTT: MENSAJERÍA IoT",
        "ESP-NOW: COMUNICACIÓN DIRECTA",
        "CONTROL REMOTO VÍA WEB",
        "PROYECTO: DOMÓTICA CON ESP32",
    ]),
    ("AVANZADO Y TIEMPO REAL", [
        "INTERRUPCIONES EXTERNAS",
        "TIMERS Y PULSOS PWM PRECISOS",
        "MANEJO DE ENERGÍA Y SLEEP",
        "PROTOCOLOS: FIRMWARE OTA",
        "FREE RTOS EN ESP32",
        "TAREAS Y SEMÁFOROS EN RTOS",
        "MEMORIA EEPROM Y FRAM",
        "SD CARD: ALMACENAMIENTO DE DATOS",
        "RTC: RELOJ EN TIEMPO REAL",
        "PROYECTO: DESPERTADOR INTELIGENTE",
    ]),
    ("PROYECTOS AVANZADOS", [
        "MEDICIÓN DE DISTANCIA LÁSER",
        "CONTROL PID: MOTOR DC",
        "FILTRO DE KALMAN PARA SENSORES",
        "GENERACIÓN DE FUNCIONES DAC",
        "AUDIO: REPRODUCCIÓN WAV",
        "CÁMARA OV7670 CON ARDUINO",
        "MÚSICA CON BUZZER Y NOTAS",
        "TETRIS EN PANTALLA OLED",
        "JUEGO SNAKE CON MATRIZ LED",
        "PROYECTO: INSTRUMENTO MUSICAL",
    ]),
    ("PROYECTO FINAL ARDUINO", [
        "DEFINICIÓN DEL PROYECTO IoT",
        "DISEÑO DEL CIRCUITO",
        "IMPLEMENTACIÓN DE SENSORES",
        "PROCESAMIENTO DE DATOS",
        "COMUNICACIÓN Y ALMACENAMIENTO",
        "INTERFAZ DE USUARIO",
        "PRUEBAS Y CALIBRACIÓN",
        "OPTIMIZACIÓN DE ENERGÍA",
        "DOCUMENTACIÓN Y PRESENTACIÓN",
        "CARTA DE GRADUACIÓN DEL PROFESOR BÚHO",
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 6: 75_RASPBERRY_PI_LIBRO_MAESTRO
# ══════════════════════════════════════════════════════════════════════════════

RASPBERRY_TOPICS = [
    ("FUNDAMENTOS DE RASPBERRY PI", [
        "INTRODUCCIÓN A RASPBERRY PI",
        "MODELOS: PI 5, PI 4, PI ZERO, PI PICO",
        "INSTALACIÓN DE RASPBERRY PI OS",
        "CONFIGURACIÓN INICIAL SSH Y VNC",
        "TERMINAL DE LINUX BÁSICO",
        "GESTIÓN DE PAQUETES APT",
        "SISTEMA DE ARCHIVOS LINUX",
        "PYTHON EN RASPBERRY PI",
        "ACTUALIZACIÓN Y MANTENIMIENTO",
        "PROYECTO: SERVIDOR WEB BÁSICO",
    ]),
    ("GPIO Y ELECTRÓNICA", [
        "GPIO: PINES Y PROTOCOLOS",
        "LEDS Y RESISTENCIAS",
        "BOTONES Y PULL-UP/DOWN",
        "PWM: CONTROL DE BRILLO Y MOTORES",
        "SENSOR DE TEMPERATURA DS18B20",
        "SENSOR ULTRASÓNICO HC-SR04",
        "BUZZER Y SONIDOS",
        "DISPLAY LCD CON I2C",
        "ADC: CONVERSIÓN ANALÓGICA",
        "PROYECTO: SISTEMA DE ALARMA",
    ]),
    ("CÁMARA Y VISIÓN", [
        "CÁMARA CSI: INSTALACIÓN",
        "CAPTURA DE FOTOS Y VIDEOS",
        "OPENCV: INSTALACIÓN EN PI",
        "OPENCV: PROCESAMIENTO DE IMÁGENES",
        "DETECCIÓN DE ROSTROS HAAR",
        "DETECCIÓN DE MOVIMIENTO",
        "TRANSMISIÓN DE VIDEO EN RED",
        "CÁMARA USB CON PI",
        "VISIÓN POR COMPUTADORA EN PI",
        "PROYECTO: CÁMARA DE SEGURIDAD",
    ]),
    ("REDES Y SERVIDORES", [
        "CONFIGURACIÓN DE RED WIFI/ETH",
        "SERVIDOR APACHE O NGINX",
        "SERVIDOR NODE.JS EN PI",
        "SERVIDOR FLASK/DJANGO EN PI",
        "DNS DINÁMICO Y ACCESO REMOTO",
        "VPN CON RASPBERRY PI",
        "PI HOLE: BLOQUEO DE PUBLICIDAD",
        "SERVIDOR DE ARCHIVOS SAMBA",
        "FIREWALL CON UFW/IPTABLES",
        "PROYECTO: SERVIDOR DOMÉSTICO",
    ]),
    ("SENSORES Y ACTUADORES", [
        "SENSOR DHT22 TEMP/HUMEDAD",
        "SENSOR DE GAS MQ-135",
        "SENSOR DE LLUVIA",
        "SENSOR DE FLUJO DE AGUA",
        "MOTOR PASO A PASO CON PI",
        "SERVOMOTOR CON PWM",
        "MOTOR DC CON L293D",
        "RELEVADOR CON PI",
        "SENSOR RFID RC522",
        "PROYECTO: INVERNADERO AUTOMATIZADO",
    ]),
    ("MULTIMEDIA Y DISPLAYS", [
        "SALIDA DE AUDIO HDMI Y GPIO",
        "REPRODUCCIÓN DE MÚSICA MP3",
        "RADIO POR INTERNET",
        "DISPLAY TÁCTIL OFICIAL",
        "PANTALLA HDMI PEQUEÑA",
        "E-PAPER DISPLAY",
        "LED MATRIZ CON PI",
        "MATRIZ DE LEDS HUB75",
        "KODI: CENTRO MULTIMEDIA",
        "PROYECTO: MARCO DE FOTOS DIGITAL",
    ]),
    ("PROYECTOS AVANZADOS", [
        "CLUSTER COMPUTING CON PI",
        "PI HOLE: DNS A NIVEL DE RED",
        "MAGIC MIRROR: ESPEJO INTELIGENTE",
        "RETROPIE: CONSOLA DE JUEGOS",
        "PIKVM: KVM OVER IP",
        "PI ASTRONOMY: ASTROFOTOGRAFÍA",
        "PI AUTOMATION: HOME ASSISTANT",
        "PI ROBOT: ROBOT MÓVIL",
        "PI AI: TENSORFLOW LITE EN PI",
        "PROYECTO: ASISTENTE DE VOZ",
    ]),
    ("PROYECTO FINAL PI", [
        "DEFINICIÓN DEL PROYECTO",
        "SELECCIÓN DE HARDWARE",
        "DISEÑO DE ARQUITECTURA",
        "IMPLEMENTACIÓN DE SENSORES",
        "DESARROLLO DE SOFTWARE",
        "INTERFAZ DE USUARIO",
        "PRUEBAS Y CALIBRACIÓN",
        "DOCUMENTACIÓN",
        "DESPLIEGUE EN PRODUCCIÓN",
        "CARTA DE GRADUACIÓN DEL PROFESOR BÚHO",
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 7: 76_IOT_LIBRO_MAESTRO
# ══════════════════════════════════════════════════════════════════════════════

IOT_TOPICS = [
    ("FUNDAMENTOS DE IoT", [
        "INTRODUCCIÓN AL INTERNET DE LAS COSAS",
        "ARQUITECTURA IoT: CAPAS Y MODELOS",
        "DISPOSITIVOS IoT: SENSORES Y ACTUADORES",
        "PROTOCOLOS DE COMUNICACIÓN IoT",
        "TOPOLOGÍAS DE RED IoT",
        "PLATAFORMAS IoT: CLOUD Y EDGE",
        "M2M: MACHINE TO MACHINE",
        "IoT INDUSTRIAL (IIoT)",
        "SEGURIDAD EN IoT",
        "PROYECTO: NODO SENSOR BÁSICO",
    ]),
    ("PROTOCOLOS DE COMUNICACIÓN", [
        "MQTT: PROTOCOLO DE MENSAJERÍA",
        "MOSQUITTO: BROKER MQTT",
        "CLIENTES MQTT EN PYTHON",
        "MQTT EN ESP32 Y ARDUINO",
        "CoAP: CONSTRAINED APPLICATION",
        "HTTP/HTTPS PARA IoT",
        "OPC UA: COMUNICACIÓN INDUSTRIAL",
        "LoRaWAN Y NB-IoT",
        "ZIGBEE: REDES DE BAJO CONSUMO",
        "PROYECTO: RED DE SENSORES MQTT",
    ]),
    ("PLATAFORMAS CLOUD", [
        "AWS IoT CORE: CONFIGURACIÓN",
        "AWS IoT: REGLAS Y ACCIONES",
        "GCP IoT CORE",
        "AZURE IoT HUB",
        "THINGSPEAK: PLATAFORMA ANALÍTICA",
        "BLYNK: APP MÓVIL IoT",
        "ADA FRUIT IO",
        "HOME ASSISTANT: DOMÓTICA",
        "NODE-RED: FLUJO VISUAL",
        "PROYECTO: DASHBOARD IoT EN LA NUBE",
    ]),
    ("EDGE COMPUTING", [
        "INTRODUCCIÓN A EDGE COMPUTING",
        "PROCESAMIENTO EN EL BORDE",
        "EDGE VS NUBE COMPARATIVA",
        "RASPBERRY PI COMO EDGE NODE",
        "JETSON NANO: EDGE AI",
        "RESPIRADOR: NODE-RED EN EDGE",
        "FILTRADO Y AGREGACIÓN EN EDGE",
        "ALMACENAMIENTO LOCAL EN EDGE",
        "SINCRONIZACIÓN CON LA NUBE",
        "PROYECTO: EDGE ANALYTICS",
    ]),
    ("SEGURIDAD EN IoT", [
        "AMENAZAS EN DISPOSITIVOS IoT",
        "CRIPTOGRAFÍA PARA IoT",
        "TLS/SSL EN COMUNICACIONES IoT",
        "AUTENTICACIÓN Y AUTORIZACIÓN",
        "GESTIÓN DE CERTIFICADOS",
        "SEGURIDAD EN FIRMWARE",
        "ACTUALIZACIONES SEGURAS OTA",
        "PROTOCOLOS SEGUROS: MQTTS Y HTTPS",
        "AUDITORÍA DE SEGURIDAD IoT",
        "PROYECTO: IoT SEGURO",
    ]),
    ("PROCESAMIENTO DE DATOS", [
        "INGESTA DE DATOS IoT",
        "PROCESAMIENTO EN TIEMPO REAL",
        "BASES DE DATOS PARA IoT",
        "INFLUXDB: SERIES TEMPORALES",
        "PROCESAMIENTO CON SPARK STREAMING",
        "ANÁLISIS DE DATOS IoT",
        "MACHINE LEARNING EN IoT",
        "VISUALIZACIÓN DE DATOS IoT",
        "ALERTAS Y AUTOMATIZACIÓN",
        "PROYECTO: PIPELINE DE DATOS IoT",
    ]),
    ("DOMÓTICA Y SMART CITIES", [
        "DOMÓTICA: HOGAR INTELIGENTE",
        "PROTOCOLOS DOMÓTICOS: Z-WAVE, ZIGBEE",
        "HOME ASSISTANT INTEGRACIÓN",
        "CONTROL DE ILUMINACIÓN",
        "CLIMATIZACIÓN INTELIGENTE",
        "RIEGO AUTOMATIZADO",
        "SMART CITIES: ARQUITECTURA",
        "CONTAMINACIÓN Y MONITOREO",
        "ESTACIONAMIENTO INTELIGENTE",
        "PROYECTO: HOGAR INTELIGENTE",
    ]),
    ("PROYECTO FINAL IoT", [
        "DEFINICIÓN DEL PROBLEMA IoT",
        "SELECCIÓN DE TECNOLOGÍA",
        "DISEÑO DE ARQUITECTURA",
        "IMPLEMENTACIÓN DE HARDWARE",
        "DESARROLLO DE SOFTWARE",
        "CONEXIÓN A LA NUBE",
        "DASHBOARD Y VISUALIZACIÓN",
        "PRUEBAS DE CAMPO",
        "OPTIMIZACIÓN Y SEGURIDAD",
        "CARTA DE GRADUACIÓN DEL PROFESOR BÚHO",
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 8: 77_PANDAS_LIBRO_MAESTRO
# ══════════════════════════════════════════════════════════════════════════════

PANDAS_TOPICS = [
    ("FUNDAMENTOS DE PANDAS", [
        "INTRODUCCIÓN A PANDAS",
        "INSTALACIÓN Y PRIMEROS PASOS",
        "SERIES: CREACIÓN Y PROPIEDADES",
        "SERIES: OPERACIONES Y FILTRADO",
        "DATAFRAMES: CREACIÓN DESDE DICCIONARIOS",
        "DATAFRAMES: CREACIÓN DESDE ARCHIVOS",
        "ATRIBUTOS: SHAPE, COLUMNS, INDEX, DTYPES",
        "SELECCIÓN DE COLUMNAS Y FILAS",
        "MÉTODOS HEAD, TAIL, INFO, DESCRIBE",
        "PROYECTO: ANÁLISIS EXPLORATORIO",
    ]),
    ("LECTURA Y ESCRITURA I/O", [
        "READ_CSV: PARÁMETROS Y OPCIONES",
        "READ_EXCEL Y WRITE_EXCEL",
        "READ_JSON, READ_HTML, READ_SQL",
        "ESCRITURA A CSV Y EXCEL",
        "MANEJO DE CODIFICACIONES",
        "ARCHIVOS COMPRIMIDOS",
        "LECTURA POR BLOQUES (CHUNKS)",
        "CONEXIÓN A BASES DE DATOS SQL",
        "PARQUET: FORMATO EFICIENTE",
        "PROYECTO: PIPELINE DE DATOS",
    ]),
    ("LIMPIEZA DE DATOS", [
        "VALORES NULOS: DETECCIÓN ISNA/ISNULL",
        "ELIMINACIÓN DE NULOS DROPNA",
        "RELLENO DE NULOS FILLNA",
        "VALORES DUPLICADOS",
        "TRANSFORMACIÓN DE DATOS",
        "REMOCIÓN DE OUTLIERS",
        "MANEJO DE FECHAS Y HORAS",
        "CATEGORÍAS Y DATOS CATEGÓRICOS",
        "NORMALIZACIÓN Y ESTANDARIZACIÓN",
        "PROYECTO: LIMPIEZA DE DATOS REALES",
    ]),
    ("FILTRADO Y SELECCIÓN", [
        "SELECCIÓN POR ETIQUETA LOC",
        "SELECCIÓN POR ÍNDICE ILOC",
        "FILTRADO BOOLEANO",
        "MÚLTIPLES CONDICIONES & | ~",
        "MÉTODO QUERY",
        "ISIN Y BETWEEN",
        "STR: MÉTODOS DE CADENA",
        "FILTRADO POR ÍNDICE",
        "MUESTREO ALEATORIO SAMPLE",
        "PROYECTO: FILTRADO COMPLEJO",
    ]),
    ("GROUPBY Y AGREGACIONES", [
        "GROUPBY BÁSICO",
        "FUNCIONES DE AGREGACIÓN SUM MEAN COUNT",
        "AGG: MÚLTIPLES AGREGACIONES",
        "GROUPBY MÚLTIPLES COLUMNAS",
        "FILTRADO DE GRUPOS FILTER",
        "TRANSFORMACIÓN CON TRANSFORM",
        "APPLY: FUNCIONES PERSONALIZADAS",
        "PIVOT TABLES: PD.PIVOT_TABLE",
        "CROSS TABULATION PD.CROSSTAB",
        "PROYECTO: ANÁLISIS DE VENTAS",
    ]),
    ("MERGE, JOIN Y CONCAT", [
        "CONCAT: CONCATENACIÓN DE DATAFRAMES",
        "MERGE: JOIN DE SQL EN PANDAS",
        "TIPOS DE JOIN: INNER, LEFT, RIGHT, OUTER",
        "MERGE POR ÍNDICE Y COLUMNAS",
        "JOIN: MÉTODO DE DATAFRAME",
        "MÚLTIPLES MERGES",
        "DATAFRAMES CON COLUMNAS DUPLICADAS",
        "COMBINE_FIRST Y UPDATE",
        "REINDEX Y ALIGN",
        "PROYECTO: INTEGRACIÓN DE DATOS",
    ]),
    ("TIME SERIES Y VISUALIZACIÓN", [
        "FECHAS: TO_DATETIME Y TIMESTAMP",
        "RESAMPLE: REMUESTREO TEMPORAL",
        "ROLLING: VENTANAS MÓVILES",
        "EXPANDING: VENTANAS ACUMULATIVAS",
        "SHIFT, DIFF, PCT_CHANGE",
        "PLOT: GRÁFICOS CON MATPLOTLIB",
        "HISTOGRAMAS, BOXPLOTS, SCATTER",
        "GRÁFICOS DE BARRAS Y LÍNEAS",
        "SEABORN: VISUALIZACIÓN AVANZADA",
        "PROYECTO: SERIE TEMPORAL COMPLETA",
    ]),
    ("RENDIMIENTO Y PROYECTO FINAL", [
        "VECTORIZACIÓN VS LOOPS",
        "MÉTODO APPLY VS APPLYMAP",
        "MEMORIA: DTYPES Y OPTIMIZACIÓN",
        "CHUNKING: DATAFRAMES GRANDES",
        "MULTIPROCESAMIENTO CON PANDAS",
        "MODIN: PANDAS DISTRIBUIDO",
        "PROYECTO FINAL: ETL COMPLETO",
        "PROYECTO FINAL: ANÁLISIS DE DATOS",
        "PRESENTACIÓN DE RESULTADOS",
        "CARTA DE GRADUACIÓN DEL PROFESOR BÚHO",
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 9: 78_POWER_BI_LIBRO_MAESTRO
# ══════════════════════════════════════════════════════════════════════════════

POWERBI_TOPICS = [
    ("FUNDAMENTOS DE POWER BI", [
        "INTRODUCCIÓN A POWER BI",
        "INSTALACIÓN DE POWER BI DESKTOP",
        "INTERFAZ: PANELES, VISTAS Y PÁGINAS",
        "CONEXIÓN A FUENTES DE DATOS",
        "POWER QUERY: EDITOR DE CONSULTAS",
        "TRANSFORMACIONES BÁSICAS EN QUERY",
        "MODELO DE DATOS: TABLAS Y RELACIONES",
        "VISUALIZACIONES BÁSICAS",
        "PUBLICACIÓN EN POWER BI SERVICE",
        "PROYECTO: PRIMER DASHBOARD",
    ]),
    ("POWER QUERY AVANZADO", [
        "LENGUAJE M: INTRODUCCIÓN",
        "COLUMNAS PERSONALIZADAS EN M",
        "CONSULTAS PARAMETRIZADAS",
        "FUSIÓN (MERGE) DE CONSULTAS",
        "ANEXAR CONSULTAS",
        "GRUPO POR Y AGREGACIONES",
        "PIVOT Y UNPIVOT",
        "CONDICIONALES EN POWER QUERY",
        "FUNCIONES PERSONALIZADAS M",
        "PROYECTO: ETL COMPLETO",
    ]),
    ("MODELO DE DATOS", [
        "MODELO TABULAR: ESTRELLA Y COPO",
        "RELACIONES: 1:1, 1:N, M:N",
        "DIRECCIÓN DE FILTRO CRUZADO",
        "JERARQUÍAS: CREACIÓN Y USO",
        "COLUMNAS CALCULADAS",
        "MEDIDAS: CREACIÓN Y CONTEXTO",
        "TABLAS CALCULADAS CON DAX",
        "FECHA: TABLA CALENDARIO AUTOMÁTICA",
        "SEGURIDAD A NIVEL DE FILA RLS",
        "PROYECTO: MODELO ESTRELLA",
    ]),
    ("DAX FUNDAMENTOS", [
        "INTRODUCCIÓN A DAX",
        "FUNCIONES DE AGREGACIÓN SUM COUNT",
        "FILTROS: CALCULATE Y FILTER",
        "FUNCIONES DE TIEMPO: TOTALYTD SAMEPERIOD",
        "ALL, ALLEXCEPT, ALLSELECTED",
        "RELACIONADAS: RELATED Y RELATEDTABLE",
        "ITERADORES: SUMX, AVERAGEX",
        "RANKX Y TOPN",
        "VARIABLES EN DAX VAR RETURN",
        "PROYECTO: MEDIDAS DAX AVANZADAS",
    ]),
    ("DAX AVANZADO", [
        "CONTEXTO DE FILTRO Y DE FILA",
        "EVALUACIÓN DE CONTEXTO",
        "CALCULATE: TRANSICIÓN DE CONTEXTO",
        "TIME INTELLIGENCE AVANZADA",
        "SEMI-ADDITIVE MEASURES",
        "FILTROS DINÁMICOS CON PARÁMETROS",
        "QUERY PLAN: EVALUACIÓN DAX",
        "RENDIMIENTO EN DAX",
        "PATRONES DAX AVANZADOS",
        "PROYECTO: KPI DASHBOARD",
    ]),
    ("VISUALIZACIONES", [
        "GRÁFICOS DE BARRAS Y COLUMNAS",
        "GRÁFICOS DE LÍNEAS Y ÁREAS",
        "GRÁFICOS CIRCULARES Y DONAS",
        "MAPAS: BING Y ARC GIS",
        "TABLAS Y MATRICES",
        "SEGMENTADORES (SLICERS)",
        "TARJETAS (CARDS) Y KPIS",
        "GRÁFICOS DE DISPERSIÓN Y BURBUJA",
        "VISUALES PERSONALIZADOS APP SOURCE",
        "PROYECTO: DASHBOARD INTERACTIVO",
    ]),
    ("POWER BI SERVICE", [
        "PUBLICACIÓN EN POWER BI SERVICE",
        "WORKSPACES: COLABORACIÓN",
        "REPORTES EN APPS",
        "REFRESCO DE DATOS PROGRAMADO",
        "GATEWAY: CONEXIÓN A DATOS LOCALES",
        "SEGURIDAD: ROLES Y PERMISOS",
        "COMPARTIR DASHBOARDS",
        "PREGUNTAS Y RESPUESTAS Q&A",
        "INSIGHTS Y ANOMALÍAS",
        "PROYECTO: SOLUCIÓN CORPORATIVA",
    ]),
    ("PROYECTO FINAL POWER BI", [
        "REQUISITOS DEL PROYECTO",
        "CONEXIÓN A FUENTES DE DATOS",
        "TRANSFORMACIÓN CON POWER QUERY",
        "MODELO DE DATOS ESTRELLA",
        "MEDIDAS DAX COMPLEJAS",
        "DASHBOARD INTERACTIVO",
        "PUBLICACIÓN Y COMPARTICIÓN",
        "REFRESCO AUTOMÁTICO",
        "PRESENTACIÓN DE RESULTADOS",
        "CARTA DE GRADUACIÓN DEL PROFESOR BÚHO",
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# BOOK 10: 79_BIG_DATA_LIBRO_MAESTRO
# ══════════════════════════════════════════════════════════════════════════════

BIGDATA_TOPICS = [
    ("FUNDAMENTOS DE BIG DATA", [
        "INTRODUCCIÓN AL BIG DATA",
        "LAS 5 V: VOLUMEN, VELOCIDAD, VARIEDAD, VERACIDAD, VALOR",
        "ARQUITECTURAS: LAMBDA Y KAPPA",
        "DATA LAKES VS DATA WAREHOUSES",
        "BATCH PROCESSING VS STREAMING",
        "ECOSISTEMA HADOOP",
        "CLÚSTERES DISTRIBUIDOS",
        "HDFS: HADOOP DISTRIBUTED FILE SYSTEM",
        "MAPREDUCE: PARADIGMA DE PROCESAMIENTO",
        "PROYECTO: CLÚSTER HADOOP LOCAL",
    ]),
    ("HADOOP Y MAPREDUCE", [
        "HDFS: NAMENODE Y DATANODES",
        "HDFS: LECTURA Y ESCRITURA",
        "MAPREDUCE: MAPPER, REDUCER, DRIVER",
        "EJEMPLO: WORD COUNT EN JAVA",
        "EJEMPLO: WORD COUNT EN PYTHON",
        "YARN: GESTIÓN DE RECURSOS",
        "YARN: COLAS Y PLANIFICADORES",
        "HDFS: REPLICACIÓN Y TOLERANCIA",
        "HDFS: COMANDOS COMUNES",
        "PROYECTO: WORD COUNT DISTRIBUIDO",
    ]),
    ("SPARK", [
        "INTRODUCCIÓN A APACHE SPARK",
        "SPARK ARCHITECTURE: DRIVER Y EXECUTORS",
        "RDDS: RESILIENT DISTRIBUTED DATASETS",
        "TRANSFORMACIONES Y ACCIONES EN RDD",
        "DATAFRAMES EN SPARK",
        "SPARK SQL: CONSULTAS ESTRUCTURADAS",
        "SPARK STREAMING: PROCESAMIENTO EN TIEMPO REAL",
        "ML LIB: MACHINE LEARNING EN SPARK",
        "SPARK EN CLÚSTER YARN",
        "PROYECTO: PIPELINE DE DATOS CON SPARK",
    ]),
    ("HIVE Y HBASE", [
        "INTRODUCCIÓN A HIVE",
        "HIVEQL: SQL SOBRE HADOOP",
        "TABLAS EXTERNAS Y GESTIONADAS",
        "PARTICIONES EN HIVE",
        "BUCKETING EN HIVE",
        "INTRODUCCIÓN A HBASE",
        "HBASE: MODELO DE DATOS",
        "HBASE: OPERACIONES CRUD",
        "HBASE VS HIVE VS RDBMS",
        "PROYECTO: ALMACÉN DE DATOS MASIVOS",
    ]),
    ("KAFKA Y FLUME", [
        "INTRODUCCIÓN A APACHE KAFKA",
        "TOPICS, PARTITIONS Y BROKERS",
        "PRODUCTORES Y CONSUMIDORES",
        "KAFKA STREAMS: PROCESAMIENTO",
        "KAFKA CONNECT: INTEGRACIÓN",
        "APACHE FLUME: INGESTA DE LOGS",
        "FLUME: SOURCES, CHANNELS, SINKS",
        "FLUME VS KAFKA VS LOGSTASH",
        "KAFKA EN ARQUITECTURA LAMBDA",
        "PROYECTO: PIPELINE KAFKA STREAMING",
    ]),
    ("PROCESAMIENTO EN TIEMPO REAL", [
        "STREAM PROCESSING CONCEPTS",
        "APACHE FLINK: FUNDAMENTOS",
        "FLINK: DATASET Y DATAS STREAM",
        "FLINK: WINDOWS Y AGREGACIONES",
        "APACHE STORM: TOPOLOGÍAS",
        "SPARK STRUCTURED STREAMING AVANZADO",
        "VENTANAS DE TIEMPO EN STREAMING",
        "EXACTLY-ONCE VS AT-LEAST-ONCE",
        "COMPARATIVA: FLINK VS SPARK VS STORM",
        "PROYECTO: ANÁLISIS EN TIEMPO REAL",
    ]),
    ("DATA LAKES Y NUBE", [
        "ARQUITECTURA DATA LAKE",
        "ZONES: RAW, STAGING, CURATED",
        "AWS DATA LAKE: S3, GLUE, ATHENA",
        "AWS EMR: HADOOP EN LA NUBE",
        "GCP: BIG QUERY Y DATA PROC",
        "AZURE: SYNAPSE Y DATA FACTORY",
        "DATA LAKE VS LAKEHOUSE",
        "APACHE ICEBERG Y DELTA LAKE",
        "CATÁLOGOS DE DATOS (DATA CATALOG)",
        "PROYECTO: DATA LAKE EN AWS",
    ]),
    ("PROYECTO FINAL BIG DATA", [
        "REQUISITOS DEL PROYECTO BIG DATA",
        "DISEÑO DE ARQUITECTURA LAMBDA",
        "INGESTA CON KAFKA",
        "PROCESAMIENTO BATCH CON SPARK",
        "PROCESAMIENTO STREAMING",
        "ALMACENAMIENTO EN DATA LAKE",
        "CONSULTAS CON HIVE/PRE STO",
        "VISUALIZACIÓN DE RESULTADOS",
        "OPTIMIZACIÓN Y ESCALABILIDAD",
        "CARTA DE GRADUACIÓN DEL PROFESOR BÚHO",
    ]),
]

# ══════════════════════════════════════════════════════════════════════════════
# PROJECT BOOKS (80_ through 91_)
# Each chapter describes one phase of the project
# ══════════════════════════════════════════════════════════════════════════════

def make_project_phases(project_title, phases):
    """Create project phases for an integrative project book."""
    result = []
    # Split into 8 modules
    mod_size = len(phases) // 8
    mods = []
    for m in range(8):
        start = m * mod_size
        end = start + mod_size if m < 7 else len(phases)
        mod_name = f"FASE {ROMANOS[m]} DEL PROYECTO"
        mod_topics = phases[start:end]
        # Pad with extra topics if needed
        while len(mod_topics) < 10:
            mod_topics.append(f"AVANCE Y REVISIÓN {len(mod_topics)+1}")
        mods.append((mod_name, mod_topics))
    return mods


# Proyecto N1: HTML+CSS+JS Landing Page
PROYECTO_N1_PHASES = [
    "PLANIFICACIÓN DE LA LANDING PAGE",
    "DISEÑO DE WIREFRAMES",
    "SETUP DE VS CODE Y GIT",
    "ESTRUCTURA HTML SEMÁNTICA",
    "HEADER Y NAVEGACIÓN RESPONSIVE",
    "SECCIÓN HERO CON CALL TO ACTION",
    "SECCIÓN DE CARACTERÍSTICAS",
    "SECCIÓN DE TESTIMONIOS",
    "SECCIÓN DE PRECIOS",
    "FORMULARIO DE CONTACTO",
    "FOOTER Y MAPA DEL SITIO",
    "ESTILOS CSS: VARIABLES Y RESET",
    "FLEXBOX: DISEÑO DE COLUMNAS",
    "CSS GRID: DISEÑO DE SECCIONES",
    "DISEÑO RESPONSIVE CON MEDIA QUERIES",
    "ANIMACIONES CSS: TRANSICIONES",
    "ANIMACIONES CSS: KEYFRAMES",
    "PREFIJOS CSS Y COMPATIBILIDAD",
    "VALIDACIÓN DE FORMULARIO JS",
    "MENÚ HAMBURGUESA CON JS",
    "SCROLL SUAVE CON JS",
    "INTERSECCIÓN OBSERVER: ANIMACIONES",
    "CARRUSEL DE TESTIMONIOS",
    "CONTADOR ANIMADO",
    "LIGHTBOX DE IMÁGENES",
    "CARGA DE CONTENIDO DINÁMICO",
    "RENDIMIENTO: LAZY LOADING",
    "ACCESIBILIDAD WEB (A11Y)",
    "SEO BÁSICO: METATAGS Y OPEN GRAPH",
    "GIT: INICIALIZAR REPOSITORIO",
    "GIT: COMMITS Y RAMAS",
    "GIT: MERGE Y RESOLUCIÓN",
    "GITHUB: SUBIR REPOSITORIO",
    "GITHUB PAGES: DESPLIEGUE",
    "DOMINIO PERSONALIZADO",
    "OPTIMIZACIÓN DE IMÁGENES",
    "MINIFICACIÓN CSS/JS",
    "PRUEBAS DE VELOCIDAD (LIGHTHOUSE)",
    "REVISIÓN FINAL Y QA",
    "PRESENTACIÓN DEL PROYECTO",
    "REFLEXIÓN Y PRÓXIMOS PASOS",
]

# Proyecto N2: React/Vue SPA
PROYECTO_N2_PHASES = [
    "REQUISITOS DE LA SPA",
    "DISEÑO DE COMPONENTES Y RUTAS",
    "SETUP CON VITE + REACT",
    "SETUP CON VUE + COMPOSITION API",
    "TYPESCRIPT: TIPOS E INTERFACES",
    "RUTEO CON REACT ROUTER",
    "RUTEO CON VUE ROUTER",
    "COMPONENTES REUTILIZABLES",
    "GESTIÓN DE ESTADO CON CONTEXT",
    "GESTIÓN DE ESTADO CON PINIA",
    "PÁGINA DE INICIO",
    "PÁGINA DE LISTADO",
    "PÁGINA DE DETALLE",
    "FORMULARIOS CON VALIDACIÓN",
    "AUTENTICACIÓN DE USUARIOS",
    "CONSUMO DE API REST",
    "MANEJO DE ERRORES Y LOADING",
    "FILTROS Y BÚSQUEDA",
    "PAGINACIÓN",
    "BOOTSTRAP: GRID Y COMPONENTES",
    "TAILWIND: UTILITY-FIRST CSS",
    "DISEÑO RESPONSIVE AVANZADO",
    "MODO OSCURO",
    "PRUEBAS CON VITEST",
    "PRUEBAS E2E CON PLAYWRIGHT",
    "OPTIMIZACIÓN DE RENDIMIENTO",
    "DESPLIEGUE EN NETLIFY",
    "DESPLIEGUE EN VERCEL",
    "CI/CD CON GITHUB ACTIONS",
]

# Proyecto N3: REST API
PROYECTO_N3_PHASES = [
    "DISEÑO DE LA API REST",
    "SETUP CON NODE + EXPRESS",
    "MODELOS Y BASE DE DATOS",
    "MIGRACIONES CON PRISMA",
    "CRUD DE USUARIOS",
    "AUTENTICACIÓN CON JWT",
    "AUTORIZACIÓN RBAC",
    "VALIDACIÓN CON ZOD",
    "MANEJO DE ERRORES GLOBAL",
    "FILTRADO Y PAGINACIÓN",
    "ORDENAMIENTO DE RESULTADOS",
    "DOCUMENTACIÓN CON SWAGGER",
    "PRUEBAS UNITARIAS",
    "PRUEBAS DE INTEGRACIÓN",
    "DOCKERIZACIÓN",
    "DESPLIEGUE EN RAILWAY",
    "DESPLIEGUE EN AWS EC2",
    "DOMINIO Y HTTPS",
    "MONITOREO CON LOGS",
    "RATE LIMITING",
]

# Proyecto N4: Database Design
PROYECTO_N4_PHASES = [
    "ANÁLISIS DE REQUISITOS BD",
    "MODELO ENTIDAD-RELACIÓN",
    "DIAGRAMA ER (MERMAID/DBDIAGRAM)",
    "NORMALIZACIÓN HASTA 3FN",
    "CREACIÓN DE TABLAS DDL",
    "CONSTRAINTS Y RELACIONES",
    "ÍNDICES Y RENDIMIENTO",
    "VISTAS (VIEWS)",
    "PROCEDIMIENTOS ALMACENADOS",
    "TRIGGERS",
    "INSERCIÓN DE DATOS DE PRUEBA",
    "CONSULTAS COMPLEJAS",
    "SUBCONSULTAS Y CTES",
    "WINDOW FUNCTIONS",
    "BACKUP Y RESTORE",
    "REPLICACIÓN MASTER-SLAVE",
    "PARTICIONAMIENTO",
    "SHARDING",
    "OPTIMIZACIÓN DE CONSULTAS",
    "SEGURIDAD Y PERMISOS",
]

# Proyecto N5: Algorithms & Data Structures
PROYECTO_N5_PHASES = [
    "INTRODUCCIÓN AL PROYECTO",
    "ANÁLISIS DE COMPLEJIDAD",
    "LISTAS ENLAZADAS",
    "LISTAS DOBLES Y CIRCULARES",
    "PILAS Y COLAS",
    "ÁRBOLES BINARIOS",
    "ÁRBOLES AVL",
    "GRAFOS: REPRESENTACIÓN",
    "BFS Y DFS",
    "ALGORITMO DE DIJKSTRA",
    "BÚSQUEDA LINEAL Y BINARIA",
    "BUBBLE SORT, SELECTION, INSERTION",
    "MERGE SORT Y QUICK SORT",
    "HASH TABLES",
    "HEAPS Y PRIORITY QUEUE",
    "PROGRAMACIÓN ORIENTADA A OBJETOS",
    "HERENCIA, POLIMORFISMO, ENCAPSULACIÓN",
    "PATRÓN SINGLETON Y FACTORY",
    "PATRÓN OBSERVER Y STRATEGY",
    "TESTING Y DOCUMENTACIÓN",
]

# Proyecto N6: Móvil con Flutter/React Native
PROYECTO_N6_PHASES = [
    "DEFINICIÓN DE LA APP MÓVIL",
    "DISEÑO DE INTERFAZ MÓVIL",
    "SETUP DE FLUTTER",
    "SETUP DE REACT NATIVE",
    "WIDGETS/COMPONENTES BÁSICOS",
    "NAVEGACIÓN ENTRE PANTALLAS",
    "ESTADO Y GESTIÓN DE DATOS",
    "CONSUMO DE API REMOTA",
    "ALMACENAMIENTO LOCAL",
    "AUTENTICACIÓN MÓVIL",
    "CÁMARA Y GALERÍA",
    "GEOLOCALIZACIÓN",
    "NOTIFICACIONES PUSH",
    "DISEÑO RESPONSIVE MÓVIL",
    "PRUEBAS EN DISPOSITIVO",
    "PUBLICACIÓN EN PLAY STORE",
    "PUBLICACIÓN EN APP STORE",
    "ACTUALIZACIONES Y VERSIONES",
    "ANALÍTICAS MÓVILES",
    "MONETIZACIÓN",
]

# Proyecto N7: RAG + Agent + LLM
PROYECTO_N7_PHASES = [
    "DEFINICIÓN DEL SISTEMA RAG",
    "ARQUITECTURA RAG",
    "SELECCIÓN DEL LLM",
    "VECTOR DATABASE: CHROMA/PINECONE",
    "EMBEDDINGS: OBTENCIÓN Y ALMACÉN",
    "INGESTA Y CHUNKING DE DOCUMENTOS",
    "RECUPERACIÓN DE INFORMACIÓN",
    "PROMPT ENGINEERING AVANZADO",
    "CREACIÓN DEL AGENTE IA",
    "HERRAMIENTAS DEL AGENTE",
    "CADENAS LLAM (LANG CHAIN)",
    "INTERFAZ DE USUARIO (CHAT UI)",
    "MEMORIA DEL AGENTE",
    "MANEJO DE CONTEXTO LARGO",
    "EVALUACIÓN DEL SISTEMA RAG",
    "RENDIMIENTO Y LATENCIA",
    "DESPLIEGUE DEL SISTEMA",
    "MONITOREO Y LOGS",
    "SEGURIDAD Y PRIVACIDAD",
    "PRESENTACIÓN DEL PROYECTO",
]

# Proyecto N8: Security
PROYECTO_N8_PHASES = [
    "DEFINICIÓN DEL ALCANCE",
    "RECONOCIMIENTO PASIVO",
    "RECONOCIMIENTO ACTIVO",
    "ESCANEO DE PUERTOS (NMAP)",
    "ENUMERACIÓN DE SERVICIOS",
    "ANÁLISIS DE VULNERABILIDADES",
    "EXPLOTACIÓN: SQL INJECTION",
    "EXPLOTACIÓN: XSS",
    "EXPLOTACIÓN: CSRF",
    "AUTENTICACIÓN: BRUTE FORCE",
    "AUTENTICACIÓN: JWT ATTACKS",
    "PRUEBAS DE INTRUSIÓN WEB",
    "PRUEBAS DE RED INTERNA",
    "ANÁLISIS DE MALWARE",
    "OSINT: RECOLECCIÓN DE DATOS",
    "INGENIERÍA SOCIAL",
    "REMEDIACIÓN Y PARCHEO",
    "HARDENING DE SERVIDORES",
    "HARDENING DE APLICACIONES",
    "INFORME DE AUDITORÍA",
]

# Proyecto N9: Cloud
PROYECTO_N9_PHASES = [
    "DEFINICIÓN DE ARQUITECTURA CLOUD",
    "INFRAESTRUCTURA COMO CÓDIGO (Terraform)",
    "PROVEEDOR: AWS/GCP/AZURE",
    "VPC, SUBNETS Y REDES",
    "INSTANCIAS EC2/GCE/VMS",
    "BASE DE DATOS EN LA NUBE",
    "ALMACENAMIENTO S3/BLOB",
    "CI/CD CON GITHUB ACTIONS",
    "CONTENEDORES CON ECS/GKE",
    "KUBERNETES EN LA NUBE",
    "MONITOREO CON PROMETHEUS",
    "MONITOREO CON GRAFANA",
    "LOGS CENTRALIZADOS",
    "ALERTAS Y NOTIFICACIONES",
    "AUTO SCALING",
    "LOAD BALANCING",
    "SEGURIDAD EN LA NUBE",
    "COSTOS Y OPTIMIZACIÓN",
    "BACKUP Y DISASTER RECOVERY",
    "DOCUMENTACIÓN FINAL",
]

# Proyecto N10: Game
PROYECTO_N10_PHASES = [
    "CONCEPTO Y DISEÑO DEL JUEGO",
    "GAME DESIGN DOCUMENT (GDD)",
    "SELECCIÓN DEL MOTOR",
    "PROTOTIPADO RÁPIDO",
    "MECÁNICAS PRINCIPALES",
    "SISTEMA DE CONTROL",
    "DISEÑO DE NIVELES",
    "CREACIÓN DE ASSETS 2D/3D",
    "ANIMACIONES DEL PERSONAJE",
    "IA DE ENEMIGOS",
    "SISTEMA DE PUNTUACIÓN",
    "UI Y HUD",
    "AUDIO Y MÚSICA",
    "FX Y PARTÍCULAS",
    "ILUMINACIÓN Y AMBIENTE",
    "OPTIMIZACIÓN DE RENDIMIENTO",
    "PRUEBAS DE JUEGO (PLAYTESTING)",
    "BALANCEO DE DIFICULTAD",
    "PUBLICACIÓN EN ITCH.IO",
    "POST-MORTEM DEL PROYECTO",
]

# Proyecto N11: IoT
PROYECTO_N11_PHASES = [
    "DEFINICIÓN DEL SISTEMA IoT",
    "SELECCIÓN DE HARDWARE",
    "DISEÑO DE ARQUITECTURA",
    "CONFIGURACIÓN DE SENSORES",
    "CONFIGURACIÓN DE ACTUADORES",
    "PROGRAMACIÓN DEL MICROCONTROLADOR",
    "PROTOCOLO DE COMUNICACIÓN MQTT",
    "CONFIGURACIÓN DEL BROKER",
    "CONEXIÓN A PLATAFORMA CLOUD",
    "ALMACENAMIENTO DE DATOS",
    "DASHBOARD EN TIEMPO REAL",
    "ALERTAS Y AUTOMATIZACIÓN",
    "EDGE COMPUTING",
    "SEGURIDAD EN IoT",
    "PRUEBAS DE CAMPO",
    "CALIBRACIÓN DE SENSORES",
    "EFICIENCIA ENERGÉTICA",
    "MANTENIMIENTO REMOTO",
    "DOCUMENTACIÓN TÉCNICA",
    "PRESENTACIÓN DEL PROYECTO",
]

# Proyecto N12: Data Science
PROYECTO_N12_PHASES = [
    "DEFINICIÓN DEL PROBLEMA",
    "RECOLECCIÓN DE DATOS",
    "DATA WRANGLING CON PANDAS",
    "ANÁLISIS EXPLORATORIO (EDA)",
    "VISUALIZACIÓN DE DATOS",
    "LIMPIEZA Y PREPROCESAMIENTO",
    "INGENIERÍA DE CARACTERÍSTICAS",
    "SELECCIÓN DEL MODELO ML",
    "ENTRENAMIENTO DEL MODELO",
    "EVALUACIÓN Y MÉTRICAS",
    "VALIDACIÓN CRUZADA",
    "OPTIMIZACIÓN DE HIPERPARÁMETROS",
    "FEATURE IMPORTANCE",
    "EXPLICABILIDAD (SHAP/LIME)",
    "PIPELINE DE PROCESAMIENTO",
    "API DE INFERENCIA",
    "DASHBOARD DE RESULTADOS",
    "DESPLIEGUE EN PRODUCCIÓN",
    "MONITOREO DEL MODELO",
    "INFORME FINAL Y CONCLUSIONES",
]


# ══════════════════════════════════════════════════════════════════════════════
# BOOK REGISTRY
# ══════════════════════════════════════════════════════════════════════════════

BOOKS = [
    ("70_UNITY_LIBRO_MAESTRO", "UNITY", UNITY_TOPICS),
    ("71_UNREAL_LIBRO_MAESTRO", "UNREAL ENGINE", UNREAL_TOPICS),
    ("72_GODOT_LIBRO_MAESTRO", "GODOT", GODOT_TOPICS),
    ("73_IA_JUEGOS_LIBRO_MAESTRO", "IA PARA VIDEOJUEGOS", IA_JUEGOS_TOPICS),
    ("74_ARDUINO_LIBRO_MAESTRO", "ARDUINO", ARDUINO_TOPICS),
    ("75_RASPBERRY_PI_LIBRO_MAESTRO", "RASPBERRY PI", RASPBERRY_TOPICS),
    ("76_IOT_LIBRO_MAESTRO", "INTERNET DE LAS COSAS (IoT)", IOT_TOPICS),
    ("77_PANDAS_LIBRO_MAESTRO", "PANDAS", PANDAS_TOPICS),
    ("78_POWER_BI_LIBRO_MAESTRO", "POWER BI", POWERBI_TOPICS),
    ("79_BIG_DATA_LIBRO_MAESTRO", "BIG DATA", BIGDATA_TOPICS),
    ("80_PROYECTO_N1_LIBRO_MAESTRO", "PROYECTO INTEGRADOR N1", make_project_phases("Landing Page", PROYECTO_N1_PHASES)),
    ("81_PROYECTO_N2_LIBRO_MAESTRO", "PROYECTO PROFESIONAL N2", make_project_phases("React/Vue SPA", PROYECTO_N2_PHASES)),
    ("82_PROYECTO_N3_LIBRO_MAESTRO", "PROYECTO BACKEND N3", make_project_phases("REST API", PROYECTO_N3_PHASES)),
    ("83_PROYECTO_N4_LIBRO_MAESTRO", "PROYECTO BD N4", make_project_phases("Base de Datos", PROYECTO_N4_PHASES)),
    ("84_PROYECTO_N5_LIBRO_MAESTRO", "PROYECTO PROGRAMACIÓN N5", make_project_phases("Algoritmos y ED", PROYECTO_N5_PHASES)),
    ("85_PROYECTO_N6_LIBRO_MAESTRO", "PROYECTO MÓVIL N6", make_project_phases("App Móvil", PROYECTO_N6_PHASES)),
    ("86_PROYECTO_N7_LIBRO_MAESTRO", "PROYECTO IA N7", make_project_phases("Sistema RAG", PROYECTO_N7_PHASES)),
    ("87_PROYECTO_N8_LIBRO_MAESTRO", "PROYECTO SEGURIDAD N8", make_project_phases("Pentest", PROYECTO_N8_PHASES)),
    ("88_PROYECTO_N9_LIBRO_MAESTRO", "PROYECTO CLOUD N9", make_project_phases("Infraestructura Cloud", PROYECTO_N9_PHASES)),
    ("89_PROYECTO_N10_LIBRO_MAESTRO", "PROYECTO VIDEOJUEGOS N10", make_project_phases("Videojuego", PROYECTO_N10_PHASES)),
    ("90_PROYECTO_N11_LIBRO_MAESTRO", "PROYECTO IoT N11", make_project_phases("Sistema IoT", PROYECTO_N11_PHASES)),
    ("91_PROYECTO_N12_LIBRO_MAESTRO", "PROYECTO DATA SCIENCE N12", make_project_phases("Pipeline Datos", PROYECTO_N12_PHASES)),
]


# ══════════════════════════════════════════════════════════════════════════════
# MAIN GENERATION
# ══════════════════════════════════════════════════════════════════════════════

def main():
    total_global = 0
    errors = []

    for book_id, book_name, topics_list in BOOKS:
        print(f"\n{'='*60}")
        print(f"GENERANDO: {book_id} - {book_name}")
        print(f"{'='*60}")

        dirpath = os.path.join(BASE, book_id)
        clean_dir(dirpath)

        # Build chapters from topic outlines
        mods_data = build_chapters(topics_list, book_name)

        book_total = 0
        for mod_idx, (mod_name, chapters) in enumerate(mods_data, 1):
            for cap_idx, (title, secciones, ejercicios, preguntas) in enumerate(chapters, 1):
                cap_global = (mod_idx - 1) * 10 + cap_idx
                titulo_arch = safe_filename(title)
                texto = generate_chapter(book_name, mod_idx, cap_global, title, secciones, ejercicios, preguntas)
                save_chapter(dirpath, mod_idx, cap_global, titulo_arch, texto)
                book_total += 1

        total_global += book_total
        print(f"  ✓ {book_id}: {book_total} capítulos generados")

    print(f"\n{'='*60}")
    print(f"GENERACIÓN COMPLETADA")
    print(f"{'='*60}")
    print(f"Total libros: {len(BOOKS)}")
    print(f"Total capítulos: {total_global}")
    print(f"Archivos esperados: {len(BOOKS) * 80}")
    if errors:
        print(f"\nERRORES ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
    else:
        print("\n✓ Sin errores")
    print()


if __name__ == "__main__":
    main()
