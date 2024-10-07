CREATE TABLE HOTEL (
    hotel_id INT PRIMARY KEY,
    nombre VARCHAR(10),
    direccion VARCHAR(18),
    catego VARCHAR(8)
);

CREATE TABLE HABITACION (
    habitacion_id INT PRIMARY KEY,
    tipo VARCHAR(5),
    capacidad VARCHAR(5),
    precio VARCHAR(5),
    CONSTRAINT fk_hotel FOREIGN KEY (hotel_id) REFERENCES HOTEL(hotel_id)
);

CREATE TABLE CLIENTE (
    cliente_id INT PRIMARY KEY,
    nombre VARCHAR(10),
    apellido VARCHAR(10),
    mail VARCHAR(10),
    telefono INT(10)
);

CREATE TABLE RESERVA (
    reserva_id INT PRIMARY KEY,
    fecha_in DATE,
    fecha_out DATE,
    cantidad_personas INT,
    CONSTRAINT fk_cliente FOREIGN KEY (cliente_id) REFERENCES CLIENTE(cliente_id),
    CONSTRAINT fk_habitacion FOREIGN KEY (habitacion_id) REFERENCES HABITACION(habitacion_id)
);

