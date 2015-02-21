-- ********************Task 4 *******************

CREATE TABLE medallions (
       medallion varchar(50),
       name varchar(50),
       type varchar(30),
       current_status varchar(10),
       DMV_license_plate varchar(10),
       vehicle_VIN_number varchar(20),
       vehicle_type varchar(10),
       model_year DECIMAL(4),
       medallion_type varchar(30),
       agent_number INTEGER,
       agent_name varchar(30),
       agent_telephone_number varchar(15),
       agent_website varchar(50),
       agent_address varchar(50),
       last_updated_date DATE,
       last_updated_time TIME
);


load data local infile 'licenses.txt' into table medallions 
	FIELDS TERMINATED BY '\t'
	LINES TERMINATED BY '\r\n'
    IGNORE 1 LINES;


--ALTER TABLE `medallions` ADD INDEX `medallion` (`medallion`);
ALTER TABLE `alltrips` ADD INDEX `medallion` (`medallion`);

-- ********************Task 4 a *******************

select 
	vehicle_type, 
	count(alltrips.medallion) as total_trips, 
	sum(alltrips.total_amount) as total_revenue, 
	sum(alltrips.tip_amount)/sum(alltrips.fare_amount) as avg_tip_percentage 
		from alltrips inner join medallions 
			on alltrips.medallion = medallions.medallion 
				group by vehicle_type;

-- ********************Task 4 b *******************

select 
	medallion_type as medallion_type, 
	count(alltrips.medallion) as total_trips, 
	sum(alltrips.total_amount) as total_revenue, 
	sum(alltrips.tip_amount)/sum(alltrips.fare_amount) as avg_tip_percentage 
		from alltrips inner join medallions  
			on alltrips.medallion = medallions.medallion 
				group by medallion_type;

-- ********************Task 4 c *******************

select agent_name, sum(alltrips.total_amount) as total_revenue 
	from alltrips inner join medallions 
		on alltrips.medallion = medallions.medallion 
			group by agent_name 
			order by total_revenue desc 
			limit 10;