select id as customer_id,
name as customer_name,
segment,state,city
from {{ source('raw_data','customers')}}