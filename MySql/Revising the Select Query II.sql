-- Problem: Revising the Select Query II
-- Difficulty: Easy
--Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
SELECT name from city
where countrycode='USA' and population>120000;
