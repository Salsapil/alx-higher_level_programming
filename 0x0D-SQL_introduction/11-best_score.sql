-- a script that lists all records with a score of the database hbtn_0c_0 in your MySQL server.
-- Select the best
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
