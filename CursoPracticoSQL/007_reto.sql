/*
Filtro por valores explicitos
*/

SELECT
	*
FROM
	alumnos a
WHERE
	tutor_id IN (
		1, 2, 3, 4
	);

/*
Filtro por rangos usando in
*/

SELECT
	*
FROM
	alumnos a
WHERE
	tutor_id >= 1
	AND tutor_id <= 10;

/*
Filtro por rangos usando between
*/

SELECT
	*
FROM
	alumnos a
WHERE
	tutor_id BETWEEN 1 AND 10;

/*
Se evalua si el valor 3 se encuentra dentro del rango 10 - 20. Regresa boolean
*/

SELECT
	int4range(
		10,
		20
	) @> 3;

/*
Se evalua si los rangos dados se solapan (hay valores de un rango dentro del otro)
*/

SELECT
	numrange(
		11.1,
		22.2
	) && numrange(
		20.0,
		30.0
	);

/*
Regresa el valor mas grande del rango
*/

SELECT
	UPPER(int8range(15, 25));

/*
Regresa el valor mas pequeño del rango
*/

SELECT
	LOWER(int8range(15, 25));

/*
Regresa el rango en donde se intersectan los rangos dados
*/

SELECT
	int4range(
		10,
		20
	) * int4range(
		15,
		25
	);

/*
Indica si el rango es un rango vacio. Regresa boolean
*/

SELECT
	isempty(numrange(1, 5));

/*
Indica los registros en donde el tutor_id esta dentro del rango definido
*/

SELECT
	*
FROM
	alumnos a
WHERE
	int4range(
		10,
		20
	) @> tutor_id;

/*
Solucion del reto
*/

SELECT
	numrange(
		(
			SELECT
				min(tutor_id)
			FROM
				alumnos a
		),
		(
			SELECT
				max(tutor_id)
			FROM
				alumnos a
		)
	)* numrange(
		(
			SELECT
				min(carrera_id)
			FROM
				alumnos a
		),
		(
			SELECT
				max(carrera_id)
			FROM
				alumnos a
		)
	);
