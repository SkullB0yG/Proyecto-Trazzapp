# Descripcion de la carpeta


Representa exactamente las tablas (o colecciones) de tu base de datos mediante un ORM como SQLAlchemy o SQLModel:
- Define columnas, tipos de datos (Integer, String, DateTime), claves primarias (primary_key=True), índices y relaciones (relationship, ForeignKey).
- Diferencia clave frente a schemas/:
	- models/ habla con la base de datos (puede tener hashed_password, deleted_at, claves internas).
	- schemas/ habla con el cliente HTTP / JSON (decide qué campos entran y cuáles salen en la respuesta).
