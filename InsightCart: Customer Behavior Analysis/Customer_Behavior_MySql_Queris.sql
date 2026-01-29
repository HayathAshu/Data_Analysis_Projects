create database if not exists customer_behavior;
use customer_behavior;

select * from customer;

# Q1. What is the total revenue generated vy male vs. female customers?
select 
	gender, 
    sum(purchase_amount) as Revenue 
from customer
	group by gender;
    
# Q2. Which customer used a discount but still spent more than the avg purchase amt?
select 
	customer_id, 
    purchase_amount 
from customer 
	where discount_applied = 'Yes' and purchase_amount >= (select avg(purchase_amount) from customer);
    
# Q3. Which is the top 5 product with the highest avg review rating?
select 
	item_purchased, 
    round(avg(review_rating),2) as Highest_Avg 
from customer
	group by item_purchased
	order by Highest_avg desc
	limit 5;

# Q4. Compare the avg Purchase Amounts between Standard and Express Shipping
select 
	shipping_type, 
    avg(purchase_amount) as Avg_Purchase_Amt 
from customer
	where shipping_type in('Standard', 'Express')
	group by shipping_type;

# Q5. Do suscribers customers spends more? Compare avg spend and total revenue between suscribers and Non - Suscribers.
select 
	subscription_status, 
    count(customer_id) as Total_Customers, 
    round(avg(purchase_amount),2) as Avg_Purchase, 
    round(sum(purchase_amount), 2) as Total_Revenue 
from customer
	group by subscription_status
	order by total_revenue, Avg_Purchase desc;
    
# Q6. Which 5 products have the highest percentage of purchase with discount applied?
select item_purchased, 
round(100 * sum(case when discount_applied = 'Yes' then 1 else 0 end) / count(*),2) as discount_rate from customer
group by item_purchased
order by discount_rate desc
limit 5;

# Q7. Segment customers into new, returning, and Loyal based on their total number of previous purchase, and show the count of each segment
with my_cte as (
	select customer_id, previous_purchases,
    case 
		when
			previous_purchases = 1 then 'New'
		when
			previous_purchases between 2 and 10 then 'Returning'
		else
			'Loyal'
		end as customer_segment
from customer
)
select customer_segment, count(*) as "Number of Customer"
from my_cte
group by customer_segment;

# Q8. What are the top 3 most purchased products within each category?
with my_cte as (
	select 
		category,
		item_purchased, 
        count(customer_id) as total_orders,
		row_number() 
			over(partition by category order by count(customer_id) desc) as item_rank
from customer
    group by item_purchased, category
)
select 
	category, 
    item_purchased, 
    item_rank, 
    total_orders 
from my_cte
	where item_rank <= 3;
    
# Q9. Are customers who are repeat buyers (more than 5 previous purchases) aslo likely to subscribe?
select
	subscription_status,
    count(customer_id) as repeat_buyers
from customer
	where previous_purchase > 5
    group by subscription_status;
    
# Q10. What are the revenue contribute of each age group?
select 
	age_group,
	round(sum(purchase_amount), 2) as total_revenue
from customer
	group by age_group
    order by total_revenue desc;
    