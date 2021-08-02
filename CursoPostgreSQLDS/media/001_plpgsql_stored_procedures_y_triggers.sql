CREATE OR REPLACE PROCEDURE test_dropcreate_procedure()
LANGUAGE SQL
AS $$
    DROP TABLE IF EXISTS aaa;
	CREATE TABLE aaa (bbb char(5) CONSTRAINT firstkey PRIMARY KEY);
$$;

CALL test_dropcreate_procedure();

CREATE OR REPLACE FUNCTION test_dropcreate_function()
RETURNS VOID
LANGUAGE plpgsql
AS $$
BEGIN
	DROP TABLE IF EXISTS aaa;
	CREATE TABLE aaa (bbb char(5) CONSTRAINT firstkey PRIMARY KEY, ccc char(5));
	DROP TABLE IF EXISTS aaab;
	CREATE TABLE aaab (bbba char(5) CONSTRAINT secondkey PRIMARY KEY, ccca char(5));
END
$$;

SELECT test_dropcreate_function();

---------

CREATE OR REPLACE FUNCTION count_total_movies()
RETURNS int
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN COUNT(*) FROM peliculas;
END
$$;

SELECT count_total_movies();

CREATE OR REPLACE FUNCTION duplicate_records()
  RETURNS trigger AS
$$
BEGIN
	INSERT INTO aaab(bbba, ccca)
	VALUES(NEW.bbb, NEW.ccc);
   	RETURN NEW;
END
$$ LANGUAGE plpgsql;

CREATE TRIGGER aaa_changes
	BEFORE INSERT
	ON aaa
	FOR EACH ROW
	EXECUTE PROCEDURE duplicate_records();

INSERT INTO aaa (bbb, ccc)
VALUES ('asdfl', 'nuevo');

DROP TRIGGER IF EXISTS aaa_changes
ON aaa;