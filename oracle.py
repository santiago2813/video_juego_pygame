import cx_Oracle


conexion = cx_Oracle.connect(dsn="localhost/xe",
                                 user="PYTHONTKINTER",
                                 password="1qazxsw2",
                                 )
cursor = conexion.cursor()
cursor.execute= ("insert into articulos(descripcion, precio) values (%s,%s)")
resultado = cursor.fetchall()
print(resultado)

conexion.close()

