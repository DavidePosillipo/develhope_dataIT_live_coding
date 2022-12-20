/* Numero di invoice per cliente e le informazioni 
anagrafiche di ogni cliente 

| customer_id | numero_di_invoice | <info anagrafiche> |

*/
/*
SELECT 
	(subquery)

FROM 
	(subquery)

WHERE
	(subquery)
;
*/

SELECT
	Customer.*,
	numero_di_invoice_table.numero_di_invoice
FROM
	Customer
	LEFT JOIN
	(
		SELECT
			CustomerID,
			Count(*) AS numero_di_invoice
		FROM
			Invoice
		GROUP BY
			CustomerId
	) AS numero_di_invoice_table
		ON Customer.CustomerId = numero_di_invoice_table.CustomerId
;