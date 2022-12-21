/* Numero di invoice per customer con informazioni anagrafiche e in aggiunta
il numero totale di tracce acquistate per customer

| customer_id | numero_di_invoice | numero_di_tracce | +info anagrafiche |

*/
WITH acquisti AS 
	(
	SELECT
		InvoiceId,
		sum(Quantity) AS acquisti_per_invoice
	FROM
		InvoiceLine
	GROUP BY
		InvoiceId 
	),
invoices_con_quantita AS (
	SELECT
		i.InvoiceId,
		i.CustomerId,
		a.acquisti_per_invoice
	FROM
		Invoice i
		LEFT JOIN
		acquisti a
			ON i.InvoiceId = a.InvoiceId
)
SELECT
	iq.InvoiceId,
	iq.acquisti_per_invoice,
	c.*
FROM
	invoices_con_quantita iq
	LEFT JOIN
	Customer c
		ON 
		iq.CustomerId = c.CustomerId
;


-- Completo facendo un Group By su customer id per contare 
-- il numero di invoice e il totale di tracce per customer
WITH acquisti AS 
	(
	SELECT
		InvoiceId,
		sum(Quantity) AS acquisti_per_invoice
	FROM
		InvoiceLine
	GROUP BY
		InvoiceId 
	),
invoices_con_quantita AS (
	SELECT
		i.InvoiceId,
		i.CustomerId,
		a.acquisti_per_invoice
	FROM
		Invoice i
		LEFT JOIN
		acquisti a
			ON i.InvoiceId = a.InvoiceId
)
SELECT
	Count(iq.InvoiceId) AS numero_di_invoices_per_customer,
	Sum(iq.acquisti_per_invoice) AS numero_di_tracce_per_customer,
	c.*
FROM
	invoices_con_quantita iq
	LEFT JOIN
	Customer c
		ON 
		iq.CustomerId = c.CustomerId
GROUP BY
	c.CustomerId
;


