

create INDEX findex on fares (medallion, hack_license, vendor_id, pickup_datetime);
create INDEX tindex on trips (medallion, hack_license, vendor_id, pickup_datetime);

create table alltrips as 
	select trips.*, 
	fares.payment_type, 
	fares.fare_amount, 
	fares.surcharge, 
	fares.mta_tax, 
	fares.tip_amount, 
	fares.tolls_amount, 
	fares.total_amount 
		from trips inner join fares on 
			trips.medallion = fares.medallion and 
			trips.hack_license = fares.hack_license and 
			trips.vendor_id = fares.vendor_id and 
			trips.pickup_datetime = fares.pickup_datetime;