


select 
	vehicle_type, 
	count(alltrips.medallion) as total_trips, 
	sum(alltrips.total_amount) as total_revenue, 
	sum(alltrips.tip_amount)/sum(alltrips.total_amount) as avg_tip_percentage 
		from alltrips inner join medallions 
			on alltrips.medallion = medallions.medallion 
				group by vehicle_type;



select 
	medallion_type as medallion_type, 
	count(alltrips.medallion) as total_trips, 
	sum(alltrips.total_amount) as total_revenue, 
	sum(alltrips.tip_amount)/sum(alltrips.total_amount) as avg_tip_percentage 
		from alltrips inner join medallions  
			on alltrips.medallion = medallions.medallion 
				group by medallion_type;



select agent_name, sum(alltrips.total_amount) as total_revenue 
	from alltrips inner join medallions 
		on alltrips.medallion = medallions.medallion 
			group by agent_name 
			order by total_revenue desc 
			limit 10;