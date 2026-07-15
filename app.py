from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="Veterinaria",
        user="postgres",
        password="74817738"
    )

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/registrar_dueno", methods=["GET", "POST"])
def registrar_dueno():
    
    if request.method == "POST":

        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        direccion = request.form["direccion"]

        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO duenos(nombre, telefono, direccion)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql,(nombre, telefono, direccion))
        conexion.commit()

        cursor.close()
        conexion.close()

        return "Dueño registrado correctamente"
    
    return render_template("registrar_dueno.html")


    
@app.route("/registrar_mascota", methods=["GET", "POST"])
def registrar_mascota():

    if request.method == "POST":

        nombre = request.form["nombre"]
        edad = request.form["edad"]
        raza = request.form["raza"]
        id_dueno = request.form["id_dueno"]

        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO mascotas(nombre, edad, raza, id_dueno)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (nombre, edad, raza, id_dueno))
        conexion.commit()

        cursor.close()
        conexion.close()

        return "Mascota registrada correctamente"
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT id_dueno, nombre FROM duenos")

    duenos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("registrar_mascota.html", duenos=duenos)

        

@app.route("/registrar_veterinario", methods=["GET", "POST"])
def registrar_veterinario():

    if request.method == "POST":

        nombre = request.form["nombre"]
        especialidad = request.form["especialidad"]

        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO veterinarios(nombre, especialidad)
        VALUES (%s, %s)
        """

        cursor.execute(sql, (nombre, especialidad))
        conexion.commit()

        cursor.close()
        conexion.close()

        return "Veterinario registrado correctamente"

    return render_template("registrar_veterinario.html")

@app.route("/registrar_cita", methods=["GET", "POST"])
def registrar_cita():

    if request.method == "POST":

        fecha = request.form["fecha"]
        hora = request.form["hora"]
        motivo = request.form["motivo"]
        id_mascota = request.form["id_mascota"]
        id_veterinario = request.form["id_veterinario"]

        conexion = conectar()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO citas(fecha, hora, motivo, id_mascota, id_veterinario)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (fecha, hora, motivo, id_mascota, id_veterinario))
        conexion.commit()

        cursor.close()
        conexion.close()

        return "Cita registrada correctamente"
    
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT id_mascota, nombre FROM mascotas")
    mascotas = cursor.fetchall()

    cursor.execute("SELECT id_veterinario, nombre FROM veterinarios")
    veterinarios = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template(
    "registrar_cita.html",
    mascotas=mascotas,
    veterinarios=veterinarios
   )

    return render_template("registrar_cita.html")


@app.route("/mostrar_duenos")
def mostrar_duenos():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM duenos")

    duenos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("mostrar_duenos.html", duenos=duenos)

@app.route("/mostrar_mascotas")
def mostrar_mascotas():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT
         m.id_mascota,
         m.nombre,
         m.edad,
         m.raza,
         d.nombre
    FROM mascotas m
    INNER JOIN duenos d
    ON m.id_dueno = d.id_dueno
    """)

    mascotas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("mostrar_mascotas.html", mascotas=mascotas)

@app.route("/mostrar_veterinarios")
def mostrar_veterinarios():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM veterinarios")

    veterinarios = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("mostrar_veterinarios.html", veterinarios=veterinarios)

@app.route("/mostrar_citas")
def mostrar_citas():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    SELECT
        c.id_cita,
        c.fecha,            
        c.hora,
        c.motivo,
        m.nombre,
        v.nombre
    FROM citas c
    INNER JOIN mascotas m
    ON c.id_mascota = m.id_mascota
    INNER JOIN veterinarios v
    ON c.id_veterinario = v.id_veterinario
    """)                      

    citas = cursor.fetchall()
    print(citas)

    cursor.close()
    conexion.close()

    return render_template("mostrar_citas.html", citas=citas)


if __name__ == "__main__":
    app.run(debug=True) 
    


 

