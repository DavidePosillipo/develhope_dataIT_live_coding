/* Numero di invoice per cliente e le informazioni 
anagrafiche di ogni cliente 

| customer_id | numero_di_invoice | <info anagrafiche> |

*/

-- JOIN "brutale"
SELECT
	Invoice.*,
	Customer.*--,
--	Count(*) AS numero_di_invoice
FROM
	Customer
	LEFT JOIN
	Invoice
		ON Customer.CustomerId = Invoice.CustomerId
--GROUP BY
--	Customer.CustomerId
;

-- Utilizzando CTE
/*
WITH nome_tabella_temporanea AS (
	istruzioni per creare la tabella temporeanea
	
)
SELECT 
FROM nome_tabella_temporanea
;
*/
WITH numero_di_invoice_table AS (
	SELECT
		CustomerID,
		Count(*) AS numero_di_invoice
	FROM
		Invoice
	GROUP BY
		CustomerId
)
SELECT
	Customer.*,
	numero_di_invoice_table.numero_di_invoice
FROM
	Customer
	LEFT JOIN
	numero_di_invoice_table
		ON Customer.CustomerId = numero_di_invoice_table.CustomerId
;







