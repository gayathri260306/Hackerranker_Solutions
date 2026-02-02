-- Problem: Weather Observation Station 4
-- Difficulty: Easy
--Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

SELECT count(city)-count(distinct city) from station;
