/*
Insert del registro duplicado para revision conceptual 
*/

INSERT
	INTO
	platzi.alumnos (
		id,
		nombre,
		apellido,
		email,
		colegiatura,
		fecha_incorporacion,
		carrera_id,
		tutor_id
	)
VALUES (
	1001,
	'Pamelina',
	NULL,
	'pmylchreestrr@salon.com',
	4800,
	'2020-04-26 10:18:51',
	12,
	16
);

/*
Encontrar registros duplicados ajenos a la pk 
*/

SELECT
	(
		platzi.alumnos.nombre,
		platzi.alumnos.apellido,
		platzi.alumnos.email,
		platzi.alumnos.colegiatura,
		platzi.alumnos.fecha_incorporacion,
		platzi.alumnos.carrera_id,
		platzi.alumnos.tutor_id
	)::TEXT,
	count(*)
FROM
	alumnos
GROUP BY
	(
		platzi.alumnos.nombre,
		platzi.alumnos.apellido,
		platzi.alumnos.email,
		platzi.alumnos.colegiatura,
		platzi.alumnos.fecha_incorporacion,
		platzi.alumnos.carrera_id,
		platzi.alumnos.tutor_id
	)
HAVING
	count(*)>1;

/*
Obtener el registro duplicado usando funciones de row id 
*/

SELECT
	*
FROM
	(
		SELECT
			a.id id2,
			ROW_NUMBER() OVER(
				PARTITION BY a.nombre,
				a.apellido,
				a.email,
				a.colegiatura,
				a.fecha_incorporacion,
				a.carrera_id,
				a.tutor_id
			ORDER BY
				a.id ASC
			) AS ROW,
			*
		FROM
			alumnos a
	) dup
WHERE
	dup.ROW>1;

/*
Solución al reto 
*/

DELETE
FROM
	alumnos
WHERE
	id = (
		SELECT
			dup.id
		FROM
			(
				SELECT
					a.id id2,
					ROW_NUMBER() OVER(
						PARTITION BY a.nombre,
						a.apellido,
						a.email,
						a.colegiatura,
						a.fecha_incorporacion,
						a.carrera_id,
						a.tutor_id
					ORDER BY
						a.id ASC
					) AS ROW,
					*
				FROM
					alumnos a
			) dup
		WHERE
			dup.ROW>1
	);
