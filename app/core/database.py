from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settingsdb


class ConnectionDB:
    USER_DB=settingsdb.USER_DB
    PASSWORD_DB=settingsdb.PASSWORD_DB
    HOST_DB=settingsdb.HOST_DB
    PORT_DB=settingsdb.PORT_DB
    NAME_DB=settingsdb.NAME_DB

    DATABASE_URL=(
        f"postgresql+psycopg://{USER_DB}:{PASSWORD_DB}"
        f"@{HOST_DB}:{PORT_DB}/{NAME_DB}"
    )

    ENGINE=create_engine(DATABASE_URL)

    SessionLocal = sessionmaker(bind=ENGINE)


    def get_db(self):
        #Permite  hacer el CRUD
        db=self.SessionLocal()

        try:
            yield db 
        finally:
            db.close()



db_connection=ConnectionDB()



