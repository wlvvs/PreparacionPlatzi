-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: db_music
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `crc_bandmember_bandroles`
--

DROP TABLE IF EXISTS `crc_bandmember_bandroles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `crc_bandmember_bandroles` (
  `llbandmemberbandrole` int NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de cruce de miembro con role',
  `llbandmember` int NOT NULL COMMENT 'llave foranea de miembro de banda',
  `llbandrole` int NOT NULL COMMENT 'llave foranea de rol de miembro en la banda',
  PRIMARY KEY (`llbandmemberbandrole`),
  KEY `fk_ctbndmem_crcbndmembndrole_bndmem` (`llbandmember`),
  KEY `fk_ctbndrole_crcbndmembndrole_bndrole` (`llbandrole`),
  CONSTRAINT `fk_ctbndmem_crcbndmembndrole_bndmem` FOREIGN KEY (`llbandmember`) REFERENCES `ct_bandmembers` (`llbandmember`),
  CONSTRAINT `fk_ctbndrole_crcbndmembndrole_bndrole` FOREIGN KEY (`llbandrole`) REFERENCES `ct_bandroles` (`llbandrole`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crc_bandmember_bandroles`
--

LOCK TABLES `crc_bandmember_bandroles` WRITE;
/*!40000 ALTER TABLE `crc_bandmember_bandroles` DISABLE KEYS */;
/*!40000 ALTER TABLE `crc_bandmember_bandroles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crc_bands_bandmembers`
--

DROP TABLE IF EXISTS `crc_bands_bandmembers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `crc_bands_bandmembers` (
  `llbandbandmember` int NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de cruce entre banda e integrantes',
  `llband` int NOT NULL COMMENT 'llave foranea de banda',
  `llbandmember` int NOT NULL COMMENT 'llave foranea de integrante de banda',
  `fcfechainicio` date NOT NULL COMMENT 'fecha en que inicio en la banda',
  `fcfechafin` date DEFAULT NULL COMMENT 'fecha en que dejo la banda',
  `boestatus` tinyint(1) NOT NULL DEFAULT '1' COMMENT 'valor booleano que indica si el registro esta activo o inactivo',
  PRIMARY KEY (`llbandbandmember`),
  KEY `fk_ctbnd_crcbndbndmem_bnd` (`llband`),
  KEY `fk_ctbndmem_crcbndbndmem_bndmem` (`llbandmember`),
  CONSTRAINT `fk_ctbnd_crcbndbndmem_bnd` FOREIGN KEY (`llband`) REFERENCES `ct_bands` (`llband`),
  CONSTRAINT `fk_ctbndmem_crcbndbndmem_bndmem` FOREIGN KEY (`llbandmember`) REFERENCES `ct_bandmembers` (`llbandmember`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crc_bands_bandmembers`
--

LOCK TABLES `crc_bands_bandmembers` WRITE;
/*!40000 ALTER TABLE `crc_bands_bandmembers` DISABLE KEYS */;
/*!40000 ALTER TABLE `crc_bands_bandmembers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `crc_musicalgenders_musicalsubgenders`
--

DROP TABLE IF EXISTS `crc_musicalgenders_musicalsubgenders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `crc_musicalgenders_musicalsubgenders` (
  `llmusicalgendersubgender` int NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de cruce de generos y subgeneros musicales',
  `llmusicalgender` int NOT NULL COMMENT 'llave foranea de generos musicales',
  `llmusicalsubgender` int NOT NULL COMMENT 'llave foranea de subgenero musical',
  PRIMARY KEY (`llmusicalgendersubgender`),
  KEY `fk_ctmusgnd_crcmusgndmussbgnd_musgnd` (`llmusicalgender`),
  KEY `fk_ctmussbgnd_crcmusgndmussbgnd_mussbgnd` (`llmusicalsubgender`),
  CONSTRAINT `fk_ctmusgnd_crcmusgndmussbgnd_musgnd` FOREIGN KEY (`llmusicalgender`) REFERENCES `ct_musicalgenders` (`llmusicalgender`),
  CONSTRAINT `fk_ctmussbgnd_crcmusgndmussbgnd_mussbgnd` FOREIGN KEY (`llmusicalsubgender`) REFERENCES `ct_musicalsubgenders` (`llmusicalsubgender`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crc_musicalgenders_musicalsubgenders`
--

LOCK TABLES `crc_musicalgenders_musicalsubgenders` WRITE;
/*!40000 ALTER TABLE `crc_musicalgenders_musicalsubgenders` DISABLE KEYS */;
/*!40000 ALTER TABLE `crc_musicalgenders_musicalsubgenders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ct_albums`
--

DROP TABLE IF EXISTS `ct_albums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ct_albums` (
  `llalbum` int NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de la tabla de albums',
  `dsnombrealbum` varchar(200) NOT NULL COMMENT 'descripcion de nombre de album',
  `fcfechapublicacion` date NOT NULL COMMENT 'fecha de publicacion de album',
  `tmduracion` time NOT NULL COMMENT 'tiempo de duracion del album',
  `lllabel` int NOT NULL COMMENT 'llave foranea de casa productora',
  `llband` int NOT NULL,
  PRIMARY KEY (`llalbum`),
  KEY `fk_ctbnd_ctalb_bnd` (`llband`),
  KEY `fk_ctlbl_ctalb_lbl` (`lllabel`),
  CONSTRAINT `fk_ctbnd_ctalb_bnd` FOREIGN KEY (`llband`) REFERENCES `ct_bands` (`llband`),
  CONSTRAINT `fk_ctlbl_ctalb_lbl` FOREIGN KEY (`lllabel`) REFERENCES `ct_labels` (`lllabel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ct_albums`
--

LOCK TABLES `ct_albums` WRITE;
/*!40000 ALTER TABLE `ct_albums` DISABLE KEYS */;
/*!40000 ALTER TABLE `ct_albums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ct_bandmembers`
--

DROP TABLE IF EXISTS `ct_bandmembers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ct_bandmembers` (
  `llbandmember` int NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de integrantes de banda',
  `dsnombre` varchar(50) NOT NULL COMMENT 'descripcion de nombre de integrante',
  `dsapellido1` varchar(50) NOT NULL COMMENT 'descripcion de primer apellido',
  `dsapellido2` varchar(50) DEFAULT NULL COMMENT 'descripcion de segundo apellido',
  `dsaka` varchar(80) DEFAULT NULL COMMENT 'descripcion de pseudonimo conocido',
  `fcfechanacimiento` date NOT NULL COMMENT 'fecha de nacimiento',
  `boestatus` tinyint(1) NOT NULL DEFAULT '1' COMMENT 'valor booleano que indica si el registro esta activo o inactivo',
  `llnationality` int NOT NULL COMMENT 'llave foranea de nacionalidad',
  PRIMARY KEY (`llbandmember`),
  KEY `fk_ctnat_ctbndmem_nat` (`llnationality`),
  CONSTRAINT `fk_ctnat_ctbndmem_nat` FOREIGN KEY (`llnationality`) REFERENCES `ct_nationalities` (`llnationality`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ct_bandmembers`
--

LOCK TABLES `ct_bandmembers` WRITE;
/*!40000 ALTER TABLE `ct_bandmembers` DISABLE KEYS */;
/*!40000 ALTER TABLE `ct_bandmembers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ct_bandroles`
--

DROP TABLE IF EXISTS `ct_bandroles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ct_bandroles` (
  `llbandrole` int NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de actividades dentro de la banda',
  `dsbandrole` varchar(100) NOT NULL COMMENT 'descripcion de role dentro de la banda',
  `boestatus` tinyint(1) NOT NULL DEFAULT '1' COMMENT 'valor booleano que indica si el registro esta activo o inactivo',
  PRIMARY KEY (`llbandrole`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ct_bandroles`
--

LOCK TABLES `ct_bandroles` WRITE;
/*!40000 ALTER TABLE `ct_bandroles` DISABLE KEYS */;
/*!40000 ALTER TABLE `ct_bandroles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ct_bands`
--

DROP TABLE IF EXISTS `ct_bands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ct_bands` (
  `llband` int NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de banda',
  `dsbanda` varchar(100) NOT NULL COMMENT 'descripcion de nombre de banda',
  `fcfechacreacion` date NOT NULL COMMENT 'fecha de creacion de banda',
  `llmusicalgender` int NOT NULL COMMENT 'llave foranea de genero musical',
  `llnationality` int NOT NULL COMMENT 'llave foranea de nacionalidad',
  `boestatus` tinyint(1) NOT NULL DEFAULT '1' COMMENT 'valor booleano que indica si la banda esta activa o inactiva',
  PRIMARY KEY (`llband`),
  KEY `fk_ctmusgnd_ctbnd_musgnd` (`llmusicalgender`),
  KEY `fk_ctnat_ctbnd_nat` (`llnationality`),
  CONSTRAINT `fk_ctmusgnd_ctbnd_musgnd` FOREIGN KEY (`llmusicalgender`) REFERENCES `ct_musicalgenders` (`llmusicalgender`),
  CONSTRAINT `fk_ctnat_ctbnd_nat` FOREIGN KEY (`llnationality`) REFERENCES `ct_nationalities` (`llnationality`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ct_bands`
--

LOCK TABLES `ct_bands` WRITE;
/*!40000 ALTER TABLE `ct_bands` DISABLE KEYS */;
/*!40000 ALTER TABLE `ct_bands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ct_labels`
--

DROP TABLE IF EXISTS `ct_labels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ct_labels` (
  `lllabel` int NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de casas productoras',
  `dslabel` varchar(100) NOT NULL COMMENT 'descripcion de nombre de casa productora',
  `boestatus` tinyint(1) NOT NULL DEFAULT '1' COMMENT 'valor booleano que indica si la casa productora esta activa o inactiva',
  `fcfechacreacion` date NOT NULL COMMENT 'fecha de apertura de la casa productora',
  PRIMARY KEY (`lllabel`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ct_labels`
--

LOCK TABLES `ct_labels` WRITE;
/*!40000 ALTER TABLE `ct_labels` DISABLE KEYS */;
/*!40000 ALTER TABLE `ct_labels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ct_musicalgenders`
--

DROP TABLE IF EXISTS `ct_musicalgenders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ct_musicalgenders` (
  `llmusicalgender` int NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de generos musicales',
  `dsmusicalgender` varchar(50) NOT NULL COMMENT 'descripcion de genero musical',
  `boestatus` tinyint(1) NOT NULL DEFAULT '1' COMMENT 'valor booleano que indica si el registro esta activo o inactivo',
  PRIMARY KEY (`llmusicalgender`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ct_musicalgenders`
--

LOCK TABLES `ct_musicalgenders` WRITE;
/*!40000 ALTER TABLE `ct_musicalgenders` DISABLE KEYS */;
/*!40000 ALTER TABLE `ct_musicalgenders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ct_musicalsubgenders`
--

DROP TABLE IF EXISTS `ct_musicalsubgenders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ct_musicalsubgenders` (
  `llmusicalsubgender` int NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de subgeneros musicales',
  `dsmusicalsubgender` varchar(50) NOT NULL COMMENT 'descripcion de subgenero musical',
  `boestatus` tinyint(1) NOT NULL DEFAULT '1' COMMENT 'valor booleano que indica si el registro esta activo o inactivo',
  PRIMARY KEY (`llmusicalsubgender`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ct_musicalsubgenders`
--

LOCK TABLES `ct_musicalsubgenders` WRITE;
/*!40000 ALTER TABLE `ct_musicalsubgenders` DISABLE KEYS */;
/*!40000 ALTER TABLE `ct_musicalsubgenders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ct_nationalities`
--

DROP TABLE IF EXISTS `ct_nationalities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ct_nationalities` (
  `llnationality` int NOT NULL AUTO_INCREMENT COMMENT 'llave primaria de nacionalidades',
  `dsnacionalidad` varchar(100) NOT NULL COMMENT 'descripcion de nacionalidad',
  PRIMARY KEY (`llnationality`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ct_nationalities`
--

LOCK TABLES `ct_nationalities` WRITE;
/*!40000 ALTER TABLE `ct_nationalities` DISABLE KEYS */;
/*!40000 ALTER TABLE `ct_nationalities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'db_music'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-12 17:55:31
