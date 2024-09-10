SELECT ai.ANIMAL_ID, ai.ANIMAL_TYPE, ai.NAME
from ANIMAL_INS ai
join ANIMAL_OUTS ao
on ai.ANIMAL_ID = ao.ANIMAL_ID
where (ao.SEX_UPON_OUTCOME like '%Neutered%' or ao.SEX_UPON_OUTCOME like '%Spayed%')
and ai.SEX_UPON_INTAKE like '%Intact%'