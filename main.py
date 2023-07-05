import psycopg2


connection = psycopg2.connect(
    host = "localhost",
    user= "postgres",
    password="gis12345",
    database="postgres",
    port="5432"

)
connection.autocommit = True

def crearTabla():
    cursor = connection.cursor()
    query = "CREATE TABLE usuario(nombre varchar(30), correo varchar(30), telefono numeric(7))"
    try:
        cursor.execute(query)
    except:
        print("La tabla usuario ya existe")
    cursor.close()
def insertarDatos(nombre, correo, telefono):
    cursor = connection.cursor()
    query = f"""INSERT INTO usuario (nombre, correo, telefono) values ('{nombre}','{correo}', '{telefono}')"""
    cursor.execute(query)
    cursor.close()
def actualizarDato():
    cursor = connection.cursor()
    query = f"""UPDATE usuario set nombre= 'Felipe' where nombre= 'Andres' """
    cursor.execute(query)
    cursor.close()
def eliminarTabla():
    cursor = connection.cursor()
    query = "DROP TABLE usuario";
    cursor.execute(query)
    cursor.close()

#crearTabla()
insertarDatos('fabian','fabian@gmail.com', 456123)
#eliminarTabla()
#actualizarDato()
    

