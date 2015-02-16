

select fare_amount as amount, count(*) as num_trips from alltrips group by fare_amount order by num_trips desc;

select count(*) as num_trips from alltrips where fare_amount < 10.00;

select passenger_count as number_of_passengers, count(*) as num_trips from alltrips group by passenger_count;

select date(dropoff_datetime) as day, sum(total_amount) from alltrips group by day;

select medallion, count(*) as num_trips from alltrips group by medallion;