import os

LIBROS = [
    {
        'folder': '16_IA_LIBRO_MAESTRO',
        'title': 'INTELIGENCIA ARTIFICIAL',
        'subtitle': 'Fundamentos de IA, Machine Learning y LLMs',
        'modules': [
            ('INTRODUCCIÓN A LA IA', [
                '¿Qué es la Inteligencia Artificial?',
                'Historia de la IA: De Turing a GPT',
                'Tipos de IA: Débil, Fuerte y Superinteligencia',
                'IA Simbólica vs Machine Learning',
                'Aplicaciones de la IA en la vida real',
                'Ética y sesgos en Inteligencia Artificial',
                'El impacto de la IA en el empleo',
                'Regulación y marco legal de la IA',
                'Herramientas y plataformas de IA',
                'Proyecto: Chatbot conversacional simple'
            ]),
            ('FUNDAMENTOS DE MACHINE LEARNING', [
                '¿Qué es Machine Learning?',
                'Aprendizaje Supervisado vs No Supervisado',
                'Regresión Lineal y Logística',
                'Árboles de Decisión y Random Forest',
                'Máquinas de Soporte Vectorial (SVM)',
                'K-Means y Clustering',
                'Métricas de evaluación de modelos',
                'Overfitting, Underfitting y Regularización',
                'Feature Engineering y Selección',
                'Proyecto: Clasificador de correos spam'
            ]),
            ('DEEP LEARNING Y REDES NEURONALES', [
                'Fundamentos de Redes Neuronales',
                'Perceptrón y Funciones de Activación',
                'Backpropagation y Gradiente Descendente',
                'Redes Convolucionales (CNN)',
                'Redes Recurrentes (RNN y LSTM)',
                'Transfer Learning y Fine-tuning',
                'Generative Adversarial Networks (GANs)',
                'Autoencoders',
                'Frameworks: TensorFlow vs PyTorch',
                'Proyecto: Clasificador de imágenes'
            ]),
            ('PROCESAMIENTO DE LENGUAJE NATURAL', [
                'Introducción al NLP',
                'Tokenización y Stemming',
                'Bag of Words y TF-IDF',
                'Word Embeddings: Word2Vec y GloVe',
                'Transformers y Attention Mechanism',
                'BERT y Modelos Pre-entrenados',
                'GPT y Modelos Generativos',
                'Análisis de Sentimientos',
                'Traducción Automática',
                'Proyecto: Asistente virtual con NLP'
            ]),
            ('LLMs Y MODELOS DE LENGUAJE', [
                '¿Qué son los Large Language Models?',
                'Arquitectura Transformer a detalle',
                'Entrenamiento de LLMs',
                'Fine-tuning y Prompt Engineering',
                'RAG (Retrieval Augmented Generation)',
                'RLHF: Aprendizaje por Refuerzo',
                'Evaluación de LLMs',
                'Despliegue de LLMs en producción',
                'Costos y optimización de LLMs',
                'Proyecto: Aplicación con API de GPT'
            ]),
            ('VISIÓN POR COMPUTADORA', [
                'Introducción a la Visión por Computadora',
                'Procesamiento de Imágenes',
                'Detección de Objetos (YOLO, SSD)',
                'Segmentación Semántica',
                'Reconocimiento Facial',
                'OCR y Lectura de Documentos',
                'Generación de Imágenes (DALL-E, Stable Diffusion)',
                'Visióm 3D y Reconstrucción',
                'Aplicaciones en Robótica',
                'Proyecto: Sistema de reconocimiento facial'
            ]),
            ('IA EN PRODUCCIÓN', [
                'MLOps: Ciclo de vida de modelos',
                'Pipeline de datos para IA',
                'Entrenamiento distribuido',
                'Versionado de modelos (DVC, MLflow)',
                'Monitorización y deriva de modelos',
                'A/B Testing en modelos ML',
                'APIs para modelos de IA',
                'Edge AI e Inferencia en dispositivo',
                'Privacidad y seguridad en IA',
                'Proyecto: API de modelo ML en Flask'
            ]),
            ('FUTURO DE LA IA Y PROYECTO FINAL', [
                'IA Generativa y Creatividad',
                'Agentes Autónomos',
                'IA Explicable (XAI)',
                'Quantum Machine Learning',
                'IA Sostenible y Green AI',
                'Superinteligencia y Singularidad',
                'IA en la Educación del Futuro',
                'Colaboración Humano-IA',
                'Ética y Responsabilidad Global',
                'Proyecto Final: Solución de IA completa'
            ]),
        ]
    },
    {
        'folder': '17_DJANGO_LIBRO_MAESTRO',
        'title': 'DJANGO: DESARROLLO WEB SIN COMPLICACIONES',
        'subtitle': 'El framework web Python para perfeccionistas con plazos',
        'modules': [
            ('INTRODUCCIÓN A DJANGO', [
                '¿Qué es Django? Filosofía y ventajas',
                'Historia y comunidad Django',
                'Modelo MTV (Model-Template-View)',
                'Instalación y configuración del entorno',
                'Primer proyecto Django',
                'Estructura de un proyecto Django',
                'Settings y configuración básica',
                'Git y control de versiones',
                'Entornos virtuales y dependencias',
                'Proyecto: Hola Mundo Django'
            ]),
            ('MODELOS Y BASE DE DATOS', [
                'Modelos y ORM de Django',
                'Migraciones y admin de Django',
                'Relaciones: ForeignKey, ManyToMany, OneToOne',
                'Consultas avanzadas con QuerySets',
                'Agregaciones y anotaciones',
                'Señales (Signals)',
                'Custom Managers',
                'Base de datos PostgreSQL con Django',
                'Optimización de consultas (N+1)',
                'Proyecto: Modelos de un blog'
            ]),
            ('VIEWS Y URLS', [
                'Function-Based Views (FBV)',
                'Class-Based Views (CBV)',
                'Generic Views',
                'URL dispatcher y patrones',
                'Parámetros en URLs',
                'Manejo de errores HTTP',
                'Paginación',
                'Vistas basadas en Mixins',
                'Decoradores útiles',
                'Proyecto: CRUD completo'
            ]),
            ('TEMPLATES Y FRONTEND', [
                'Motor de plantillas Django',
                'Herencia de templates',
                'Template tags y filters',
                'Formularios con Django Forms',
                'Validación de formularios',
                'ModelForms y FormSets',
                'Mensajes flash',
                'Static files y media',
                'Bootstrap y Django',
                'Proyecto: Frontend del blog'
            ]),
            ('AUTENTICACIÓN Y USUARIOS', [
                'Sistema de autenticación',
                'Registro y login de usuarios',
                'Permisos y grupos',
                'Personalización del User model',
                'Autenticación con JWT',
                'OAuth y redes sociales',
                'Seguridad en formularios (CSRF, XSS)',
                'Recuperación de contraseñas',
                'Middleware de seguridad',
                'Proyecto: Sistema completo de usuarios'
            ]),
            ('APIS CON DJANGO REST FRAMEWORK', [
                'Introducción a Django REST Framework',
                'Serializers y ViewSets',
                'Autenticación en APIs',
                'Permisos y throttling',
                'Filtrado y búsqueda',
                'Paginación de APIs',
                'Documentación con Swagger/DRF',
                'Testing de APIs',
                'Versionado de APIs',
                'Proyecto: API REST completa'
            ]),
            ('TESTING Y DEPLOY', [
                'Testing en Django (UnitTest, pytest)',
                'Test de modelos y views',
                'Test de APIs',
                'Test Driven Development (TDD)',
                'Configuración de producción',
                'Variables de entorno',
                'Base de datos en producción',
                'Servidores WSGI (Gunicorn)',
                'Nginx y Django',
                'Proyecto: Deploy en Railway'
            ]),
            ('PROYECTO FINAL: E-COMMERCE', [
                'Planificación del proyecto',
                'Modelos de productos y carrito',
                'Sistema de pagos (Stripe/PAYU)',
                'Panel de administración',
                'API de productos',
                'Frontend del e-commerce',
                'Autenticación de clientes',
                'Órdenes y facturación',
                'Testing integral',
                'Deploy y presentación'
            ]),
        ]
    },
    {
        'folder': '18_DOCKER_LIBRO_MAESTRO',
        'title': 'DOCKER: CONTENEDORES',
        'subtitle': 'Despliega aplicaciones con Docker y contenedores',
        'modules': [
            ('FUNDAMENTOS DE CONTENEDORES', [
                '¿Qué son los contenedores?',
                'Contenedores vs Máquinas Virtuales',
                'Historia de Docker',
                'Arquitectura de Docker',
                'Instalación de Docker',
                'Primeros comandos docker',
                'Imágenes y contenedores',
                'Docker Hub y registros',
                'Ciclo de vida de un contenedor',
                'Proyecto: Hola Mundo en Docker'
            ]),
            ('IMÁGENES Y DOCKERFILES', [
                '¿Qué es un Dockerfile?',
                'Instrucciones básicas (FROM, RUN, COPY)',
                'Multi-stage builds',
                'Optimización de imágenes',
                'Capas y caché de Docker',
                'Variables de entorno',
                'ENTRYPOINT vs CMD',
                'HEALTHCHECK y labels',
                'Buenas prácticas en Dockerfiles',
                'Proyecto: Dockerizar app Python'
            ]),
            ('DOCKER COMPOSE', [
                'Introducción a Docker Compose',
                'Archivo docker-compose.yml',
                'Servicios y redes',
                'Volúmenes y datos persistentes',
                'Variables de entorno en Compose',
                'Dependencias entre servicios',
                'Escalado de servicios',
                'Logs y debugging',
                'Perfiles y múltiples entornos',
                'Proyecto: App multi-servicio'
            ]),
            ('REDES Y ALMACENAMIENTO', [
                'Redes en Docker',
                'Bridge, Host y Overlay',
                'DNS y descubrimiento',
                'Volúmenes y bind mounts',
                'tmpfs mounts',
                'Persistencia de datos',
                'Backup y restauración',
                'Seguridad de redes',
                'Plugins de red y almacenamiento',
                'Proyecto: Red multicontenedor'
            ]),
            ('DOCKER EN PRODUCCIÓN', [
                'Docker Swarm',
                'Servicios y stacks en Swarm',
                'Kubernetes vs Docker Swarm',
                'Orquestación básica',
                'Health checks y reinicios',
                'Logging y monitoreo',
                'Actualizaciones rolling',
                'Secretos y configuraciones',
                'Limitación de recursos',
                'Proyecto: Cluster Swarm local'
            ]),
            ('CI/CD CON DOCKER', [
                'Docker en pipelines CI/CD',
                'GitHub Actions con Docker',
                'GitLab CI y Docker',
                'Registro privado de imágenes',
                'Tags y versionado',
                'Tests en contenedores',
                'Deploy automatizado',
                'Seguridad en CI/CD',
                'Kaniko y build sin Docker',
                'Proyecto: Pipeline completo'
            ]),
            ('SEGURIDAD Y BUENAS PRÁCTICAS', [
                'Principios de seguridad en contenedores',
                'Escaneo de vulnerabilidades',
                'Usuarios no root',
                'Límites de recursos',
                'Firmado de imágenes',
                'Secrets management',
                'Auditoría y logs',
                'Network policies',
                'CIS benchmarks para Docker',
                'Proyecto: Hardening de contenedores'
            ]),
            ('PROYECTO FINAL: MICROSERVICIOS', [
                'Arquitectura de microservicios',
                'Diseño de servicios',
                'API Gateway',
                'Comunicación entre servicios',
                'Bases de datos por servicio',
                'Docker Compose para microservicios',
                'Monitoreo centralizado',
                'Logging distribuido',
                'Deploy y escalado',
                'Presentación final'
            ]),
        ]
    },
    {
        'folder': '19_GIT_LIBRO_MAESTRO',
        'title': 'GIT Y GITHUB',
        'subtitle': 'Control de versiones y trabajo colaborativo',
        'modules': [
            ('INTRODUCCIÓN A GIT', [
                '¿Qué es Git y por qué usarlo?',
                'Historia de Git y Linus Torvalds',
                'Instalación y configuración inicial',
                'Primeros pasos: init, add, commit',
                'El área de staging',
                'Estados de archivos en Git',
                'Configuración global y local',
                'Alias útiles para Git',
                'Git help y documentación',
                'Proyecto: Primer repositorio local'
            ]),
            ('RAMAS Y MERGE', [
                '¿Qué son las ramas (branches)?',
                'Crear y cambiar de rama',
                'Merge: fusión de ramas',
                'Conflictos y resolución',
                'Git merge vs rebase',
                'Fast-forward y 3-way merge',
                'Gestión de ramas',
                'Ramas remotas y tracking',
                'Cherry-pick',
                'Proyecto: Flujo de ramas'
            ]),
            ('GITHUB Y TRABAJO REMOTO', [
                'Introducción a GitHub',
                'Repositorios remotos (origin)',
                'Push y Pull',
                'Clone y Fork',
                'Pull Requests',
                'Code Review en GitHub',
                'Issues y Project Boards',
                'GitHub Actions básico',
                'GitHub Pages',
                'Proyecto: Colaboración en GitHub'
            ]),
            ('REBASE Y ESTRATEGIAS AVANZADAS', [
                'Rebase interactivo',
                'Squash de commits',
                'Amend y modificación de commits',
                'Git reflog',
                'Stash y trabajo temporal',
                'Bisect para encontrar bugs',
                'Tags y versionado semántico',
                'Submodules y subtrees',
                'Git hooks',
                'Proyecto: Historia limpia de commits'
            ]),
            ('FLUJOS DE TRABAJO PROFESIONALES', [
                'GitFlow',
                'GitHub Flow',
                'Trunk-Based Development',
                'Feature Branches',
                'Release Branches',
                'Hotfixes',
                'Code Review efectivo',
                'Conventional Commits',
                'Semantic Release',
                'Proyecto: Implementar GitFlow'
            ]),
            ('GIT AVANZADO', [
                'Git internals: objetos y referencias',
                'Reescribiendo historia',
                'Filter-branch y BFG',
                'Git LFS para archivos grandes',
                'Hooks del lado del servidor',
                'GPG y firma de commits',
                'Merge strategies profundas',
                'Worktrees',
                'Rendimiento en repos grandes',
                'Proyecto: Automatización con hooks'
            ]),
            ('DEVOPS Y CI/CD CON GIT', [
                'Integración continua con Git',
                'GitHub Actions avanzado',
                'GitLab CI/CD',
                'Protección de ramas',
                'Status checks y reglas',
                'Deploy automático por rama',
                'Monorepo vs multirepo',
                'Estrategias de versionado',
                'Changelog automatizado',
                'Proyecto: Pipeline CI/CD completo'
            ]),
            ('PROYECTO FINAL: OPEN SOURCE', [
                'Elección del proyecto',
                'Configuración del repositorio',
                'CONTRIBUTING.md y LICENSE',
                'Plantillas de issues y PRs',
                'Revisión colaborativa',
                'Release y tags',
                'Documentación del proyecto',
                'Comunidad y mantenimiento',
                'GitHub Pages para docs',
                'Presentación y publicación'
            ]),
        ]
    },
    {
        'folder': '20_API_LIBRO_MAESTRO',
        'title': 'APIs RESTFUL',
        'subtitle': 'Diseño y construcción de APIs profesionales',
        'modules': [
            ('FUNDAMENTOS DE APIs', [
                '¿Qué es una API?',
                'Historia de las APIs',
                'REST: Principios y filosofía',
                'HTTP: Verbos, códigos y cabeceras',
                'Recursos y endpoints',
                'JSON y XML',
                'SOAP vs REST vs GraphQL',
                'API First design',
                'Documentación de APIs',
                'Proyecto: Primera API REST'
            ]),
            ('DISEÑO DE APIs REST', [
                'Naming de endpoints',
                'Versionado de APIs',
                'HATEOAS',
                'Paginación y filtros',
                'Manejo de errores',
                'Códigos de estado HTTP',
                'Validación de entrada',
                'Idempotencia',
                'Rate Limiting',
                'Proyecto: API de libros'
            ]),
            ('AUTENTICACIÓN Y AUTORIZACIÓN', [
                'API Keys',
                'Basic Auth',
                'JWT (JSON Web Tokens)',
                'OAuth 2.0',
                'OpenID Connect',
                'Refresh Tokens',
                'Roles y permisos',
                'RBAC vs ABAC',
                'Seguridad en headers',
                'Proyecto: Autenticación JWT'
            ]),
            ('BASES DE DATOS Y APIs', [
                'Conexión a base de datos',
                'ORM vs SQL directo',
                'Modelado de datos para APIs',
                'Migraciones',
                'Consultas eficientes',
                'Caching con Redis',
                'N+1 problem',
                'Transacciones',
                'Pooling de conexiones',
                'Proyecto: API con PostgreSQL'
            ]),
            ('TESTING DE APIs', [
                'Pruebas unitarias',
                'Pruebas de integración',
                'Postman y colecciones',
                'pytest y requests',
                'Mocking de servicios',
                'Pruebas de carga',
                'Contratos de API',
                'Documentación con Swagger',
                'OpenAPI Specification',
                'Proyecto: Suite de tests'
            ]),
            ('DESPLIEGUE Y MONITOREO', [
                'Servidores WSGI/ASGI',
                'Contenedores para APIs',
                'API Gateway',
                'Load Balancing',
                'Logging estructurado',
                'Métricas y alertas',
                'Health checks',
                'Graceful shutdown',
                'Backup y recovery',
                'Proyecto: Deploy en producción'
            ]),
            ('GRAPHQL Y OTRAS ALTERNATIVAS', [
                'GraphQL: Query Language',
                'Resolvers y Schema',
                'Mutations y Subscriptions',
                'Apollo Server',
                'gRPC: RPC moderno',
                'Protocol Buffers',
                'WebSockets',
                'Event-Driven APIs',
                'AsyncAPI',
                'Proyecto: API GraphQL'
            ]),
            ('PROYECTO FINAL: API DE COMERCIO', [
                'Diseño del sistema',
                'Endpoints y recursos',
                'Base de datos y modelos',
                'Autenticación y roles',
                'Carrito y órdenes',
                'Integración de pagos',
                'Documentación completa',
                'Tests integrales',
                'Deploy y monitoreo',
                'Presentación final'
            ]),
        ]
    },
    {
        'folder': '21_SEGURIDAD_LIBRO_MAESTRO',
        'title': 'SEGURIDAD WEB',
        'subtitle': 'Protege tus aplicaciones web',
        'modules': [
            ('FUNDAMENTOS DE SEGURIDAD', [
                '¿Por qué es importante la seguridad?',
                'Triada CIA: Confidencialidad, Integridad, Disponibilidad',
                'Principios de seguridad informática',
                'Superficie de ataque',
                'Amenazas vs Vulnerabilidades vs Riesgos',
                'Criptografía básica',
                'Autenticación vs Autorización',
                'Modelo de confianza cero',
                'Cumplimiento y regulaciones',
                'Proyecto: Evaluación de seguridad'
            ]),
            ('OWASP TOP 10', [
                '¿Qué es OWASP?',
                'Broken Access Control',
                'Cryptographic Failures',
                'Injection (SQL, NoSQL, Command)',
                'Insecure Design',
                'Security Misconfiguration',
                'Vulnerable Components',
                'Authentication Failures',
                'Data Integrity Failures',
                'Proyecto: Laboratorio OWASP'
            ]),
            ('SEGURIDAD EN APLICACIONES WEB', [
                'XSS: Cross-Site Scripting',
                'CSRF: Cross-Site Request Forgery',
                'SSRF: Server-Side Request Forgery',
                'File Upload vulnerabilities',
                'IDOR: Insecure Direct Object Reference',
                'Rate Limiting y DoS',
                'Manejo seguro de sesiones',
                'CORS y Content Security Policy',
                'Seguridad en formularios',
                'Proyecto: App segura'
            ]),
            ('AUTENTICACIÓN SEGURA', [
                'Hashing de contraseñas',
                'MFA: Autenticación multifactor',
                'Passwordless authentication',
                'OAuth 2.0 y OpenID Connect',
                'JWT seguro',
                'Session management',
                'Biometric authentication',
                'SSO (Single Sign-On)',
                'WebAuthn y FIDO2',
                'Proyecto: Sistema de login seguro'
            ]),
            ('SEGURIDAD EN APIs', [
                'API Security Best Practices',
                'Rate limiting avanzado',
                'Input validation',
                'API keys management',
                'GraphQL security',
                'gRPC security',
                'WebSocket security',
                'API gateway como firewall',
                'API discovery y shadow APIs',
                'Proyecto: API hardening'
            ]),
            ('HACKING ÉTICO Y PENTESTING', [
                'Metodología de pentesting',
                'Reconocimiento y footprinting',
                'Escaneo de vulnerabilidades',
                'Explotación básica',
                'Post-explotación',
                'Burp Suite profesional',
                'Automatización de pentests',
                'Bug Bounty programs',
                'Reportes de seguridad',
                'Proyecto: Pentest guiado'
            ]),
            ('DEVSECOPS', [
                'Seguridad en CI/CD',
                'SAST: Static Analysis',
                'DAST: Dynamic Analysis',
                'SCA: Software Composition Analysis',
                'Secret scanning',
                'Container security',
                'Infrastructure as Code security',
                'Security Champions',
                'Shift Left: seguridad temprana',
                'Proyecto: Pipeline DevSecOps'
            ]),
            ('PROYECTO FINAL: APP SEGURA', [
                'Análisis de requerimientos',
                'Diseño seguro',
                'Implementación con controles',
                'Pruebas de penetración',
                'Corrección de hallazgos',
                'Hardening final',
                'Documentación de seguridad',
                'Plan de respuesta a incidentes',
                'Monitoreo continuo',
                'Presentación y defensa'
            ]),
        ]
    },
    {
        'folder': '22_LINUX_LIBRO_MAESTRO',
        'title': 'LINUX PARA DESARROLLADORES',
        'subtitle': 'La terminal y el ecosistema Linux',
        'modules': [
            ('INTRODUCCIÓN A LINUX', [
                '¿Qué es Linux? Historia y filosofía',
                'Distribuciones: Ubuntu, Debian, Fedora, Arch',
                'Instalación de Linux',
                'El sistema de archivos Linux',
                'Usuarios y permisos',
                'Terminal vs Shell',
                'Primeros comandos básicos',
                'Hombre: cómo obtener ayuda',
                'Editores de texto (nano, vim)',
                'Proyecto: Explorando Linux'
            ]),
            ('COMANDOS ESENCIALES', [
                'Navegación: ls, cd, pwd',
                'Archivos: cp, mv, rm, touch',
                'Visualización: cat, less, head, tail',
                'Búsqueda: find, locate, grep',
                'Procesamiento: sort, uniq, wc',
                'Redirección y pipes',
                'Comandos de red: curl, wget, ping',
                'Procesos: ps, top, kill',
                'Compresión: tar, gzip, zip',
                'Proyecto: Automatización con comandos'
            ]),
            ('SCRIPTS Y AUTOMATIZACIÓN', [
                'Introducción a Bash scripting',
                'Variables y expansión',
                'Condicionales y loops',
                'Funciones en Bash',
                'Argumentos y flags',
                'Cron y scheduling',
                'Systemd services',
                'Logging en scripts',
                'Manejo de errores',
                'Proyecto: Script de backup'
            ]),
            ('ADMINISTRACIÓN DEL SISTEMA', [
                'Gestión de usuarios y grupos',
                'Permisos avanzados (chmod, chown)',
                'ACLs y atributos extendidos',
                'Montaje de discos y fstab',
                'LVM y particionamiento',
                'Systemd y servicios',
                'Logs del sistema (journalctl)',
                'Monitorización del sistema',
                'Actualizaciones y paquetes (apt, yum)',
                'Proyecto: Servidor web LAMP'
            ]),
            ('REDES EN LINUX', [
                'Configuración de red',
                'Interfaces y routing',
                'iptables y nftables',
                'DNS y resolución',
                'SSH y conexión remota',
                'SSH keys y hardening',
                'SCP, RSYNC y transferencia',
                'Nginx como proxy',
                'Firewall básico',
                'Proyecto: Servidor seguro SSH'
            ]),
            ('CONTENEDORES Y VIRTUALIZACIÓN', [
                'Docker en Linux',
                'LXC/LXD',
                'KVM y QEMU',
                'Vagrant',
                'Gestión de contenedores',
                'Redes en contenedores',
                'Volúmenes y almacenamiento',
                'Orquestación local',
                'Performance y recursos',
                'Proyecto: Laboratorio con Vagrant'
            ]),
            ('LINUX EN PRODUCCIÓN', [
                'Hardening de servidores',
                'SELinux y AppArmor',
                'Auditoría con auditd',
                'Monitoreo con Prometheus',
                'Backup y restauración',
                'High Availability',
                'Load balancing',
                'Recuperación ante desastres',
                'Performance tuning',
                'Proyecto: Servidor en producción'
            ]),
            ('PROYECTO FINAL: INFRAESTRUCTURA', [
                'Diseño de la infraestructura',
                'Configuración de servidores',
                'Automatización con scripts',
                'Monitoreo y alertas',
                'Seguridad y hardening',
                'Backup y DRP',
                'Documentación',
                'Pruebas de estrés',
                'Optimización final',
                'Presentación del proyecto'
            ]),
        ]
    },
    {
        'folder': '23_ARQUITECTURA_LIBRO_MAESTRO',
        'title': 'ARQUITECTURA DE SOFTWARE',
        'subtitle': 'Patrones de diseño y buenas prácticas',
        'modules': [
            ('FUNDAMENTOS DE ARQUITECTURA', [
                '¿Qué es la arquitectura de software?',
                'Atributos de calidad',
                'Estilos arquitectónicos',
                'Principios SOLID',
                'DRY, KISS, YAGNI',
                'Ley de Conway',
                'Documentación arquitectónica',
                'Stakeholders y requerimientos',
                'Decisiones arquitectónicas (ADR)',
                'Proyecto: Documentar arquitectura'
            ]),
            ('PATRONES DE DISEÑO CREACIONALES', [
                'Singleton y sus usos',
                'Factory Method',
                'Abstract Factory',
                'Builder',
                'Prototype',
                'Object Pool',
                'Dependency Injection',
                'Service Locator',
                'Creación de objetos en Python',
                'Proyecto: Implementar patrones'
            ]),
            ('PATRONES ESTRUCTURALES', [
                'Adapter',
                'Bridge',
                'Composite',
                'Decorator',
                'Facade',
                'Flyweight',
                'Proxy',
                'MVC y sus variantes',
                'Layered Architecture',
                'Proyecto: Refactorizar con patrones'
            ]),
            ('PATRONES DE COMPORTAMIENTO', [
                'Chain of Responsibility',
                'Command',
                'Interpreter',
                'Iterator',
                'Mediator',
                'Memento',
                'Observer',
                'State',
                'Strategy y Template Method',
                'Proyecto: Sistema de eventos'
            ]),
            ('ARQUITECTURAS MODERNAS', [
                'Microservicios',
                'Event-Driven Architecture',
                'CQRS y Event Sourcing',
                'Hexagonal Architecture',
                'Clean Architecture',
                'Domain-Driven Design (DDD)',
                'Bounded Contexts',
                'Event Storming',
                'Arquitectura Serverless',
                'Proyecto: Clean Architecture'
            ]),
            ('PATRONES DE MICROSERVICIOS', [
                'API Gateway',
                'Service Discovery',
                'Circuit Breaker',
                'Bulkhead',
                'Saga Pattern',
                'Eventual Consistency',
                'CQRS en microservicios',
                'Observabilidad distribuida',
                'Testing de microservicios',
                'Proyecto: Sistema distribuido'
            ]),
            ('CALIDAD Y DEUDA TÉCNICA', [
                'Métricas de calidad',
                'Code Smells y refactorización',
                'Deuda técnica',
                'Testing arquitectónico',
                'Performance testing',
                'Security architecture review',
                'Architecture Decision Records',
                'Revisión de arquitectura',
                'Evolución arquitectónica',
                'Proyecto: Auditoría y mejora'
            ]),
            ('PROYECTO FINAL: SISTEMA COMPLETO', [
                'Requerimientos y alcance',
                'Decisiones arquitectónicas',
                'Diseño de componentes',
                'Implementación',
                'Pruebas de integración',
                'Evaluación de atributos',
                'Documentación',
                'Presentación a stakeholders',
                'Lecciones aprendidas',
                'Entrega final'
            ]),
        ]
    },
    {
        'folder': '24_LIDERAZGO_LIBRO_MAESTRO',
        'title': 'LIDERAZGO TECNOLÓGICO',
        'subtitle': 'De desarrollador a líder de equipo',
        'modules': [
            ('FUNDAMENTOS DEL LIDERAZGO', [
                '¿Qué es liderazgo tecnológico?',
                'Liderazgo vs Gestión',
                'Los 5 niveles de liderazgo',
                'Inteligencia emocional',
                'Autoconocimiento y propósito',
                'Valores y principios',
                'Comunicación efectiva',
                'Empatía y escucha activa',
                'Visión y estrategia',
                'Proyecto: Plan de liderazgo personal'
            ]),
            ('GESTIÓN DE EQUIPOS TÉCNICOS', [
                'Formación de equipos',
                'Roles y responsabilidades',
                'Delegación efectiva',
                'Feedback constructivo',
                'Mentoría y coaching',
                'Diversidad e inclusión',
                'Resolución de conflictos',
                'Motivación del equipo',
                'Cultura de alto rendimiento',
                'Proyecto: Dinámica de equipo'
            ]),
            ('COMUNICACIÓN TÉCNICA', [
                'Comunicación con stakeholders',
                'Presentaciones técnicas',
                'Documentación para decisiones',
                'Reuniones efectivas',
                'Standups y retrospectivas',
                'Reporting y métricas',
                'Comunicación asíncrona',
                'Negociación técnica',
                'Persuasión y argumentación',
                'Proyecto: Presentación ejecutiva'
            ]),
            ('GESTIÓN DE PROYECTOS', [
                'Metodologías ágiles (Scrum, Kanban)',
                'Estimación y planificación',
                'Priorización (MoSCoW, RICE)',
                'Roadmaps técnicos',
                'Gestión de riesgos',
                'Sprint planning y review',
                'OKRs y KPIs',
                'Burn-down y velocity',
                'Herramientas (Jira, Trello)',
                'Proyecto: Planificación de sprint'
            ]),
            ('ARQUITECTURA Y DECISIONES TÉCNICAS', [
                'Toma de decisiones técnicas',
                'Trade-offs y compensaciones',
                'Tech Debt management',
                'Code Review como líder',
                'Estandarización y guías',
                'Innovación técnica',
                'Prototipado y experimentación',
                'Evaluación de tecnologías',
                'Arquitectura evolutiva',
                'Proyecto: RFC técnico'
            ]),
            ('CRECIMIENTO PROFESIONAL', [
                'Carrera técnica vs gerencial',
                'Habilidades del Staff Engineer',
                'Construcción de marca personal',
                'Networking profesional',
                'Speaking y conferencias',
                'Escritura técnica',
                'Open Source contribution',
                'Balance vida-trabajo',
                'Prevención de burnout',
                'Proyecto: Plan de carrera'
            ]),
            ('CULTURA Y ORGANIZACIÓN', [
                'Cultura de ingeniería',
                'Onboarding de nuevos miembros',
                'Documentación y conocimiento',
                'Comunidades de práctica',
                'Innovación y experimentación',
                'Remote y distributed teams',
                'Cambio organizacional',
                'Métricas de equipo',
                'Celebración y reconocimiento',
                'Proyecto: Propuesta cultural'
            ]),
            ('PROYECTO FINAL: TRANSFORMACIÓN', [
                'Diagnóstico del equipo',
                'Plan de transformación',
                'Implementación de cambios',
                'Métricas de impacto',
                'Ajustes y mejora continua',
                'Escalamiento del liderazgo',
                'Legado y sucesión',
                'Presentación ejecutiva',
                'Plan de seguimiento',
                'Entrega final y reflexión'
            ]),
        ]
    },
]

BASE = os.path.dirname(os.path.abspath(__file__))
LIBROS_DIR = os.path.join(BASE, 'libros')

AUTOR = "Esteban Gutiérrez A."
COAUTOR = "Profesor Búho AI"

for libro in LIBROS:
    folder_path = os.path.join(LIBROS_DIR, libro['folder'])
    os.makedirs(folder_path, exist_ok=True)
    
    for idx_mod, (mod_nombre, capitulos) in enumerate(libro['modules'], 1):
        mod_dir = os.path.join(folder_path, f'MODULO_{idx_mod:02d}')
        os.makedirs(mod_dir, exist_ok=True)
        
        base_chapter = (idx_mod - 1) * 10
        
        for idx_cap, cap_titulo in enumerate(capitulos, 1):
            cap_num = base_chapter + idx_cap
            cap_file = f'{cap_num:02d}_CAPITULO_{cap_num:02d}_{cap_titulo.upper().replace(" ", "_").replace(":", "").replace("?", "").replace("¡", "").replace("¿", "").replace(",", "").replace("á", "A").replace("é", "E").replace("í", "I").replace("ó", "O").replace("ú", "U").replace("ñ", "N").replace("()", "").replace("(", "").replace(")", "").replace(".", "").replace("&", "Y").replace("/", "_")[:50]}.txt'
            
            content = f"""===============================================================================
LUCAS EGA ACADEMY
LIBRO MAESTRO DE {libro['title']}
MÓDULO {idx_mod}
CAPÍTULO {cap_num}

{cap_titulo.upper()}

Versión Editorial 1.0

Autor:
{AUTOR}

Coautor Editorial:
{COAUTOR}

===============================================================================

"Nunca construyas una aplicación.
Construye conocimiento.
Las aplicaciones cambian.
El conocimiento permanece."

— {COAUTOR}

===============================================================================
BIENVENIDA DEL PROFESOR BÚHO
===============================================================================

Bienvenido.

En este capítulo exploraremos los fundamentos esenciales que todo profesional
debe conocer. Recuerda que el conocimiento técnico sin una base sólida es como
un edificio sin cimientos: se derrumba ante la primera tormenta.

Toma tu tiempo, practica cada concepto y, sobre todo, nunca dejes de hacer
preguntas. La tecnología avanza, pero los principios fundamentales permanecen.

===============================================================================
{cap_titulo.upper()}
===============================================================================

En este capítulo aprenderás los conceptos fundamentales relacionados con
{cap_titulo.lower()}. Este conocimiento es esencial para tu desarrollo
como profesional en el mundo de la tecnología.

===============================================================================
CONTENIDO DEL CAPÍTULO
===============================================================================

1. INTRODUCCIÓN

{cap_titulo} es un tema fundamental en el ecosistema tecnológico actual.
Comprender sus principios te permitirá construir soluciones más robustas,
escalables y mantenibles.

2. CONCEPTOS FUNDAMENTALES

Para dominar {cap_titulo.lower()}, es necesario comprender primero
sus conceptos básicos y cómo se relacionan con el resto del ecosistema
tecnológico.

3. APLICACIONES PRÁCTICAS

La teoría cobra vida cuando la aplicamos a problemas reales. A lo largo
de este capítulo, exploraremos casos de uso concretos y ejemplos
prácticos que ilustran cada concepto.

4. MEJORES PRÁCTICAS

La experiencia de la industria nos ha enseñado ciertas prácticas que
funcionan mejor que otras. Aprender estos patrones te ahorrará tiempo
y frustraciones.

===============================================================================
RESUMEN DEL CAPÍTULO
===============================================================================

- {cap_titulo} es esencial para el desarrollo profesional moderno
- Los fundamentos son la base de cualquier conocimiento sólido
- La práctica constante es la clave del dominio técnico
- Las mejores prácticas existen por una razón: aprende a aplicarlas

===============================================================================
EJERCICIOS PRÁCTICOS
===============================================================================

1. Investiga y documenta tres aplicaciones reales de {cap_titulo.lower()}
2. Identifica cómo se aplica en tu área de trabajo o estudio
3. Prepara un resumen ejecutivo de una cuartilla
4. Comparte tus hallazgos con un compañero de estudio

===============================================================================
PREPARACIÓN PARA EL SIGUIENTE CAPÍTULO
===============================================================================

En el siguiente capítulo exploraremos temas avanzados relacionados con
el material aquí presentado. Asegúrate de dominar estos conceptos antes
de continuar.

===============================================================================
PREGUNTAS DE REPASO
===============================================================================

1. ¿Por qué es importante {cap_titulo.lower()}?
2. ¿Cómo se relaciona con otros temas del ecosistema?
3. ¿Cuáles son los principios fundamentales que debes recordar?
4. ¿Qué aplicación práctica te parece más relevante?

===============================================================================
NOTAS DEL ESTUDIANTE
===============================================================================



===============================================================================
FRASE DEL PROFESOR BÚHO
===============================================================================

"El conocimiento no es poder. El conocimiento aplicado es poder.
La sabiduría está en saber cuándo aplicar cada conocimiento."

— {COAUTOR}

===============================================================================
"""
            
            filepath = os.path.join(mod_dir, cap_file)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content.strip() + '\n')
        
        print(f"  ✅ {libro['folder']} / Módulo {idx_mod:02d}: {len(capitulos)} capítulos")

    # Create final grad / farewell files
    ultimo_mod = os.path.join(folder_path, f'MODULO_08')
    farewell_path = os.path.join(ultimo_mod, f'80_CAPITULO_80_GRADUACION_Y_PROYECTO_FINAL_{libro["title"].upper().replace(" ", "_")[:40]}.txt')
    with open(farewell_path, 'w', encoding='utf-8') as f:
        f.write(f"""===============================================================================
LUCAS EGA ACADEMY
LIBRO MAESTRO DE {libro['title']}
MÓDULO 8
CAPÍTULO 80

GRADUACIÓN Y PROYECTO FINAL

Versión Editorial 1.0

===============================================================================

"{libro['title']}"
{libro['subtitle']}

===============================================================================

Querido estudiante,

Has llegado al final de este viaje de aprendizaje. Ocho módulos, ochenta
capítulos, incontables horas de estudio y práctica.

Has construido conocimiento. Y el conocimiento, a diferencia de las
tecnologías que cambian cada año, permanece contigo para siempre.

===============================================================================
LA CARTA DEL PROFESOR BÚHO
===============================================================================

Hoy no hay un capítulo técnico. Hoy hay una conversación entre maestro
y estudiante. Entre el que guía y el que camina.

Has demostrado disciplina, curiosidad y perseverancia. Has hecho preguntas,
has resuelto problemas, has fallado y te has levantado. Eso es lo que
realmente importa.

El mundo de la tecnología necesita más que buenos programadores.
Necesita personas con criterio, con ética, con visión. Personas como tú.

Sigue aprendiendo. Sigue construyendo. Sigue compartiendo.

El conocimiento que hoy adquieres será el cimiento de lo que construirás mañana.

Con admiración y respeto,

{COAUTOR}

===============================================================================
CERTIFICADO DE FINALIZACIÓN
===============================================================================

Se otorga el presente certificado a:

_________________________________

Por haber completado satisfactoriamente el

{libro['title'].upper()}

{libro['subtitle']}

Ocho módulos · Ochenta capítulos · Proyecto final integrador

Fecha: _______________

Firma del fundador:
{AUTOR}

===============================================================================
© 2026 Lucas EGA Academy — Una división de Colibrí Digital
===============================================================================
""")
    
    print(f"📚 {libro['folder']}: {libro['title']} — COMPLETADO ({len(libro['modules'])} módulos, 80 capítulos)")

print("\n🎉 TODOS LOS LIBROS GENERADOS EXITOSAMENTE")
