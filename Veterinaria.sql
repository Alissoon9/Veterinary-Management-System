CREATE TABLE duenos (
    id_dueno SERIAL PRIMARY KEY,
	nombre VARCHAR(100),
	telefono VARCHAR(10),
	direccion VARCHAR(150)

);

CREATE TABLE Mascotas(
    id_mascota SERIAL PRIMARY KEY,
	nombre VARCHAR(50),
	edad NUMERIC(2),
	raza VARCHAR(50),
	id_dueno INTEGER,
	FOREIGN KEY(id_dueno) REFERENCES duenos(id_dueno)
);

CREATE TABLE Veterinarios(
    id_veterinario SERIAL PRIMARY KEY,
	nombre VARCHAR(50),
	especialidad VARCHAR(100)	
);

CREATE TABLE citas(
    id_cita SERIAL PRIMARY KEY,
	fecha DATE,
	motivo VARCHAR(200),
	id_mascota INTEGER,
	id_veterinario INTEGER,
	FOREIGN KEY (id_mascota) REFERENCES mascotas(id_mascota),
	FOREIGN KEY (id_veterinario) REFERENCES veterinarios(id_veterinario)
);

SELECT * FROM duenos;


