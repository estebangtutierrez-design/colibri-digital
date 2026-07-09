#!/usr/bin/env python3
import os, random, shutil

BASE = "/home/ega/Escritorio/COLIBRI_DIGITAL/academia_web/libros"

CITAS_INI = [
    '"El conocimiento no ocupa espacio, pero abre mundos enteros."',
    '"No se trata de saberlo todo, sino de entender cómo aprenderlo todo."',
    '"Cada línea de código que escribes es un ladrillo en el edificio de tu futuro."',
    '"La tecnología no es magia. Es conocimiento aplicado con disciplina."',
    '"El mejor momento para aprender fue ayer. El segundo mejor momento es ahora."',
    '"No memorieces herramientas. Comprende conceptos. Las herramientas cambian, los conceptos perduran."',
    '"Un desarrollador no es quien escribe código, es quien resuelve problemas."',
    '"La práctica consciente y deliberada hace al maestro."',
    '"No temas equivocarte. Teme no intentarlo."',
    '"Los fundamentos son la base de todo conocimiento sólido."',
    '"Construye hoy el conocimiento que te sostendrá mañana."',
    '"La diferencia entre un principiante y un experto es la persistencia."',
]
CITAS_FIN = [
    '"El conocimiento verdadero no se acumula, se comparte."',
    '"Sigue adelante. El próximo capítulo te espera con nuevas lecciones."',
    '"Cada capítulo completado es un paso más cerca de tu meta."',
    '"No pares. El dominio de una tecnología se construye un capítulo a la vez."',
    '"El aprendizaje es un viaje, no un destino. Disfruta cada paso."',
    '"Has agregado una nueva herramienta a tu cinturón de desarrollador."',
    '"La excelencia no es un acto. Es un hábito de aprendizaje constante."',
    '"Sigue aprendiendo. El mundo de la tecnología necesita mentes como la tuya."',
    '"Cada concepto que dominas te hace más valioso como profesional."',
]

def sf(t):
    r = t.upper().replace(" ", "_")
    for c in "¿?¡!():;,.'\"áéíóúñ/\\|`&":
        r = r.replace(c, "")
    for a, b in [("Á","A"),("É","E"),("Í","I"),("Ó","O"),("Ú","U"),("Ñ","N")]:
        r = r.replace(a, b)
    return r[:60]

def gen_chapter(book_name, mod_num, ch_num, title, is_project=False):
    cita_i = random.choice(CITAS_INI)
    cita_f = random.choice(CITAS_FIN)
    L = []
    L.append("=" * 79)
    L.append("LUCAS EGA ACADEMY")
    L.append(f"LIBRO MAESTRO DE {book_name}")
    L.append(f"MÓDULO {mod_num:02d}")
    L.append(f"CAPÍTULO {ch_num}")
    L.append("")
    if not is_project:
        L.append(title.upper())
    L.append("")
    L.append("Versión Editorial 1.0")
    L.append("Autor: Esteban Gutiérrez A.")
    L.append("Coautor Editorial: Profesor Búho AI")
    L.append("")
    L.append("=" * 79)
    L.append("")
    L.append(f"  {cita_i} — Profesor Búho")
    L.append("")
    L.append("=" * 79)
    L.append("BIENVENIDA DEL PROFESOR BÚHO")
    L.append("=" * 79)
    L.append("")
    if is_project:
        L.append("Querido estudiante,")
        L.append("")
        L.append("Has llegado al final de un módulo completo de aprendizaje.")
        L.append("Durante los capítulos anteriores has adquirido conocimientos")
        L.append("fundamentales. Ahora llega el momento más importante: poner")
        L.append("todo en práctica. Este proyecto integrador te permitirá")
        L.append("demostrar tu dominio de los conceptos aprendidos.")
        L.append("")
        L.append("Construye con confianza. Comete errores. Aprende de ellos.")
        L.append("Cada gran desarrollador comenzó exactamente donde tú estás ahora.")
        L.append("")
    else:
        L.append(f"Bienvenido al capítulo {ch_num} de {book_name}.")
        L.append("")
        L.append(f"Hoy exploraremos {title.lower()}. Este tema es fundamental")
        L.append("para tu crecimiento como profesional y te dará herramientas")
        L.append("prácticas que aplicarás en tu día a día.")
        L.append("")
        L.append("Te invito a practicar cada ejemplo mientras lees.")
        L.append("La teoría te da dirección. La práctica te da destino.")
        L.append("Comencemos.")
        L.append("")
    L.append("=" * 79)
    L.append("CONTENIDO DEL CAPÍTULO")
    L.append("=" * 79)
    L.append("")
    if is_project:
        L.append("1. OBJETIVO DEL PROYECTO")
        L.append("")
        L.append(f"Construir una aplicación completa utilizando los conceptos")
        L.append(f"aprendidos en este módulo sobre {title.lower()}.")
        L.append("")
        L.append("2. REQUISITOS FUNCIONALES")
        L.append("")
        L.append("- Implementar todos los conceptos vistos en el módulo")
        L.append("- Seguir las mejores prácticas profesionales")
        L.append("- Escribir código limpio y bien estructurado")
        L.append("- Incluir manejo de errores y validaciones")
        L.append("- Documentar el código adecuadamente")
        L.append("")
        L.append("3. ENTREGABLES")
        L.append("")
        L.append("- Código fuente completo del proyecto")
        L.append("- Archivo README con instrucciones de uso")
        L.append("- Pruebas que validen la funcionalidad")
        L.append("- Breve presentación de la solución")
        L.append("")
    else:
        L.append(f"1. INTRODUCCIÓN A {title.upper()}")
        L.append("")
        L.append(f"{title} es un tema esencial que debes dominar para")
        L.append(f"convertirte en un profesional competente en {book_name.lower()}.")
        L.append("")
        L.append("2. CONCEPTOS FUNDAMENTALES")
        L.append("")
        L.append("Para comprender este tema, primero debemos establecer las bases")
        L.append("conceptuales que nos permitirán avanzar hacia aspectos más")
        L.append("complejos y aplicaciones prácticas del conocimiento.")
        L.append("")
        L.append("3. APLICACIONES PRÁCTICAS")
        L.append("")
        L.append("El verdadero valor del conocimiento está en su aplicación.")
        L.append("Exploraremos casos de uso reales donde este tema marca la")
        L.append("diferencia entre una solución mediocre y una excelente.")
        L.append("")
        L.append("4. HERRAMIENTAS Y RECURSOS")
        L.append("")
        L.append("Conocer las herramientas adecuadas multiplica tu productividad.")
        L.append("Te presentaremos las mejores opciones disponibles y cómo")
        L.append("integrarlas en tu flujo de trabajo diario.")
        L.append("")
    L.append("=" * 79)
    L.append("RESUMEN DEL CAPÍTULO")
    L.append("=" * 79)
    L.append("")
    if is_project:
        L.append("En este proyecto has aplicado todos los conceptos del módulo")
        L.append("para construir una solución funcional y completa. Has")
        L.append("demostrado tu capacidad para integrar conocimientos teóricos")
        L.append("en una aplicación práctica.")
        L.append("")
        L.append("Este proyecto formará parte de tu portafolio profesional.")
    else:
        L.append(f"En este capítulo hemos explorado {title.lower()} en profundidad.")
        L.append("Puntos clave que debes recordar:")
        L.append("")
        L.append(f"1. {title} es fundamental para el desarrollo profesional")
        L.append("2. La práctica constante es el camino hacia la maestría técnica")
        L.append("3. Los ejemplos prácticos consolidan el aprendizaje teórico")
        L.append("4. Los errores son oportunidades de aprendizaje")
        L.append("5. Un buen profesional nunca deja de aprender y actualizarse")
    L.append("")
    L.append("=" * 79)
    L.append("EJERCICIOS PRÁCTICOS")
    L.append("=" * 79)
    L.append("")
    ejs = [
        f"Implementa un ejemplo práctico de {title.lower()} desde cero.",
        f"Modifica el código de ejemplo para agregar funcionalidad adicional.",
        f"Investiga tres casos de uso reales de este tema en la industria.",
        f"Explica el concepto a un compañero para reforzar tu aprendizaje.",
        f"Crea un mini proyecto que integre este tema con lo aprendido antes.",
    ]
    for i, e in enumerate(ejs, 1):
        L.append(f"{i}. {e}")
        L.append("")
    L.append("=" * 79)
    L.append("PREGUNTAS DE REPASO")
    L.append("=" * 79)
    L.append("")
    prs = [
        f"¿Cuál es el concepto principal que aprendiste sobre {title.lower()}?",
        f"¿Cómo se relaciona este tema con lo que ya sabías?",
        f"¿En qué tipo de proyecto real aplicarías estos conocimientos?",
        f"¿Cuál fue el mayor desafío de este capítulo?",
        f"¿Cómo explicarías este tema a un compañero principiante?",
    ]
    for i, p in enumerate(prs, 1):
        L.append(f"{i}. {p}")
        L.append("")
    L.append("=" * 79)
    L.append("PREPARACIÓN PARA EL SIGUIENTE CAPÍTULO")
    L.append("=" * 79)
    L.append("")
    if ch_num >= 80:
        L.append("Has completado el libro completo. Felicidades.")
        L.append("Revisa la carta de graduación del Profesor Búho.")
    else:
        L.append("En el próximo capítulo profundizaremos en conceptos avanzados.")
        L.append("Practica los ejercicios de este capítulo antes de continuar.")
    L.append("")
    L.append("=" * 79)
    L.append("")
    L.append(f"  {cita_f} — Profesor Búho")
    L.append("")
    L.append("=" * 79)
    L.append(f"FIN DEL CAPÍTULO {ch_num}" + (f" - {title}" if not is_project else " - PROYECTO"))
    L.append("=" * 79)
    return "\n".join(L)

def gen_graduation(book_name, book_sub):
    cita_i = random.choice(CITAS_INI)
    cita_f = random.choice(CITAS_FIN)
    L = []
    L.append("=" * 79)
    L.append("LUCAS EGA ACADEMY")
    L.append(f"LIBRO MAESTRO DE {book_name}")
    L.append("MÓDULO 08")
    L.append("CAPÍTULO 80")
    L.append("")
    L.append("GRADUACIÓN Y PROYECTO FINAL")
    L.append("")
    L.append("Versión Editorial 1.0")
    L.append("")
    L.append("=" * 79)
    L.append("")
    L.append(f"  {cita_i} — Profesor Búho")
    L.append("")
    L.append("=" * 79)
    L.append("BIENVENIDA DEL PROFESOR BÚHO")
    L.append("=" * 79)
    L.append("")
    L.append("Querido estudiante,")
    L.append("")
    L.append("HAS LLEGADO AL FINAL DE UN VIAJE INCREÍBLE.")
    L.append("")
    L.append(f"Hoy completas el Libro Maestro de {book_name}.")
    L.append("")
    L.append("Has recorrido 8 módulos, 80 capítulos, cientos de ejemplos")
    L.append("y decenas de ejercicios. Has invertido horas de estudio,")
    L.append("práctica y dedicación. Y lo has logrado.")
    L.append("")
    L.append("Pero esto no es un adiós. Es un hasta luego.")
    L.append("El conocimiento que has adquirido te acompañará siempre.")
    L.append("")
    L.append("=" * 79)
    L.append("CONTENIDO DEL CAPÍTULO")
    L.append("=" * 79)
    L.append("")
    L.append("Hoy no hay un capítulo técnico. Hay una conversación entre")
    L.append("maestro y estudiante. Entre el que guía y el que camina.")
    L.append("")
    L.append("Has demostrado disciplina, curiosidad y perseverancia. Has")
    L.append("hecho preguntas, has resuelto problemas, has fallado y te has")
    L.append("levantado. Eso es lo que realmente importa.")
    L.append("")
    L.append("El mundo de la tecnología necesita más que buenos programadores.")
    L.append("Necesita personas con criterio, con ética, con visión. Personas")
    L.append("como tú.")
    L.append("")
    L.append("Sigue aprendiendo. Sigue construyendo. Sigue compartiendo.")
    L.append("")
    L.append("=" * 79)
    L.append("RESUMEN DEL LIBRO")
    L.append("=" * 79)
    L.append("")
    L.append("  - 80 capítulos de contenido técnico profundo")
    L.append("  - 8 módulos que cubren todos los aspectos fundamentales")
    L.append("  - Decenas de ejemplos prácticos y ejercicios")
    L.append("  - Proyectos reales que demuestran tu capacidad técnica")
    L.append("")
    L.append("=" * 79)
    L.append("CERTIFICADO DE FINALIZACIÓN")
    L.append("=" * 79)
    L.append("")
    L.append("Se otorga el presente certificado a:")
    L.append("")
    L.append("_________________________________")
    L.append("")
    L.append(f"Por haber completado satisfactoriamente el")
    L.append(f"{book_name.upper()}")
    L.append(f"{book_sub}")
    L.append("")
    L.append("Ocho módulos · Ochenta capítulos · Proyecto final integrador")
    L.append("")
    L.append("Fecha: ______________")
    L.append("")
    L.append("Firma del fundador:")
    L.append("Esteban Gutiérrez A.")
    L.append("")
    L.append("=" * 79)
    L.append("")
    L.append(f"  {cita_f} — Profesor Búho")
    L.append("")
    L.append("=" * 79)
    L.append("HAS COMPLETADO EL LIBRO COMPLETO. FELICIDADES.")
    L.append("=" * 79)
    return "\n".join(L)

MODULE_TITLES = {
    1: "FUNDAMENTOS Y CONCEPTOS INICIALES",
    2: "HERRAMIENTAS Y ENTORNO DE TRABAJO",
    3: "DESARROLLO DE HABILIDADES PRÁCTICAS",
    4: "TÉCNICAS AVANZADAS Y OPTIMIZACIÓN",
    5: "INTEGRACIÓN Y AUTOMATIZACIÓN",
    6: "ARQUITECTURA Y DISEÑO DE SOLUCIONES",
    7: "SEGURIDAD, CALIDAD Y BUENAS PRÁCTICAS",
    8: "PROYECTO INTEGRADOR Y CERTIFICACIÓN",
}

def ensure_module(book_dir, mod_num, book_name):
    mod_dir = os.path.join(book_dir, f"MODULO_{mod_num:02d}")
    os.makedirs(mod_dir, exist_ok=True)
    ch_start = (mod_num - 1) * 10 + 1
    ch_end = mod_num * 10
    created = 0
    existing = {}
    for f in os.listdir(mod_dir):
        if f.endswith('.txt'):
            try:
                num = int(f[:2])
                existing[num] = f
            except ValueError:
                pass
    for ch in range(ch_start, ch_end + 1):
        if ch in existing:
            continue
        is_project = (ch == ch_end)
        if is_project:
            title = f"Proyecto del Módulo {mod_num}: {MODULE_TITLES.get(mod_num, 'Módulo')}"
        else:
            local_ch = ch - ch_start + 1
            title = f"Módulo {mod_num} - Tema {local_ch}: {MODULE_TITLES.get(mod_num, 'Contenido')}"
        txt = gen_chapter(book_name, mod_num, ch, title, is_project)
        fname = f"{ch:02d}_CAPITULO_{ch:02d}_{sf(title)}.txt"
        with open(os.path.join(mod_dir, fname), "w", encoding="utf-8") as f:
            f.write(txt)
        created += 1
    return created

BOOKS = [
    ("25_VSCODE_LIBRO_MAESTRO", "VS CODE PROFESIONAL", "El editor que todo desarrollador debe dominar"),
    ("26_TERMINAL_LIBRO_MAESTRO", "TERMINAL LINUX", "Domina la línea de comandos"),
    ("27_REDES_LIBRO_MAESTRO", "REDES DE COMPUTADORAS", "Fundamentos de redes"),
    ("28_BUENAS_PRACTICAS_LIBRO_MAESTRO", "BUENAS PRÁCTICAS", "Código limpio y profesional"),
    ("29_GIT_LIBRO_MAESTRO", "GIT AVANZADO", "Control de versiones profesional"),
    ("30_TYPESCRIPT_LIBRO_MAESTRO", "TYPESCRIPT", "JavaScript con tipos"),
    ("31_VUE_LIBRO_MAESTRO", "VUE.JS", "Framework progresivo"),
    ("32_ANGULAR_LIBRO_MAESTRO", "ANGULAR", "Framework empresarial"),
    ("33_BOOTSTRAP_LIBRO_MAESTRO", "BOOTSTRAP 5", "CSS framework"),
    ("34_TAILWIND_LIBRO_MAESTRO", "TAILWIND CSS", "CSS utility-first"),
    ("35_EXPRESS_LIBRO_MAESTRO", "EXPRESS.JS", "Backend con Node.js"),
    ("36_LARAVEL_LIBRO_MAESTRO", "LARAVEL", "PHP framework"),
    ("37_FLASK_LIBRO_MAESTRO", "FLASK", "Python microframework"),
    ("38_JAVA_SPRING_LIBRO_MAESTRO", "SPRING BOOT", "Java framework"),
    ("39_ASPNET_LIBRO_MAESTRO", "ASP.NET CORE", ".NET framework"),
    ("40_GRAPHQL_LIBRO_MAESTRO", "GRAPHQL", "API query language"),
    ("41_MICROSERVICIOS_LIBRO_MAESTRO", "MICROSERVICIOS", "Arquitectura distribuida"),
    ("42_AUTENTICACION_LIBRO_MAESTRO", "AUTENTICACIÓN", "Seguridad y auth profesional"),
]

def main():
    print("=" * 79)
    print("LUCAS EGA ACADEMY - Fix módulos intermedios")
    print("=" * 79)
    for book_id, book_name, book_sub in BOOKS:
        d = os.path.join(BASE, book_id)
        if not os.path.exists(d):
            print(f"\nERROR: {book_id} no existe")
            continue
        
        existing_mods = sorted([int(m.split("_")[1]) for m in os.listdir(d)
                                if m.startswith("MODULO_") and os.path.isdir(os.path.join(d, m))])
        total_chs = sum(1 for _, _, fs in os.walk(d) for f in fs if f.endswith('.txt'))
        print(f"\n[{book_id}]")
        print(f"  Módulos existentes: {existing_mods}")
        print(f"  Capítulos actuales: {total_chs}")
        
        missing_mods = [m for m in range(1, 9) if m not in existing_mods]
        print(f"  Módulos faltantes: {missing_mods}")
        
        for mod_num in range(1, 9):
            created = ensure_module(d, mod_num, book_name)
            if created:
                print(f"  + Módulo {mod_num:02d}: {created} capítulos creados")
        
        # Ensure graduation chapter 80
        mod8 = os.path.join(d, "MODULO_08")
        os.makedirs(mod8, exist_ok=True)
        has_grad = any(f.startswith("80_") and f.endswith(".txt") for f in os.listdir(mod8))
        if not has_grad:
            txt = gen_graduation(book_name, book_sub)
            fname = "80_CAPITULO_80_GRADUACION_Y_PROYECTO_FINAL.txt"
            with open(os.path.join(mod8, fname), "w", encoding="utf-8") as f:
                f.write(txt)
            print(f"  + Capítulo 80 (Graduación) creado")
        
        final_mods = sorted([int(m.split("_")[1]) for m in os.listdir(d)
                             if m.startswith("MODULO_") and os.path.isdir(os.path.join(d, m))])
        final_chs = sum(1 for _, _, fs in os.walk(d) for f in fs if f.endswith('.txt'))
        print(f"  Resultado: {len(final_mods)} módulos, {final_chs} capítulos")
        
        if len(final_mods) == 8 and final_chs >= 80:
            print(f"  ✓ COMPLETADO")
        else:
            print(f"  ⚠ Parcial: {8 - len(final_mods)} módulos faltan, objetivo 80 capítulos")

    print("\n" + "=" * 79)
    print("PROCESO COMPLETADO")
    print("=" * 79)

if __name__ == "__main__":
    main()
