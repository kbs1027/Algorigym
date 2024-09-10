SELECT bk.CATEGORY, SUM(bs.SALES) as TOTAL_SALES
from BOOK bk
join BOOK_SALES bs
on bk.BOOK_ID = bs.BOOK_ID
where YEAR(bs.SALES_DATE) = 2022
and MONTH(bs.SALES_DATE) = 1
group by bk.CATEGORY
order by bk.CATEGORY asc