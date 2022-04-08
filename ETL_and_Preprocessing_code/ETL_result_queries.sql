-- check tables loaded from ETL correctly

SELECT * FROM public."Genome_Scores"
LIMIT 100

SELECT COUNT(*) FROM public."Genome_Scores"
 
SELECT * FROM public."Genome_Tags"
LIMIT 100

SELECT COUNT(*) FROM public."Genome_Tags"

SELECT * FROM public."Links"
LIMIT 100

SELECT COUNT(*) FROM public."Links"

SELECT * FROM public."Movies"
LIMIT 100

SELECT COUNT(*) FROM public."Movies"

SELECT * FROM public."Ratings"
LIMIT 100

SELECT COUNT(*) FROM public."Ratings"

SELECT * FROM public."Tags"
LIMIT 100

SELECT COUNT(*) FROM public."Tags"

--all tables loaded with unwanted "index" column

--copy links table for testing 

SELECT * 
INTO public."copy_links"
FROM public."Links"

-- drop index column from copy_links

SELECT * FROM public."copy_links"
LIMIT 100

ALTER TABLE public."copy_links"
DROP COLUMN index

SELECT * FROM public."copy_links"
LIMIT 100

-- delete copy_links table 

DROP TABLE public."copy_links"

-- drop index column from tables

ALTER TABLE public."Genome_Scores"
DROP COLUMN index

ALTER TABLE public."Genome_Tags"
DROP COLUMN index

ALTER TABLE public."Links"
DROP COLUMN index

ALTER TABLE public."Movies"
DROP COLUMN index

ALTER TABLE public."Ratings"
DROP COLUMN index

ALTER TABLE public."Tags"
DROP COLUMN index

