SELECT 
	Name,
	Milliseconds as TrackLenght,
CASE
	WHEN Milliseconds >= 200000 THEN 'Lunga'
	ElSE 'Corta'
END AS classe_durata
FROM 
	Track
ORDER BY
	classe_durata,
	Name