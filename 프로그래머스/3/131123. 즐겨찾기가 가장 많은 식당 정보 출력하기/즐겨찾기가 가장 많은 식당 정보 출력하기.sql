-- 코드를 입력하세요
WITH MANY_FAVORITE AS (
    SELECT FOOD_TYPE, MAX(FAVORITES) FAVORITES
    FROM REST_INFO
    GROUP BY FOOD_TYPE
)

SELECT I.FOOD_TYPE, REST_ID, REST_NAME, I.FAVORITES
FROM REST_INFO I, MANY_FAVORITE F
WHERE I.FOOD_TYPE = F.FOOD_TYPE
    AND I.FAVORITES = F.FAVORITES
ORDER BY I.FOOD_TYPE DESC


# SELECT * FROM MANY_FAVORITE