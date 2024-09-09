SELECT mp.MEMBER_NAME, rr.REVIEW_TEXT, DATE_FORMAT(rr.REVIEW_DATE,'%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE mp
join REST_REVIEW rr
on mp.MEMBER_ID = rr.MEMBER_ID
where mp.MEMBER_ID = (
    select MEMBER_ID
    from REST_REVIEW
    group by MEMBER_ID
    order by count(*) desc
    limit 1
)
ORDER BY rr.REVIEW_DATE ASC, rr.REVIEW_TEXT ASC;