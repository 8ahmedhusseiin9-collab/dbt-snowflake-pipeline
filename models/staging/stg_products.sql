select id as product_id,
store_id,
total_price,base_price,units_sold
from {{ source('raw_data','products')}}