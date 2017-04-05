1.
SELECT C.circode, C.cirname, C.city, COUNT(P.circode)
FROM Circuit C LEFT JOIN Race P ON C.circode = P.circode
GROUP BY C.circode, C.cirname, C.city;
2.
SELECT DISTINCT E.teamcode, E.teamname
FROM Team E, Driver P
WHERE P.teamcode=E.teamcode AND P.birthdate > '01/01/1985';
3.
SELECT P.num, P.drivername
FROM Driver P
WHERE 3 <= (SELECT COUNT(*) FROM Participates Pa
 WHERE P.num = Pa.num AND Pa.puntos > 5);
4.
SELECT circode, cirname
FROM Circuit
WHERE km > (SELECT AVG(km) FROM Circuit); 
5.
SELECT C.circode, C.cirname
FROM Circuit C
WHERE NOT EXISTS (SELECT * FROM Race P WHERE P.circode=C.circode
 AND P.num_drivers <= 10)
 AND EXISTS (SELECT * FROM Race P WHERE P.circode=C.circode);
Another option, without using the derived attribute, is:
SELECT C.circode, C.cirname
FROM Circuit C
WHERE NOT EXISTS (SELECT * FROM Race P WHERE P.circode=C.circode
 AND 10 >= (SELECT COUNT(*) FROM Participates Pa
 WHERE Pa.year=P.year AND Pa.circode=P.circode))
 AND EXISTS (SELECT * FROM Race P WHERE P.circode=C.circode);
6.
SELECT P.num, P.drivername
FROM Driver P
WHERE 6 <= (SELECT COUNT(*) FROM Participates Pa
 WHERE P.num = Pa.num AND Pa.year = 2004);
7.
SELECT P.num, P.drivername
FROM Driver P, Participates Pa
WHERE P.num = Pa.num
GROUP BY P.num, P.drivername
HAVING COUNT(*) >= ALL (SELECT COUNT(*) FROM Participates Pa2
 GROUP BY Pa2.num); 