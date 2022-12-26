WITH trackstable AS 
	(
	SELECT 
		InvoiceId,
		COUNT(*) AS Tracks_per_singola_invoice
	FROM
		InvoiceLine
	GROUP BY
		InvoiceID
	),
	
	temp1 AS 
	(
	SELECT 
		i.InvoiceId,
		i.CustomerId,
		t.Tracks_per_singola_invoice
	FROM
		Invoice i
	LEFT JOIN
		trackstable t
		ON i.InvoiceId = t.InvoiceId
	)
-- come info anagrafiche prendo solo 3 campi per non creare troppe colonne ma potrei fare c.* e prendere tutta la tabella dei customer 
	
SELECT
	c.CustomerID,
	c.FirstName,
	c.LastName,
	COUNT(*) as inv_per_customer,
	SUM(Tracks_per_singola_invoice)
FROM 
	temp1 
	LEFT JOIN 
		Customer c 
		ON
			temp1.CustomerId = c.CustomerId 
			
GROUP BY
	temp1.CustomerId