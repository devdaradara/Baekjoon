-- 코드를 작성해주세요

SELECT E.DEPT_ID, 
    DEPT_NAME_EN, 
    ROUND(AVG(SAL)) AVG_SAL
FROM HR_EMPLOYEES E
    JOIN HR_DEPARTMENT D ON E.DEPT_ID = D.DEPT_ID
GROUP BY DEPT_ID
ORDER BY AVG_SAL DESC