from pydantic_settings import BaseSettings, SettingsConfigDict


class Env_db(BaseSettings):
    # Se define los nombres exactos de variable que ya estan en el .env con su tipo de dato
    USER_DB:str
    PASSWORD_DB:str
    HOST_DB:str
    NAME_DB:str
    PORT_DB:str

    # Esto le dice a pydantic donde buscar el archivo
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

   
settingsdb = Env_db() #type: ignore

