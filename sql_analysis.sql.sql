create database stock_analysis;
use stock_analysis;

create table stock_data (
Date date,
Stock varchar(50),
Open float,
High float,
Low float,
Close float,
Volume bigint,
Daily_Return float,
MA_10 float,
MA_50 float,
Volatility float,
Risk_Category varchar(20));

select * from stock_data;


select stock, round(avg(Daily_Return), 5) as avg_return from stock_data group by stock order by avg_return desc limit 5;

select stock, round(stddev(Daily_Return), 5) as risk from stock_data group by stock order by risk desc;

select Risk_Category, 
count(*) as total_records
from stock_data group by Risk_Category;

select Risk_Category, round(avg(Daily_Return), 5) as Avg_Return
from stock_data group by Risk_Category order by Avg_Return desc;

select Date, stock, Daily_Return from stock_data 
order by Daily_Return desc limit 10;

select Date, stock, Daily_Return from stock_data 
order by Daily_Return limit 10;

select Date, stock, Close, MA_10, MA_50 from stock_data where stock = 'RELIANCE.NS';

select stock, avg(Daily_Return) as Avg_Return, 
stddev(Daily_Return) as Risk from stock_data group by stock 
having Avg_Return > 0.001 and Risk > 0.02
order by Avg_Return desc;

select stock, avg(Daily_Return) as Avg_Return, 
stddev(Daily_Return) as Risk from stock_data group by stock 
having Risk > 0.015
order by Avg_Return desc;

SELECT Stock, SUM(Volume) AS Total_Volume
FROM stock_data
GROUP BY Stock
ORDER BY Total_Volume desc;