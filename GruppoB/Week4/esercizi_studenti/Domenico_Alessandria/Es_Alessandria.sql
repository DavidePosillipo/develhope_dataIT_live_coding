/* Numero di invoice per customer con informazioni anagrafiche e in aggiunta
il numero totale di tracce acquistate per customer

| customer_id | numero_di_invoice | numero_di_tracce | +info anagrafiche |

*/


SELECT 
	 c.customerId,
	 count(i.invoiceId),
	 sum(num_line_table.num_of_tracks),
	 c.*
FROM 
	Customer c
	left join Invoice i on c.CustomerId=i.CustomerId
	left join (select 
		InvoiceID,
		count(InvoiceLineId) as num_of_tracks
	from 
		InvoiceLine il 
	group by
		InvoiceID) num_line_table on num_line_table.invoiceid=i.InvoiceId
group BY 
	c.CustomerId;
	
-- Fare la stessa query con il CTE 
with table_1 as ( 
	select 
		InvoiceId,
		count(InvoiceLineID) as num_of_tracks
	from
		InvoiceLine il 
	group by
		InvoiceID)

	select 
		c.customerId,
		count(i.Invoiceid),
		sum(table_1.num_of_tracks)
	from 
		Customer c 
		left join Invoice i on i.CustomerId  = c.CustomerId 
		left join table_1 on i.InvoiceId = table_1.InvoiceId
	group BY 
		c.CustomerId;
	
	
-- Metodo alternativo creato con visualizzazione di tabelle
	
with InID_NumTrack as(
	SELECT 
		count(Quantity) as Numtrack
		InvoiceId 
	from
		InvoiceLine il 
	group by
		InvoiceId ),
	
CustomerID_InID as
	(select 
		c.CustomerId ,
		InvoiceID
	FROM 
		Customer c 
		left join Invoice i on c.CustomerId = i.CustomerId )
	
	select 
		NumTrack,
		InvoiceID,
		customer.*
	from
		CustomerId_InID
		left join InID_NumTrack on c.CustomerId = InvoiceId
	
	group BY
		customerID
		
		
