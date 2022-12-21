/* Numero di invoice per customer con informazioni anagrafiche e in aggiunta
il numero totale di tracce acquistate per customer

| customer_id | numero_di_invoice | numero_di_tracce | +info anagrafiche |

ATTENZIONE NON E' COMPLETO AL MOMENTO: DA FINIRE

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
invoice_per_customer AS (
	SELECT
		CustomerId,
		InvoiceId,
		Count(*) AS numero_invoice_per_customer
	FROM
		Invoice
	GROUP BY
		CustomerId
)
SELECT
	invoice_per_customer.*,
	acquisti.acquisti_per_invoice
FROM
	invoice_per_customer
	LEFT JOIN
	acquisti
		ON
		invoice_per_customer.InvoiceId = acquisti.InvoiceId
;






