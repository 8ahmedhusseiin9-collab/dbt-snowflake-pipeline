select
id as item_id,
order_id,
product_id,
quantity,
price_at_purchase
from {{ source('raw_data','order_items')}}