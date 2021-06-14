/*
Cambios referidos a un detalle con la determinación del genero musical de un disco con respecto a catalogos.
Este cambio hara que el disco rija el genero de la banda y de alcance tambien a los sub generos asociados al disco
*/

ALTER TABLE ct_bands DROP CONSTRAINT fk_ctmusgnd_ctbnd_musgnd;

ALTER TABLE ct_bands DROP COLUMN llmusicalgender;

ALTER TABLE crc_musicalgenders_musicalsubgenders RENAME TO crc_musicalgenders_musicalsubgenders_albums;

COMMENT ON
TABLE crc_musicalgenders_musicalsubgenders_albums IS 'tabla de cruce entre generos musicales y subgeneros musicales asociados a un album en especifico';

ALTER TABLE crc_musicalgenders_musicalsubgenders_albums ADD llalbum integer NOT NULL;

COMMENT ON
COLUMN crc_musicalgenders_musicalsubgenders_albums.llalbum IS 'llave foranea de album';

ALTER TABLE crc_musicalgenders_musicalsubgenders_albums RENAME CONSTRAINT fk_ctmusgnd_crcmusgndmussbgnd_musgnd TO fk_ctmusgnd_crcmusgndmussbgndalb_musgnd;

ALTER TABLE crc_musicalgenders_musicalsubgenders_albums RENAME CONSTRAINT fk_ctmussbgnd_crcmusgndmussbgnd_mussbgnd TO fk_ctmussbgnd_crcmusgndmussbgndalb_mussbgnd;

ALTER TABLE crc_musicalgenders_musicalsubgenders_albums ADD CONSTRAINT fk_ctalb_crcmusgndmussbgndalb_alb FOREIGN KEY (llalbum) REFERENCES ct_albums (llalbum);

ALTER TABLE crc_musicalgenders_musicalsubgenders_albums ALTER COLUMN llmusicalsubgender DROP NOT NULL;
