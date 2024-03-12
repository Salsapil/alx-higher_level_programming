-- a script that lists the number of records with the same score of the database hbtn_0c_0 in your MySQL server.
-- number by score
SELECT score, Count(*) as number FROM second_table GROUP BY score;
