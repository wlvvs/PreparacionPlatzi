insert into ct_labels (dslabel, fcfechacreacion) values ('Columbia Records','1890-01-15');
insert into ct_labels (dslabel, fcfechacreacion) values ('DGC Records','1990-01-01');
insert into ct_labels (dslabel, fcfechacreacion) values ('Fat Possum Records','1992-06-04');

--

insert into ct_musicalgenders (dsmusicalgender) values ('Rock');
insert into ct_musicalgenders (dsmusicalgender) values ('Grunge');

--

insert into ct_musicalsubgenders (dsmusicalsubgender) values('Alternative');
insert into ct_musicalsubgenders (dsmusicalsubgender) values('Folk');
insert into ct_musicalsubgenders (dsmusicalsubgender) values('Jazz');
insert into ct_musicalsubgenders (dsmusicalsubgender) values('Blues');
insert into ct_musicalsubgenders (dsmusicalsubgender) values('Garage');

--

ALTER TABLE ct_nationalities CHANGE dsnacionalidad dsnationality varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'descripcion de nacionalidad';

insert into ct_nationalities (dsnationality) values ('American');
insert into ct_nationalities (dsnationality) values ('German');
insert into ct_nationalities (dsnationality) values ('Danish');

--

insert into ct_bands (dsbanda, fcfechacreacion, boestatus, llnationality) values ('Jeff Buckley','1990-02-01', 0, 1);
insert into ct_bands (dsbanda, fcfechacreacion, boestatus, llnationality) values ('Nirvana','1987-04-12', 0, 1);
insert into ct_bands (dsbanda, fcfechacreacion, llnationality) values ('The Black Keys','2001-12-21',1);

--

insert into ct_albums (dsnombrealbum, fcfechapublicacion, tmduracion, lllabel, llband) values ('Grace','1994-08-23','00:51:43',1,1);
insert into ct_albums (dsnombrealbum, fcfechapublicacion, tmduracion, lllabel, llband) values ('Nevermind','1991-09-24','00:49:07',2,2);
insert into ct_albums (dsnombrealbum, fcfechapublicacion, tmduracion, lllabel, llband) values ('Thickfreakness','2003-04-08','00:39:01',3,3);

--

insert into crc_musicalgenders_musicalsubgenders_albums (llmusicalgender, llmusicalsubgender, llalbum) values (1,1,1);
insert into crc_musicalgenders_musicalsubgenders_albums (llmusicalgender, llmusicalsubgender, llalbum) values (1,2,1);
insert into crc_musicalgenders_musicalsubgenders_albums (llmusicalgender, llmusicalsubgender, llalbum) values (1,3,1);
insert into crc_musicalgenders_musicalsubgenders_albums (llmusicalgender, llmusicalsubgender, llalbum) values (2,NULL,2);
insert into crc_musicalgenders_musicalsubgenders_albums (llmusicalgender, llmusicalsubgender, llalbum) values (1,1,2);
insert into crc_musicalgenders_musicalsubgenders_albums (llmusicalgender, llmusicalsubgender, llalbum) values (1,4,3);
insert into crc_musicalgenders_musicalsubgenders_albums (llmusicalgender, llmusicalsubgender, llalbum) values (1,5,3);

--

insert into ct_bandmembers (dsnombre, dsapellido1, dsapellido2, dsaka, fcfechanacimiento, boestatus, llnationality) values ('Jeff','Scott','Buckley','Scott Moorhead','1966-11-17', 0, 1);
insert into ct_bandmembers (dsnombre, dsapellido1, dsapellido2, dsaka, fcfechanacimiento, boestatus, llnationality) values ('Karl','Hans','Berger',NULL,'1935-03-30', 0, 2);
insert into ct_bandmembers (dsnombre, dsapellido1, dsapellido2, dsaka, fcfechanacimiento, boestatus, llnationality) values ('Mick','Grondahl',NULL,NULL,'1968-05-07', 0, 3);
insert into ct_bandmembers (dsnombre, dsapellido1, dsapellido2, dsaka, fcfechanacimiento, boestatus, llnationality) values ('Michael','Oliver','Tighe',NULL,'1969-04-15', 0, 1);
insert into ct_bandmembers (dsnombre, dsapellido1, dsapellido2, dsaka, fcfechanacimiento, boestatus, llnationality) values ('Andy','Wallace',NULL,NULL,'1947-07-25', 0, 1);
insert into ct_bandmembers (dsnombre, dsapellido1, dsapellido2, dsaka, fcfechanacimiento, boestatus, llnationality) values ('Kurt','Donald','Cobain',NULL,'1967-02-20', 0, 1);
insert into ct_bandmembers (dsnombre, dsapellido1, dsapellido2, dsaka, fcfechanacimiento, boestatus, llnationality) values ('Krist','Anthony','Novoselic',NULL,'1965-05-16', 0, 1);
insert into ct_bandmembers (dsnombre, dsapellido1, dsapellido2, dsaka, fcfechanacimiento, boestatus, llnationality) values ('David','Eric','Grohl','Late!','1969-01-14', 0, 1);
insert into ct_bandmembers (dsnombre, dsapellido1, dsapellido2, dsaka, fcfechanacimiento, boestatus, llnationality) values ('Bryan','David','Vig','Butch','1955-08-02', 0, 1);
insert into ct_bandmembers (dsnombre, dsapellido1, dsapellido2, dsaka, fcfechanacimiento, boestatus, llnationality) values ('Daniel','Quine','Auerbach',NULL,'1979-05-14', 1, 1);
insert into ct_bandmembers (dsnombre, dsapellido1, dsapellido2, dsaka, fcfechanacimiento, boestatus, llnationality) values ('Patrick','James','Cartney',NULL,'1980-04-15', 1, 1);

--

insert into ct_bandroles (dsbandrole) values ('Singer');
insert into ct_bandroles (dsbandrole) values ('Songwriter');
insert into ct_bandroles (dsbandrole) values ('Guitarrist');
insert into ct_bandroles (dsbandrole) values ('Keyboards');
insert into ct_bandroles (dsbandrole) values ('Bass');
insert into ct_bandroles (dsbandrole) values ('Producer');
insert into ct_bandroles (dsbandrole) values ('Enginer');
insert into ct_bandroles (dsbandrole) values ('Drums');
insert into ct_bandroles (dsbandrole) values ('Mixer');
insert into ct_bandroles (dsbandrole) values ('Percussion');

--

insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (1,1);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (1,2);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (1,3);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (2,4);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (3,5);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (4,3);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (5,6);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (5,7);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (6,1);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (6,3);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (6,8);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (7,1);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (7,5);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (8,1);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (8,8);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (9,6);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (9,7);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (5,9);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (10,1);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (10,3);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (10,5);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (11,6);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (11,8);
insert into crc_bandmember_bandroles (llbandmember, llbandrole) values (11,10);

--

insert into crc_bands_bandmembers (llband, llbandmember, fcfechainicio, fcfechafin, boestatus) values (1,1,'1990-02-01','1997-05-29', 0);
insert into crc_bands_bandmembers (llband, llbandmember, fcfechainicio, fcfechafin, boestatus) values (1,2,'1993-12-01','1994-08-23', 0);
insert into crc_bands_bandmembers (llband, llbandmember, fcfechainicio, fcfechafin, boestatus) values (1,3,'1990-02-01','1997-05-29', 0);
insert into crc_bands_bandmembers (llband, llbandmember, fcfechainicio, fcfechafin, boestatus) values (1,4,'1993-12-01','1994-08-23', 0);
insert into crc_bands_bandmembers (llband, llbandmember, fcfechainicio, fcfechafin, boestatus) values (1,5,'1993-12-01','1994-08-23', 0);
insert into crc_bands_bandmembers (llband, llbandmember, fcfechainicio, fcfechafin, boestatus) values (2,6,'1987-03-15','1994-04-05', 0);
insert into crc_bands_bandmembers (llband, llbandmember, fcfechainicio, fcfechafin, boestatus) values (2,7,'1987-03-15','1994-04-05', 0);
insert into crc_bands_bandmembers (llband, llbandmember, fcfechainicio, fcfechafin, boestatus) values (2,8,'1987-03-15','1994-04-05', 0);
insert into crc_bands_bandmembers (llband, llbandmember, fcfechainicio, fcfechafin, boestatus) values (2,9,'1990-04-10','1991-09-24', 0);
insert into crc_bands_bandmembers (llband, llbandmember, fcfechainicio, fcfechafin, boestatus) values (2,5,'1990-04-10','1991-09-24', 0);
insert into crc_bands_bandmembers (llband, llbandmember, fcfechainicio, fcfechafin, boestatus) values (3,10,'2001-12-21',NULL, 1);
insert into crc_bands_bandmembers (llband, llbandmember, fcfechainicio, fcfechafin, boestatus) values (3,11,'2001-12-21',NULL, 1);
