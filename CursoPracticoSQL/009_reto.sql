/*
Ejemplos de self join (join de una tabla consigo misma) 
*/

SELECT
	concat(a.nombre, ' ', a.apellido)alumno,
	concat(t.nombre, ' ', t.apellido)tutor
FROM
	alumnos a
INNER JOIN alumnos t ON
	a.tutor_id = t.id;

SELECT
	concat(t.nombre, ' ', t.apellido)tutor,
	count(*) alumnos_x_tutor
FROM
	alumnos a
INNER JOIN alumnos t ON
	a.tutor_id = t.id
GROUP BY
	tutor
ORDER BY
	2 DESC
LIMIT 5;

/*
Solucion del reto 
*/

WITH u AS (
	SELECT
		concat(t.nombre, ' ', t.apellido) tutor,
		count(*) alumnos_x_tutor
	FROM
		alumnos a
	INNER JOIN alumnos t ON
		a.tutor_id = t.id
	GROUP BY
		1
	ORDER BY
		2 DESC
)
SELECT
	trunc(avg(u.alumnos_x_tutor), 2) promedio
FROM
	u;