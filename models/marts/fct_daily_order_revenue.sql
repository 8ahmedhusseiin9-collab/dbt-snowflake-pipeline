select 
o.order_date,
O.order_id,
sum(sales) as total_price
from
{{ ref('stg_orders') }} O
left join {{ ref('stg_order_items') }} OI
on O.order_id = OI.order_id
group by 1,2
