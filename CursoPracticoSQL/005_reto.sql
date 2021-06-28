/*
Uso de extract como parte de un filtro 
*/

SELECT
	*
FROM
	alumnos a
WHERE
	(
		EXTRACT (
			YEAR
		FROM
			fecha_incorporacion
		)
	) = '2019';

/*
Uso de date_part como parte de un filtro 
*/

SELECT
	*
FROM
	alumnos a
WHERE
	date_part('YEAR', fecha_incorporacion) = '2019';

/*
Uso de extract como parte de un filtro en subquery
*/

SELECT
	*
FROM
	(
		SELECT
			*,
			(
				EXTRACT (
					YEAR
				FROM
					fecha_incorporacion
				)
			) anio
		FROM
			alumnos a
		WHERE
			(
				EXTRACT (
					YEAR
				FROM
					fecha_incorporacion
				) = '2019'
			)
	) z
WHERE
	z.anio = 2019;

/*
Reto resuelto 
*/

SELECT
	*
FROM
	alumnos a
WHERE
	TO_CHAR(fecha_incorporacion, 'YYYYMM') = '201805';
