CREATE SCHEMA IF NOT EXISTS matriculas;
SET search_path TO matriculas, public;
CREATE TABLE IF NOT EXISTS matriculas.estudiantes(
    carnet NUMERIC PRIMARY KEY,
    nombre TEXT,
    apellidos TEXT,
    creditos NUMERIC
);

\echo 'Cargando'
\COPY matriculas.estudiantes    FROM './datos_estudiantes.csv' WITH (FORMAT csv, DELIMITER E',', NULL '\N', ENCODING 'UTF-8');

CREATE TABLE IF NOT EXISTS matriculas.asignaturas (
    codigo NUMERIC PRIMARY KEY,
    nombre TEXT,
    caracter TEXT,
    creditos NUMERIC
);

\COPY matriculas.asignaturas    FROM './datos_asignaturas.csv' WITH (FORMAT csv, DELIMITER E',', NULL '\N', ENCODING 'UTF-8');

CREATE TABLE IF NOT EXISTS matriculas (
    carnet_estu NUMERIC,
    codigo_asig NUMERIC,
    nota NUMERIC,
    
    PRIMARY KEY (carnet_estu, codigo_asig),
    FOREIGN KEY (carnet_estu) REFERENCES estudiantes(carnet) ON UPDATE RESTRICT ON DELETE RESTRICT,
    FOREIGN KEY (codigo_asig) REFERENCES asignaturas(codigo) ON UPDATE RESTRICT ON DELETE RESTRICT
);

\COPY matriculas.matriculas    FROM './datos_matriculas.csv' WITH (FORMAT csv, DELIMITER E',', NULL '\N', ENCODING 'UTF-8');
