-- script that  lists all records with a score >= 10 in the table second_table of database hbtn_0c_0
-- does not fail
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
