/*
Cambios referidos a un detalle con la determinación del genero musical de un disco con respecto a catalogos.
Este cambio hara que el disco rija el genero de la banda y de alcance tambien a los sub generos asociados al disco
*/

ALTER TABLE ct_bands DROP CONSTRAINT fk_ctmusgnd_ctbnd_musgnd;

ALTER TABLE ct_bands DROP COLUMN llmusicalgender;

ALTER TABLE crc_musicalgenders_musicalsubgenders RENAME TO crc_musicalgenders_musicalsubgenders_albums;

ALTER TABLE crc_musicalgenders_musicalsubgenders_albums ADD llalbum integer NOT NULL;

ALTER TABLE crc_musicalgenders_musicalsubgenders_albums MODIFY COLUMN llalbum int NOT NULL COMMENT 'llave foranea de album';

ALTER TABLE crc_musicalgenders_musicalsubgenders_albums ADD CONSTRAINT fk_ctalb_crcmusgndmussbgndalb_alb FOREIGN KEY (llalbum) REFERENCES ct_albums (llalbum);

ALTER TABLE crc_musicalgenders_musicalsubgenders_albums DROP CONSTRAINT fk_ctmusgnd_crcmusgndmussbgnd_musgnd;
ALTER TABLE crc_musicalgenders_musicalsubgenders_albums ADD CONSTRAINT fk_ctmusgnd_crcmusgndmussbgndalb_musgnd FOREIGN KEY (llmusicalgender) REFERENCES ct_musicalgenders (llmusicalgender);

ALTER TABLE crc_musicalgenders_musicalsubgenders_albums DROP CONSTRAINT fk_ctmussbgnd_crcmusgndmussbgnd_mussbgnd;
ALTER TABLE crc_musicalgenders_musicalsubgenders_albums ADD CONSTRAINT fk_ctmussbgnd_crcmusgndmussbgndalb_mussbgnd FOREIGN KEY (llmusicalsubgender) REFERENCES ct_musicalsubgenders (llmusicalsubgender);

ALTER TABLE crc_musicalgenders_musicalsubgenders_albums MODIFY COLUMN llmusicalsubgender int NULL COMMENT 'llave foranea de subgenero musical';
