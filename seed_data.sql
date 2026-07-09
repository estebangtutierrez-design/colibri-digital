-- ============================================================
-- SEED DATA: Contenidos gratuitos, productos, capturas, pedidos
-- ============================================================

-- ========== CONTENIDOS GRATUITOS (artículos / previews) ==========

-- ACADEMIA
INSERT OR IGNORE INTO contenidos (id, division_id, titulo, resumen, contenido_texto, etiquetas, gratuito, destacado) VALUES
(1,'academia','¿Qué es HTML5?','Introducción completa a HTML5, sus nuevas etiquetas semánticas y APIs modernas.','HTML5 es la quinta revisión del lenguaje de marcado estándar para la web. Introduce elementos semánticos como <header>, <nav>, <article>, <section>, <aside> y <footer>, así como APIs nativas para canvas, geolocalización, almacenamiento local y más. En Lucas EGA Academy te enseñamos paso a paso.','html5,web,principiantes',1,1),
(2,'academia','10 Comandos de Git que Todo Dev Debe Saber','Los comandos esenciales para el control de versiones.','Git no es opcional. Domina init, add, commit, push, pull, branch, merge, rebase, log y stash.','git,github,devops',1,0),
(3,'academia','Introducción a Python','Por qué Python es el lenguaje más popular del momento.','Python se usa en data science, automatización, web, IA y más. Su sintaxis clara lo hace ideal para principiantes.','python,programacion,principiantes',1,0);

-- LEGADO ANCESTRAL
INSERT OR IGNORE INTO contenidos (id, division_id, titulo, resumen, contenido_texto, etiquetas, gratuito, destacado) VALUES
(4,'legado','El Maguey: Árbol de las Maravillas','Historia y usos del maguey en la cultura mexicana ancestral.','El maguey (Agave) era considerado por los mexicas como un regalo de los dioses. De él se obtenía pulque, fibras para vestimenta, papel amate, medicina tradicional y construcción. Cada parte de la planta tenía un propósito sagrado.','maguey,agave,cultura,historia',1,1),
(5,'legado','Plantas Medicinales de la Sierra Tarahumara','Tradición herbal de los rarámuris.','Los rarámuris (tarahumaras) han usado por siglos plantas como la gobernadora, el chaparro amargoso y la damiana para curar enfermedades.','medicina,plantas,tradicion',1,0),
(6,'legado','Cocina Prehispánica: Ingredientes Sagrados','Maíz, frijol, chile, calabaza, amaranto.','Estos cinco ingredientes formaban la base de la alimentación mesoamericana y siguen siendo fundamentales en la cocina mexicana actual.','cocina,prehispanico,maiz,chile',1,0);

-- HISTORIAS DE MÉXICO
INSERT OR IGNORE INTO contenidos (id, division_id, titulo, resumen, contenido_texto, etiquetas, gratuito, destacado) VALUES
(7,'historias','La Llorona: Origen de la Leyenda','Los múltiples orígenes de la leyenda más famosa de México.','Desde la época prehispánica hasta la colonia, la leyenda de La Llorona ha evolucionado. Algunos estudiosos la vinculan con la diosa Cihuacóatl, que según la tradición mexica vagaba por las calles de Tenochtitlán llorando por sus hijos.','leyendas,llorona,historia',1,1),
(8,'historias','El Callejón del Beso en Guanajuato','La trágica historia de amor que dio nombre a este famoso callejón.','Cuenta la leyenda que dos jóvenes enamorados, Doña Carmen y Don Luis, se besaban a escondidas desde los balcones de este angosto callejón, hasta que el padre de ella descubrió el romance.','leyendas,amor,guanajuato',1,0),
(9,'historias','Los Túneles de Puebla','El misterio subterráneo que conecta la ciudad de los ángeles.','Bajo la ciudad de Puebla existe una red de túneles construidos en el siglo XVI que conectan iglesias, plazas y edificios históricos. Su propósito original sigue siendo un misterio.','misterio,puebla,tuneles',1,0);

-- MUNDO ESOTÉRICO
INSERT OR IGNORE INTO contenidos (id, division_id, titulo, resumen, contenido_texto, etiquetas, gratuito, destacado) VALUES
(10,'esoterico','Los 7 Chakras: Guía para Principiantes','Conoce los centros energéticos del cuerpo y cómo equilibrarlos.','Los chakras son centros de energía que regulan diferentes aspectos de nuestra vida física, emocional y espiritual. Desde el chakra raíz (supervivencia) hasta el corona (conexión universal).','chakras,energia,espiritualidad',1,1),
(11,'esoterico','Qué es el Ho''oponopono','El arte hawaiano de la reconciliación y el perdón.','Ho''oponopono es una antigua práctica hawaiana de sanación basada en cuatro frases: Lo siento, Perdóname, Te amo, Gracias.','hooponopono,sanacion,perdon',1,0),
(12,'esoterico','Inciensos y su Significado Espiritual','Guía de inciensos para limpieza energética.','Sahumerio, palo santo, copal, sándalo, lavanda… cada incienso tiene una vibración y propósito diferente.','inciensos,limpieza,energia',1,0);

-- ========== PRODUCTOS OTRAS DIVISIONES ==========

-- LEGADO
INSERT OR IGNORE INTO productos (sku, titulo, descripcion, division_id, categoria, precio_fisico, precio_pdf, precio_audio, precio_video, precio_premium, autor, activo) VALUES
('LGD-BOTIQUIN','Botiquín de Plantas Medicinales Mexicanas','Guía ilustrada de 50 plantas medicinales de México con usos tradicionales y preparación.','legado','medicina',349,179,249,449,699,'Esteban Gutiérrez',1),
('LGD-COCINA','Cocina Tradicional Mexicana: Recetas de la Abuela','Más de 100 recetas tradicionales con ingredientes y técnicas ancestrales.','legado','cocina',399,199,299,499,799,'Esteban Gutiérrez',1),
('LGD-RITUALES','Rituales y Ceremonias del México Antiguo','Las prácticas ceremoniales de mexicas, mayas, zapotecas y otras culturas.','legado','rituales',449,219,329,549,849,'Esteban Gutiérrez',1),
('LGD-HERBOLARIO','Herbolaria Mexicana: Enciclopedia Visual','Catálogo ilustrado de 100 plantas medicinales con fotografías y descripciones detalladas.','legado','medicina',499,249,349,599,899,'Esteban Gutiérrez',1),
('LGD-MILPA','La Milpa: Sabiduría Agrícola Mesoamericana','El sistema de cultivo milenario que sigue alimentando a México.','legado','agricultura',349,179,249,449,699,'Esteban Gutiérrez',1),
('LGD-PIRAMIDES','Pirámides de México: Guía de Sitios Arqueológicos','Recorrido por las 30 zonas arqueológicas más importantes de México.','legado','arqueologia',449,219,329,549,849,'Esteban Gutiérrez',1);

-- HISTORIAS
INSERT OR IGNORE INTO productos (sku, titulo, descripcion, division_id, categoria, precio_fisico, precio_pdf, precio_audio, precio_video, precio_premium, autor, activo) VALUES
('HMX-NAHUAL','El Nahual y Otras Leyendas','Colección de 20 leyendas mexicanas: nahuales, chaneques, aluxes y más.','historias','leyendas',349,179,249,449,699,'Esteban Gutiérrez',1),
('HMX-FANTASMAL','México Fantasmal: Rutas de Turismo Oscuro','Los 15 lugares más embrujados de México con historias documentadas.','historias','misterio',399,199,299,499,799,'Esteban Gutiérrez',1),
('HMX-CRIMEN','Crímenes que Conmocionaron a México','Casos reales de la historia criminal de México contados con rigor periodístico.','historias','crimen',449,219,329,549,849,'Esteban Gutiérrez',1),
('HMX-CALLEJONES','Leyendas de Calles y Callejones','Historias y mitos detrás de los nombres de las calles más emblemáticas de México.','historias','leyendas',349,179,249,449,699,'Esteban Gutiérrez',1),
('HMX-EXORCISMOS','Exorcismos y Poseídos en México','Casos documentados de posesiones y exorcismos en la historia de México.','historias','misterio',399,199,299,499,799,'Esteban Gutiérrez',1);

-- ESOTÉRICO
INSERT OR IGNORE INTO productos (sku, titulo, descripcion, division_id, categoria, precio_fisico, precio_pdf, precio_audio, precio_video, precio_premium, autor, activo) VALUES
('MES-CHAKRAS','Chakras: Guía Completa de Sanación','Los 7 chakras explicados en detalle con ejercicios, meditaciones y cristales.','esoterico','chakras',399,199,299,499,799,'Esteban Gutiérrez',1),
('MES-TAROT','Tarot: Lectura e Interpretación','Aprende a leer el tarot desde cero: arcanos mayores, menores, tiradas y spreads.','esoterico','tarot',449,219,329,549,849,'Esteban Gutiérrez',1),
('MES-SUEÑOS','Diccionario de los Sueños','Interpretación de más de 500 símbolos oníricos desde la perspectiva espiritual.','esoterico','suenos',349,179,249,449,699,'Esteban Gutiérrez',1),
('MES-CRISTALES','Cristales y Piedras Energéticas','Guía de 60 cristales con sus propiedades curativas, usos y limpieza.','esoterico','cristales',399,199,299,499,799,'Esteban Gutiérrez',1),
('MES-ASTRAL','Viaje Astral: Técnicas de Proyección','Métodos probados para la proyección astral y la experiencia fuera del cuerpo.','esoterico','astral',449,219,329,549,849,'Esteban Gutiérrez',1),
('MES-MEDITACION','Meditación Guiada: 30 Días de Transformación','Programa completo de 30 días con meditaciones guiadas para transformar tu vida.','esoterico','meditacion',349,179,249,449,699,'Esteban Gutiérrez',1);

-- MUNDO INFANTIL
INSERT OR IGNORE INTO productos (sku, titulo, descripcion, division_id, categoria, precio_fisico, precio_pdf, precio_audio, precio_video, precio_premium, autor, activo) VALUES
('INF-PELUCHE-OSO','Peluche Oso de Felpa 40cm','Peluche suave de oso de felpa hipoalergénico, ideal para abrazar.','infantil','juguetes',299,0,0,0,0,'Esteban Gutiérrez',1),
('INF-PELUCHE-CONEJO','Peluche Conejita Rosa 35cm','Peluche de conejo con orejas largas, textura ultra suave.','infantil','juguetes',279,0,0,0,0,'Esteban Gutiérrez',1),
('INF-CARRITO','Carrito de Bomberos con Luces','Camión de bomberos a escala con luces LED y sonido realista.','infantil','juguetes',449,0,0,0,0,'Esteban Gutiérrez',1),
('INF-MUÑECA','Muñeca Bebé Llorona 40cm','Muñeca interactiva que llora, come y hace sonidos. Incluye accesorios.','infantil','juguetes',399,0,0,0,0,'Esteban Gutiérrez',1),
('INF-BLOQUES','Bloques de Construcción 100 piezas','Set de 100 bloques de madera coloridos para estimular la creatividad.','infantil','juguetes',349,0,0,0,0,'Esteban Gutiérrez',1),
('INF-PUZZLE','Puzzle Dinosaurios 60 piezas','Rompecabezas de dinosaurios con piezas grandes para niños 4+.','infantil','juguetes',199,0,0,0,0,'Esteban Gutiérrez',1),
('INF-PLAY-DOH','Set de Plastilina 12 colores','Maletín de plastilina no tóxica con 12 colores y moldes.','infantil','juguetes',249,0,0,0,0,'Esteban Gutiérrez',1),
('INF-PLAYMOBIL','Playmobil Granja con Animales','Set de granja Playmobil con 35 piezas, animales y figuras.','infantil','juguetes',599,0,0,0,0,'Esteban Gutiérrez',1),

-- ROPA NIÑA
('INF-VESTIDO-UNI','Vestido Unicornio pastel 2-8 años','Vestido de manga corta con estampado de unicornio, algodón orgánico.','infantil','ropa',349,0,0,0,0,'Esteban Gutiérrez',1),
('INF-VESTIDO-FLOR','Vestido de Flores 2-8 años','Vestido estampado floral con vuelo, fresco y cómodo.','infantil','ropa',329,0,0,0,0,'Esteban Gutiérrez',1),
('INF-LEGGINS','Leggins Niña 2-10 años','Leggins de algodón elastizado, varios colores.','infantil','ropa',199,0,0,0,0,'Esteban Gutiérrez',1),

-- ROPA NIÑO
('INF-PLAYERA-DINO','Playera Dinosaurios Niño 2-10 años','Playera de algodón con estampado de dinosaurios, manga corta.','infantil','ropa',229,0,0,0,0,'Esteban Gutiérrez',1),
('INF-SHORT','Short Deportivo Niño 2-10 años','Short deportivo con cintura elástica y bolsillos.','infantil','ropa',249,0,0,0,0,'Esteban Gutiérrez',1),
('INF-PARKA','Chamarra Impermeable Niños 2-10 años','Chamarra con capucha, impermeable, ideal para lluvia.','infantil','ropa',599,0,0,0,0,'Esteban Gutiérrez',1),

-- UNISEX
('INF-PIJAMA','Pijama Unisex Algodón 2-10 años','Pijama de algodón suave con estampados divertidos.','infantil','ropa',349,0,0,0,0,'Esteban Gutiérrez',1),
('INF-CONJUNTO','Set Ropa Deportiva Niño/Niña 2-10 años','Conjunto de pants y playera, ideal para jugar.','infantil','ropa',499,0,0,0,0,'Esteban Gutiérrez',1),

-- LIBROS INFANTILES
('INF-LIBRO-DINOS','Dinosaurios: El Gran Libro Ilustrado','Libro infantil con ilustraciones gigantes de dinosaurios y datos curiosos.','infantil','libros',249,149,199,0,399,'Esteban Gutiérrez',1),
('INF-LIBRO-ANIMALES','Mis Primeros Animales','Libro de cartón grueso con fotos reales de animales para bebés.','infantil','libros',199,99,0,0,0,'Esteban Gutiérrez',1),
('INF-LIBRO-CUENTOS','Cuentos antes de Dormir: Vol 1','10 cuentos cortos ilustrados para leer antes de dormir.','infantil','libros',279,169,229,0,449,'Esteban Gutiérrez',1),
('INF-LIBRO-COLORES','Aprende los Colores con Pepito','Libro interactivo para aprender los colores solapas y texturas.','infantil','libros',229,129,0,0,0,'Esteban Gutiérrez',1),
('INF-LIBRO-ABC','Mi Primer ABC','Abecedario ilustrado con dibujos y palabras en español.','infantil','libros',249,149,0,0,0,'Esteban Gutiérrez',1),
('INF-LIBRO-UNI','El Unicornio Mágico','Historia de un unicornio que descubre el valor de la amistad.','infantil','libros',269,159,219,0,449,'Esteban Gutiérrez',1),

-- ACCESORIOS
('INF-MOCHILA-CARRO','Mochila Infantil Carro','Mochila con diseño de carro, ideal para preescolar.','infantil','accesorios',349,0,0,0,0,'Esteban Gutiérrez',1),
('INF-MOCHILA-UNI','Mochila Infantil Unicornio','Mochila con diseño de unicornio y detalles brillantes.','infantil','accesorios',349,0,0,0,0,'Esteban Gutiérrez',1),
('INF-LONCHERA','Lonchera Térmica Infantil','Lonchera con aislamiento térmico, diseño infantil divertido.','infantil','accesorios',249,0,0,0,0,'Esteban Gutiérrez',1),
('INF-BOTELLA','Botella Agua Infantil 400ml','Botella reutilizable con pico suave, diseño infantil.','infantil','accesorios',179,0,0,0,0,'Esteban Gutiérrez',1),
('INF-GORRA','Gorra Infantil Ajustable','Gorra ajustable con visera curva, protección solar.','infantil','accesorios',199,0,0,0,0,'Esteban Gutiérrez',1),

-- BEBÉS
('INF-BABERO','Set Baberos Algodón 3 piezas','Baberos de algodón orgánico con bolsillo recolector.','infantil','bebes',249,0,0,0,0,'Esteban Gutiérrez',1),
('INF-MORDEDOR','Set Mordedores Silicona 2 piezas','Mordedores de silicona de grado alimenticio, formas divertidas.','infantil','bebes',179,0,0,0,0,'Esteban Gutiérrez',1),
('INF-SONAJA','Sonaja Musical Pato','Sonaja con forma de pato que hace sonidos al agitarlo.','infantil','bebes',149,0,0,0,0,'Esteban Gutiérrez',1),
('INF-COBIJA','Cobija de Algodón 70x90cm','Cobija suave de algodón para bebé, estampado de estrellas.','infantil','bebes',399,0,0,0,0,'Esteban Gutiérrez',1),

-- EDUCACIÓN
('INF-PIZARRON','Pizarrón Magnético Infantil','Pizarrón de doble cara con letras magnéticas y marcadores.','infantil','educacion',449,0,0,0,0,'Esteban Gutiérrez',1),
('INF-COLORES','Set Colores 24 piezas','Caja de 24 colores de cera, acuarelas y lápices de colores.','infantil','educacion',249,0,0,0,0,'Esteban Gutiérrez',1),
('INF-LIBRO-123','Aprende a Contar del 1 al 20','Libro de actividades para aprender números y contar.','infantil','educacion',199,0,0,0,0,'Esteban Gutiérrez',1),
('INF-RELOJ','Reloj para Aprender la Hora','Reloj didáctico con manecillas móviles para aprender la hora.','infantil','educacion',179,0,0,0,0,'Esteban Gutiérrez',1);

-- ========== MUNDO FEMENINO ==========
INSERT OR IGNORE INTO productos (sku, titulo, descripcion, division_id, categoria, precio_fisico, precio_pdf, precio_audio, precio_video, precio_premium, autor, activo) VALUES

-- ROPA
('FEM-VESTIDO-NOCHE','Vestido de Noche Elegante','Vestido largo con detalles de encaje, ideal para ocasiones especiales.','femenino','ropa',899,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-VESTIDO-VERA','Vestido de Verano Floral','Vestido corto estampado floral, fresco y ligero para días cálidos.','femenino','ropa',549,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-BLUSA','Blusa de Seda con Lazada','Blusa de seda suave con detalle de lazada en el cuello.','femenino','ropa',499,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-JEANS','Jeans Pitillo Elásticos','Jeans ajustados con elasticidad cómoda, varios colores y tallas.','femenino','ropa',599,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-FALDA','Funda Lápiz Tubo','Falda lápiz clásica, ideal para oficina.','femenino','ropa',399,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-CHAMARRA','Chamarra de Cuero Sintético','Chamarra de cuero ecológico con forro interior, corte moderno.','femenino','ropa',899,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-PLAYERA','Playera Básica Algodón','Playera de algodón orgánico, corte recto, varios colores.','femenino','ropa',249,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-SHORT','Short Vaquero','Short vaquero de tiro alto, cómodo y moderno.','femenino','ropa',399,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-SUDADERA','Sudadera con Capucha','Sudadera de algodón con capucha y bolsillo canguro.','femenino','ropa',599,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-LEGGINS','Leggins Deportivos','Leggins de compresión para yoga y ejercicio.','femenino','ropa',449,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-PANTS','Pants Deportivo','Pants con cintura elástica y pierna recta, ideal para gym.','femenino','ropa',549,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-ABRIGO','Abrigo Largo Invernal','Abrigo largo con forro térmico, elegante y abrigador.','femenino','ropa',1299,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-TOP','Top Deportivo','Top de soporte medio para actividades deportivas.','femenino','ropa',299,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-TRAJE-BANO','Traje de Baño Enterizo','Traje de baño enterizo con estampado tropical.','femenino','ropa',499,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-BIKINI','Bikini Triángulo','Bikini de triángulo ajustable, varios colores y estampados.','femenino','ropa',399,0,0,0,0,'Esteban Gutiérrez',1),

-- COSMÉTICOS
('FEM-LABIAL','Labial Mate 12 horas','Barra de labios de larga duración, acabado mate, 12 tonos.','femenino','cosmeticos',199,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-RIMEL','Rímel Voluminizador','Máscara de pestañas con efecto voluminizador y alargador.','femenino','cosmeticos',249,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-BASE','Base Líquida Cobertura Total','Base facial de cobertura total con acabado natural y SPF30.','femenino','cosmeticos',349,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-CORRECTOR','Corrector Iluminador','Corrector líquido con efecto iluminador para ojeras y manchas.','femenino','cosmeticos',229,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-PALETA','Paleta de Sombras 24 colores','Paleta profesional con 24 sombras mate y brillantes.','femenino','cosmeticos',449,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-DELINEADOR','Delineador Líquido Precision','Delineador líquido de punta fina para trazo preciso.','femenino','cosmeticos',179,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-POLVO','Polvo Compacto Matificante','Polvo facial compacto que controla brillos y fija el maquillaje.','femenino','cosmeticos',299,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-BRONCER','Bronzer en Polvo','Polvo bronceador para efecto soleado natural.','femenino','cosmeticos',279,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-ILUMINADOR','Iluminador Líquido','Iluminador líquido con partículas reflectantes, acabado glow.','femenino','cosmeticos',249,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-CEJA','Kit de Cejas 3 en 1','Kit con gel, polvo y delineador para cejas perfectas.','femenino','cosmeticos',229,0,0,0,0,'Esteban Gutiérrez',1),

-- BELLEZA (cuidado facial/corporal)
('FEM-CREMA-FACIAL','Crema Facial Anti-edad 50ml','Crema hidratante con ácido hialurónico y colágeno.','femenino','belleza',449,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-SERUM','Sérum Vitamina C 30ml','Sérum facial con vitamina C pura para iluminar y unificar.','femenino','belleza',399,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-CONTORNO','Contorno de Ojos','Crema para contorno de ojos con cafeína y péptidos.','femenino','belleza',329,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-EXFOLIANTE','Exfoliante Facial Enzimático','Exfoliante suave con enzimas naturales para renovar la piel.','femenino','belleza',279,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-MASCARILLA','Mascarilla Facial de Colágeno','Mascarilla en hoja con colágeno y vitamina E, pack 10 piezas.','femenino','belleza',249,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-PROTECTOR','Protector Solar Facial SPF50','Protector solar de amplio espectro, libre de aceite.','femenino','belleza',299,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-CREMA-CORPORAL','Crema Corporal Hidratante 400ml','Crema corporal con manteca de karité y aceite de coco.','femenino','belleza',349,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-ACEITE','Aceite Corporal Brillo Natural','Aceite seco con vitamina E para piel radiante.','femenino','belleza',299,0,0,0,0,'Esteban Gutiérrez',1),

-- CABELLO
('FEM-SHAMPOO','Shampoo Profesional 500ml','Shampoo profesional sin sulfatos para todo tipo de cabello.','femenino','cabello',249,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-CONDICIONADOR','Condicionador Reparador 500ml','Condicionador con keratina y aceite de argán.','femenino','cabello',249,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-MASCARILLA-CAP','Mascarilla Capilar Reparación Intensa','Mascarilla capilar con keratina y biotina, 300g.','femenino','cabello',349,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-ACEITE-CAP','Aceite de Argán Capilar 100ml','Aceite de argán puro para puntas abiertas y brillo.','femenino','cabello',279,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-SECADOR','Secador de Pelo Profesional 2000W','Secador iónico con difusor y 3 temperaturas.','femenino','electricos',799,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-PLANCHA','Plancha Alisadora de Cerámica','Plancha de cerámica con temperatura ajustable hasta 230°C.','femenino','electricos',699,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-RIZADOR','Rizador de Pelo 3 en 1','Rizador intercambiable con 3 barriles para diferentes rizos.','femenino','electricos',599,0,0,0,0,'Esteban Gutiérrez',1),

-- ACCESORIOS
('FEM-ANILLO','Anillo de Plata 925','Anillo de plata ley 925 con zircone cúbico.','femenino','accesorios',449,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-ARETES','Aretes de Aro Dorados','Aretes de aro en tono dorado, tamaño mediano.','femenino','accesorios',299,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-COLLAR','Collar Colgante Corazón','Collar con dije de corazón en plata y cadena ajustable.','femenino','accesorios',399,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-PULSERA','Pulsera de Cuentas Doradas','Pulsera elástica con cuentas doradas y detalles brillantes.','femenino','accesorios',249,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-BOLSO','Bolso Tote de Cuero','Bolso tipo tote en cuero genuino, amplio y elegante.','femenino','accesorios',1299,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-MOCHILA','Mochila Urbana Mujer','Mochila de poliéster resistente con múltiples compartimentos.','femenino','accesorios',599,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-CINTO','Cinturón Ancho Elástico','Cinturón ancho con hebilla dorada, ajuste elástico.','femenino','accesorios',349,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-BUFANDA','Bufanda de Seda Estampada','Bufanda cuadrada de seda natural con estampado floral.','femenino','accesorios',399,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-GAFAS','Gafas de Sol Cateye','Gafas de sol estilo cateye con protección UV400.','femenino','accesorios',499,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-RELÓ','Reloj de Pulsera Femenino','Reloj analógico con correa de acero inoxidable y bisutería.','femenino','accesorios',699,0,0,0,0,'Esteban Gutiérrez',1),

-- ELÉCTRICOS BELLEZA
('FEM-CEPILLO','Cepillo Eléctrico Air Styler','Cepillo secador y alisador 2 en 1 con tecnología iónica.','femenino','electricos',999,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-DEPILADORA','Depiladora Eléctrica','Depiladora de luz pulsada IPL para uso doméstico.','femenino','electricos',1599,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-LIMPIADORA','Limpiadora Facial Eléctrica','Cepillo limpiador facial sónico con cabezales intercambiables.','femenino','electricos',699,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-MASAJEADOR','Masajeador Corporal Eléctrico','Masajeador de percusión con 4 cabezales y múltiples velocidades.','femenino','electricos',899,0,0,0,0,'Esteban Gutiérrez',1),
('FEM-ALISADOR','Alisador de Pelo Inalámbrico','Plancha alisadora inalámbrica recargable, ideal para viajes.','femenino','electricos',799,0,0,0,0,'Esteban Gutiérrez',1);

-- ========== MUNDO MASCULINO ==========
INSERT OR IGNORE INTO productos (sku, titulo, descripcion, division_id, categoria, precio_fisico, precio_pdf, precio_audio, precio_video, precio_premium, autor, activo) VALUES

-- CONSTRUCTORES
('MASC-MARTILLO','Martillo de Uña 20oz','Martillo profesional con mango de fibra de vidrio y cabeza forjada.','masculino','constructores',349,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-TALADRO','Taladro Percutor 650W','Taladro eléctrico con percutor, velocidad variable y mandril 13mm.','masculino','constructores',899,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-SIERRA','Sierra Circular 1800W','Sierra circular profesional con guía láser y corte 55mm.','masculino','constructores',1499,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-CINTAMETRICA','Cinta Métrica 8m','Cinta métrica profesional 8m con doble gancho y cinta antideslizante.','masculino','constructores',199,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-NIVEL','Nivel Láser Autonivelante','Nivel láser de línea cruzada autonivelante con trípode.','masculino','constructores',1299,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-CASCO','Casco de Seguridad','Casco dieléctrico con suspensión ajustable, certificado ANSI.','masculino','constructores',299,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-GUANTES-CONST','Guantes de Trabajo Reforzados','Guantes con palma reforzada y nudillos protectores.','masculino','constructores',249,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-LLAVE-INGL','Llave Inglesa 12"','Llave inglesa ajustable profesional con mango antideslizante.','masculino','constructores',349,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-PALAYUDA','Pala Cuadrada con Mango','Pala para construcción con mango de madera y acero templado.','masculino','constructores',399,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-CARRETILLA','Carretilla de Construcción 100L','Carretilla de acero reforzado con capacidad de 100 litros y neumático.','masculino','constructores',899,0,0,0,0,'Esteban Gutiérrez',1),

-- MECÁNICA
('MASC-CATRIN','Gato Hidráulico 3 Ton','Gato de botella hidráulico 3 toneladas para vehículos.','masculino','mecanica',699,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-LLAVE-CARRO','Juego de Llaves Combinadas 15 piezas','Set de llaves combinadas métricas de 8mm a 22mm.','masculino','mecanica',599,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-DADOS','Juego de Dados 1/2" 24 piezas','Set profesional de dados con trinquete, extensiones y adaptador.','masculino','mecanica',799,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-TORQUIMETRO','Torquímetro 1/2" 40-210Nm','Llave dinamométrica para apriete preciso de tuercas y tornillos.','masculino','mecanica',899,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-COMPRESOR','Compresor de Aire 24L','Compresor portátil 2HP con tanque 24L e inflador.','masculino','mecanica',1999,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-PISTOLA-AIRE','Pistola de Aire Comprimido','Pistola de soplido para limpieza y secado en taller.','masculino','mecanica',249,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-OVEROL','Overol de Mecánico','Overol de algodón resistente con múltiples bolsillos y cierre.','masculino','mecanica',599,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-LAMPARA-TALLER','Lámpara LED para Taller','Lámpara LED recargable 2000 lúmenes con imán y gancho.','masculino','mecanica',449,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-CABALLETE','Caballete de Seguridad 3 Ton','Par de caballetes plegables para levantar vehículos.','masculino','mecanica',899,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-EXTRACTOR','Extractor de Aceite Manual','Bomba manual para cambio de aceite, capacidad 5L.','masculino','mecanica',399,0,0,0,0,'Esteban Gutiérrez',1),

-- YARDERO
('MASC-CORTADORA','Cortadora de Pasto Eléctrica 1200W','Cortadora de pasto con motor eléctrico, ancho de corte 40cm.','masculino','yardero',2499,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-DESMALEZADORA','Desmalezadora a Gasolina 52cc','Desmalezadora con motor 2 tiempos, cabezal de hilo y cuchilla.','masculino','yardero',1899,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-MANGUERA','Manguera de Jardín 50m','Manguera expandible con conector universal y pistola ajustable.','masculino','yardero',499,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-AZEITE','Aceite para Motosierra 1L','Aceite lubricante para motosierra y desmalezadora.','masculino','yardero',149,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-TIJERAS-PODAR','Tijeras de Podar Profesionales','Tijeras de podar con hoja de acero al carbono y mango ergonómico.','masculino','yardero',349,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-RASTRILLO','Rastrillo de Jardín 60cm','Rastrillo metálico con mango largo para hojas y escombros.','masculino','yardero',249,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-PALA-JARDIN','Pala de Jardín con Mango','Pala de punta redonda para jardinería y excavación ligera.','masculino','yardero',299,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-SOPLADOR','Soplador de Hojas Eléctrico','Soplador aspirador eléctrico 250km/h con bolsa recolectora.','masculino','yardero',999,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-MOTOSIERRA','Motosierra Eléctrica 2000W','Motosierra eléctrica 16", freno de cadena y lubricación automática.','masculino','yardero',1799,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-SEMILLAS','Kit Semillas de Pasto 5kg','Mezcla de semillas de pasto para césped resistente.','masculino','yardero',299,0,0,0,0,'Esteban Gutiérrez',1),

-- LLANTEROS
('MASC-DESMONTADORA','Desmontadora de Llantas Manual','Palanca desmontadora de llantas con punta plana y curva.','masculino','llanteros',349,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-COMPRESOR-LLANTA','Compresor de Llantas Portátil','Compresor digital portátil 12V con corte automático.','masculino','llanteros',599,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-MEDIDOR','Medidor de Presión Digital','Medidor digital con pantalla LCD y rango 0-150PSI.','masculino','llanteros',199,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-KIT-PONCHADURA','Kit de Reparación de Ponchaduras','Kit con parches, pegamento, lima y aplicador para reparación rápida.','masculino','llanteros',149,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-BALANCIN','Balancín para Llantas','Herramienta para balanceo manual de llantas con soporte.','masculino','llanteros',799,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-TAPONES','Juego de Tapones para Válvulas','Set de 10 tapones cromados para válvulas de llanta.','masculino','llanteros',79,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-CRUZ-LLANTA','Cruz para Llantas 4 vías','Cruz desmontadora de 4 vías para tuercas de llanta.','masculino','llanteros',449,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-GATO-LATA','Gato de Lata 2 Ton','Gato de tijera compacto 2 toneladas para emergencias.','masculino','llanteros',399,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-CALZAS','Calzas para Llantas 2 piezas','Calzas de seguridad de goma para inmovilizar llantas.','masculino','llanteros',199,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-BOLSA-HERR','Bolsa para Herramientas','Bolsa plegable de lona resistente con múltiples bolsillos.','masculino','llanteros',349,0,0,0,0,'Esteban Gutiérrez',1),

-- FITNESS
('MASC-MAN CUERDAS','Juego de Mancuernas 20kg','Par de mancuernas hexagonales de neopreno 2x10kg.','masculino','fitness',699,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-BARRA','Barra Olímpica 20kg','Barra olímpica cromada 20kg con pesas incluidas 100kg.','masculino','fitness',2499,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-BANCA','Banca de Pesas Ajustable','Banca de ejercicios ajustable 4 posiciones.','masculino','fitness',1799,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-PESAS','Set Pesas Rusas 8-16-24kg','Juego de 3 pesas rusas de acero fundido.','masculino','fitness',1599,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-BARRA-DOM','Barra de Dominadas Pared','Barra de dominadas con soporte de pared, capacidad 150kg.','masculino','fitness',899,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-CUERDA','Cuerda para Saltar','Cuerda de velocidad con rodamientos y mango ergonómico.','masculino','fitness',199,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-GUANTES-FIT','Guantes de Gimnasio','Guantes con soporte de muñeca y palma acolchada.','masculino','fitness',299,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-FAJI','Faja de Levantamiento','Faja lumbar de cuero para levantamiento de pesas.','masculino','fitness',499,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-PROTEINA','Proteína Whey 2kg','Proteína de suero de leche sabor chocolate 2kg.','masculino','fitness',799,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-CREATINA','Creatina Monohidratada 500g','Creatina pura micronizada 500 gramos.','masculino','fitness',449,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-RODILLERA','Rodillera de Neopreno','Rodillera de compresión para levantamiento de pesas.','masculino','fitness',349,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-BANDA','Bandas de Resistencia 5 niveles','Set de 5 bandas elásticas con diferentes niveles de resistencia.','masculino','fitness',299,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-TAPIZ','Tapiz de Yoga 180x60cm','Tapete antideslizante para ejercicio y yoga 6mm.','masculino','fitness',399,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-SHAKER','Shaker 700ml con Compartimento','Botella mezcladora con compartimento para proteína en polvo.','masculino','fitness',199,0,0,0,0,'Esteban Gutiérrez',1),
('MASC-CINTURON','Cinturón Porta Peso','Cinturón para cadenas con gancho para discos de peso.','masculino','fitness',349,0,0,0,0,'Esteban Gutiérrez',1);

-- ========== CAPTURAS EMAIL DEMO ==========
INSERT OR IGNORE INTO capturas_email (email, nombre, origen, interes) VALUES
('maria@example.com','María García','academia','html5'),
('juan@example.com','Juan Pérez','legado','plantas-medicinales'),
('ana@example.com','Ana López','historias','leyendas'),
('carlos@example.com','Carlos Ruiz','esoterico','chakras'),
('laura@example.com','Laura Martínez','holding','general'),
('pedro@example.com','Pedro Sánchez','academia','javascript');

-- ========== PEDIDOS DE EJEMPLO ==========
INSERT OR IGNORE INTO pedidos (id, cliente_nombre, cliente_email, items_json, subtotal, envio, total, estatus) VALUES
(1,'María García','maria@example.com','[{"id":1,"titulo":"HTML5: El Lenguaje de la Web","formato":"fisico","cantidad":1,"precio":399}]',399,99,498,'entregado'),
(2,'Juan Pérez','juan@example.com','[{"id":17,"titulo":"Botiquín de Plantas Medicinales Mexicanas","formato":"fisico","cantidad":1,"precio":349},{"id":2,"titulo":"CSS3: Diseño y Estilo Web","formato":"pdf","cantidad":1,"precio":199}]',548,99,647,'confirmado'),
(3,'Ana López','ana@example.com','[{"id":22,"titulo":"El Nahual y Otras Leyendas","formato":"fisico","cantidad":1,"precio":349}]',349,99,448,'pendiente');

-- ========== AMAZON AFILIADOS ==========
-- Actualizar URL de afiliado para productos (marcador: reemplazar COLIBRI_TAG con tu tag)
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=vestido+de+noche+elegante+mujer&tag=etceterastore-20' WHERE sku='FEM-VESTIDO-NOCHE';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=vestido+de+verano+floral+mujer&tag=etceterastore-20' WHERE sku='FEM-VESTIDO-VERA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=blusa+de+seda+mujer&tag=etceterastore-20' WHERE sku='FEM-BLUSA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=jeans+pitillo+elasticos+mujer&tag=etceterastore-20' WHERE sku='FEM-JEANS';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=falda+lapiz+tubo+mujer&tag=etceterastore-20' WHERE sku='FEM-FALDA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=chamarra+cuero+sintetico+mujer&tag=etceterastore-20' WHERE sku='FEM-CHAMARRA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=playera+algodon+basica+mujer&tag=etceterastore-20' WHERE sku='FEM-PLAYERA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=short+vaquero+mujer&tag=etceterastore-20' WHERE sku='FEM-SHORT';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=sudadera+capucha+mujer&tag=etceterastore-20' WHERE sku='FEM-SUDADERA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=leggins+deportivos+mujer&tag=etceterastore-20' WHERE sku='FEM-LEGGINS';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=pants+deportivo+mujer&tag=etceterastore-20' WHERE sku='FEM-PANTS';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=abrigo+largo+invernal+mujer&tag=etceterastore-20' WHERE sku='FEM-ABRIGO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=top+deportivo+mujer&tag=etceterastore-20' WHERE sku='FEM-TOP';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=traje+de+bano+enterizo+mujer&tag=etceterastore-20' WHERE sku='FEM-TRAJE-BANO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=bikini+triangulo+mujer&tag=etceterastore-20' WHERE sku='FEM-BIKINI';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=labial+mate+larga+duracion&tag=etceterastore-20' WHERE sku='FEM-LABIAL';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=rimel+voluminizador&tag=etceterastore-20' WHERE sku='FEM-RIMEL';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=base+liquida+cobertura+total&tag=etceterastore-20' WHERE sku='FEM-BASE';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=corrector+iluminador+ojeras&tag=etceterastore-20' WHERE sku='FEM-CORRECTOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=paleta+de+sombras+24+colores&tag=etceterastore-20' WHERE sku='FEM-PALETA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=delineador+liquido+precision&tag=etceterastore-20' WHERE sku='FEM-DELINEADOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=polvo+compacto+matificante&tag=etceterastore-20' WHERE sku='FEM-POLVO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=bronzer+en+polvo&tag=etceterastore-20' WHERE sku='FEM-BRONCER';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=iluminador+liquido+glow&tag=etceterastore-20' WHERE sku='FEM-ILUMINADOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=kit+de+cejas+3+en+1&tag=etceterastore-20' WHERE sku='FEM-CEJA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=crema+facial+anti-edad+acido+hialuronico&tag=etceterastore-20' WHERE sku='FEM-CREMA-FACIAL';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=serum+vitamina+c+facial&tag=etceterastore-20' WHERE sku='FEM-SERUM';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=crema+contorno+de+ojos&tag=etceterastore-20' WHERE sku='FEM-CONTORNO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=exfoliante+facial+enzimatico&tag=etceterastore-20' WHERE sku='FEM-EXFOLIANTE';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=mascarilla+facial+colageno&tag=etceterastore-20' WHERE sku='FEM-MASCARILLA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=protector+solar+facial+spf50&tag=etceterastore-20' WHERE sku='FEM-PROTECTOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=crema+corporal+hidratante+karite&tag=etceterastore-20' WHERE sku='FEM-CREMA-CORPORAL';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=aceite+corporal+brillo+natural&tag=etceterastore-20' WHERE sku='FEM-ACEITE';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=shampoo+profesional+sin+sulfatos&tag=etceterastore-20' WHERE sku='FEM-SHAMPOO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=acondicionador+reparador+keratina&tag=etceterastore-20' WHERE sku='FEM-CONDICIONADOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=mascarilla+capilar+reparacion+intensa&tag=etceterastore-20' WHERE sku='FEM-MASCARILLA-CAP';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=aceite+de+argan+capilar&tag=etceterastore-20' WHERE sku='FEM-ACEITE-CAP';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=anillo+plata+925+mujer&tag=etceterastore-20' WHERE sku='FEM-ANILLO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=aretes+de+aro+dorados+mujer&tag=etceterastore-20' WHERE sku='FEM-ARETES';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=collar+colgante+corazon+mujer&tag=etceterastore-20' WHERE sku='FEM-COLLAR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=pulsera+cuentas+doradas+mujer&tag=etceterastore-20' WHERE sku='FEM-PULSERA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=bolso+tote+cuero+mujer&tag=etceterastore-20' WHERE sku='FEM-BOLSO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=mochila+urbana+mujer&tag=etceterastore-20' WHERE sku='FEM-MOCHILA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=cinturon+ancho+hebilla+dorada&tag=etceterastore-20' WHERE sku='FEM-CINTO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=bufanda+seda+estampada+mujer&tag=etceterastore-20' WHERE sku='FEM-BUFANDA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=gafas+sol+cateye+mujer&tag=etceterastore-20' WHERE sku='FEM-GAFAS';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=reloj+pulsera+femenino&tag=etceterastore-20' WHERE sku='FEM-RELÓ';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=cepillo+secador+air+styler&tag=etceterastore-20' WHERE sku='FEM-CEPILLO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=depiladora+electrica+ip+luz+pulsada&tag=etceterastore-20' WHERE sku='FEM-DEPILADORA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=limpiadora+facial+electrica+sonica&tag=etceterastore-20' WHERE sku='FEM-LIMPIADORA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=masajeador+corporal+electrico+percusion&tag=etceterastore-20' WHERE sku='FEM-MASAJEADOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=alisador+pelo+inalambrico&tag=etceterastore-20' WHERE sku='FEM-ALISADOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=secador+pelo+profesional+ionico&tag=etceterastore-20' WHERE sku='FEM-SECADOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=plancha+alisadora+ceramica&tag=etceterastore-20' WHERE sku='FEM-PLANCHA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=rizador+pelo+3+en+1&tag=etceterastore-20' WHERE sku='FEM-RIZADOR';

-- INFANTIL
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=peluche+oso+felpa+40cm&tag=etceterastore-20' WHERE sku='INF-PELUCHE-OSO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=peluche+conejo+rosa&tag=etceterastore-20' WHERE sku='INF-PELUCHE-CONEJO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=carro+bomberos+luces+sonido&tag=etceterastore-20' WHERE sku='INF-CARRITO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=muneca+bebe+llorona+interactiva&tag=etceterastore-20' WHERE sku='INF-MUÑECA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=bloques+construccion+madera+100+piezas&tag=etceterastore-20' WHERE sku='INF-BLOQUES';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=puzzle+dinosaurios+60+piezas&tag=etceterastore-20' WHERE sku='INF-PUZZLE';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=plastilina+12+colores+no+toxica&tag=etceterastore-20' WHERE sku='INF-PLAY-DOH';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=playmobil+granja+animales&tag=etceterastore-20' WHERE sku='INF-PLAYMOBIL';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=vestido+unicornio+nina&tag=etceterastore-20' WHERE sku='INF-VESTIDO-UNI';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=vestido+flores+nina&tag=etceterastore-20' WHERE sku='INF-VESTIDO-FLOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=leggins+nina+algodon&tag=etceterastore-20' WHERE sku='INF-LEGGINS';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=playera+dinosaurios+nino&tag=etceterastore-20' WHERE sku='INF-PLAYERA-DINO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=short+deportivo+nino&tag=etceterastore-20' WHERE sku='INF-SHORT';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=chamarra+impermeable+ninos&tag=etceterastore-20' WHERE sku='INF-PARKA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=pijama+algodon+unisex+ninos&tag=etceterastore-20' WHERE sku='INF-PIJAMA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=conjunto+deportivo+nino+nina&tag=etceterastore-20' WHERE sku='INF-CONJUNTO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=libro+dinosaurios+infantil+ilustrado&tag=etceterastore-20' WHERE sku='INF-LIBRO-DINOS';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=libro+mis+primeros+animales+bebe&tag=etceterastore-20' WHERE sku='INF-LIBRO-ANIMALES';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=cuentos+antes+dormir+infantil&tag=etceterastore-20' WHERE sku='INF-LIBRO-CUENTOS';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=libro+aprender+colores+infantil&tag=etceterastore-20' WHERE sku='INF-LIBRO-COLORES';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=abecedario+ilustrado+infantil&tag=etceterastore-20' WHERE sku='INF-LIBRO-ABC';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=cuento+unicornio+magico+infantil&tag=etceterastore-20' WHERE sku='INF-LIBRO-UNI';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=mochila+infantil+carro&tag=etceterastore-20' WHERE sku='INF-MOCHILA-CARRO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=mochila+infantil+unicornio&tag=etceterastore-20' WHERE sku='INF-MOCHILA-UNI';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=lonchera+termica+infantil&tag=etceterastore-20' WHERE sku='INF-LONCHERA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=botella+agua+infantil+400ml&tag=etceterastore-20' WHERE sku='INF-BOTELLA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=gorra+infantil+ajustable&tag=etceterastore-20' WHERE sku='INF-GORRA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=set+baberos+algodon+bebe&tag=etceterastore-20' WHERE sku='INF-BABERO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=mordedores+silicona+bebe&tag=etceterastore-20' WHERE sku='INF-MORDEDOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=sonaja+musical+pato+bebe&tag=etceterastore-20' WHERE sku='INF-SONAJA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=cobija+algodon+bebe&tag=etceterastore-20' WHERE sku='INF-COBIJA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=pizarron+magnetico+infantil&tag=etceterastore-20' WHERE sku='INF-PIZARRON';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=set+colores+cera+acuarela+infantil&tag=etceterastore-20' WHERE sku='INF-COLORES';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=libro+aprender+a+contar+infantil&tag=etceterastore-20' WHERE sku='INF-LIBRO-123';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=reloj+didactico+aprender+hora&tag=etceterastore-20' WHERE sku='INF-RELOJ';

-- MASCULINO
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=martillo+uña+20oz+profesional&tag=etceterastore-20' WHERE sku='MASC-MARTILLO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=taladro+percutor+650w&tag=etceterastore-20' WHERE sku='MASC-TALADRO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=sierra+circular+1800w+laser&tag=etceterastore-20' WHERE sku='MASC-SIERRA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=cinta+metrica+8m+profesional&tag=etceterastore-20' WHERE sku='MASC-CINTAMETRICA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=nivel+laser+autonivelante+linea+cruzada&tag=etceterastore-20' WHERE sku='MASC-NIVEL';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=casco+seguridad+dielectrico&tag=etceterastore-20' WHERE sku='MASC-CASCO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=guantes+trabajo+reforzados&tag=etceterastore-20' WHERE sku='MASC-GUANTES-CONST';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=llave+inglesa+12+pulgadas&tag=etceterastore-20' WHERE sku='MASC-LLAVE-INGL';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=pala+cuadrada+construccion&tag=etceterastore-20' WHERE sku='MASC-PALAYUDA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=carretilla+construccion+100+litros&tag=etceterastore-20' WHERE sku='MASC-CARRETILLA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=gato+hidraulico+3+toneladas&tag=etceterastore-20' WHERE sku='MASC-CATRIN';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=llaves+combinadas+15+piezas&tag=etceterastore-20' WHERE sku='MASC-LLAVE-CARRO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=juego+dados+media+pulgada+24+piezas&tag=etceterastore-20' WHERE sku='MASC-DADOS';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=torquimetro+llave+dinamometrica&tag=etceterastore-20' WHERE sku='MASC-TORQUIMETRO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=compresor+aire+24+litros&tag=etceterastore-20' WHERE sku='MASC-COMPRESOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=pistola+aire+comprimido+soplido&tag=etceterastore-20' WHERE sku='MASC-PISTOLA-AIRE';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=overol+mecanico+algodon&tag=etceterastore-20' WHERE sku='MASC-OVEROL';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=lampara+led+taller+recargable&tag=etceterastore-20' WHERE sku='MASC-LAMPARA-TALLER';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=caballete+seguridad+3+toneladas&tag=etceterastore-20' WHERE sku='MASC-CABALLETE';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=extractor+aceite+manual&tag=etceterastore-20' WHERE sku='MASC-EXTRACTOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=cortadora+pasto+electrica+1200w&tag=etceterastore-20' WHERE sku='MASC-CORTADORA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=desmalezadora+gasolina+52cc&tag=etceterastore-20' WHERE sku='MASC-DESMALEZADORA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=manguera+jardin+expandible+50m&tag=etceterastore-20' WHERE sku='MASC-MANGUERA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=aceite+motosierra+lubricante&tag=etceterastore-20' WHERE sku='MASC-AZEITE';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=tijeras+podar+profesionales&tag=etceterastore-20' WHERE sku='MASC-TIJERAS-PODAR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=rastrillo+jardin+metalico&tag=etceterastore-20' WHERE sku='MASC-RASTRILLO';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=pala+jardin+punta+redonda&tag=etceterastore-20' WHERE sku='MASC-PALA-JARDIN';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=soplador+hojas+electrico+aspirador&tag=etceterastore-20' WHERE sku='MASC-SOPLADOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=motosierra+electrica+16+pulgadas&tag=etceterastore-20' WHERE sku='MASC-MOTOSIERRA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=semillas+pasto+cesped+5kg&tag=etceterastore-20' WHERE sku='MASC-SEMILLAS';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=desmontadora+llantas+manual&tag=etceterastore-20' WHERE sku='MASC-DESMONTADORA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=compresor+llantas+portatil+digital&tag=etceterastore-20' WHERE sku='MASC-COMPRESOR-LLANTA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=medidor+presion+llantas+digital&tag=etceterastore-20' WHERE sku='MASC-MEDIDOR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=kit+reparacion+ponchaduras+llanta&tag=etceterastore-20' WHERE sku='MASC-KIT-PONCHADURA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=balancin+balanceo+llantas&tag=etceterastore-20' WHERE sku='MASC-BALANCIN';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=tapones+valvula+llanta+cromados&tag=etceterastore-20' WHERE sku='MASC-TAPONES';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=cruz+desmontadora+llantas+4+vias&tag=etceterastore-20' WHERE sku='MASC-CRUZ-LLANTA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=gato+de+lata+tijera+2+toneladas&tag=etceterastore-20' WHERE sku='MASC-GATO-LATA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=calzas+seguridad+goma+llantas&tag=etceterastore-20' WHERE sku='MASC-CALZAS';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=bolsa+herramientas+lona+plegable&tag=etceterastore-20' WHERE sku='MASC-BOLSA-HERR';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=mancuernas+hexagonales+10kg&tag=etceterastore-20' WHERE sku='MASC-MAN CUERDAS';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=barra+olimpica+pesas+100kg&tag=etceterastore-20' WHERE sku='MASC-BARRA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=banca+pesas+ajustable&tag=etceterastore-20' WHERE sku='MASC-BANCA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=pesas+rusas+kettlebell+set&tag=etceterastore-20' WHERE sku='MASC-PESAS';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=barra+dominadas+pared&tag=etceterastore-20' WHERE sku='MASC-BARRA-DOM';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=cuerda+saltar+velocidad&tag=etceterastore-20' WHERE sku='MASC-CUERDA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=guantes+gimnasio+muneca&tag=etceterastore-20' WHERE sku='MASC-GUANTES-FIT';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=faja+levantamiento+pesas+cuero&tag=etceterastore-20' WHERE sku='MASC-FAJI';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=proteina+whey+chocolate+2kg&tag=etceterastore-20' WHERE sku='MASC-PROTEINA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=creatina+monohidratada+500g&tag=etceterastore-20' WHERE sku='MASC-CREATINA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=rodillera+neopreno+levantamiento&tag=etceterastore-20' WHERE sku='MASC-RODILLERA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=bandas+resistencias+ejercicio+set&tag=etceterastore-20' WHERE sku='MASC-BANDA';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=tapete+yoga+antideslizante&tag=etceterastore-20' WHERE sku='MASC-TAPIZ';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=shaker+proteina+700ml&tag=etceterastore-20' WHERE sku='MASC-SHAKER';
UPDATE productos SET url_afiliado='https://www.amazon.com/s?k=cinturon+porta+peso+leva&tag=etceterastore-20' WHERE sku='MASC-CINTURON';
