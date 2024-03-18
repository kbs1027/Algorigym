select 
    ROUTE,
    concat(round(sum(D_BETWEEN_DIST),1),'km') as TOTAL_DISTANCE,
    concat(round(avg(D_BETWEEN_DIST),2),'km') as AVERAGE_DISTANCE
from
    SUBWAY_DISTANCE 
GROUP BY
    ROUTE
ORDER BY
    SUM(D_BETWEEN_DIST) DESC