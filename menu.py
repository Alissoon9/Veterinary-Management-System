import psycopg2

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="Veterinaria",
        user="postgres",
        password="74817738"
    )

def registrar_dueno():
    nombre = input("nombre: ")
    telefono = input("telefono: ")
    direccion = input("direccion: ")

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    INSERT INTO duenos (nombre, telefono, direccion)
    VALUES (%s, %s, %s)
    """

    cursor.execute(sql, (nombre, telefono, direccion))
    conexion.commit()

    print("dueno registrado correctamente")

    cursor.close()
    conexion.close()


def registrar_mascota():
    nombre = input("nombre de la mascota: ")
    edad = input("edad: ")
    raza = input("raza: ")
    id_dueno = int(input("id del dueno: "))

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    INSERT INTO mascotas(nombre, edad, raza, id_dueno)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (nombre, edad, raza, id_dueno))
    conexion.commit()

    print("mascota registrada correctamente")

    cursor.close()
    conexion.close()


def registrar_veterinarios():
    nombre = input("nombre: ")
    especialidad = input("especialidad: ")

    conexion = conectar()
    cursor = conexion.cursor()

    
    sql = """
    INSERT INTO veterinarios(nombre, especialidad)
    VALUES (%s, %s)
    """

    cursor.execute(sql, (nombre, especialidad))
    conexion.commit()

    print("veterinario registrado correctamente")

    cursor.close()
    conexion.close()


    
def registrar_cita():
    fecha = input("fecha: ")
    hora = input("hora (HH:MM): ")
    motivo = input("motivo: ")
    id_mascota= int(input("id de la mascota: "))
    id_veterinario = int(input("id del veterinario: "))

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    INSERT INTO citas(fecha, hora, motivo, id_mascota, id_veterinario)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(sql, (fecha, hora, motivo, id_mascota, id_veterinario))
    conexion.commit()

    print("Cita registrada correctamente")
    
    cursor.close()
    conexion.close()

def mostrar_duenos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM duenos")

    for dueno in cursor.fetchall():
        print("----------------------------------")
        print(f"ID: {dueno[0]}")
        print(f"nombre: {dueno[1]}")
        print(f"telefono: {dueno[2]}")
        print(f"direccion: {dueno[3]}")

    cursor.close()
    conexion.close()


def mostrar_citas():
    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
    SELECT
        mascotas.nombre,
        duenos.nombre,
        veterinarios.nombre,
        citas.fecha,
        citas.hora,
        citas.motivo
    FROM citas
    JOIN mascotas
        ON citas.id_mascota = mascotas.id_mascota
    JOIN duenos
        ON mascotas.id_dueno = duenos.id_dueno
    JOIN veterinarios
        ON citas.id_veterinario = veterinarios.id_veterinario
    """

    cursor.execute(sql)

    citas = cursor.fetchall()

    for cita in citas:
        print("-------------------------")
        print("mascota:", cita[0])
        print("dueno:", cita[1])
        print("veterinario:", cita[2])
        print("fecha:", cita[3])
        print("hora:", cita[4])
        print("motivo:", cita[5])
    
    cursor.close()
    conexion.close()

while True:
    print("\n===== Veterinaria =====")
    print("1. registrar dueno")
    print("2. registrar mascota")
    print("3. registrar veterinario")
    print("4. registrar cita")
    print("5. mostrar duenos")
    print("6. mostrar citas")
    print("7. salir")

    opcion = input("opcion: ")

    if opcion == "1":
        registrar_dueno()

    elif opcion == "2":
        registrar_mascota()

    elif opcion == "3":
        registrar_veterinarios() 

    elif opcion == "4":
        registrar_cita()

    elif opcion == "5":
        mostrar_duenos() 


    elif opcion == "7":
        mostrar_citas()     

    elif opcion == "8":
        break







