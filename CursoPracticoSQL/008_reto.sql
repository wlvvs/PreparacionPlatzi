/*
Pruebas de maximos y minimos 
*/

SELECT
	carrera_id,
	max(fecha_incorporacion)
FROM
	alumnos a
GROUP BY
	carrera_id
ORDER BY
	carrera_id;

SELECT
	MIN(nombre)
FROM
	alumnos;

SELECT
	tutor_id,
	MIN(nombre)
FROM
	alumnos
GROUP BY
	tutor_id
ORDER BY
	tutor_id;
