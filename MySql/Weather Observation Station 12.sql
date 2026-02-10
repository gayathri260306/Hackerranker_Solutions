-- Problem: Weather Observation Station 12
-- Difficulty: Easy
--Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.

select distinct city from station
where city regexp '^[^aeiouAEIOU]' AND city regexp '[^aeiouAEIOU]$';
