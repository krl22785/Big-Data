-- ********************Task 3 *******************

-- ********************Task 3 a *******************
 
select medallion, pickup_datetime, count(*) as num_trips 
	from alltrips 
		group by medallion, pickup_datetime 
		Having num_trips > 1;

# Yes, there is more than one record for a given taxi at the same time.  There are approximately 248 records where the medallion number and the pickup
# datetime appear more than one time in the dataset.  What is interesting about it is the fact that each of these records appear about 4x in the 
# dataset. 

-- ********************Task 3 b *******************''
select x.medallion, (IFNULL(gps,0)/count(*)) * 100  as percentage_of_trips 
	from alltrips x left join (
		select medallion, count(*) as gps 
			from alltrips 
				where 
					pickup_longitude = 0 and 
					pickup_latitude = 0 and 
					dropoff_longitude = 0 and 
					dropoff_latitude = 0 
						group by medallion) y 
	on x.medallion = y.medallion 
	group by x.medallion;

-- ********************Task 3 c *******************

select hack_license, count(medallion) as taxis 
	from alltrips 
		group by hack_license 
		order by taxis desc limit 100;

# There are several things that are unusual.  Several hack_licneses have several hundred medallions linked to them in the 3 day time period.  
# That is not humanly possible we can assume there is an issue here with the data.  