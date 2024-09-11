SELECT fh.FLAVOR
from FIRST_HALF fh
join JULY j
on fh.FLAVOR = j.FLAVOR
group by fh.FLAVOR, j.FLAVOR
order by sum(fh.TOTAL_ORDER) + sum(j.TOTAL_ORDER) desc
limit 3