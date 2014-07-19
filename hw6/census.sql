-- Week 6 Problem 1 Template

DROP TABLE IF EXISTS myCensus;
CREATE TABLE myCensus -- your code goes here

.separator ,
.import ss12pil_sql.csv myCensus

-- uncomment below to check the first 10 lines
-- SELECT * FROM myCensus LIMIT 10;

DROP TABLE IF EXISTS moreCensus;
CREATE TABLE moreCensus -- your code goes here

.separator ,
.import ss12pil_favorite_number.csv moreCensus

-- uncomment below to check the first 10 lines
-- SELECT * FROM moreCensus LIMIT 10;

DROP TABLE IF EXISTS myMoreCensus;
CREATE TABLE myMoreCensus AS SELECT -- your code goes here

-- uncomment below to check the first 10 lines
-- SELECT * FROM myMoreCensus LIMIT 10;

INSERT -- your code goes here

SELECT -- your code goes here
