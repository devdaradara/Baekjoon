-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) YEAR,
    MONTH(SALES_DATE) MONTH,
    GENDER,
    COUNT(DISTINCT U.USER_ID) USERS
FROM ONLINE_SALE O
    JOIN USER_INFO U ON U.USER_ID = O.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY 1, 2, 3
ORDER BY 1, 2, 3