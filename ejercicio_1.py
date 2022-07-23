import sqlite3

conn = sqlite3.connect('alumnos.db')
cursor = conn.cursor()
try:
    cursor.execute("""CREATE TABLE alumnos(
                        id INT PRIMARY KEY AUTOINCREMENT, 
                        nombre TEXT, 
                        apellido TEXT)""")
except sqlite3.OperationalError:
    print('La tabla alumnos ya existe')

cursor.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?, ?)", ("Max", "Power"))
cursor.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?, ?)", ("Esteban", "Quito"))
cursor.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?, ?)", ("Dolores", "Fuertes de Cabeza"))
cursor.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?, ?)", ("Elsa", "Bor del Encuentro"))
cursor.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?, ?)", ("Aquiles", "Bailo"))
cursor.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?, ?)", ("Pepe", "Botella"))
cursor.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?, ?)", ("James", "Saborido"))
cursor.execute("INSERT INTO alumnos(nombre, apellido) VALUES(?, ?)", ("Alex", "Unvago"))

conn.commit()

row = cursor.execute("SELECT nombre, apellido FROM alumnos WHERE apellido=?", ("Power",)).fetchone()

if row != None:
    print(row)
else:
    print("No existe un alumno con el apellido ingresado")

cursor.close()
conn.close()