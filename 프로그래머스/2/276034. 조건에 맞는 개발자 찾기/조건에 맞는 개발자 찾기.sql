-- 코드를 작성해주세요

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE & (
    SELECT SUM(CODE)
    FROM SKILLCODES S
    WHERE NAME IN ("C#", "PYTHON")
) > 0
ORDER BY ID