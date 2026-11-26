from  core.database import db_connection
from sqlalchemy import text


db = db_connection.get_db()
Base = db_connection.Base

try:
    result=db.execute(text("SELECT * FROM usuarios"))
    print(result.all())
    Base
except:
    print("Error")