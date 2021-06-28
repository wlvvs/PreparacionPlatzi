/*
Revision de joins 
*/

SELECT
	carrera_id,
	count(*)
FROM
	alumnos a
GROUP BY
	carrera_id
ORDER BY
	2 DESC;

DELETE
FROM
	carreras
WHERE
	id BETWEEN 30 AND 40;

SELECT
	a.nombre,
	a.apellido,
	a.carrera_id,
	c.id,
	c.carrera
FROM
	alumnos a
LEFT JOIN carreras c ON
	c.id = a.carrera_id
WHERE
	c.id IS NULL
ORDER BY
	a.carrera_id;

SELECT
	a.nombre,
	a.apellido,
	a.carrera_id,
	c.id,
	c.carrera
FROM
	alumnos a
FULL OUTER JOIN carreras c ON
	c.id = a.carrera_id
ORDER BY
	a.carrera_id;
