-- ********************Task 2 *******************

-- ********************Task 2 a *******************
select fare_amount as amount, count(*) as num_trips 
	from alltrips 
		group by fare_amount 
		order by num_trips desc;

-- ********************Task 2 b *******************
select count(*) as num_trips 
	from alltrips 
		where fare_amount < 10.00;

-- ********************Task 2 c *******************
select passenger_count as number_of_passengers, count(*) as num_trips 
	from alltrips 
	group by passenger_count;

-- ********************Task 2 d *******************
select date(dropoff_datetime) as day, sum(total_amount) as total_revenue 
	from alltrips group by day;

-- ********************Task 2 e *******************
select medallion, count(*) as num_trips 
	from alltrips group by medallion;