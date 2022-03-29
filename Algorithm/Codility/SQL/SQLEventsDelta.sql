
-- PostgreSQL
-- write your code in PostgreSQL 9.4
SELECT event_type, num1 - num2 AS value
FROM (
  SELECT 
    event_type
    ,MAX(CASE WHEN rnk = 1 THEN value END) AS num1
    ,MAX(CASE WHEN rnk = 2 THEN value END) AS num2
  FROM (
    SELECT 
      event_type
      , RANK() OVER(
          PARTITION BY event_type 
          ORDER BY event_type ASC, time DESC) AS rnk 
      ,value
    FROM events
  ) AS t1 
  WHERE rnk < 3
  GROUP BY event_type
) as t2
WHERE num1 - num2 IS NOT NULL
;
