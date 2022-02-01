-- Script for list the numbers of records with the same score of the table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
