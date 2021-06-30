/*
Ejemplos de expresiones regulares
*/

SELECT
	email
FROM
	alumnos a
WHERE
	email ~* '[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}';


SELECT
	email
FROM
	alumnos a
WHERE
	email ~* '[A-Z0-9._%+-]+@google[A-Z0-9.-]+\.[A-Z]{2,4}';
