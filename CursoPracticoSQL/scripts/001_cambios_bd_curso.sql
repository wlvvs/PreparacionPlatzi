ALTER DATABASE db_music RENAME TO db_platzi;

CREATE SCHEMA platzi AUTHORIZATION postgres;

GRANT ALL ON SCHEMA platzi TO postgres;
