SELECT
	i.CustomerID,
	c.FirstName,
	c.LastName,
	COUNT(*) as inv_per_customer,
	SUM(Tracks_per_singola_invoice)
FROM 
	(SELECT 
		InvoiceId,
		COUNT(*) AS Tracks_per_singola_invoice
	FROM
		InvoiceLine
	GROUP BY
		InvoiceID
	) as trackstable
	LEFT JOIN 
		Invoice i 	
		ON
			i.InvoiceId = trackstable.InvoiceId
	LEFT JOIN 
		Customer c 
		ON
			i.CustomerId = c.CustomerId 
			
GROUP BY
	i.CustomerId