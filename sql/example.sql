#### 상위 몇건 조회


- ORACLE
SELECT NAME 
FROM ( SELECT NAME
      FROM ANIMAL_INS
      ORDER BY  DATETIME)
WHERE ROWNUM < 2;

- MYSQL

SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1


#### 중복 카운트

- ORACLE/MYSQL
SELECT COUNT(DISTINCT NAME)
FROM ANIMAL_INS;

#### 날짜형


- MYSQL
SELECT DATE_FORMAT(DATETIME, '%Y-%m-%d %h:%i:%s') FROM ANIMAL_OUTS;



- ORACLE
REGULAR EXPRESSION
https://kutar37.tistory.com/entry/oracle-REGEXPLIKE

RIGHT, LEFT
https://www.hackerrank.com/challenges/more-than-75-marks/forum
https://pangate.com/675

오른쪽 왼쪽 처리에 대해 같은 결과지만 다른 방법으로 풀어내고 있음


