/* Numero di invoice per customer con informazioni anagrafiche e in aggiunta il numero totale di tracce acquistate per customer


| customer_id | numero_di_invoice | numero_di_tracce | +info anagrafiche | */


-- CTE - Versione aggiornata e presumibilmente migliorata
WITH CTE AS (
	SELECT
		i.CustomerId,
		count(DISTINCT i.invoiceId) AS NumOfInvoice,
		sum(il.Quantity) AS TotalQuantityPurchased
	FROM
		InvoiceLine il
		LEFT JOIN
			Invoice i
			ON
			il.InvoiceId = i.InvoiceId  
	GROUP BY
		CustomerId
)
SELECT
	c.CustomerId AS CustomerId,
	CTE.NumOfInvoice AS NumOfInvoice,
	CTE.TotalQuantityPurchased AS TotalQuantityPurchased,
	c.*
FROM
	Customer c
	LEFT JOIN
		CTE
		ON
		CTE.CustomerId = c.CustomerId
GROUP BY
	c.CustomerId 
;

-- CTE - Versione originale presentata durante live coding, inutilmente complessa e probabilmente lenta a causa di operazioni ridondanti 
WITH QuantityForCustomerTable AS (
	SELECT
		Invoice.InvoiceId,
		sum(InvoiceLine.Quantity) AS QuantityForCustomer
	FROM
		InvoiceLine
		LEFT JOIN
			Invoice
			ON
			InvoiceLine.InvoiceId = invoice.InvoiceId
	GROUP BY
		CustomerId
	),
InvoiceForCustomerTable AS (
	SELECT
		InvoiceId,
		CustomerId,
		count(*) AS InvoiceForCustomer
	FROM
		Invoice
	GROUP BY
		CustomerId
	)
SELECT
	Customer.CustomerId AS CustomerId,
	InvoiceForCustomerTable.InvoiceForCustomer AS NumOfInvoice,
	QuantityForCustomerTable.QuantityForCustomer AS TotalQuantityPurchased,
	Customer.*
FROM
	Customer
	LEFT JOIN
	InvoiceForCustomerTable
		ON
		Customer.CustomerId = InvoiceForCustomerTable.CustomerId
			LEFT JOIN
			QuantityForCustomerTable
				ON
				InvoiceForCustomerTable.InvoiceId = QuantityForCustomerTable.InvoiceId
;

-- Subquery
SELECT
	c.CustomerId AS CustomerId,
	subquery.NumOfInvoice AS NumOfInvoice,
	subquery.TotalQuantityPurchased AS TotalQuantityPurchased,
	c.*
FROM
	Customer c
	LEFT JOIN
		(SELECT
			i.CustomerId,
			count(DISTINCT i.invoiceId) AS NumOfInvoice,
			sum(il.Quantity) AS TotalQuantityPurchased
		FROM
			InvoiceLine il
			LEFT JOIN
				Invoice i
				ON
				il.InvoiceId = i.InvoiceId  
		GROUP BY
			CustomerId)
			AS subquery
				ON
				c.CustomerId = subquery.CustomerId
;