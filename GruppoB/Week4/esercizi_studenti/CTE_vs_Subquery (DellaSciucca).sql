/* Numero di invoice per customer con informazioni anagrafiche e in aggiunta
il numero totale di tracce acquistate per customer */

--CTE solution
with Truck_Count as (
SELECT
	ii.InvoiceId,
	count(ii.TrackID) as Inv_per_Truck
from
	invoice_items ii
group by 
	ii.InvoiceID
)
select 
	count(i.InvoiceID) as Invoice_Count,
	sum(Truck_Count.Inv_per_Truck) as Truck_Count,
	c.*
from customers c
	left join invoices i on c.CustomerID = i.CustomerID 
		left join Truck_Count on i.InvoiceID = Truck_Count.InvoiceID
group BY 
	c.CustomerID


--subquery solution	
SELECT
	count(i.InvoiceID) as Invoice_count,
	sum(Invoice_Tracks) as Tracks_Purchased,
	c.*
from customers c 
	left join invoices i on c.CustomerId = i.CustomerId 
		left join (select
					InvoiceID,
					count(TrackID) as Invoice_Tracks
				from 
					invoice_items ii 
				group by 
					InvoiceID) num_tracks on i.InvoiceId = num_tracks.InvoiceID
group by 
	c.CustomerID;
	