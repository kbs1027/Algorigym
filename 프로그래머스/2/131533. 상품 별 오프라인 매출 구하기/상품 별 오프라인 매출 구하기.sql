SELECT PRODUCT_CODE, SUM(pd.PRICE * os.SALES_AMOUNT) as SALES
from PRODUCT pd
join OFFLINE_SALE os
on pd.PRODUCT_ID = os.PRODUCT_ID
group by PRODUCT_CODE
order by SALES desc, PRODUCT_CODE asc
