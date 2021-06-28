/*
Consulta que recupera todos los registros de la tabla cuando el row_id
pertenece a una lista predefinida
*/

SELECT
	*
FROM
	(
		SELECT
			ROW_NUMBER() OVER() AS row_id,
			*
		FROM
			alumnos a
	) z
WHERE
	row_id IN (
		1, 5, 10, 12, 15, 20
	);

/*
Consulta que recupera todos los registros de la tabla cuando el id
de la tabla pertenece a la recuperacion de una subconsulta
*/

SELECT
	*
FROM
	alumnos a
WHERE
	id IN (
		SELECT
			id
		FROM
			alumnos a2
		WHERE
			tutor_id = 30
	);

/*
Consulta que recupera todos los registros de la tabla cuando el id
de la tabla no pertenece a la recuperacion de una subconsulta
*/

SELECT
	*
FROM
	alumnos a
WHERE
	id IN (
		SELECT
			id
		FROM
			alumnos a2
		WHERE
			tutor_id <> 30
	);
