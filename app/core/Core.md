# Descripcion de la carpeta


Es el soporte técnico compartido por todas las capas. No pertenece a ningún recurso específico (como usuarios o productos), sino a todo el proyecto:
- config.py: Lee variables de entorno (.env) usando pydantic-settings (URL de la base de datos, claves secretas JWT, modo debug, orígenes CORS).
- database.py: Crea el motor de conexión (create_engine), la fábrica de sesiones (SessionLocal) y la dependencia get_db() que se inyecta en los endpoints.
- security.py (opcional): Funciones globales para hashear contraseñas (bcrypt) o generar y validar tokens JWT.
- exceptions.py (opcional): Excepciones personalizadas y manejadores globales de errores.
