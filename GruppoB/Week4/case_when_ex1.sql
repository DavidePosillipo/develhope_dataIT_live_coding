/* Utilizzo di CASE WHEN */

/* Creare una colonna "durata" con modalità "lunga" e "breve"
 * sulla base del valore nella colonna Milliseconds
 */

-- Metodo "artigianale"
SELECT
	'breve' AS durata,
	Track.*
FROM
	Track
WHERE
	Milliseconds < 200000
	
UNION

SELECT
	'lunga' AS durata,
	Track.*
FROM
	Track
WHERE
	Milliseconds >= 200000
;

-- metodo "professionale"
SELECT
	CASE
		WHEN Milliseconds < 200000 THEN 'breve'
		WHEN Milliseconds >= 200000 THEN 'lunga'
	END durata,
	Track.*
FROM
	Track;

-- inserisco l'ELSE
SELECT
	CASE
		WHEN Milliseconds < 200000 THEN 'breve'
		ELSE 'lunga'
	END durata,
	Track.*
FROM
	Track;

WITH durate_categoriali AS (
SELECT
	CASE
		WHEN Milliseconds < 200000 THEN 'breve'
		WHEN Milliseconds >= 200000 AND Milliseconds < 300000 THEN 'media'
		ELSE 'lunga'
	END durata,
	Track.*
FROM
	Track
) 
SELECT
	durata,
	Count(*) AS numero_canzoni
FROM
	durate_categoriali
GROUP BY
	durata
;

	
	












