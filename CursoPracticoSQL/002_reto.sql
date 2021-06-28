/*
Consulta para obtener la segunda colegiatura mas alta 
*/

SELECT
	DISTINCT colegiatura
FROM
	alumnos a
WHERE
	2 = (
		SELECT
			count(DISTINCT colegiatura)
		FROM
			alumnos a2
		WHERE
			a.colegiatura <= a2.colegiatura
	);


/*
Consulta para obtener la segunda colegiatura mas alta 
*/

SELECT
	DISTINCT colegiatura
FROM
	alumnos a
ORDER BY
	1 DESC
LIMIT 1 OFFSET 1;


/*
Consulta para obtener los alumnos que tienen la segunda colegiatura mas alta 
*/

SELECT
	*
FROM
	alumnos a
INNER JOIN (
		SELECT
			DISTINCT colegiatura
		FROM
			alumnos a2
		ORDER BY
			1 DESC
		LIMIT 1 OFFSET 1
	) b ON
	a.colegiatura = b.colegiatura;

/*
Consulta para obtener los alumnos que tienen la segunda colegiatura mas alta 
*/

SELECT
	*
FROM
	alumnos a
WHERE
	colegiatura = (
		SELECT
			DISTINCT colegiatura
		FROM
			alumnos a2
		ORDER BY
			1 DESC
		LIMIT 1 OFFSET 1
	);


/*
Consulta que trae la segunda mitad de la tabla. Consulta del reto
*/

SELECT
	*
FROM
	(
		SELECT
			*
		FROM
			alumnos a2
		ORDER BY
			id DESC
		LIMIT (
			SELECT
				count(a.id)/ 2
			FROM
				alumnos a
		)
	) z
ORDER BY
	1;

/*
Solución del profesor
*/

SELECT
	ROW_NUMBER() OVER() AS row_id,
	*
FROM
	alumnos a OFFSET(
		SELECT
			count(*)/ 2
		FROM
			alumnos a2
	);
