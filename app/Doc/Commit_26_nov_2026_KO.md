# Commit inicial de la rama de desarrollo

**Contenido** :  integracion de conexion a la base de datos en la ruta `core\database.py`
___
*Descripcion:* En esta parte realice la implementacion de la conexion a la base de datos por medio de **sqlalchemy** y **settingdb** para las variables de entorno adicionalmente corregi un bug del modulo setting ya que al realizar el "mapeo de las variables de entorno agrege omiti borrar una linea que decia `DEBUG:bool` ubicada en la linea #11. 

Para usar esta nueva implementacion lo que se debe realizar es importar **from  core.database import db_connection** esto nos data 

## Keneth Ojeda