#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador de contenido educativo REAL para Lucas EGA Academy Niveles 4-6."""

import os
import shutil

BASE = "/home/ega/Escritorio/COLIBRI_DIGITAL/academia_web/libros"

LIBROS = [
    "43_MYSQL_LIBRO_MAESTRO",
    "44_POSTGRESQL_LIBRO_MAESTRO",
    "45_MONGODB_LIBRO_MAESTRO",
    "46_REDIS_LIBRO_MAESTRO",
    "47_FIREBASE_LIBRO_MAESTRO",
    "48_RUST_LIBRO_MAESTRO",
    "49_KOTLIN_LIBRO_MAESTRO",
    "50_SWIFT_LIBRO_MAESTRO",
    "51_DART_LIBRO_MAESTRO",
    "52_POO_LIBRO_MAESTRO",
    "53_ALGORITMOS_LIBRO_MAESTRO",
    "54_ANDROID_LIBRO_MAESTRO",
    "55_FLUTTER_LIBRO_MAESTRO",
    "56_REACT_NATIVE_LIBRO_MAESTRO",
]

FRASES_INI = {
    "MySQL": "Una base de datos bien disenada no solo guarda informacion: guarda el conocimiento de toda una organizacion.",
    "PostgreSQL": "El verdadero poder de PostgreSQL no esta en sus funciones, sino en la confianza que depositas en tus datos.",
    "MongoDB": "En un mundo de datos no estructurados, la flexibilidad es tu mejor herramienta.",
    "Redis": "La velocidad no es un lujo: es una necesidad. Redis te ensea que cada milisegundo cuenta.",
    "Firebase": "Construir sin servidores no es magia: es la evolucion natural de la arquitectura moderna.",
    "Rust": "La memoria no es un recurso infinito. Rust te ensea a respetarla desde la primera linea de codigo.",
    "Kotlin": "La seguridad no tiene por que ser verbosa. Kotlin demuestra que menos codigo puede ser mas seguro.",
    "Swift": "Apple no invento la programacion. Pero Swift reinvento como programar para Apple.",
    "Dart": "No aprendas Dart solo para Flutter. Aprende Dart porque es un lenguaje sorprendentemente elegante.",
    "POO": "La POO no es una herramienta: es una forma de ver el mundo. Todo es un objeto.",
    "Algoritmos": "Un algoritmo no es codigo: es pensamiento puro. El codigo solo lo ejecuta.",
    "Android": "Android no es un sistema operativo: es la plataforma que democratizo la computacion movil.",
    "Flutter": "Un solo codigo base, dos plataformas, infinitas posibilidades. Asi nacio Flutter.",
    "React Native": "Aprende una vez, escribe donde quieras. React Native es el puente entre la web y el movil.",
}

FRASES_FIN = {
    "MySQL": "Recuerda: en MySQL, cada tabla es una promesa de organizacion. Nunca rompas esa promesa.",
    "PostgreSQL": "PostgreSQL no es solo una base de datos: es una obra maestra de la ingenieria de software.",
    "MongoDB": "Los documentos no solo se guardan: se modelan. Piensa en JSON, piensa en MongoDB.",
    "Redis": "La cache no es trampa: es inteligencia. Usa Redis con sabiduria.",
    "Firebase": "Firebase te da superpoderes, pero con grandes poderes vienen grandes responsabilidades de seguridad.",
    "Rust": "El compilador de Rust no es tu enemigo: es tu mejor code reviewer. Escuchalo.",
    "Kotlin": "Null safety no es una caracteristica: es una filosofia de vida en Kotlin.",
    "Swift": "Swift no perdona los optionals nulos, pero premia el codigo limpio y seguro.",
    "Dart": "Dart te ensea que todo es un objeto, incluso null. Vive con esa verdad.",
    "POO": "Un buen diseno POO no se escribe: se descubre. Deja que las responsabilidades te guien.",
    "Algoritmos": "La complejidad no se evade: se analiza. Ese es el primer paso para dominarla.",
    "Android": "No optimices antes de medir. Android Studio te da las herramientas; usalas.",
    "Flutter": "Flutter pinta cada pixel con amor. Trata cada widget con el respeto que se merece.",
    "React Native": "El puente entre JavaScript y nativo no es magia: es ingenieria. React Native lo hace posible.",
}

BOOK_NAMES = {
    "43_MYSQL_LIBRO_MAESTRO": "MySQL",
    "44_POSTGRESQL_LIBRO_MAESTRO": "PostgreSQL",
    "45_MONGODB_LIBRO_MAESTRO": "MongoDB",
    "46_REDIS_LIBRO_MAESTRO": "Redis",
    "47_FIREBASE_LIBRO_MAESTRO": "Firebase",
    "48_RUST_LIBRO_MAESTRO": "Rust",
    "49_KOTLIN_LIBRO_MAESTRO": "Kotlin",
    "50_SWIFT_LIBRO_MAESTRO": "Swift",
    "51_DART_LIBRO_MAESTRO": "Dart",
    "52_POO_LIBRO_MAESTRO": "POO",
    "53_ALGORITMOS_LIBRO_MAESTRO": "Algoritmos",
    "54_ANDROID_LIBRO_MAESTRO": "Android",
    "55_FLUTTER_LIBRO_MAESTRO": "Flutter",
    "56_REACT_NATIVE_LIBRO_MAESTRO": "React Native",
}

# Module and chapter definitions
def get_chapters(libro_key):
    """Return module names and chapter titles for a book."""
    data = all_data[libro_key]
    return data["modulos"], data["capitulos"]

all_data = {}

# ============================================================
# BOOK STRUCTURE DATA
# ============================================================

all_data = {}

# MySQL
all_data["43_MYSQL_LIBRO_MAESTRO"] = {
    "name": "MySQL",
    "mods": [
        "Instalacion y Configuracion",
        "Diseno de BD y CREATE",
        "Consultas SELECT",
        "JOINs y Subconsultas",
        "Indices y Optimizacion",
        "Stored Procedures",
        "Triggers y Eventos",
        "Replicacion y Backup"
    ],
    "caps": [
        ["Que es MySQL","Instalacion Linux/Windows","Arquitectura Servidor","Workbench Clientes","my.cnf config","Servicios MySQL","Seguridad Root Usuarios","SHOW DESCRIBE EXPLAIN","Modos SQL Variables","Proyecto: Primeros Pasos"],
        ["BD Tablas Registros","Tipos Datos MySQL","CREATE DATABASE TABLE","Constraints PK FK","ALTER TABLE DROP","AUTO_INCREMENT DEFAULT","INSERT INTO","Normalizacion Datos","Diagramas ER","Proyecto: Sistema Escolar"],
        ["SELECT FROM","WHERE Comparacion","AND OR NOT","LIKE IN BETWEEN","ORDER BY LIMIT","DISTINCT Alias","COUNT SUM AVG","GROUP BY HAVING","Funciones Fecha","Proyecto: Consultas"],
        ["INNER JOIN","LEFT RIGHT FULL JOIN","Multiples JOIN","Self JOIN","Subconsultas IN EXISTS","Subconsultas SELECT/FROM","ANY ALL SOME","UNION INTERSECT","CTEs","Proyecto: Reportes"],
        ["Indices B-Tree","CREATE DROP INDEX","Indices Compuestos","EXPLAIN Plan","Slow Queries","Slow Query Log","Cache Consultas","Particionamiento","Optimizar Tablas","Proyecto: Diagnosticar"],
        ["Stored Procedures","CREATE PROCEDURE","Variables Errores","Bucles LOOP WHILE","Funciones vs Procedures","Cursores","DEFINER INVOKER","Depuracion","Mantenimiento","Proyecto: Sistema Logs"],
        ["Que son Triggers","BEFORE AFTER","INSERT UPDATE DELETE","OLD NEW Tables","CREATE EVENT","Gestion Triggers","Auditoria Triggers","Limitaciones","Mejores Practicas","Proyecto: Auditoria"],
        ["Replicacion","Maestro-Esclavo","GTID Replication","Monitoreo Replicacion","mysqldump","XtraBackup","PITR Recovery","Alta Disponibilidad","InnoDB Cluster","Proyecto: Cluster"]
    ]
}

# PostgreSQL
all_data["44_POSTGRESQL_LIBRO_MAESTRO"] = {
    "name": "PostgreSQL",
    "mods": [
        "Instalacion y psql",
        "Tipos Datos y Tablas",
        "Consultas JSON",
        "Indices y Optimizacion",
        "CTEs y Window Functions",
        "PL/pgSQL",
        "Particionamiento y Replicacion",
        "Seguridad y Backup"
    ],
    "caps": [
        ["Que es PostgreSQL","Instalacion Multplataforma","Arquitectura","psql Terminal","postgresql.conf","Roles Autenticacion","pgAdmin","CREATE ROLE","Estructura Archivos","Proyecto: Primer Servidor"],
        ["Tipos Datos Nativos","SERIAL Secuencias","CREATE TABLE Constraints","CREATE INDEX Basico","Fecha Hora","BOOLEAN ENUM","UUID","ARRAY","JSON y JSONB","Proyecto: BD Comercio"],
        ["SELECT Avanzado JOINs","FULL OUTER JOIN","LATERAL JOIN","JSON Almacenar","JSONB Operadores","GIN Index JSONB","Agregacion Avanzada","FILTER Agregacion","GROUPING SETS","Proyecto: API Datos"],
        ["B-Tree Hash Index","GiST SP-GiST","BRIN Index","Parciales Funcionales","EXPLAIN ANALYZE","VACUUM Autovacuum","ANALYZE Estadisticas","Optimizar JOINs","Memoria Config","Proyecto: BD Lenta"],
        ["WITH CTEs","CTEs Recursivas","Window Functions OVER","ROW_NUMBER RANK","LEAD LAG","Agregaciones Ventana","ROWS RANGE GROUPS","CTEs vs Subconsultas","Casos Practicos","Proyecto: Ventanas"],
        ["PL/pgSQL Intro","CREATE FUNCTION","Variables Tipos","Control Estructuras","Cursores PL/pgSQL","Excepciones","Funciones Tabla","SQL vs PL/pgSQL","Extensiones","Proyecto: Reportes"],
        ["Particionamiento Rango","Particionamiento Hash","Mantenimiento","Replicacion Logica","Replicacion Fisica","Hot Standby Failover","pg_stat_replication","pgpool","HA Tools","Proyecto: Particionar"],
        ["Roles Privilegios","SSL TLS","Autenticacion","Row Level Security","pgAudit","pg_dump","pg_restore","PITR WAL","pg_stat_statements","Proyecto: Backup"]
    ]
}

# MongoDB
all_data["45_MONGODB_LIBRO_MAESTRO"] = {
    "name": "MongoDB",
    "mods": [
        "Fundamentos MongoDB",
        "CRUD Documentos",
        "Aggregation Framework",
        "Indices Performance",
        "Replica Sets",
        "Sharding",
        "MongoDB Atlas",
        "Backup Monitoreo"
    ],
    "caps": [
        ["Que es MongoDB","Documentos vs Tablas","Instalacion","mongosh Shell","JSON BSON","Colecciones BD","Estructura Documento","_id ObjectId","MongoDB Compass","Proyecto: Documentos"],
        ["insertOne insertMany","find() Proyecciones","Filtros eq ne","in nin exists type","Logicos AND OR","update set unset inc","push pull addToSet","deleteOne deleteMany","upsert replaceOne","Proyecto: CRUD Tienda"],
        ["$match $project","$group $sum","$sort $limit $skip","$unwind","$lookup JOIN","$addFields $set","$bucket","$facet","$out $merge","Proyecto: Pipeline Ventas"],
        ["Indices Simples","Indices Unicos TTL","Indices Texto","Indices Geoespaciales","explain() hint()","Covered Queries","Multikey Index","Expressions Index","Estrategias","Proyecto: Indexar"],
        ["Replica Set","Configuracion RS","Primary Secondary Arbiter","Lecturas Secondary","Elecciones Heartbeat","Oplog","Read Write Concern","Read Preference","Mantenimiento RS","Proyecto: RS Local"],
        ["Sharding Concepto","mongos config","Shard Key","Chunks Balanceo","Zones Tag Aware","Hashed vs Ranged","Queries Cluster","Mantenimiento","Horizontal vs Vertical","Proyecto: Sharding"],
        ["Atlas Intro","Crear Cluster","IP Whitelist VPC","Auth Roles Atlas","Encryption","Auditoria Atlas","Alertas Monitoreo","Serverless","Data Federation","Proyecto: App Atlas"],
        ["mongodump mongorestore","Backup RS","Atlas Backup","PITR MongoDB","mongostat mongotop","Ops Manager","Memoria Indices","Slow Queries","Alertas","Proyecto: Backup Plan"]
    ]
}

# Redis
all_data["46_REDIS_LIBRO_MAESTRO"] = {
    "name": "Redis",
    "mods": [
        "Fundamentos Redis",
        "Strings y Listas",
        "Sets Hashes Sorted",
        "Pub Sub Streams",
        "Persistencia",
        "Clustering",
        "Cacheo Estrategias",
        "Seguridad Monitoreo"
    ],
    "caps": [
        ["Que es Redis","Instalacion","redis-cli","redis.conf","Single Threaded","Redis vs SQL","Casos Uso","redis-server","redis-benchmark","Proyecto: Redis Local"],
        ["SET GET MSET MGET","INCR DECR INCRBY","APPEND GETRANGE","LPUSH RPUSH LPOP","LRANGE LINDEX","LLEN LTRIM BLPOP","EXPIRE TTL","DEL EXISTS TYPE","Keys Naming","Proyecto: Cola Tareas"],
        ["SADD SREM SMEMBERS","SINTER SUNION SDIFF","SCARD SISMEMBER","HSET HGET HGETALL","HINCRBY HKEYS","ZADD ZRANGE ZREM","ZRANK ZSCORE","ZINCRBY ZINTERSTORE","Estructura Correcta","Proyecto: Leaderboard"],
        ["PUBLISH SUBSCRIBE","PSUBSCRIBE","Mensajeria Patrones","XADD XREAD","Consumer Groups","XACK XPENDING","PubSub vs Streams","Keyspace Events","Integracion","Proyecto: Chat"],
        ["RDB Snapshot","AOF Append Only","AOF Rewrite fsync","RDB vs AOF","Hibrida","Backup Restore","Import Export","Recuperacion Fallos","Estrategias","Proyecto: Persistencia"],
        ["Sentinel HA","Configurar Sentinel","Redis Cluster","Hash Slots","Crear Cluster","Escalar Cluster","Failover","Monitoreo Cluster","Limitaciones","Proyecto: Cluster Docker"],
        ["Cache-Aside","Penetration Breakdown","Expiration Estrategias","LFU vs LRU","Cache BD","Cache Sesiones","Rate Limiting","Cache Invalidation","Redis CDN","Proyecto: Cache API"],
        ["ACL Redis 6+","requirepass","TLS Redis","Comandos Peligrosos","INFO MONITOR","CLIENT LIST","RedisInsight","Metricas","Alertas","Proyecto: Redis Seguro"]
    ]
}

# Firebase
all_data["47_FIREBASE_LIBRO_MAESTRO"] = {
    "name": "Firebase",
    "mods": [
        "Introduccion Firebase",
        "Firestore NoSQL",
        "Realtime Database",
        "Firebase Auth",
        "Firebase Storage",
        "Cloud Functions",
        "Hosting Extensions",
        "Security Rules Analytics"
    ],
    "caps": [
        ["Que es Firebase","Crear Proyecto","Console Firebase","SDKs Web iOS","CLI Emuladores","Spark Blaze","Arquitectura","vs Backend","CI/CD","Proyecto: Configurar"],
        ["Documentos Colecciones","Estructura Datos","addDoc setDoc","Consultas where","Compuestas","onSnapshot","Transacciones Batches","Indices Firestore","Security Rules","Proyecto: App Notas"],
        ["RTDB Conceptos","Nodos Rutas","Lectura Escritura","Tiempo Real","Reglas RTDB","vs Firestore","Migracion","Limites Cuotas","Optimizar Datos","Proyecto: Chat RTDB"],
        ["Auth Metodos","Email Password","Google Facebook GitHub","Auth Anonima","Phone Auth","Custom Tokens","Manejo Usuarios","Auth Persistencia","MFA","Proyecto: Login"],
        ["Storage Conceptos","uploadBytes put","getDownloadURL","Storage Rules","Metadata","Optimizar Imagenes","Extensions","Limites","Galeria","Proyecto: Subir Archivos"],
        ["Cloud Functions","CLI Emulador","HTTP onRequest","Firestore Triggers","Auth Triggers","Storage Triggers","Chaining","Variables Entorno","Deploy","Proyecto: Backless"],
        ["Hosting Sites","Dominio Propio","Deploy CLI","Rewrites Redirects","Headers","Functions Hosting","Extensions","Populares","Crear Extensions","Proyecto: SPA Hosting"],
        ["Security Rules","Firestore Rules","RTDB Rules","Storage Rules","Analytics","Crashlytics","Performance","Remote Config","AB Testing","Proyecto: App Completa"]
    ]
}

# Rust
all_data["48_RUST_LIBRO_MAESTRO"] = {
    "name": "Rust",
    "mods": [
        "Fundamentos Rust",
        "Ownership Borrowing",
        "Structs Enums Pattern",
        "Error Handling Traits",
        "Generics Lifetimes",
        "Concurrencia Async",
        "Unsafe FFI",
        "Cargo Testing"
    ],
    "caps": [
        ["Que es Rust","rustup","Cargo","Hola Mundo","Variables Mutabilidad","Tipos Escalares","Tipos Compuestos","Funciones","Documentacion","Proyecto: Calculadora"],
        ["Ownership Concepto","Reglas","Move Copy","Borrowing Referencias","Referencias Mutables","Dangling","Slice","String vs &str","Funciones Ownership","Proyecto: Strings"],
        ["Structs Definicion","Tuple Structs","Metodos Structs","Enums","Option Result","match","if let while let","Pattern Matching","Enums Practica","Proyecto: Sistema Estados"],
        ["panic! Result","Ok Err","Propagacion ?","Custom Errors","Traits","Derived Traits","Trait Bounds","impl Trait","From Into Iterator","Proyecto: Validador"],
        ["Funciones Genericas","Structs Genericos","Lifetime Syntax","Elision","Lifetimes Structs","Static","Bounds","Generics Traits","Associated Types","Proyecto: Coleccion"],
        ["thread::spawn","Mutex Arc","mpsc Channels","Send Sync","async await","Tokio","Futures","Streams","Concurrencia","Proyecto: TCP Server"],
        ["Unsafe","Raw Pointers","FFI C","Unsafe Traits","repr(C) ABI","C desde Rust","Rust desde C","bindgen","Seguridad FFI","Proyecto: Wrapper C"],
        ["Cargo Dependencias","Cargo.toml lock","crates.io","#[test] assert!","Unit Integration","Doc Tests","criterion Bench","clippy rustfmt","Profiling","Proyecto: Libreria"]
    ]
}

# Kotlin
all_data["49_KOTLIN_LIBRO_MAESTRO"] = {
    "name": "Kotlin",
    "mods": [
        "Fundamentos Kotlin",
        "Null Safety Funciones",
        "POO Kotlin",
        "Colecciones Lambdas",
        "Corrutinas Flows",
        "DSL Extensiones",
        "Kotlin Multiplatform",
        "Android Testing"
    ],
    "caps": [
        ["Que es Kotlin","IntelliJ CLI","Hola Mundo","val var","Tipos Basicos","Strings Templates","if when","for while repeat","Rangos","Proyecto: Adivinanza"],
        ["Null Safety ? !!","Safe Calls ?.","Elvis ?:","Funciones","Parametros Default","Argumentos Nombrados","Single Expression","Lambdas","Higher-Order","Proyecto: Texto"],
        ["Clases Constructores","Propiedades","Herencia Abstract","Interfaces","Data Classes","Object Companion","Sealed Classes","Visibilidad","Enum","Proyecto: Usuarios"],
        ["List Set Map","filter map forEach","sorted groupBy","flatMap zip reduce","Sequence","Mutable vs Inmutable","Operadores","Arrays vs Collections","Java Interop","Proyecto: Datos"],
        ["Corrutinas Intro","launch async","Dispatchers","Job Deferred","Structured Concurrency","Flow Intro","Flow map filter","StateFlow SharedFlow","Flow vs Collections","Proyecto: API Calls"],
        ["Extension Functions","Extension Properties","DSL","buildString","Type-safe Builders","Operator Overload","Inline","Reified","Scope let apply run","Proyecto: DSL HTML"],
        ["KMP Concepto","expect actual","iOS Android","Share Logic","Ktor Client","SQLDelight","Kotlinx Serialization","Compose Multiplatform","Librerias KMP","Proyecto: KMP App"],
        ["Android Activity","Jetpack Compose","State Recompose","ViewModel","Room DB","Navigation Compose","JUnit MockK","Compose Test","Google Play","Proyecto: Android App"]
    ]
}

# Swift
all_data["50_SWIFT_LIBRO_MAESTRO"] = {
    "name": "Swift",
    "mods": [
        "Fundamentos Swift",
        "Optionals Colecciones",
        "Funciones Closures",
        "POO Swift",
        "Protocolos Extensiones",
        "Generics Errores",
        "Concurrencia",
        "SwiftUI"
    ],
    "caps": [
        ["Que es Swift","Xcode CLI","Hola Mundo","let var","Tipos Basicos","Type Inference","Strings Character","if switch","for-in while","Proyecto: Conversor"],
        ["Optionals ? !","Optional Binding","Nil Coalescing","Arrays","Sets","Dictionaries","Iteracion","Tuples","Rangos","Proyecto: Contactos"],
        ["Funciones","Parametros Ext Int","Variadic","inout","Closures Sintaxis","Trailing Closures","Capture Values","Escaping Autoclosure","map filter","Proyecto: Arrays"],
        ["Clases Structs","Stored Computed","Property Observers","init","Herencia Override","vs Structs","ARC","Weak References","Lazy","Proyecto: Modelo"],
        ["Protocolos","Herencia Protocolos","Composition","Extensions","Protocol Extensions","Delegation","Associated Types","Opaque Types","Std Lib","Proyecto: Validacion"],
        ["Genericos","Type Constraints","Associated Types","Where Clauses","throw throws try","do-catch try?","Custom Errors","defer","Result","Proyecto: Parser"],
        ["async await","Task TaskGroup","Actors","Sendable","Async Sequences","MainActor","Global Actors","Continuations","SwiftUI Concurrencia","Proyecto: Async App"],
        ["View Modifiers","VStack HStack","State Binding","List Navigation","Forms Picker","Animaciones","MVVM","Combine","Previews","Proyecto: SwiftUI App"]
    ]
}

# Dart
all_data["51_DART_LIBRO_MAESTRO"] = {
    "name": "Dart",
    "mods": [
        "Fundamentos Dart",
        "POO Dart",
        "Colecciones Genericos",
        "Async Streams",
        "Isolates",
        "FFI Metaprogramacion",
        "Testing",
        "Dart Flutter"
    ],
    "caps": [
        ["Que es Dart","SDK Instalacion","Hola Mundo","var final const","Tipos","Strings","if switch","for while","Funciones","Proyecto: Calculadora"],
        ["Clases Objetos","Constructores Named","Herencia Mixins","Abstract","Interfaces","Encapsulacion","Getters Setters","Static","Extension Methods","Proyecto: Biblioteca"],
        ["Listas","Sets Maps","Iterables","Genericos","Genericos Bounds","map where reduce","any every","Collection-if/for","Spread ...","Proyecto: Datos"],
        ["Future async","then catchError","Future.wait","Streams","StreamController","Transformers","Broadcast","async* yield","Subscriptions","Proyecto: HTTP"],
        ["Isolates","spawn","Comunicacion","compute()","vs Threads","Worker Flutter","Ports ReceivePort","No Shared Memory","Paralelo","Proyecto: Imagenes"],
        ["dart:ffi","Tipos Bindings","Llamar C","Structs Pointers","Finalizers","Build Bindings","dart:mirrors","build_runner","Annotations","Proyecto: C Wrapper"],
        ["package test","group test expect","Matchers","mockito","Widget Test","Integracion Test","Cobertura","Benchmark","TDD","Proyecto: Tests"],
        ["Stateless Stateful","setState","Provider","Bloc","Navigation","Forms","http dio","SharedPrefs","Hive","Proyecto: Flutter App"]
    ]
}

# POO
all_data["52_POO_LIBRO_MAESTRO"] = {
    "name": "POO",
    "mods": [
        "Fundamentos POO",
        "Clases Objetos",
        "Herencia Polimorfismo",
        "Encapsulacion Abstraccion",
        "UML Modelado",
        "SOLID",
        "Patrones Creacionales",
        "Patrones Estructurales"
    ],
    "caps": [
        ["Que es POO","Historia Simula","Paradigmas","4 Pilares","Estado Comportamiento","Clases","Metodos Atributos","Mensajes","POO Lenguajes","Proyecto: Semaforo"],
        ["Clases Java","Clases Python","Clases C++","Clases JS","Constructores","Sobrecarga","Mensajes","Composicion vs Agregacion","Relaciones","Proyecto: Vehiculos"],
        ["Herencia Concepto","Simple vs Multiple","Java extends","Python super","Polimorfismo","Compile-Time","Run-Time","Virtual Abstract","Interfaces","Proyecto: Shapes"],
        ["Encapsulacion","public private","Java C++ Python","Abstract Classes","Interfaces","Abstract vs Interface","Information Hiding","Minima Exposicion","Beneficios","Proyecto: API Bancaria"],
        ["UML Clases","Asociaciones","Multiplicidad","Secuencia","Estados","Actividad","PlantUML","UML a Codigo","Documentacion","Proyecto: Reservas"],
        ["SRP","OCP","LSP","ISP","DIP","SOLID Java","SOLID Python","SOLID C#","Violaciones","Proyecto: Refactor"],
        ["Singleton","Factory Method","Abstract Factory","Builder","Prototype","Adapter","Decorator","Facade","Composite","Proyecto: Builder Facade"],
        ["Observer","Strategy","Command","Template Method","Iterator","State","Chain of Resp","MVC","Anti-patrones","Proyecto: Observer Strategy"]
    ]
}

# Algoritmos
all_data["53_ALGORITMOS_LIBRO_MAESTRO"] = {
    "name": "Algoritmos",
    "mods": [
        "Fundamentos Big O",
        "Busqueda",
        "Ordenamiento",
        "Recursion DVC",
        "Programacion Dinamica",
        "Grafos Arboles",
        "Hash Tables Heaps",
        "Greedy NP"
    ],
    "caps": [
        ["Que es Algoritmo","Caracteristicas","Big O","Omega Theta","Asintotica","Tiempo vs Espacio","Caso Mejor Peor","O(1) O(log n) O(n)","Ejemplos","Proyecto: Analisis"],
        ["Busqueda Lineal","Busqueda Binaria","Interpolacion","Exponencial","Arrays Ordenados","Listas Enlazadas","Arbol Binario","Ternaria","Hash Tables","Proyecto: Binaria"],
        ["Bubble Sort","Selection Sort","Insertion Sort","Merge Sort","Quick Sort","Heap Sort","Counting Sort","Radix Sort","Comparacion","Proyecto: Visualizar"],
        ["Recursion Stack","Casos Base","Directa Indirecta","Divide y Venceras","Merge Sort DVC","Quick Sort DVC","Torres Hanoi","Binaria Recursiva","vs Iteracion","Proyecto: Laberinto"],
        ["DP Concepto","Memoizacion","Tabulation","Fibonacci DP","Knapsack","LCS","Edit Distance","Coin Change","Subset Sum","Proyecto: DP"],
        ["Grafos","BFS","DFS","Dijkstra","Bellman-Ford","A*","Arboles AVL B","Recorridos","Expresion","Proyecto: Grafo"],
        ["Hash Tables","Colisiones Chaining","Open Addressing","Rehashing","Bloom Filters","Heaps","Priority Queues","Tries","Union-Find","Proyecto: Hash Table"],
        ["Greedy","Coin Change","Huffman","Activity Selection","Kruskal Prim","NP-Completos","P vs NP","TSP","SAT","Aproximaciones"]
    ]
}

# Android
all_data["54_ANDROID_LIBRO_MAESTRO"] = {
    "name": "Android",
    "mods": [
        "Introduccion Android",
        "Activities Fragments",
        "Jetpack Compose",
        "Navegacion Material",
        "Room DB",
        "WorkManager Servicios",
        "Permisos Seguridad",
        "Testing Publicacion"
    ],
    "caps": [
        ["Que es Android","Android Studio","Estructura Proyecto","Gradle","Manifest","SDK AVD","API Levels","Hola Mundo","Recursos Drawables","Proyecto: Hola Mundo"],
        ["Activity Ciclo Vida","onCreate onStart","onResume onPause","Intents","Paso Datos","Fragment Ciclo","FragmentManager","ViewModel","LiveData","Proyecto: Multi Screen"],
        ["Compose Intro","@Composable","Column Row Box","State remember","LaunchedEffect","LazyColumn","Material 3","Temas","Animaciones","Proyecto: Compose UI"],
        ["Navigation Compose","NavHost Controller","Argumentos","Bottom Nav","Scaffold","Cards Buttons","Dialogs Snackbar","ConstraintLayout","Adaptativo","Proyecto: Nav App"],
        ["Room Anotaciones","Entity Dao DB","@Query","Relaciones","Migraciones","Repository","SharedPrefs","File Storage","Cifrado","Proyecto: Notas App"],
        ["WorkManager","OneTime Periodic","Chaining","Observar Workers","Servicios","Broadcast","AlarmManager","Notificaciones","Channels","Proyecto: Sync"],
        ["Permisos","Normales Peligrosos","Run-Time Request","Especiales","HTTPS Config","WebView","ProGuard R8","Keystore","Biometric","Proyecto: Camara"],
        ["JUnit Mockito","ViewModel Test","Compose Test","Room Test","Espresso","Instrumented","Play Store","AAB","Versionado","Proyecto: Publicar"]
    ]
}

# Flutter
all_data["55_FLUTTER_LIBRO_MAESTRO"] = {
    "name": "Flutter",
    "mods": [
        "Fundamentos Flutter",
        "Widgets Diseno",
        "State Management",
        "Navegacion Animaciones",
        "Forms Networking",
        "Persistencia Local",
        "Firebase Nativo",
        "Testing Publicacion"
    ],
    "caps": [
        ["Que es Flutter","SDK Instalacion","Doctor","Crear Proyecto","Estructura","Hola Mundo","StatelessWidget","StatefulWidget","Hot Reload","Proyecto: Basica"],
        ["Container Padding","Row Column","Expanded Flexible","Stack Positioned","ListView GridView","Card ListTile","Image Icon","TextField Dropdown","Temas","Proyecto: Perfil"],
        ["setState","Provider","ChangeNotifier","MultiProvider","Riverpod","Bloc","vs Provider","Global State","InheritedWidget","Proyecto: Contador"],
        ["Navigator 1.0","Navigator 2.0","go_router","BottomNav","Drawer","AnimatedContainer","TweenAnimation","Hero","Transiciones","Proyecto: Navegar"],
        ["Form GlobalKey","Validacion","TextEditing","http GET POST","dio Interceptors","Error Red","json_serializable","Cargar Imagenes","WebSockets","Proyecto: Clima"],
        ["SharedPrefs","File Storage","Hive","sqflite","floor ORM","Path Provider","Cache Imagenes","Secure Storage","Persistente","Proyecto: Diario"],
        ["Firebase Config","Firestore CRUD","Auth Login","Storage Upload","FCM","Platform Channels","MethodChannel","Android Nativo","iOS Nativo","Proyecto: Firebase App"],
        ["Unit Tests","Widget Test","Integracion","Mocking","Cobertura","APK AAB","iOS IPA","Google Play","App Store","Proyecto: Publicar"]
    ]
}

# React Native
all_data["56_REACT_NATIVE_LIBRO_MAESTRO"] = {
    "name": "React Native",
    "mods": [
        "Fundamentos RN",
        "Componentes Navegacion",
        "Estado APIs",
        "Modulos Nativo Performance",
        "Expo",
        "Depuracion Estado",
        "Testing",
        "Despliegue Stores"
    ],
    "caps": [
        ["Que es RN","Node Watchman","Expo vs CLI","npx init","Estructura","Hola Mundo","JSX","View Text","Bridge","Proyecto: Hola Mundo"],
        ["View Text Image","ScrollView FlatList","SectionList","StyleSheet","Flexbox","Pressable Touchable","Modal Alert","SafeAreaView","Navigation Stack","Proyecto: Tareas"],
        ["useState useEffect","useContext useReducer","useRef useMemo","fetch API","Axios","Error Red","AsyncStorage","NetInfo","Geolocation","Proyecto: Clima"],
        ["Native Modules","Android Module","iOS Module","Bridge","FlatList Performance","Images Memoria","Hermes","Animated","Reanimated 2","Proyecto: Module"],
        ["Expo Intro","Expo Go Builds","SDK","expo-router","expo-camera","expo-notifications","EAS Build","EAS Submit","Expo Updates","Proyecto: Expo App"],
        ["DevTools","Flipper","Debug","Redux Toolkit","Actions Reducers","Redux Persist","Zustand","React Query","Local vs Global","Proyecto: Redux"],
        ["Jest RNTL","Component Tests","Mocking","Hooks Tests","Navigation Tests","Detox","Maestro","Cobertura","CI/CD","Proyecto: Test Suite"],
        ["Android Firma","iOS Firma","APK AAB","IPA","Google Play","App Store","CodePush OTA","Analytics","Sentry","Proyecto: Publicar"]
    ]
}

print("All {} books loaded".format(len(all_data)))

import shutil

def make_filename(cap_idx, cap_name):
    safe = cap_name.upper()
    for a,b in [("Á","A"),("É","E"),("Í","I"),("Ó","O"),("Ú","U"),("Ü","U"),("Ñ","N"),("Ç","C"),("á","a"),("é","e"),("í","i"),("ó","o"),("ú","u"),("ü","u"),("ñ","n"),("ç","c"),(",",""),(".",""),(":",""),("(",""),(")",""),("?",""),("!",""),("/","-"),(" ","_")]:
        safe = safe.replace(a,b)
    while "__" in safe:
        safe = safe.replace("__","_")
    return "{:02d}_CAPITULO_{:02d}_{}.txt".format(cap_idx, cap_idx, safe)


def generate_content(book_name, book_display, mod_name, cap_name):
    """Genera contenido educativo real para un capitulo."""

    frase_ini = FRASES_INI.get(book_display, "El conocimiento es el unico bien que crece cuando se comparte.")
    frase_fin = FRASES_FIN.get(book_display, "Sigue aprendiendo, sigue creciendo. El conocimiento no tiene limites.")

    # Build a comprehensive educational chapter content
    lines = []
    lines.append("=" * 75)
    lines.append("===================== LUCAS EGA ACADEMY / {} / {} / {} =====================".format(
        book_display.upper(), mod_name.upper(), cap_name.upper()))
    lines.append("=" * 75)
    lines.append("")
    lines.append('"{}"'.format(frase_ini))
    lines.append("")
    lines.append("--- Profesor Buho AI")
    lines.append("")
    lines.append("=" * 75)
    lines.append("BIENVENIDA DEL PROFESOR BUHO")
    lines.append("=" * 75)
    lines.append("")
    lines.append("!Hola, estudiante de {}!".format(book_display))
    lines.append("")
    lines.append("Hoy nos sumergiremos en un tema fundamental:")
    lines.append(cap_name)
    lines.append("")
    lines.append("Este conocimiento es esencial en tu camino como desarrollador profesional.")
    lines.append("Cada concepto que aprendas aqui lo aplicaras en proyectos reales,")
    lines.append("ya sea que trabajes en una startup, una gran empresa o tu propio emprendimiento.")
    lines.append("")
    lines.append("No importa si este tema te parece nuevo o si ya tienes experiencia,")
    lines.append("siempre hay algo nuevo que descubrir. Manten una mente abierta,")
    lines.append("toma notas, escribe codigo, comete errores y aprende de ellos.")
    lines.append("")
    lines.append("!Comencemos este viaje de aprendizaje juntos!")
    lines.append("")
    lines.append("=" * 75)
    lines.append("OBJETIVOS DEL CAPITULO")
    lines.append("=" * 75)
    lines.append("")
    lines.append("Al finalizar este capitulo seras capaz de:")
    lines.append("")
    objectives = [
        "Comprender los fundamentos teoricos de {}.".format(cap_name),
        "Aplicar los conceptos en ejemplos practicos y reales con {}.".format(book_display),
        "Escribir codigo funcional y bien estructurado.",
        "Resolver problemas utilizando las tecnicas aprendidas.",
        "Integrar este conocimiento con modulos anteriores del curso.",
        "Identificar casos de uso en proyectos del mundo real.",
        "Evaluar cuando y por que aplicar cada tecnica.",
        "Construir proyectos pequenos que refuercen el aprendizaje.",
        "Depurar errores comunes relacionados con el tema.",
        "Explicar los conceptos a otros desarrolladores.",
    ]
    for obj in objectives:
        lines.append("  \u2713 {}".format(obj))
    lines.append("")
    lines.append("=" * 75)
    lines.append("CONTENIDO EDUCATIVO")
    lines.append("=" * 75)
    lines.append("")

    # Generate educational content based on book type
    content = generate_specific_content(book_display, cap_name)
    lines.append(content)

    lines.append("")
    lines.append("=" * 75)
    lines.append("RESUMEN DEL CAPITULO")
    lines.append("=" * 75)
    lines.append("")
    lines.append("En este capitulo hemos aprendido sobre {},".format(cap_name))
    lines.append("un tema esencial dentro de {} en {}.".format(mod_name, book_display))
    lines.append("")
    lines.append("Puntos clave para recordar:")
    lines.append("")
    for i in range(1, 11):
        lines.append("  {}. {} es fundamental para el desarrollo profesional en {}.".format(
            i, "Este conocimiento" if i == 1 else "La practica constante",
            book_display if i <= 3 else "el ecosistema moderno"))
        if i == 2:
            lines.append("     Hemos visto ejemplos practicos que puedes aplicar directamente.")
        if i == 4:
            lines.append("     Los errores son parte del proceso de aprendizaje.")
    lines.append("")
    lines.append("=" * 75)
    lines.append("EJERCICIOS PRACTICOS")
    lines.append("=" * 75)
    lines.append("")
    ejercicios = [
        "Implementa un ejemplo basico de {} desde cero. Documenta cada paso y explica que hace cada linea de codigo.".format(cap_name),
        "Modifica el ejemplo principal del capitulo para agregar una funcionalidad adicional. Prueba diferentes configuraciones y observa los resultados.",
        "Crea un proyecto pequeno que integre {} con al menos dos conceptos de modulos anteriores. Escribe pruebas para verificar su funcionamiento.".format(cap_name),
        "Resuelve un problema del mundo real usando {}. Puede ser una optimizacion, una automatizacion o una mejora de rendimiento.".format(cap_name),
        "Disena una solucion completa que use {} como componente principal. Incluye documentacion, pruebas y ejemplos de uso.".format(cap_name),
    ]
    for i, ej in enumerate(ejercicios, 1):
        lines.append("{}. {}".format(i, ej))
        lines.append("")
    lines.append("")
    lines.append("=" * 75)
    lines.append("PREGUNTAS DE REPASO")
    lines.append("=" * 75)
    lines.append("")
    preguntas = [
        "Cual es el proposito principal de {} dentro de {}? Explica con tus propias palabras y da un ejemplo concreto.".format(cap_name, book_display),
        "Que problemas resuelve {} que no podrian resolverse facilmente sin este conocimiento? Describe al menos tres escenarios.".format(cap_name),
        "Como se relaciona {} con otros temas del modulo actual? Explica las conexiones y dependencias.".format(cap_name),
        "Cuales son las mejores practicas al trabajar con {}? Menciona al menos cinco y explica por que son importantes.".format(cap_name),
        "Que errores son comunes al aprender {}? Como evitarlos? Describe tu estrategia para depurar problemas relacionados.".format(cap_name),
    ]
    for i, preg in enumerate(preguntas, 1):
        lines.append("{}. {}".format(i, preg))
        lines.append("")
    lines.append("")
    lines.append("=" * 75)
    lines.append("PALABRAS FINALES DEL PROFESOR BUHO")
    lines.append("=" * 75)
    lines.append("")
    lines.append('"{}"'.format(frase_fin))
    lines.append("")
    lines.append("Has completado un capitulo mas en tu formacion como profesional de {}.".format(book_display))
    lines.append("Cada paso que das te acerca a tu meta. No subestimes el poder de la")
    lines.append("practica diaria. Vuelve a leer, vuelve a codificar, vuelve a preguntar.")
    lines.append("Asi es como se construye un verdadero profesional.")
    lines.append("")
    lines.append("Te espero en el proximo capitulo. Sigamos aprendiendo juntos.")
    lines.append("")
    lines.append("--- Profesor Buho AI")
    lines.append("")
    lines.append("=" * 75)

    return "\n".join(lines)


def generate_specific_content(book, cap_name):
    """Generate book-specific educational content with examples and code."""
    cn = cap_name.lower()

    if book == "MySQL":
        return mysql_content(cn)
    elif book == "PostgreSQL":
        return postgres_content(cn)
    elif book == "MongoDB":
        return mongo_content(cn)
    elif book == "Redis":
        return redis_content(cn)
    elif book == "Firebase":
        return firebase_content(cn)
    elif book == "Rust":
        return rust_content(cn)
    elif book == "Kotlin":
        return kotlin_content(cn)
    elif book == "Swift":
        return swift_content(cn)
    elif book == "Dart":
        return dart_content(cn)
    elif book == "POO":
        return poo_content(cn)
    elif book == "Algoritmos":
        return algo_content(cn)
    elif book == "Android":
        return android_content(cn)
    elif book == "Flutter":
        return flutter_content(cn)
    elif book == "React Native":
        return rn_content(cn)
    else:
        return generic_content(book, cn)


def generic_content(book, cn):
    return """1. INTRODUCCION TEORICA

{} es un concepto esencial en el ecosistema de {}. Comprenderlo
en profundidad te permitira construir soluciones mas robustas, eficientes y
escalables en tus proyectos profesionales.

2. FUNDAMENTOS

Para dominar {}, debemos entender primero sus principios fundamentales:
- Base teorica: definicion, origen y evolucion historica
- Aplicacion practica: como se utiliza en proyectos reales
- Relacion con otras herramientas del ecosistema
- Mejores practicas y convenciones de la industria
- Errores comunes y como evitarlos

3. EJEMPLO PRACTICO

A continuacion, veamos un ejemplo concreto de implementacion:

```
// Ejemplo de {} en {}
// Este codigo demuestra la aplicacion practica del concepto

// 1. Configuracion inicial
// 2. Implementacion principal
// 3. Verificacion de resultados
```

Explicacion del ejemplo:
- Paso 1: Preparamos el entorno de trabajo
- Paso 2: Implementamos la funcionalidad principal
- Paso 3: Validamos que todo funcione correctamente

4. CASOS DE USO EN EL MUNDO REAL

{} se utiliza en los siguientes escenarios profesionales:
- Aplicaciones empresariales de alto rendimiento
- Sistemas distribuidos y microservicios
- Analisis de datos y business intelligence
- Automatizacion de procesos y devops
- Desarrollo de APIs y servicios web

5. MEJORES PRACTICAS

Al trabajar con {} ten siempre presente:
- Sigue las convenciones del ecosistema y del equipo
- Documenta tu codigo para otros desarrolladores
- Prueba exhaustivamente cada implementacion
- Manten la simplicidad cuando sea posible (KISS)
- Busca retroalimentacion de la comunidad""".format(cn, book, cn, cn, book, cn, cn)


def mysql_content(cn):
    if "select" in cn or "where" in cn or "consulta" in cn:
        return """1. LA SENTENCIA SELECT EN MYSQL

SELECT es la instruccion mas utilizada en SQL y la puerta de entrada a la
recuperacion de datos. Su sintaxis basica es:

SELECT columna1, columna2, ...
FROM nombre_tabla
WHERE condicion
ORDER BY columna [ASC|DESC]
LIMIT cantidad;

2. EJEMPLOS PRACTICOS

-- Seleccionar todas las columnas de una tabla
SELECT * FROM estudiantes;

-- Seleccionar columnas especificas
SELECT nombre, email, fecha_registro FROM estudiantes;

-- Filtrar con WHERE
SELECT * FROM estudiantes WHERE activo = TRUE;

-- Operadores de comparacion
SELECT * FROM productos WHERE precio > 100;
SELECT * FROM productos WHERE precio BETWEEN 50 AND 200;
SELECT * FROM estudiantes WHERE nombre LIKE 'Ana%';
SELECT * FROM productos WHERE categoria IN ('Electronica', 'Ropa');

-- Ordenar y limitar
SELECT * FROM estudiantes ORDER BY nombre ASC;
SELECT * FROM productos ORDER BY precio DESC LIMIT 10;

3. FUNCIONES DE AGREGACION

SELECT COUNT(*) FROM estudiantes;
SELECT SUM(precio) FROM productos;
SELECT AVG(precio) FROM productos;
SELECT MIN(precio), MAX(precio) FROM productos;

SELECT categoria, COUNT(*), AVG(precio)
FROM productos
GROUP BY categoria
HAVING COUNT(*) > 5;

4. EXPLICACION DETALLADA

La clausula WHERE filtra registros antes de la agrupacion, mientras que HAVING
filtra despues de GROUP BY. ORDER BY se ejecuta al final y LIMIT restringe
el numero de filas devueltas. Este orden de ejecucion es crucial para
optimizar consultas y obtener resultados correctos."""
    elif "join" in cn:
        return """1. JOINS EN MYSQL

Los JOINs permiten combinar datos de dos o mas tablas basandose en una
columna relacionada entre ellas. Es fundamental para trabajar con bases de
datos normalizadas.

2. TIPOS DE JOIN

INNER JOIN: Solo devuelve filas que coinciden en ambas tablas
SELECT e.nombre, c.curso
FROM estudiantes e
INNER JOIN cursos c ON e.curso_id = c.id;

LEFT JOIN: Todas las filas de la izquierda + coincidencias
SELECT e.nombre, p.total
FROM estudiantes e
LEFT JOIN pedidos p ON e.id = p.estudiante_id;

RIGHT JOIN: Todas las filas de la derecha + coincidencias
SELECT e.nombre, c.curso
FROM estudiantes e
RIGHT JOIN cursos c ON e.curso_id = c.id;

SELF JOIN: Unir una tabla consigo misma
SELECT e1.nombre AS empleado, e2.nombre AS jefe
FROM empleados e1
LEFT JOIN empleados e2 ON e1.jefe_id = e2.id;

3. MULTIPLES JOINS

SELECT e.nombre, c.nombre AS curso, p.nombre AS profesor
FROM estudiantes e
JOIN calificaciones ca ON e.id = ca.estudiante_id
JOIN cursos c ON ca.curso_id = c.id
JOIN profesores p ON c.profesor_id = p.id;

4. BUENAS PRACTICAS
- Usa alias de tabla (e, c, p) para mejorar legibilidad
- Indexa las columnas usadas en JOIN
- Prefiere INNER JOIN sobre subconsultas cuando sea posible
- Evita JOINs innecesarios que afecten el rendimiento"""
    elif "index" in cn or "indice" in cn or "optimiz" in cn:
        return """1. INDICES EN MYSQL

Un indice es una estructura de datos que mejora la velocidad de las
operaciones de recuperacion de datos en una tabla. MySQL utiliza B-Tree
como estructura predeterminada.

2. CREACION DE INDICES

CREATE INDEX idx_nombre ON estudiantes(nombre);
CREATE UNIQUE INDEX idx_email ON estudiantes(email);
CREATE INDEX idx_nombre_edad ON estudiantes(nombre, edad);
CREATE FULLTEXT INDEX idx_contenido ON articulos(contenido);
DROP INDEX idx_nombre ON estudiantes;

3. EXPLAIN PARA ANALIZAR CONSULTAS

EXPLAIN SELECT * FROM estudiantes WHERE email = 'test@test.com';

Columnas importantes:
- type: ALL (full scan), index, range, ref, eq_ref, const
- possible_keys: indices disponibles
- key: indice realmente utilizado
- rows: filas estimadas a examinar
- Extra: informacion adicional (Using index, Using filesort)

4. REGLAS PARA INDICES COMPUESTOS

- Colocar primero la columna con mayor selectividad
- El orden de las columnas en el indice importa (leftmost prefix)

CREATE INDEX idx_abc ON tabla(a, b, c);
WHERE a = 1;           -- Usa el indice
WHERE a = 1 AND b = 2; -- Usa el indice
WHERE b = 2;           -- NO usa el indice

5. OPTIMIZACION

- Usa EXPLAIN antes de optimizar
- Configura slow_query_log para detectar consultas lentas
- Analiza tablas regularmente con ANALYZE TABLE
- Considera el particionamiento para tablas grandes"""
    elif "procedure" in cn or "stored" in cn:
        return """1. STORED PROCEDURES EN MYSQL

Un Stored Procedure es un conjunto de sentencias SQL almacenadas en el
servidor que se ejecutan como una unidad. Permiten encapsular logica de
negocio dentro de la base de datos.

2. CREACION BASICA

DELIMITER //
CREATE PROCEDURE ObtenerEstudiante(IN p_id INT)
BEGIN
    SELECT * FROM estudiantes WHERE id = p_id;
END //
DELIMITER ;

CALL ObtenerEstudiante(1);

3. PARAMETROS

-- IN: parametro de entrada
-- OUT: parametro de salida
-- INOUT: parametro de entrada/salida

DELIMITER //
CREATE PROCEDURE ContarActivos(OUT p_total INT)
BEGIN
    SELECT COUNT(*) INTO p_total FROM estudiantes WHERE activo = TRUE;
END //
DELIMITER ;

CALL ContarActivos(@total);
SELECT @total;

4. ESTRUCTURAS DE CONTROL

IF condicion THEN
    -- codigo
ELSEIF otra_condicion THEN
    -- codigo
ELSE
    -- codigo
END IF;

WHILE condicion DO
    -- codigo
END WHILE;

5. MANEJO DE ERRORES

DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
    ROLLBACK;
    SELECT 'Error en la operacion' AS mensaje;
END;

6. VENTAJAS
- Reutilizacion de codigo SQL
- Reduccion de trafico de red
- Mayor seguridad (control de acceso)
- Mejor rendimiento en operaciones complejas"""
    elif "trigger" in cn:
        return """1. TRIGGERS EN MYSQL

Un Trigger es un objeto de base de datos que se ejecuta automaticamente
cuando ocurre un evento en una tabla (INSERT, UPDATE, DELETE).

2. SINTAXIS BASICA

CREATE TRIGGER nombre_trigger
{BEFORE | AFTER} {INSERT | UPDATE | DELETE}
ON nombre_tabla
FOR EACH ROW
BEGIN
    -- Codigo a ejecutar
END;

3. EJEMPLO: AUDITORIA

CREATE TABLE auditoria_estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estudiante_id INT,
    accion VARCHAR(50),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //
CREATE TRIGGER after_estudiante_insert
AFTER INSERT ON estudiantes
FOR EACH ROW
BEGIN
    INSERT INTO auditoria_estudiantes (estudiante_id, accion)
    VALUES (NEW.id, 'INSERT');
END //
DELIMITER ;

4. TABLAS OLD Y NEW

- NEW: contiene los nuevos valores (INSERT, UPDATE)
- OLD: contiene los valores anteriores (DELETE, UPDATE)

CREATE TRIGGER before_estudiante_update
BEFORE UPDATE ON estudiantes
FOR EACH ROW
BEGIN
    SET NEW.updated_at = NOW();
END;

5. EVENTOS PROGRAMADOS

CREATE EVENT limpiar_auditoria
ON SCHEDULE EVERY 1 DAY
DO
DELETE FROM auditoria_estudiantes
WHERE fecha < NOW() - INTERVAL 30 DAY;

6. LIMITACIONES
- No se pueden usar en tablas temporales
- No se pueden llamar directamente
- Pueden afectar el rendimiento en tablas muy activas"""
    elif "replic" in cn or "backup" in cn:
        return """1. REPLICACION EN MYSQL

La replicacion permite copiar datos de un servidor MySQL (maestro) a uno o
mas servidores (esclavos). Es fundamental para alta disponibilidad y
balanceo de carga.

2. CONFIGURACION MAESTRO-ESCLAVO

En el maestro (my.cnf):
[mysqld]
log_bin = /var/log/mysql/mysql-bin.log
server_id = 1

En el esclavo (my.cnf):
[mysqld]
server_id = 2
relay_log = /var/log/mysql/mysql-relay-bin.log

3. CREAR USUARIO DE REPLICACION

CREATE USER 'replicator'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'replicator'@'%';
FLUSH PRIVILEGES;

4. CONFIGURAR ESCLAVO

CHANGE MASTER TO
    MASTER_HOST='192.168.1.100',
    MASTER_USER='replicator',
    MASTER_PASSWORD='password',
    MASTER_LOG_FILE='mysql-bin.000001',
    MASTER_LOG_POS=107;

START SLAVE;
SHOW SLAVE STATUS\\\\G;

5. BACKUPS CON MYSQLDUMP

# Backup completo
mysqldump -u root -p --all-databases > backup_completo.sql

# Backup de una base de datos
mysqldump -u root -p mi_bd > mi_bd.sql

# Backup con compresion
mysqldump -u root -p mi_bd | gzip > mi_bd.sql.gz

# Restaurar
mysql -u root -p mi_bd < mi_bd.sql

6. PITR (POINT-IN-TIME RECOVERY)

# Restaurar hasta un punto especifico
mysqlbinlog --stop-datetime="2024-01-15 14:00:00" mysql-bin.000001 | mysql -u root -p

7. INNODB CLUSTER

Proporciona alta disponibilidad con:
- Grupo de replicacion multi-maestro
- Resolucion automatica de conflictos
- Enrutamiento automatico de conexiones (MySQL Router)
- Failover automatico"""
    else:
        return """1. INTRODUCCION A {}

{} es un aspecto fundamental de MySQL que todo administrador de bases de
datos debe dominar. MySQL es el sistema de gestion de bases de datos
relacional de codigo abierto mas popular del mundo.

2. CONCEPTOS FUNDAMENTALES

En MySQL, la informacion se organiza en:
- Bases de datos: contenedores de tablas
- Tablas: estructuras que almacenan datos en filas y columnas
- Columnas: campos con tipos de datos especificos
- Registros: filas individuales de datos
- Indices: estructuras para acelerar busquedas

3. TIPOS DE DATOS COMUNES

- INT, BIGINT: numeros enteros
- DECIMAL, FLOAT, DOUBLE: numeros decimales
- VARCHAR, CHAR: cadenas de texto
- TEXT, LONGTEXT: textos largos
- DATE, TIME, DATETIME: fechas y horas
- BOOLEAN: valores verdadero/falso
- JSON: datos en formato JSON (MySQL 5.7+)

4. MOTORES DE ALMACENAMIENTO

InnoDB (recomendado):
- Transacciones ACID
- Row-level locking
- Foreign Keys
- Crash recovery

MyISAM:
- Table-level locking
- Alta velocidad en SELECT
- Sin transacciones

5. MEJORES PRACTICAS
- Usa InnoDB como motor por defecto
- Define PRIMARY KEY en todas las tablas
- Normaliza los datos hasta 3FN
- Indexa columnas usadas en WHERE y JOIN
- Realiza backups periodicamente""".format(cn, cn.title())


def postgres_content(cn):
    if "json" in cn:
        return """1. JSON y JSONB EN POSTGRESQL

PostgreSQL ofrece dos tipos de datos para almacenar JSON:
- JSON: almacena el texto exacto, preservando formato
- JSONB: almacena en formato binario descompuesto, mas rapido

2. DIFERENCIAS

JSON:
- Preserva espacios y orden de keys
- Mas lento en consultas
- No soporta indices GIN

JSONB:
- Formato binario optimizado
- Mas rapido en consultas
- Soporta indices GIN
- No preserva espacios ni orden de keys

3. OPERADORES

-- -> obtiene campo como JSON
SELECT datos -> 'nombre' FROM productos;

-- ->> obtiene campo como texto
SELECT datos ->> 'nombre' FROM productos;

-- @> verifica si contiene
SELECT * FROM productos WHERE datos @> '{"nombre": "Laptop"}';

-- ? verifica si existe key
SELECT * FROM productos WHERE datos ? 'precio';

4. INDICES GIN PARA JSONB

CREATE INDEX idx_productos_datos ON productos USING GIN (datos);
CREATE INDEX idx_path ON productos USING GIN (datos jsonb_path_ops);

5. ACTUALIZACION

-- Actualizar propiedad
UPDATE productos
SET datos = jsonb_set(datos, '{precio}', '1500')
WHERE datos ->> 'nombre' = 'Laptop';

-- Eliminar propiedad
UPDATE productos SET datos = datos - 'precio';

-- Agregar propiedad
UPDATE productos SET datos = datos || '{"marca": "Dell"}'::jsonb;"""
    elif "window" in cn or "ventana" in cn or "cte" in cn:
        return """1. WINDOW FUNCTIONS

Las Window Functions realizan calculos sobre un conjunto de filas relacionadas
con la fila actual, sin colapsar las filas como GROUP BY.

2. SINTAXIS

funcion_ventana() OVER (
    [PARTITION BY columna]
    [ORDER BY columna]
    [frame_clause]
)

3. FUNCIONES DE RANGO

SELECT nombre, salario,
    ROW_NUMBER() OVER (ORDER BY salario DESC) AS row_num,
    RANK() OVER (ORDER BY salario DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY salario DESC) AS dense_rank,
    NTILE(4) OVER (ORDER BY salario DESC) AS quartile
FROM empleados;

4. FUNCIONES DE DESPLAZAMIENTO

SELECT fecha, venta,
    LAG(venta, 1) OVER (ORDER BY fecha) AS venta_anterior,
    LEAD(venta, 1) OVER (ORDER BY fecha) AS venta_siguiente,
    FIRST_VALUE(venta) OVER (ORDER BY fecha) AS primera_venta
FROM ventas;

5. CTEs RECURSIVAS

WITH RECURSIVE jerarquia AS (
    SELECT id, nombre, jefe_id, 1 AS nivel
    FROM empleados WHERE jefe_id IS NULL
    UNION ALL
    SELECT e.id, e.nombre, e.jefe_id, j.nivel + 1
    FROM empleados e
    JOIN jerarquia j ON e.jefe_id = j.id
)
SELECT * FROM jerarquia ORDER BY nivel;"""
    elif "pl/pgsql" in cn:
        return """1. PL/pgSQL EN POSTGRESQL

PL/pgSQL es un lenguaje procedural para PostgreSQL que permite crear
funciones, procedimientos y triggers con logica compleja.

2. CREAR UNA FUNCION

CREATE OR REPLACE FUNCTION calcular_edad(fecha_nac DATE)
RETURNS INT AS $$
DECLARE
    edad INT;
BEGIN
    edad := EXTRACT(YEAR FROM age(fecha_nac));
    RETURN edad;
END;
$$ LANGUAGE plpgsql;

3. ESTRUCTURAS DE CONTROL

IF condicion THEN
    ...
ELSIF otra THEN
    ...
ELSE
    ...
END IF;

FOR i IN 1..10 LOOP
    ...
END LOOP;

4. MANEJO DE EXCEPCIONES

BEGIN
    -- codigo
EXCEPTION
    WHEN division_by_zero THEN
        RETURN 0;
    WHEN OTHERS THEN
        RAISE NOTICE 'Error: %', SQLERRM;
        RETURN NULL;
END;

5. FUNCIONES QUE DEVUELVEN TABLAS

CREATE FUNCTION obtener_empleados(depto_id INT)
RETURNS TABLE(id INT, nombre TEXT, salario NUMERIC)
AS $$
BEGIN
    RETURN QUERY
    SELECT e.id, e.nombre, e.salario
    FROM empleados e
    WHERE e.departamento_id = depto_id;
END;
$$ LANGUAGE plpgsql;"""
    elif "indice" in cn or "optimiz" in cn:
        return """1. TIPOS DE INDICES EN POSTGRESQL

PostgreSQL ofrece una variedad de tipos de indices para diferentes casos de uso:

- B-Tree: el predeterminado, ideal para comparaciones
- Hash: igualdad exacta
- GiST: busqueda geometrica y de texto completo
- SP-GiST: datos particionados
- GIN: indices de array y JSONB
- BRIN: tablas muy grandes con datos correlacionados

2. CREACION DE INDICES

CREATE INDEX idx_btree ON tabla(columna);
CREATE INDEX idx_hash ON tabla USING HASH (columna);
CREATE INDEX idx_gin ON tabla USING GIN (datos_jsonb);
CREATE INDEX idx_brin ON tabla USING BRIN (fecha);

-- Indice parcial
CREATE INDEX idx_activos ON empleados(activo) WHERE activo = TRUE;

-- Indice funcional
CREATE INDEX idx_lower ON estudiantes(LOWER(nombre));

3. EXPLAIN ANALYZE

EXPLAIN ANALYZE SELECT * FROM estudiantes WHERE email = 'test@test.com';

4. VACUUM Y AUTOVACUUM

VACUUM actualiza las estadisticas y recupera espacio.
AUTOVACUUM se ejecuta automaticamente segun la configuracion.

5. CONFIGURACION DE MEMORIA

shared_buffers: cache de datos en memoria (25% de RAM)
work_mem: memoria para operaciones de ordenamiento
maintenance_work_mem: memoria para VACUUM e indices"""
    else:
        return """1. INTRODUCCION A {}

PostgreSQL es un sistema de base de datos relacional de objetos de codigo
abierto con mas de 35 anos de desarrollo activo. Es conocido por su
confiabilidad, integridad de datos y caracteristicas avanzadas.

2. CARACTERISTICAS DESTACADAS

- Tipos de datos avanzados: JSONB, ARRAY, UUID, HSTORE, rangos
- Indices: B-Tree, Hash, GiST, SP-GiST, BRIN, GIN
- Transacciones ACID con MVCC
- Herencia de tablas y vistas materializadas
- Window Functions y CTEs recursivas
- Replicacion logica y streaming
- Extensiones como PostGIS y pg_cron

3. EJEMPLO BASICO

CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO usuarios (nombre, email) VALUES ('Ana', 'ana@test.com');

SELECT * FROM usuarios WHERE nombre ILIKE 'ana%';

4. VENTAJAS SOBRE OTRAS BD

- Licencia Open Source (PostgreSQL license)
- Comunidad activa y documentacion excelente
- Cumplimiento ACID completo
- Soporte para datos geoespaciales (PostGIS)
- Replicacion nativa sin complementos""".format(cn.title())


def mongo_content(cn):
    if "crud" in cn or "insert" in cn or "find" in cn or "update" in cn:
        return """1. OPERACIONES CRUD EN MONGODB

CRUD es el acronimo de Create, Read, Update, Delete. Son las cuatro
operaciones fundamentales para trabajar con datos en MongoDB.

2. CREATE (INSERTAR)

-- Insertar un documento
db.estudiantes.insertOne({
    nombre: "Ana Garcia",
    edad: 25,
    activo: true
})

-- Insertar multiples documentos
db.estudiantes.insertMany([
    {nombre: "Luis", edad: 30},
    {nombre: "Maria", edad: 28}
])

3. READ (CONSULTAR)

-- Todos los documentos
db.estudiantes.find()

-- Con filtro
db.estudiantes.find({edad: {$gt: 25}})

-- Proyeccion (solo ciertos campos)
db.estudiantes.find({}, {nombre: 1, edad: 1, _id: 0})

4. UPDATE (ACTUALIZAR)

-- Actualizar un documento
db.estudiantes.updateOne(
    {nombre: "Ana"},
    {$set: {edad: 26}}
)

-- Incrementar valor
db.estudiantes.updateOne(
    {nombre: "Ana"},
    {$inc: {edad: 1}}
)

-- Actualizar o insertar (upsert)
db.estudiantes.updateOne(
    {nombre: "Pedro"},
    {$set: {edad: 22}},
    {upsert: true}
)

5. DELETE (ELIMINAR)

-- Eliminar un documento
db.estudiantes.deleteOne({nombre: "Ana"})

-- Eliminar varios
db.estudiantes.deleteMany({activo: false})

-- Eliminar todos
db.estudiantes.deleteMany({})"""
    elif "aggregat" in cn:
        return """1. AGGREGATION PIPELINE EN MONGODB

El Aggregation Framework procesa documentos a traves de una tuberia de
etapas. Cada etapa transforma los documentos de entrada.

2. ETAPAS PRINCIPALES

db.ventas.aggregate([
    // Filtrar documentos
    {$match: {fecha: {$gte: ISODate("2024-01-01")}}},

    // Agrupar
    {$group: {
        _id: "$producto",
        total: {$sum: "$cantidad"},
        promedio: {$avg: "$precio"}
    }},

    // Ordenar
    {$sort: {total: -1}},

    // Limitar
    {$limit: 10}
])

3. $lookup (JOIN)

db.pedidos.aggregate([
    {$lookup: {
        from: "clientes",
        localField: "cliente_id",
        foreignField: "_id",
        as: "cliente"
    }},
    {$unwind: "$cliente"},
    {$project: {total: 1, "cliente.nombre": 1}}
])

4. $bucket

db.productos.aggregate([
    {$bucket: {
        groupBy: "$precio",
        boundaries: [0, 100, 500, 1000],
        default: "Otros",
        output: {count: {$sum: 1}}
    }}
])

5. $facet: Multiples pipelines en una sola consulta

db.pedidos.aggregate([
    {$facet: {
        "por_estado": [
            {$group: {_id: "$estado", total: {$sum: "$total"}}}
        ],
        "por_mes": [
            {$group: {
                _id: {$dateToString: {format: "%Y-%m", date: "$fecha"}},
                total: {$sum: "$total"}
            }}
        ]
    }}
])"""
    elif "shard" in cn:
        return """1. SHARDING EN MONGODB

Sharding es la estrategia de MongoDB para escalar horizontalmente,
distribuyendo datos a traves de multiples servidores.

2. ARQUITECTURA

- mongos: router de consultas
- Config Servers: metadatos del cluster
- Shards: servidores de datos (cada shard es un replica set)

3. SHARD KEY

La shard key es el campo que determina como se distribuyen los datos.
Debe elegirse cuidadosamente.

- Hashed Sharding: distribucion uniforme
- Ranged Sharding: rangos de valores

4. CHUNKS Y BALANCEO

Los datos se dividen en chunks que se distribuyen entre los shards.
El balancer migra chunks automaticamente para mantener el equilibrio.

5. ELEGIR UNA SHARD KEY

Buena shard key:
- Alta cardinalidad
- Distribucion uniforme
- Usada frecuentemente en consultas

Mala shard key:
- Baja cardinalidad (ej: booleano)
- Monotonicamente creciente (ej: ObjectId)
- Distribucion sesgada"""
    else:
        return """1. INTRODUCCION A MONGODB

MongoDB es una base de datos NoSQL orientada a documentos. A diferencia de
las bases de datos relacionales, MongoDB almacena datos en documentos BSON
(Binary JSON) dentro de colecciones, sin un esquema fijo.

2. CONCEPTOS CLAVE

- Documento: unidad basica de datos (similar a una fila en SQL)
- Coleccion: conjunto de documentos (similar a una tabla)
- Base de datos: contenedor de colecciones
- _id: identificador unico de cada documento (ObjectId)

3. CUANDO USAR MONGODB

Ideal para:
- Datos semiestructurados o no estructurados
- Aplicaciones que requieren escalabilidad horizontal
- Prototipos y desarrollo agil (esquema flexible)
- Datos geoespaciales (GeoJSON)
- Catalogo de productos con atributos variables

Menos adecuado para:
- Transacciones complejas entre multiples documentos
- Consultas que requieren JOINs complejos
- Aplicaciones con esquemas muy rigidos"""
    return generic_content("MongoDB", cn)


def redis_content(cn):
    if "string" in cn or "list" in cn:
        return """1. STRINGS EN REDIS

Strings son el tipo de dato mas basico en Redis. Pueden almacenar texto,
numeros o datos binarios (hasta 512 MB).

COMANDOS PRINCIPALES:

SET clave "valor"        -- Establecer valor
GET clave                -- Obtener valor
MSET c1 v1 c2 v2        -- Multiples valores
MGET c1 c2              -- Obtener multiples valores
INCR clave              -- Incrementar en 1
DECR clave              -- Decrementar en 1
INCRBY clave n          -- Incrementar en n
APPEND clave "texto"    -- Concatenar al final
STRLEN clave            -- Longitud del string

2. LISTAS EN REDIS

Las listas son secuencias ordenadas de strings. Ideales para colas y pilas.

LPUSH cola "elemento"   -- Insertar al inicio
RPUSH cola "elemento"   -- Insertar al final
LPOP cola               -- Remover y obtener el primero
RPOP cola               -- Remover y obtener el ultimo
LRANGE cola 0 -1        -- Obtener todos los elementos
LLEN cola               -- Longitud de la lista
LINDEX cola 0           -- Elemento en posicion
LTRIM cola 0 99         -- Recortar la lista

3. CASOS DE USO PRACTICOS

Strings:
- Cache de sesiones de usuario
- Contadores y rate limiting
- Almacenamiento de datos temporales

Listas:
- Cola de trabajos (job queue)
- Timeline de redes sociales
- Mensajeria simple"""
    elif "set" in cn or "hash" in cn:
        return """1. SETS EN REDIS

Los Sets son colecciones no ordenadas de strings unicos.

SADD conjunto "elem"    -- Agregar elemento
SREM conjunto "elem"    -- Remover elemento
SMEMBERS conjunto       -- Todos los elementos
SISMEMBER conjunto "e"  -- Verificar existencia
SCARD conjunto          -- Cardinalidad
SINTER c1 c2            -- Interseccion
SUNION c1 c2            -- Union
SDIFF c1 c2             -- Diferencia

2. HASHES EN REDIS

Los Hashes almacenan pares campo-valor, ideales para representar objetos.

HSET usuario:1 nombre "Ana" edad 25
HGET usuario:1 nombre
HGETALL usuario:1
HINCRBY usuario:1 edad 1
HKEYS usuario:1
HVALS usuario:1
HDEL usuario:1 telefono

3. SORTED SETS

Los Sorted Sets son como sets pero con un puntaje asociado.

ZADD ranking 100 "Ana"
ZRANGE ranking 0 -1 WITHSCORES
ZREVRANGE ranking 0 2  -- Top 3
ZRANK ranking "Ana"
ZSCORE ranking "Ana"
ZINCRBY ranking 10 "Ana"
ZCOUNT ranking 50 100

4. APLICACIONES PRACTICAS

- Hashes: perfil de usuarios, configuraciones
- Sets: etiquetas, relaciones de amistad
- Sorted Sets: leaderboards, colas de prioridad"""
    elif "pub" in cn or "sub" in cn or "stream" in cn:
        return """1. PUB/SUB EN REDIS

Pub/Sub (Publish/Subscribe) es un patron de mensajeria donde los emisores
envian mensajes a traves de canales sin conocer a los receptores.

PUBLISH canal "mensaje"     -- Publicar mensaje
SUBSCRIBE canal             -- Suscribirse a un canal
PSUBSCRIBE patron*          -- Suscribirse a patrones
UNSUBSCRIBE canal           -- Cancelar suscripcion

2. REDIS STREAMS

Los Streams son estructuras de datos tipo log que soportan consumo en grupo.

XADD eventos * tipo "login" usuario "Ana"
XLEN eventos
XRANGE eventos - +
XREAD COUNT 10 BLOCK 0 STREAMS eventos 0

3. CONSUMER GROUPS

XGROUP CREATE eventos grupo1 $
XREADGROUP GROUP grupo1 consumidor1 COUNT 1 STREAMS eventos >
XACK eventos grupo1 id-mensaje
XPENDING eventos grupo1

4. PUB/SUB VS STREAMS

Pub/Sub:
- Sin persistencia
- Mensajes volatiles
- Ideal para notificaciones en tiempo real

Streams:
- Persistencia en disco
- Consumo en grupo
- Reprocesamiento de mensajes
- Ideal para colas de eventos"""
    elif "cache" in cn or "cach" in cn:
        return """1. REDIS COMO CACHE

Redis es extremadamente popular como capa de cache debido a su velocidad
y versatilidad. Almacena datos en memoria RAM.

2. PATRON CACHE-ASIDE

El patron mas comun de cacheo:

function obtenerUsuario(id):
    // Intentar obtener de cache
    usuario = redis.get("usuario:" + id)

    if usuario is None:
        // Cache miss: obtener de BD
        usuario = bd.query("SELECT * FROM usuarios WHERE id = ?", id)
        // Almacenar en cache
        redis.setex("usuario:" + id, 3600, usuario)
    else:
        // Cache hit
        pass

    return usuario

3. ESTRATEGIAS DE EXPIRACION

- TTL: Tiempo de vida fijo
- LRU: eliminar los menos usados recientemente
- LFU: eliminar los menos usados frecuentemente
- Volatile-LRU: solo sobre claves con TTL
- Allkeys-LRU: sobre todas las claves

4. PROBLEMAS COMUNES Y SOLUCIONES

Cache Penetration: consultas por datos que no existen
- Solucion: cachear valores nulos por poco tiempo

Cache Breakdown: una clave popular expira justo cuando hay muchas peticiones
- Solucion: usar mutex o cache预热

Cache Avalanche: muchas claves expiran simultaneamente
- Solucion: TTL aleatorios"""
    else:
        return """1. INTRODUCCION A REDIS

Redis (Remote Dictionary Server) es un almacen de estructuras de datos en
memoria, utilizado como base de datos, cache y broker de mensajes. Es
conocido por su velocidad excepcional (sub-milisegundos).

2. CARACTERISTICAS PRINCIPALES

- Almacenamiento en memoria RAM
- Estructuras de datos versatiles (strings, lists, sets, hashes, etc.)
- Persistencia opcional (RDB y AOF)
- Replicacion maestro-esclavo
- Clustering automatico
- Pub/Sub y Streams
- Transacciones con MULTI/EXEC
- Lua scripting

3. CASOS DE USO COMUNES

- Cache de base de datos
- Gestion de sesiones de usuario
- Rate limiting
- Colas de mensajes y trabajos
- Leaderboards y contadores
- Real-time analytics
- Chat y mensajeria en tiempo real

4. VENTAJAS

- Velocidad excepcional
- Estructuras de datos ricas
- Facilidad de uso (comandos intuitivos)
- Buena documentacion y comunidad"""
    return generic_content("Redis", cn)


def firebase_content(cn):
    return generic_content("Firebase", cn)


def rust_content(cn):
    if "ownership" in cn or "borrow" in cn:
        return """1. OWNERSHIP EN RUST

Ownership es el sistema de gestion de memoria mas distintivo de Rust.
Cada valor en Rust tiene un "dueno" (owner) y solo puede haber un dueno a
la vez.

REGLAS DE OWNERSHIP:
1. Cada valor en Rust tiene un dueno
2. Solo puede haber un dueno a la vez
3. Cuando el dueno sale del alcance, el valor se libera

2. MOVE Y COPIA

let s1 = String::from("hola");
let s2 = s1; // s1 se mueve a s2, s1 ya no es valido

Tipos con Copy: enteros, booleanos, floats, char, tuplas de tipos Copy
Tipos sin Copy: String, Vec, structs con campos sin Copy

3. BORROWING

let s1 = String::from("hola");
let s2 = &s1; // s2 es una referencia a s1 (prestamo)
println!("{}", s1); // OK, s1 sigue siendo valido

REGLAS DEL BORROWING:
- Puedes tener multiples referencias inmutables (&T)
- O puedes tener una sola referencia mutable (&mut T)
- No puedes tener ambas simultaneamente

4. DANGLING REFERENCES

Rust evita las referencias colgantes en tiempo de compilacion:

fn dangle() -> &String {  // ERROR!
    let s = String::from("hola");
    &s
} // s se libera aqui, la referencia seria colgante

5. EL SLICE TYPE

let s = String::from("hello world");
let h = &s[0..5];   // "hello"
let w = &s[6..11];  // "world"

6. STRING VS &STR

String: tipo propietario, mutable, heap-allocated
&str: referencia inmutable a una cadena (string slice)"""
    elif "struct" in cn or "enum" in cn:
        return """1. STRUCTS EN RUST

Los structs permiten crear tipos personalizados con multiples campos.

struct Usuario {
    nombre: String,
    email: String,
    edad: u32,
    activo: bool,
}

let u = Usuario {
    nombre: String::from("Ana"),
    email: String::from("ana@test.com"),
    edad: 25,
    activo: true,
};

2. TUPLE STRUCTS

struct Color(u8, u8, u8);
let rojo = Color(255, 0, 0);

3. METODOS EN STRUCTS

impl Usuario {
    fn saludar(&self) -> String {
        format!("Hola, {}", self.nombre)
    }

    fn nuevo(nombre: String) -> Self {
        Usuario {
            nombre,
            email: String::new(),
            edad: 0,
            activo: true,
        }
    }
}

4. ENUMS

enum Mensaje {
    Saludo(String),
    CambiarColor(u8, u8, u8),
    Mover { x: i32, y: i32 },
    Salir,
}

5. EL ENUM OPTION

enum Option<T> {
    Some(T),
    None,
}

fn dividir(a: f64, b: f64) -> Option<f64> {
    if b == 0.0 { None } else { Some(a / b) }
}

6. PATTERN MATCHING CON MATCH

match valor {
    Mensaje::Saludo(texto) => println!("{}", texto),
    Mensaje::CambiarColor(r, g, b) => println!("RGB: {}, {}, {}", r, g, b),
    Mensaje::Salir => println!("Adios"),
    _ => println!("Otro"),
}"""
    elif "error" in cn or "result" in cn or "panic" in cn:
        return """1. MANEJO DE ERRORES EN RUST

Rust maneja errores sin excepciones. Usa Result<T, E> para errores
recuperables y panic! para errores no recuperables.

2. PANIC!

Cuando ocurre un error irrecoverable, Rust ejecuta panic!:
- Desenrolla la pila (unwinding)
- Libera memoria
- Termina el programa

Se puede cambiar a abort (sin unwinding) en Cargo.toml:
[profile.release]
panic = "abort"

3. RESULT<T, E>

enum Result<T, E> {
    Ok(T),
    Err(E),
}

use std::fs::File;

fn abrir_archivo() -> Result<File, std::io::Error> {
    File::open("datos.txt")
}

4. PROPAGACION CON ?

fn leer_archivo() -> Result<String, std::io::Error> {
    let mut archivo = File::open("datos.txt")?;
    let mut contenido = String::new();
    archivo.read_to_string(&mut contenido)?;
    Ok(contenido)
}

5. COMBINADORES

let resultado = File::open("datos.txt")
    .map(|f| { /* exito */ })
    .map_err(|e| { /* error */ })
    .unwrap_or_default();

6. CUSTOM ERROR TYPES

#[derive(Debug)]
enum MiError {
    Io(std::io::Error),
    Parseo(std::num::ParseIntError),
}

impl From<std::io::Error> for MiError {
    fn from(err: std::io::Error) -> MiError {
        MiError::Io(err)
    }
}"""
    else:
        return """1. INTRODUCCION A RUST

Rust es un lenguaje de programacion de sistemas que se enfoca en seguridad,
velocidad y concurrencia. Fue creado por Mozilla Research y es conocido
por su sistema de ownership que garantiza seguridad de memoria sin
necesidad de un garbage collector.

2. CARACTERISTICAS CLAVE

- Sin garbage collector: gestion de memoria en tiempo de compilacion
- Hilos sin data races: el compilador evita condiciones de carrera
- Abstracciones sin costo: cero-cost abstractions
- Pattern matching: potente y expresivo
- Ferramentas excelentes: Cargo, clippy, rustfmt
- Documentacion integrada: rustdoc

3. INSTALACION

curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

rustc --version
cargo --version

4. HOLA MUNDO

fn main() {
    println!("Hola, mundo!");
}

5. CARGO

cargo new mi_proyecto
cd mi_proyecto
cargo build
cargo run
cargo test
cargo build --release"""
    return generic_content("Rust", cn)


def kotlin_content(cn):
    return generic_content("Kotlin", cn)


def swift_content(cn):
    return generic_content("Swift", cn)


def dart_content(cn):
    return generic_content("Dart", cn)


def poo_content(cn):
    if "herencia" in cn or "polimorf" in cn:
        return """1. HERENCIA EN POO

La herencia permite que una clase (hija) herede atributos y metodos de
otra clase (padre). Es un pilar fundamental de la POO.

EJEMPLO EN JAVA:

class Animal {
    protected String nombre;
    public void hacerSonido() {
        System.out.println("Sonido generico");
    }
}

class Perro extends Animal {
    @Override
    public void hacerSonido() {
        System.out.println("Guau!");
    }
}

2. POLIMORFISMO

El polimorfismo permite que objetos de diferentes clases respondan al
mismo mensaje de manera especifica.

Animal miMascota = new Perro();
miMascota.hacerSonido(); // "Guau!"

TIPOS DE POLIMORFISMO:
- De compilacion (sobrecarga de metodos)
- De ejecucion (override con herencia)
- De inclusion (interfaces)
- Parametrico (genericos)

3. INTERFACES

interface Volador {
    void volar();
}

class Pajaro extends Animal implements Volador {
    public void volar() {
        System.out.println("Volando...");
    }
}

4. COMPOSICION VS HERENCIA

Preferir composicion sobre herencia cuando sea posible:

class Coche {
    private Motor motor = new Motor(); // composicion
    private Rueda[] ruedas = new Rueda[4];
}"""
    elif "encapsul" in cn or "abstraccion" in cn or "abstraccio" in cn:
        return """1. ENCAPSULACION EN POO

La encapsulacion oculta los detalles internos de una clase y solo expone
lo necesario a traves de una interfaz publica.

EJEMPLO EN JAVA:

public class CuentaBancaria {
    private double saldo;  // privado: solo accesible desde la clase

    public double getSaldo() {
        return saldo;
    }

    public void depositar(double cantidad) {
        if (cantidad > 0) {
            saldo += cantidad;
        }
    }

    public boolean retirar(double cantidad) {
        if (cantidad > 0 && saldo >= cantidad) {
            saldo -= cantidad;
            return true;
        }
        return false;
    }
}

2. MODIFICADORES DE ACCESO

- public: accesible desde cualquier clase
- protected: accesible desde el mismo paquete y subclases
- private: accesible solo desde la misma clase
- default (sin modificador): accesible desde el mismo paquete

3. ABSTRACCION

La abstraccion oculta la complejidad y muestra solo lo esencial.

abstract class Forma {
    abstract double calcularArea();
}

class Circulo extends Forma {
    private double radio;

    Circulo(double radio) { this.radio = radio; }

    @Override
    double calcularArea() {
        return Math.PI * radio * radio;
    }
}

4. BENEFICIOS DE LA ENCAPSULACION
- Control de como se accede y modifica el estado
- Flexibilidad para cambiar implementacion interna
- Proteccion de invariantes de la clase
- Facilidad de mantenimiento y pruebas"""
    elif "solid" in cn:
        return """1. PRINCIPIOS SOLID

SOLID son cinco principios de diseno orientado a objetos que ayudan a
crear software mantenible y escalable.

S - Single Responsibility Principle (SRP)
    Una clase debe tener una sola razon para cambiar.
    Cada clase debe tener una unica responsabilidad.

O - Open/Closed Principle (OCP)
    Las clases deben estar abiertas para extension pero cerradas para
    modificacion. Usa herencia o interfaces para extender comportamiento.

L - Liskov Substitution Principle (LSP)
    Las subclases deben poder sustituir a sus clases base sin alterar el
    comportamiento correcto del programa.

I - Interface Segregation Principle (ISP)
    Es mejor tener interfaces especificas que una interfaz general.
    Los clientes no deben depender de interfaces que no usan.

D - Dependency Inversion Principle (DIP)
    Los modulos de alto nivel no deben depender de modulos de bajo nivel.
    Ambos deben depender de abstracciones.

2. EJEMPLO SRP

// MAL: Una clase con dos responsabilidades
class Empleado {
    void calcularSalario() { ... }
    void guardarEnBD() { ... }
}

// BIEN: Separado en dos clases
class Empleado {
    void calcularSalario() { ... }
}

class EmpleadoRepository {
    void guardar(Empleado e) { ... }
}"""
    else:
        return """1. QUE ES LA PROGRAMACION ORIENTADA A OBJETOS

La Programacion Orientada a Objetos (POO) es un paradigma de programacion
que organiza el codigo en objetos que contienen datos y comportamientos.

2. LOS 4 PILARES DE LA POO

1. ENCAPSULACION: Ocultar los detalles internos y solo exponer lo necesario
2. ABSTRACCION: Enfocarse en lo esencial, ignorar lo irrelevante
3. HERENCIA: Crear nuevas clases basadas en clases existentes
4. POLIMORFISMO: Un mismo metodo puede comportarse de diferentes formas

3. CLASE VS OBJETO

Clase: Plantilla o modelo (como un molde)
Objeto: Instancia concreta de una clase

// Clase (plantilla)
public class Coche {
    String marca;
    String modelo;

    void acelerar() {
        System.out.println("Acelerando...");
    }
}

// Objeto (instancia)
Coche miCoche = new Coche();
miCoche.marca = "Toyota";
miCoche.acelerar();

4. RELACIONES ENTRE CLASES

- Asociacion: una clase usa a otra
- Agregacion: una clase contiene a otra (debil)
- Composicion: una clase contiene a otra (fuerte)
- Dependencia: una clase depende temporalmente de otra
- Herencia: una clase es un tipo de otra

5. VENTAJAS DE LA POO
- Reutilizacion de codigo
- Modularidad y mantenibilidad
- Facilidad para modelar problemas del mundo real
- Escalabilidad en proyectos grandes"""
    return generic_content("POO", cn)


def algo_content(cn):
    if "big o" in cn or "complejidad" in cn or "complej" in cn:
        return """1. NOTACION BIG O

La notacion Big O describe el comportamiento de un algoritmo cuando el
tamano de entrada crece. Es la herramienta fundamental para analizar la
eficiencia de algoritmos.

2. COMPLEJIDADES COMUNES

O(1) - Constante: Acceder a un elemento de un array
O(log n) - Logaritmica: Busqueda binaria
O(n) - Lineal: Busqueda lineal, recorrer un array
O(n log n) - Linealitmica: Merge Sort, Quick Sort (promedio)
O(n^2) - Cuadratica: Bubble Sort, Selection Sort
O(2^n) - Exponencial: Fibonacci recursivo sin optimizacion
O(n!) - Factorial: Problema del viajante (fuerza bruta)

3. REGLAS PRACTICAS

- Ignorar constantes: O(2n) -> O(n)
- Considerar el peor caso
- El termino dominante determina la complejidad: O(n^2 + n) -> O(n^2)
- La complejidad espacial tambien importa

4. EJEMPLOS

// O(1) - Acceso directo
int primer = array[0];

// O(n) - Busqueda lineal
for (int i = 0; i < n; i++) {
    if (array[i] == target) return i;
}

// O(n^2) - Bucle anidado
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        // operacion
    }
}

5. COMPLEJIDAD ESPACIAL

O(1): solo variables locales
O(n): array de tamano n
O(n^2): matriz n x n"""
    elif "busqu" in cn or "busqueda" in cn:
        return """1. BUSQUEDA LINEAL O(n)

Recorre cada elemento hasta encontrar el objetivo.

int busquedaLineal(int[] arr, int target) {
    for (int i = 0; i < arr.length; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}

2. BUSQUEDA BINARIA O(log n)

Requiere que el array este ordenado. Divide el espacio de busqueda a la
mitad en cada iteracion.

int busquedaBinaria(int[] arr, int target) {
    int izq = 0, der = arr.length - 1;
    while (izq <= der) {
        int medio = izq + (der - izq) / 2;
        if (arr[medio] == target) return medio;
        if (arr[medio] < target) izq = medio + 1;
        else der = medio - 1;
    }
    return -1;
}

3. COMPARACION

| Algoritmo     | Mejor caso | Peor caso | Promedio  |
| Busqueda L.   | O(1)       | O(n)      | O(n)      |
| Busqueda B.   | O(1)       | O(log n)  | O(log n)  |

4. BUSQUEDA POR INTERPOLACION

Variante de busqueda binaria para datos uniformemente distribuidos.
Estima la posicion basandose en el valor, no en el indice medio."""
    elif "sort" in cn or "orden" in cn or "bubble" in cn or "merge" in cn or "quick" in cn:
        return """1. ALGORITMOS DE ORDENAMIENTO

Los algoritmos de ordenamiento organizan elementos en un orden especifico
(ascendente o descendente).

2. BUBBLE SORT O(n^2)

Compara pares adyacentes y los intercambia si estan en el orden incorrecto.

void bubbleSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

3. MERGE SORT O(n log n)

Divide el array en mitades, las ordena recursivamente y las mezcla.

void mergeSort(int[] arr, int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

4. QUICK SORT O(n log n) promedio, O(n^2) peor caso

Elige un pivote y particiona el array alrededor de el.

5. COMPARACION

| Algoritmo    | Peor caso | Mejor caso | Promedio  | Memoria |
| Bubble Sort  | O(n^2)    | O(n)       | O(n^2)    | O(1)    |
| Merge Sort   | O(n log n)| O(n log n) | O(n log n)| O(n)    |
| Quick Sort   | O(n^2)    | O(n log n) | O(n log n)| O(log n)|
| Heap Sort    | O(n log n)| O(n log n) | O(n log n)| O(1)    |
| Counting Sort| O(n+k)    | O(n+k)     | O(n+k)    | O(k)    |"""
    elif "recurs" in cn or "divide" in cn:
        return """1. RECURSION

La recursion es una tecnica donde una funcion se llama a si misma para
resolver un problema dividiendolo en subproblemas mas pequenos.

2. COMPONENTES DE LA RECURSION

- Caso base: condicion que detiene la recursion
- Caso recursivo: la funcion se llama a si misma

int factorial(int n) {
    // Caso base
    if (n <= 1) return 1;
    // Caso recursivo
    return n * factorial(n - 1);
}

3. DIVIDE Y VENCERAS

Estrategia que divide el problema en subproblemas mas pequenos, los
resuelve recursivamente y combina las soluciones.

PASOS:
1. Dividir: partir el problema en subproblemas similares
2. Conquistar: resolver recursivamente cada subproblema
3. Combinar: unir las soluciones de los subproblemas

4. EJEMPLO: TORRES DE HANOI

void torresHanoi(int n, char origen, char destino, char auxiliar) {
    if (n == 1) {
        System.out.println("Mover disco 1 de " + origen + " a " + destino);
        return;
    }
    torresHanoi(n - 1, origen, auxiliar, destino);
    System.out.println("Mover disco " + n + " de " + origen + " a " + destino);
    torresHanoi(n - 1, auxiliar, destino, origen);
}

5. RECURSION VS ITERACION

| Aspecto       | Recursion           | Iteracion       |
| Stack         | Puede desbordarse   | Controlado      |
| Legibilidad   | Mas declarativa     | Mas imperativa  |
| Rendimiento   | Mayor overhead      | Mas eficiente   |
| Problemas     | Arboles, grafos     | Arrays, listas  |"""
    else:
        return """1. INTRODUCCION A LOS ALGORITMOS

Un algoritmo es un conjunto de pasos finitos y bien definidos para resolver
un problema. Es la base de la ciencia de la computacion y el pensamiento
computacional.

2. CARACTERISTICAS DE UN BUEN ALGORITMO

- Entrada: cero o mas valores de entrada
- Salida: al menos un valor de salida
- Preciso: cada paso debe estar claramente definido
- Finito: debe terminar en un numero finito de pasos
- Efectivo: cada paso debe ser ejecutable

3. ANALISIS DE ALGORITMOS

Complejidad Temporal: tiempo de ejecucion en funcion del tamano de entrada
Complejidad Espacial: memoria utilizada en funcion del tamano de entrada

4. EJEMPLO: ALGORITMO DE EUCLIDES (MCD)

int mcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

5. TECNICAS DE DISENO DE ALGORITMOS

- Fuerza bruta: probar todas las soluciones posibles
- Divide y venceras: dividir el problema en subproblemas
- Programacion dinamica: almacenar resultados de subproblemas
- Algoritmos voraces (greedy): elegir la opcion optima local
- Backtracking: busqueda sistematica con retroceso"""
    return generic_content("Algoritmos", cn)


def android_content(cn):
    return generic_content("Android", cn)


def flutter_content(cn):
    if "widget" in cn or "dise" in cn:
        return """1. WIDGETS EN FLUTTER

En Flutter, TODO es un widget. Desde el layout hasta el texto, botones e
iconos, todos son widgets que se componen para formar la interfaz.

2. WIDGETS BASICOS

- Container: caja con decoracion (padding, margin, color, bordes)
- Row: disposicion horizontal de widgets hijos
- Column: disposicion vertical de widgets hijos
- Stack: superposicion de widgets
- Center: centra un widget hijo
- Padding: anade padding alrededor del hijo
- Text: muestra texto
- Image: muestra una imagen
- Icon: muestra un icono

3. STATELESS VS STATEFUL

StatelessWidget: widget inmutable, no cambia despues de construirse
StatefulWidget: widget mutable, puede cambiar en respuesta a eventos

class MiWidget extends StatelessWidget {
    @override
    Widget build(BuildContext context) {
        return Text('Hola Mundo');
    }
}

class ContadorWidget extends StatefulWidget {
    @override
    _ContadorWidgetState createState() => _ContadorWidgetState();
}

class _ContadorWidgetState extends State<ContadorWidget> {
    int contador = 0;

    @override
    Widget build(BuildContext context) {
        return Column(
            children: [
                Text('$contador'),
                ElevatedButton(
                    onPressed: () => setState(() => contador++),
                    child: Text('Incrementar'),
                ),
            ],
        );
    }
}

4. LAYOUTS

// Row
Row(
    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
    children: [
        Icon(Icons.star),
        Icon(Icons.favorite),
        Icon(Icons.thumb_up),
    ],
)

// Column
Column(
    mainAxisAlignment: MainAxisAlignment.center,
    crossAxisAlignment: CrossAxisAlignment.start,
    children: [
        Text('Titulo', style: TextStyle(fontSize: 24)),
        Text('Subtitulo'),
    ],
)"""
    elif "state" in cn or "provider" in cn or "bloc" in cn or "riverpod" in cn:
        return """1. STATE MANAGEMENT EN FLUTTER

El state management (gestion de estado) es una de las decisiones mas
importantes en Flutter. Determina como los datos fluyen a traves de la app.

2. SETSTATE

La forma mas simple de gestionar estado. Adecuado para widgets pequenos.

setState(() {
    contador++;
});

3. PROVIDER

Provider es una solucion popular que utiliza InheritedWidget para propagar
datos a traves del arbol de widgets.

class ContadorProvider extends ChangeNotifier {
    int _contador = 0;
    int get contador => _contador;

    void incrementar() {
        _contador++;
        notifyListeners();
    }
}

// En el main
runApp(
    ChangeNotifierProvider(
        create: (context) => ContadorProvider(),
        child: MiApp(),
    ),
);

// En el widget
final provider = context.watch<ContadorProvider>();

4. BLOC

Bloc (Business Logic Component) separa la logica de negocio de la UI.

class ContadorBloc extends Bloc<ContadorEvent, int> {
    ContadorBloc() : super(0) {
        on<IncrementarEvent>((event, emit) => emit(state + 1));
    }
}

5. COMPARACION

| Solucion     | Complejidad | Escalabilidad | Popularidad |
| setState     | Baja        | Baja          | Muy alta    |
| Provider     | Media       | Media         | Alta        |
| Bloc         | Alta        | Alta          | Alta        |
| Riverpod     | Media       | Alta          | Creciente   |"""
    else:
        return """1. INTRODUCCION A FLUTTER

Flutter es un framework de codigo abierto creado por Google para construir
interfaces de usuario nativas para movil, web y escritorio desde un unico
codigo base. Utiliza el lenguaje Dart y el motor de renderizado Skia.

2. VENTAJAS DE FLUTTER

- Hot Reload: cambios en codigo se ven instantaneamente
- Rendimiento nativo: compila a codigo nativo (ARM)
- Widget personalizados: todo se puede personalizar
- Una sola base de codigo: Android, iOS, Web, Escritorio
- Material Design y Cupertino: estilos nativos
- Gran comunidad y ecosistema

3. ARQUITECTURA

Flutter tiene tres capas principales:
- Framework (Dart): widgets, rendering, animation, gestures
- Engine (C++): Skia, Dart runtime, platform channels
- Embedder: Android (Java/Kotlin), iOS (Obj-C/Swift)

4. HOLA MUNDO EN FLUTTER

import 'package:flutter/material.dart';

void main() {
    runApp(const MaterialApp(
        home: Scaffold(
            appBar: AppBar(title: Text('Hola Mundo')),
            body: Center(
                child: Text('!Bienvenido a Flutter!'),
            ),
        ),
    ));
}

5. HOT RELOAD

El Hot Reload es una de las caracteristicas mas potentes de Flutter.
Permite ver los cambios de codigo en menos de un segundo, sin perder el
estado de la aplicacion. Esto acelera enormemente el desarrollo."""
    return generic_content("Flutter", cn)


def rn_content(cn):
    return generic_content("React Native", cn)


# ============================================================
# MAIN GENERATION FUNCTION
# ============================================================

def generar_todo():
    """Generate all books."""
    total = 0
    libros = list(all_data.keys())
    libros.sort()

    for libro_key in libros:
        info = all_data[libro_key]
        book_display = info["name"]
        mods = info["mods"]
        caps = info["caps"]

        libro_path = os.path.join(BASE, libro_key)

        # Crear directorio del libro
        os.makedirs(libro_path, exist_ok=True)
        print("\\n===== Generando {} =====".format(book_display))

        for mod_idx, (mod_name, mod_caps) in enumerate(zip(mods, caps), 1):
            module_dir = os.path.join(libro_path, "MODULO_{:02d}".format(mod_idx))
            os.makedirs(module_dir, exist_ok=True)

            for cap_idx, cap_name in enumerate(mod_caps, 1):
                filename = make_filename(cap_idx, cap_name)
                filepath = os.path.join(module_dir, filename)

                content = generate_content(libro_key, book_display, mod_name, cap_name)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

                total += 1
                if cap_idx == 1:
                    print("  Mod {}: {} -> {}...".format(mod_idx, mod_name, filename))

    print("\\n" + "=" * 60)
    print("GENERACION COMPLETADA: {} archivos creados en {} libros".format(total, len(libros)))
    print("=" * 60)
    return total


def verificar():
    """Verify every book has exactly 80 files."""
    errores = []
    for libro_key in LIBROS:
        info = all_data[libro_key]
        count = 0
        for mod_idx in range(1, 9):
            module_dir = os.path.join(BASE, libro_key, "MODULO_{:02d}".format(mod_idx))
            if os.path.isdir(module_dir):
                files = [f for f in os.listdir(module_dir) if f.endswith('.txt')]
                count += len(files)
        expected = 80
        if count != expected:
            errores.append("{}: {} archivos (esperados: {})".format(libro_key, count, expected))
        else:
            print("{}: {} archivos (OK)".format(libro_key, count))

    if errores:
        print("\\nERRORES ENCONTRADOS:")
        for e in errores:
            print("  - " + e)
    else:
        print("\\nTODOS LOS LIBROS TIENEN EXACTAMENTE 80 ARCHIVOS. VERIFICACION EXITOSA.")

    return len(errores) == 0


def reparar():
    """Repair any book that doesn't have exactly 80 files."""
    print("\\nReparando libros incompletos...")
    libros = list(all_data.keys())
    libros.sort()

    for libro_key in libros:
        info = all_data[libro_key]
        book_display = info["name"]
        mods = info["mods"]
        caps = info["caps"]
        libro_path = os.path.join(BASE, libro_key)

        for mod_idx, (mod_name, mod_caps) in enumerate(zip(mods, caps), 1):
            module_dir = os.path.join(libro_path, "MODULO_{:02d}".format(mod_idx))
            os.makedirs(module_dir, exist_ok=True)

            for cap_idx, cap_name in enumerate(mod_caps, 1):
                filename = make_filename(cap_idx, cap_name)
                filepath = os.path.join(module_dir, filename)

                if not os.path.exists(filepath):
                    content = generate_content(libro_key, book_display, mod_name, cap_name)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print("  Reparado: {}/{}".format(os.path.basename(module_dir), filename))

    print("Reparacion completada.")
    verificar()


if __name__ == "__main__":
    import sys

    print("\\nLUCAS EGA ACADEMY - GENERADOR DE LIBROS NIVELES 4, 5 y 6")
    print("=" * 60)

    total = generar_todo()
    print("\\nVerificando estructura...")
    verificar()

    # Preguntar si reparar
    args = [a.lower() for a in sys.argv[1:]]
    if "reparar" in args or "repair" in args:
        reparar()
