-- Summer/Winter Coding(2019)
-- level4 - SQL : 우유와 요거트가 담긴 장바구니

SELECT CART_ID FROM (
	SELECT CART_ID, GROUP_CONCAT(NAME SEPARATOR ',') AS NAMES FROM CART_PRODUCTS
	WHERE NAME = '우유' OR NAME = '요거트'
	GROUP BY CART_ID HAVING NAMES LIKE '%우유%' AND NAMES LIKE '%요거트%'
) AS MILK_YOGERT