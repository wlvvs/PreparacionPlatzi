/*
Las siguientes consultas hacen la recuperación de los primeros
5 registros de una tabla sin la necesidad de interactuar con las
columnas que tienen.
Con respecto a la información, se explica brevemente como actua cada
una de las consultas:

 1. Se utiliza la opción de consulta fetch first para indicar que del
 universo de datos, elija los primeros, despues se indica cuantos, en 
 este caso, seran 5
 
 2. Se usa la opción de consulta limit para indicar que nos traiga todos
 los registros y frene con respecto al numero de salidas en pantalla que
 requerimos, en este caso, 5
 
 3. Por medio de una función de ventana, se genera el valor del row_id
 que conceptualmente difiere con el de PK y con base a ese numero, se traen
 los primeros 5 valores

*/

SELECT
	*
FROM
	alumnos a FETCH FIRST 5 ROWS ONLY;

---

SELECT
	*
FROM
	alumnos a
LIMIT 5;

---

SELECT
	*
FROM
	(
		SELECT
			ROW_NUMBER() OVER() AS row_id,
			*
		FROM
			alumnos a
	) AS alumnos_with_row_nums
WHERE
	row_id <= 5;