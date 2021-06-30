/*
Left join exclusivo 
*/

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
	c.id IS NULL;

/*
Left join inclusivo
*/

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
	1 = 1;

/*
Inner join / Default
*/

SELECT
	a.nombre,
	a.apellido,
	a.carrera_id,
	c.id,
	c.carrera
FROM
	alumnos a
INNER JOIN carreras c ON
	c.id = a.carrera_id
WHERE
	1 = 1;

/*
Diferencia simetrica / Lo que esta en ambos universos excepto la intercepcion
*/

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
WHERE
	(
		a.id IS NULL
			OR c.id IS NULL
	);
