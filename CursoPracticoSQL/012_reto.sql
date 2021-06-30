/*
Uso de lpad y rpad
*/

SELECT
	lpad('1', id, '*')
FROM
	alumnos a
WHERE
	id < 10;

SELECT
	lpad('1', CAST(row_id AS int), '*')
FROM
	(
		SELECT
			ROW_NUMBER() OVER(
			ORDER BY
				carrera_id
			) AS row_id,
			*
		FROM
			alumnos a
	)z
WHERE
	row_id <= 5
ORDER BY
	carrera_id ;
	
SELECT
	rpad('1', id, '*')
FROM
	alumnos a
WHERE
	id < 10;

SELECT
	rpad('1', CAST(row_id AS int), '*')
FROM
	(
		SELECT
			ROW_NUMBER() OVER(
			ORDER BY
				carrera_id
			) AS row_id,
			*
		FROM
			alumnos a
	)z
WHERE
	row_id <= 5
ORDER BY
	carrera_id ;
