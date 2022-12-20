-- numero di invoice per customer id
SELECT
	CustomerId,
	Count(*) AS numero_invoice_per_customer
FROM
	Invoice
GROUP BY
	CustomerId
;

-- Utilizzo una subquery nel FROM per incrociare queste info con la tabella Customer
SELECT
	Customer.*,
	invoice_per_customer.numero_invoice_per_customer
FROM
	(
		SELECT
			CustomerId,
			Count(*) AS numero_invoice_per_customer
		FROM
			Invoice
		GROUP BY
			CustomerId
	) AS invoice_per_customer
	LEFT JOIN
	Customer
		ON invoice_per_customer.CustomerId = Customer.CustomerId
;
	
	