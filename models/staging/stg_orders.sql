select id as order_id,
customer_id,
order_date,
sales
from {{ source('raw_data','orders')}}