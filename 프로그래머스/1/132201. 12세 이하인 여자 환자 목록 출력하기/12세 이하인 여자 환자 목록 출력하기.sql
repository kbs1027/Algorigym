-- 코드를 입력하세요
SELECT PT_NAME,PT_NO,GEND_CD, AGE, if(TLNO is null,'NONE', TLNO) as TLNO
from PATIENT
where GEND_CD = 'W'
AND AGE <=12
order by AGE DESC, PT_NAME asc