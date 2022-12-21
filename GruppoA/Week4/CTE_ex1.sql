-- numero di invoice per customer id
SELECT
	CustomerId,
	Count(*) AS numero_invoice_per_customer
FROM
	Invoice
GROUP BY
	CustomerId
;

-- Reperisco le info anagrafiche dei clienti tramite JOIN
SELECT
	i.*,
	c.*,
	Count(*) AS numero_invoice_per_customer
FROM
	Invoice i 
	LEFT JOIN
	Customer c 
		ON i.CustomerId = c.CustomerId
GROUP BY
	i.CustomerId
;

-- Utilizzo CTE per rendere il risultato più leggibile
WITH invoice_per_customer AS (
	SELECT
		CustomerId,
		Count(*) AS numero_invoice_per_customer
	FROM
		Invoice
	GROUP BY
		CustomerId
)
SELECT
	invoice_per_customer.numero_invoice_per_customer,
	Customer.*
FROM
	invoice_per_customer
	LEFT JOIN
	Customer
		ON invoice_per_customer.CustomerId = Customer.CustomerId
;
	
	
	
	
	