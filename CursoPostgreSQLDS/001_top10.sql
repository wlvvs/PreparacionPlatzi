/*
En este script se genera un top 10 de peliculas.
Es importante revisar que el top se maneja de dos formas, ambas haciendo uso de window functions
La primera hace uso de dense rank, que muestra como resultado el top 10 pero respetando los lugares similares
La segunda hace uso de row number para mostrar un ID consecutivo del 1 al 10
La tercera hace uso de percent rank para mostrar el valor en percentil con respecto al universo de datos

Ambos casos usan como referencia el conteo descendente de valores correspondientes a la extracción total de la
consulta
*/

SELECT
	p.pelicula_id AS id,
	p.titulo,
	count(*) AS rentas,
	DENSE_RANK () OVER (
	ORDER BY
		count(*) DESC
	) AS top_1,
	ROW_NUMBER () OVER (
	ORDER BY
		count(*) DESC
	) AS top_2,
	PERCENT_RANK () OVER (
	ORDER BY
		count(*) ASC
	) AS top_3
FROM
	rentas r
INNER JOIN inventarios i ON
	i.inventario_id = r.inventario_id
INNER JOIN peliculas p ON
	p.pelicula_id = i.pelicula_id
GROUP BY
	p.pelicula_id
ORDER BY
	rentas DESC
LIMIT 10;