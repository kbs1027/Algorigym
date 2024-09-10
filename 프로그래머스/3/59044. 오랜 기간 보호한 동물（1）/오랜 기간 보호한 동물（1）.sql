SELECT ai.NAME, ai.DATETIME
from ANIMAL_INS ai 
left JOIN ANIMAL_OUTS ao
on ai.ANIMAL_ID = ao.ANIMAL_ID
where ao.ANIMAL_ID is null
order by ai.DATETIME asc
limit 3