/*
Consulta para extraer el año de una fecha
*/

SELECT
	EXTRACT(
		YEAR
	FROM
		fecha_incorporacion
	) anio
FROM
	alumnos a;

/*
Consulta para extraer el año de una fecha
*/

SELECT
	date_part('YEAR' , fecha_incorporacion) anio
FROM
	alumnos a;

/*
Consulta para extraer los valores de un timestamp
*/

SELECT
	ID,
	concat('ANIO: ', date_part('YEAR' , fecha_incorporacion),
	'| MES: ', date_part('MONTH' , fecha_incorporacion),
	'| DIA: ', date_part('DAY' , fecha_incorporacion),
	'| HORA: ', date_part('HOUR' , fecha_incorporacion),
	'| MINUTO: ', date_part('MINUTE' , fecha_incorporacion),
	'| SEGUNDO: ', date_part('SECOND' , fecha_incorporacion) ) fecha_incorporacion
FROM
	alumnos a;
