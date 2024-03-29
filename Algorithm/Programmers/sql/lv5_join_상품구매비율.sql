# level5 - join 
#상품을 구매한 회원 비율 구하기
#https://school.programmers.co.kr/learn/courses/30/lessons/131534


# CASE 1.

SELECT
    SUBSTRING(SALES_DATE,1,4) AS YEAR
    ,SUBSTRING(SALES_DATE,5,6) AS MONTH
    ,SALES_CNT AS PUCHASED_USERS
    ,ROUND(SALES_CNT/USER_CNT,1) AS PUCHASED_RATIO
FROM (
    SELECT
        COUNT(DISTINCT OS.USER_ID) AS SALES_CNT
        ,DATE_FORMAT(OS.SALES_DATE,'%Y%m') AS SALES_DATE
        ,MAX(U.CNT) AS USER_CNT
    FROM ONLINE_SALE AS OS
    INNER JOIN (
        SELECT USER_ID, COUNT(*) OVER() AS CNT
        FROM USER_INFO
        WHERE JOINED >= '2021-01-01' AND JOINED <= '2021-12-31'
    ) AS U
    ON OS.USER_ID = U.USER_ID
    GROUP BY 2
) AS T
ORDER BY YEAR,MONTH ASC

