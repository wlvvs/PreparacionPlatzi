/*
Trabajo y uso de rangos
*/

SELECT
	*
FROM
	generate_series(1.1, 6, 1.1);

SELECT
	current_date + s.a AS dates
FROM
	generate_series(0, 14, 7) AS s(a);

SELECT
	*
FROM
	generate_series('2021-06-29 15:38:00'::timestamp, '2021-06-30 15:38:00'::timestamp, '5 hours 22 minutes');

SELECT
	a.id,
	a.nombre,
	a.apellido,
	a.carrera_id,
	s.a
FROM
	alumnos a
INNER JOIN generate_series(1, 10) AS s(a) ON
	s.a = a.carrera_id
ORDER BY
	a.carrera_id ;
