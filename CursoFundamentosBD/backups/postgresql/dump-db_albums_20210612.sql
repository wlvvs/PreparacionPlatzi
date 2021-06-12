--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

-- Started on 2021-06-12 17:59:21

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 8 (class 2615 OID 117953)
-- Name: db_albums; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA db_albums;


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 224 (class 1259 OID 118013)
-- Name: crc_bandmember_bandroles; Type: TABLE; Schema: db_albums; Owner: -
--

CREATE TABLE db_albums.crc_bandmember_bandroles (
    llbandmemberbandrole integer NOT NULL,
    llbandmember integer NOT NULL,
    llbandrole integer NOT NULL
);


--
-- TOC entry 2941 (class 0 OID 0)
-- Dependencies: 224
-- Name: TABLE crc_bandmember_bandroles; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON TABLE db_albums.crc_bandmember_bandroles IS 'cruce de miembro de banda con roles';


--
-- TOC entry 2942 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN crc_bandmember_bandroles.llbandmemberbandrole; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.crc_bandmember_bandroles.llbandmemberbandrole IS 'llave primaria de cruce de miembro con role';


--
-- TOC entry 2943 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN crc_bandmember_bandroles.llbandmember; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.crc_bandmember_bandroles.llbandmember IS 'llave foranea de miembro de banda';


--
-- TOC entry 2944 (class 0 OID 0)
-- Dependencies: 224
-- Name: COLUMN crc_bandmember_bandroles.llbandrole; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.crc_bandmember_bandroles.llbandrole IS 'llave foranea de rol de miembro en la banda';


--
-- TOC entry 223 (class 1259 OID 118011)
-- Name: crc_bandmemberbandroles_llbandmemberbandrole_seq; Type: SEQUENCE; Schema: db_albums; Owner: -
--

ALTER TABLE db_albums.crc_bandmember_bandroles ALTER COLUMN llbandmemberbandrole ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME db_albums.crc_bandmemberbandroles_llbandmemberbandrole_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 220 (class 1259 OID 118001)
-- Name: crc_bands_bandmembers; Type: TABLE; Schema: db_albums; Owner: -
--

CREATE TABLE db_albums.crc_bands_bandmembers (
    llbandbandmember integer NOT NULL,
    llband integer NOT NULL,
    llbandmember integer NOT NULL,
    fcfechainicio date NOT NULL,
    fcfechafin date,
    boestatus boolean DEFAULT true NOT NULL
);


--
-- TOC entry 2945 (class 0 OID 0)
-- Dependencies: 220
-- Name: TABLE crc_bands_bandmembers; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON TABLE db_albums.crc_bands_bandmembers IS 'cruce de bandas con miembros de banda';


--
-- TOC entry 2946 (class 0 OID 0)
-- Dependencies: 220
-- Name: COLUMN crc_bands_bandmembers.llbandbandmember; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.crc_bands_bandmembers.llbandbandmember IS 'llave primaria de cruce entre banda e integrantes';


--
-- TOC entry 2947 (class 0 OID 0)
-- Dependencies: 220
-- Name: COLUMN crc_bands_bandmembers.llband; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.crc_bands_bandmembers.llband IS 'llave foranea de banda';


--
-- TOC entry 2948 (class 0 OID 0)
-- Dependencies: 220
-- Name: COLUMN crc_bands_bandmembers.llbandmember; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.crc_bands_bandmembers.llbandmember IS 'llave foranea de integrante de banda';


--
-- TOC entry 2949 (class 0 OID 0)
-- Dependencies: 220
-- Name: COLUMN crc_bands_bandmembers.fcfechainicio; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.crc_bands_bandmembers.fcfechainicio IS 'fecha en que inicio en la banda';


--
-- TOC entry 2950 (class 0 OID 0)
-- Dependencies: 220
-- Name: COLUMN crc_bands_bandmembers.fcfechafin; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.crc_bands_bandmembers.fcfechafin IS 'fecha en que dejo la banda';


--
-- TOC entry 2951 (class 0 OID 0)
-- Dependencies: 220
-- Name: COLUMN crc_bands_bandmembers.boestatus; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.crc_bands_bandmembers.boestatus IS 'valor booleano que indica si el registro esta activo o inactivo';


--
-- TOC entry 219 (class 1259 OID 117999)
-- Name: crc_bands_bandmembers_llbandbandmember_seq; Type: SEQUENCE; Schema: db_albums; Owner: -
--

ALTER TABLE db_albums.crc_bands_bandmembers ALTER COLUMN llbandbandmember ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME db_albums.crc_bands_bandmembers_llbandbandmember_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 214 (class 1259 OID 117985)
-- Name: crc_musicalgenders_musicalsubgenders; Type: TABLE; Schema: db_albums; Owner: -
--

CREATE TABLE db_albums.crc_musicalgenders_musicalsubgenders (
    llmusicalgendersubgender integer NOT NULL,
    llmusicalgender integer NOT NULL,
    llmusicalsubgender integer NOT NULL
);


--
-- TOC entry 2952 (class 0 OID 0)
-- Dependencies: 214
-- Name: TABLE crc_musicalgenders_musicalsubgenders; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON TABLE db_albums.crc_musicalgenders_musicalsubgenders IS 'tabla de cruce entre generos musicales y subgeneros musicales';


--
-- TOC entry 2953 (class 0 OID 0)
-- Dependencies: 214
-- Name: COLUMN crc_musicalgenders_musicalsubgenders.llmusicalgendersubgender; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.crc_musicalgenders_musicalsubgenders.llmusicalgendersubgender IS 'llave primaria de cruce de generos y subgeneros musicales';


--
-- TOC entry 2954 (class 0 OID 0)
-- Dependencies: 214
-- Name: COLUMN crc_musicalgenders_musicalsubgenders.llmusicalgender; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.crc_musicalgenders_musicalsubgenders.llmusicalgender IS 'llave foranea de generos musicales';


--
-- TOC entry 2955 (class 0 OID 0)
-- Dependencies: 214
-- Name: COLUMN crc_musicalgenders_musicalsubgenders.llmusicalsubgender; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.crc_musicalgenders_musicalsubgenders.llmusicalsubgender IS 'llave foranea de subgenero musical';


--
-- TOC entry 213 (class 1259 OID 117983)
-- Name: crc_musicalgenders_musicalsubgend_llmusicalgendersubgenders_seq; Type: SEQUENCE; Schema: db_albums; Owner: -
--

ALTER TABLE db_albums.crc_musicalgenders_musicalsubgenders ALTER COLUMN llmusicalgendersubgender ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME db_albums.crc_musicalgenders_musicalsubgend_llmusicalgendersubgenders_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 204 (class 1259 OID 117956)
-- Name: ct_albums; Type: TABLE; Schema: db_albums; Owner: -
--

CREATE TABLE db_albums.ct_albums (
    llalbum integer NOT NULL,
    dsnombrealbum character varying(200) NOT NULL,
    fcfechapublicacion date NOT NULL,
    tmduracion time(0) without time zone NOT NULL,
    lllabel integer NOT NULL,
    llband integer NOT NULL
);


--
-- TOC entry 2956 (class 0 OID 0)
-- Dependencies: 204
-- Name: TABLE ct_albums; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON TABLE db_albums.ct_albums IS 'tabla catalogo de registro de albums';


--
-- TOC entry 2957 (class 0 OID 0)
-- Dependencies: 204
-- Name: COLUMN ct_albums.llalbum; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_albums.llalbum IS 'llave primaria de la tabla de albums';


--
-- TOC entry 2958 (class 0 OID 0)
-- Dependencies: 204
-- Name: COLUMN ct_albums.dsnombrealbum; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_albums.dsnombrealbum IS 'descripcion de nombre de album';


--
-- TOC entry 2959 (class 0 OID 0)
-- Dependencies: 204
-- Name: COLUMN ct_albums.fcfechapublicacion; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_albums.fcfechapublicacion IS 'fecha de publicacion de album';


--
-- TOC entry 2960 (class 0 OID 0)
-- Dependencies: 204
-- Name: COLUMN ct_albums.tmduracion; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_albums.tmduracion IS 'tiempo de duracion del album';


--
-- TOC entry 2961 (class 0 OID 0)
-- Dependencies: 204
-- Name: COLUMN ct_albums.lllabel; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_albums.lllabel IS 'llave foranea de casa productora';


--
-- TOC entry 203 (class 1259 OID 117954)
-- Name: ct_albums_llalbum_seq; Type: SEQUENCE; Schema: db_albums; Owner: -
--

ALTER TABLE db_albums.ct_albums ALTER COLUMN llalbum ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME db_albums.ct_albums_llalbum_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 218 (class 1259 OID 117995)
-- Name: ct_bandmembers; Type: TABLE; Schema: db_albums; Owner: -
--

CREATE TABLE db_albums.ct_bandmembers (
    llbandmember integer NOT NULL,
    dsnombre character varying(50) NOT NULL,
    dsapellido1 character varying(50) NOT NULL,
    dsapellido2 character varying(50),
    dsaka character varying(80),
    fcfechanacimiento date NOT NULL,
    boestatus boolean DEFAULT true NOT NULL,
    llnationality integer NOT NULL
);


--
-- TOC entry 2962 (class 0 OID 0)
-- Dependencies: 218
-- Name: TABLE ct_bandmembers; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON TABLE db_albums.ct_bandmembers IS 'catalogo de integrantes de una banda';


--
-- TOC entry 2963 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ct_bandmembers.llbandmember; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bandmembers.llbandmember IS 'llave primaria de integrantes de banda';


--
-- TOC entry 2964 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ct_bandmembers.dsnombre; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bandmembers.dsnombre IS 'descripcion de nombre de integrante';


--
-- TOC entry 2965 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ct_bandmembers.dsapellido1; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bandmembers.dsapellido1 IS 'descripcion de primer apellido';


--
-- TOC entry 2966 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ct_bandmembers.dsapellido2; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bandmembers.dsapellido2 IS 'descripcion de segundo apellido';


--
-- TOC entry 2967 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ct_bandmembers.dsaka; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bandmembers.dsaka IS 'descripcion de pseudonimo conocido';


--
-- TOC entry 2968 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ct_bandmembers.fcfechanacimiento; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bandmembers.fcfechanacimiento IS 'fecha de nacimiento';


--
-- TOC entry 2969 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ct_bandmembers.boestatus; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bandmembers.boestatus IS 'valor booleano que indica si el registro esta activo o inactivo';


--
-- TOC entry 2970 (class 0 OID 0)
-- Dependencies: 218
-- Name: COLUMN ct_bandmembers.llnationality; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bandmembers.llnationality IS 'llave foranea de nacionalidad';


--
-- TOC entry 217 (class 1259 OID 117993)
-- Name: ct_bandmembers_llbandmember_seq; Type: SEQUENCE; Schema: db_albums; Owner: -
--

ALTER TABLE db_albums.ct_bandmembers ALTER COLUMN llbandmember ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME db_albums.ct_bandmembers_llbandmember_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 222 (class 1259 OID 118007)
-- Name: ct_bandroles; Type: TABLE; Schema: db_albums; Owner: -
--

CREATE TABLE db_albums.ct_bandroles (
    llbandrole integer NOT NULL,
    dsbandrole character varying(100) NOT NULL,
    boestatus boolean DEFAULT true NOT NULL
);


--
-- TOC entry 2971 (class 0 OID 0)
-- Dependencies: 222
-- Name: TABLE ct_bandroles; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON TABLE db_albums.ct_bandroles IS 'catalogo de actividades que realizan los integrantes de las bandas';


--
-- TOC entry 2972 (class 0 OID 0)
-- Dependencies: 222
-- Name: COLUMN ct_bandroles.llbandrole; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bandroles.llbandrole IS 'llave primaria de actividades dentro de la banda';


--
-- TOC entry 2973 (class 0 OID 0)
-- Dependencies: 222
-- Name: COLUMN ct_bandroles.dsbandrole; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bandroles.dsbandrole IS 'descripcion de role dentro de la banda';


--
-- TOC entry 2974 (class 0 OID 0)
-- Dependencies: 222
-- Name: COLUMN ct_bandroles.boestatus; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bandroles.boestatus IS 'valor booleano que indica si el registro esta activo o inactivo';


--
-- TOC entry 221 (class 1259 OID 118005)
-- Name: ct_bandroles_llbandrole_seq; Type: SEQUENCE; Schema: db_albums; Owner: -
--

ALTER TABLE db_albums.ct_bandroles ALTER COLUMN llbandrole ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME db_albums.ct_bandroles_llbandrole_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 208 (class 1259 OID 117967)
-- Name: ct_bands; Type: TABLE; Schema: db_albums; Owner: -
--

CREATE TABLE db_albums.ct_bands (
    llband integer NOT NULL,
    dsbanda character varying(100) NOT NULL,
    fcfechacreacion date NOT NULL,
    llmusicalgender integer NOT NULL,
    llnationality integer NOT NULL,
    boestatus boolean DEFAULT true NOT NULL
);


--
-- TOC entry 2975 (class 0 OID 0)
-- Dependencies: 208
-- Name: TABLE ct_bands; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON TABLE db_albums.ct_bands IS 'catalogo de bandas';


--
-- TOC entry 2976 (class 0 OID 0)
-- Dependencies: 208
-- Name: COLUMN ct_bands.llband; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bands.llband IS 'llave primaria de banda';


--
-- TOC entry 2977 (class 0 OID 0)
-- Dependencies: 208
-- Name: COLUMN ct_bands.dsbanda; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bands.dsbanda IS 'descripcion de nombre de banda';


--
-- TOC entry 2978 (class 0 OID 0)
-- Dependencies: 208
-- Name: COLUMN ct_bands.fcfechacreacion; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bands.fcfechacreacion IS 'fecha de creacion de banda';


--
-- TOC entry 2979 (class 0 OID 0)
-- Dependencies: 208
-- Name: COLUMN ct_bands.llmusicalgender; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bands.llmusicalgender IS 'llave foranea de genero musical';


--
-- TOC entry 2980 (class 0 OID 0)
-- Dependencies: 208
-- Name: COLUMN ct_bands.llnationality; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bands.llnationality IS 'llave foranea de nacionalidad';


--
-- TOC entry 2981 (class 0 OID 0)
-- Dependencies: 208
-- Name: COLUMN ct_bands.boestatus; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_bands.boestatus IS 'valor booleano que indica si la banda esta activa o inactiva';


--
-- TOC entry 207 (class 1259 OID 117965)
-- Name: ct_bands_llband_seq; Type: SEQUENCE; Schema: db_albums; Owner: -
--

ALTER TABLE db_albums.ct_bands ALTER COLUMN llband ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME db_albums.ct_bands_llband_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 206 (class 1259 OID 117961)
-- Name: ct_labels; Type: TABLE; Schema: db_albums; Owner: -
--

CREATE TABLE db_albums.ct_labels (
    lllabel integer NOT NULL,
    dslabel character varying(100) NOT NULL,
    boestatus boolean DEFAULT true NOT NULL,
    fcfechacreacion date NOT NULL
);


--
-- TOC entry 2982 (class 0 OID 0)
-- Dependencies: 206
-- Name: TABLE ct_labels; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON TABLE db_albums.ct_labels IS 'catalogo de casas productoras que emiten albums';


--
-- TOC entry 2983 (class 0 OID 0)
-- Dependencies: 206
-- Name: COLUMN ct_labels.lllabel; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_labels.lllabel IS 'llave primaria de casas productoras';


--
-- TOC entry 2984 (class 0 OID 0)
-- Dependencies: 206
-- Name: COLUMN ct_labels.dslabel; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_labels.dslabel IS 'descripcion de nombre de casa productora';


--
-- TOC entry 2985 (class 0 OID 0)
-- Dependencies: 206
-- Name: COLUMN ct_labels.boestatus; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_labels.boestatus IS 'valor booleano que indica si la casa productora esta activa o inactiva';


--
-- TOC entry 2986 (class 0 OID 0)
-- Dependencies: 206
-- Name: COLUMN ct_labels.fcfechacreacion; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_labels.fcfechacreacion IS 'fecha de apertura de la casa productora';


--
-- TOC entry 205 (class 1259 OID 117959)
-- Name: ct_labels_lllabel_seq; Type: SEQUENCE; Schema: db_albums; Owner: -
--

ALTER TABLE db_albums.ct_labels ALTER COLUMN lllabel ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME db_albums.ct_labels_lllabel_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 210 (class 1259 OID 117973)
-- Name: ct_musicalgenders; Type: TABLE; Schema: db_albums; Owner: -
--

CREATE TABLE db_albums.ct_musicalgenders (
    llmusicalgender integer NOT NULL,
    dsmusicalgender character varying(50) NOT NULL,
    boestatus boolean DEFAULT true NOT NULL
);


--
-- TOC entry 2987 (class 0 OID 0)
-- Dependencies: 210
-- Name: TABLE ct_musicalgenders; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON TABLE db_albums.ct_musicalgenders IS 'catalogo de generos musicales que puede tener una banda';


--
-- TOC entry 2988 (class 0 OID 0)
-- Dependencies: 210
-- Name: COLUMN ct_musicalgenders.llmusicalgender; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_musicalgenders.llmusicalgender IS 'llave primaria de generos musicales';


--
-- TOC entry 2989 (class 0 OID 0)
-- Dependencies: 210
-- Name: COLUMN ct_musicalgenders.dsmusicalgender; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_musicalgenders.dsmusicalgender IS 'descripcion de genero musical';


--
-- TOC entry 2990 (class 0 OID 0)
-- Dependencies: 210
-- Name: COLUMN ct_musicalgenders.boestatus; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_musicalgenders.boestatus IS 'valor booleano que indica si el registro esta activo o inactivo';


--
-- TOC entry 209 (class 1259 OID 117971)
-- Name: ct_musicalgenders_llmusicalgender_seq; Type: SEQUENCE; Schema: db_albums; Owner: -
--

ALTER TABLE db_albums.ct_musicalgenders ALTER COLUMN llmusicalgender ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME db_albums.ct_musicalgenders_llmusicalgender_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 212 (class 1259 OID 117979)
-- Name: ct_musicalsubgenders; Type: TABLE; Schema: db_albums; Owner: -
--

CREATE TABLE db_albums.ct_musicalsubgenders (
    llmusicalsubgender integer NOT NULL,
    dsmusicalsubgender character varying(50) NOT NULL,
    boestatus boolean DEFAULT true NOT NULL
);


--
-- TOC entry 2991 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN ct_musicalsubgenders.llmusicalsubgender; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_musicalsubgenders.llmusicalsubgender IS 'llave primaria de subgeneros musicales';


--
-- TOC entry 2992 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN ct_musicalsubgenders.dsmusicalsubgender; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_musicalsubgenders.dsmusicalsubgender IS 'descripcion de subgenero musical';


--
-- TOC entry 2993 (class 0 OID 0)
-- Dependencies: 212
-- Name: COLUMN ct_musicalsubgenders.boestatus; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_musicalsubgenders.boestatus IS 'valor booleano que indica si el registro esta activo o inactivo';


--
-- TOC entry 211 (class 1259 OID 117977)
-- Name: ct_musicalsubgenders_llmusicalsubgender_seq; Type: SEQUENCE; Schema: db_albums; Owner: -
--

ALTER TABLE db_albums.ct_musicalsubgenders ALTER COLUMN llmusicalsubgender ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME db_albums.ct_musicalsubgenders_llmusicalsubgender_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 216 (class 1259 OID 117990)
-- Name: ct_nationalities; Type: TABLE; Schema: db_albums; Owner: -
--

CREATE TABLE db_albums.ct_nationalities (
    llnationality integer NOT NULL,
    dsnacionalidad character varying(100) NOT NULL
);


--
-- TOC entry 2994 (class 0 OID 0)
-- Dependencies: 216
-- Name: TABLE ct_nationalities; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON TABLE db_albums.ct_nationalities IS 'catalogo de nacionalidades';


--
-- TOC entry 2995 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN ct_nationalities.llnationality; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_nationalities.llnationality IS 'llave primaria de nacionalidades';


--
-- TOC entry 2996 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN ct_nationalities.dsnacionalidad; Type: COMMENT; Schema: db_albums; Owner: -
--

COMMENT ON COLUMN db_albums.ct_nationalities.dsnacionalidad IS 'descripcion de nacionalidad';


--
-- TOC entry 215 (class 1259 OID 117988)
-- Name: ct_nationalities_llnacionalidad_seq; Type: SEQUENCE; Schema: db_albums; Owner: -
--

ALTER TABLE db_albums.ct_nationalities ALTER COLUMN llnationality ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME db_albums.ct_nationalities_llnacionalidad_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 2935 (class 0 OID 118013)
-- Dependencies: 224
-- Data for Name: crc_bandmember_bandroles; Type: TABLE DATA; Schema: db_albums; Owner: -
--

COPY db_albums.crc_bandmember_bandroles (llbandmemberbandrole, llbandmember, llbandrole) FROM stdin;
\.


--
-- TOC entry 2931 (class 0 OID 118001)
-- Dependencies: 220
-- Data for Name: crc_bands_bandmembers; Type: TABLE DATA; Schema: db_albums; Owner: -
--

COPY db_albums.crc_bands_bandmembers (llbandbandmember, llband, llbandmember, fcfechainicio, fcfechafin, boestatus) FROM stdin;
\.


--
-- TOC entry 2925 (class 0 OID 117985)
-- Dependencies: 214
-- Data for Name: crc_musicalgenders_musicalsubgenders; Type: TABLE DATA; Schema: db_albums; Owner: -
--

COPY db_albums.crc_musicalgenders_musicalsubgenders (llmusicalgendersubgender, llmusicalgender, llmusicalsubgender) FROM stdin;
\.


--
-- TOC entry 2915 (class 0 OID 117956)
-- Dependencies: 204
-- Data for Name: ct_albums; Type: TABLE DATA; Schema: db_albums; Owner: -
--

COPY db_albums.ct_albums (llalbum, dsnombrealbum, fcfechapublicacion, tmduracion, lllabel, llband) FROM stdin;
\.


--
-- TOC entry 2929 (class 0 OID 117995)
-- Dependencies: 218
-- Data for Name: ct_bandmembers; Type: TABLE DATA; Schema: db_albums; Owner: -
--

COPY db_albums.ct_bandmembers (llbandmember, dsnombre, dsapellido1, dsapellido2, dsaka, fcfechanacimiento, boestatus, llnationality) FROM stdin;
\.


--
-- TOC entry 2933 (class 0 OID 118007)
-- Dependencies: 222
-- Data for Name: ct_bandroles; Type: TABLE DATA; Schema: db_albums; Owner: -
--

COPY db_albums.ct_bandroles (llbandrole, dsbandrole, boestatus) FROM stdin;
\.


--
-- TOC entry 2919 (class 0 OID 117967)
-- Dependencies: 208
-- Data for Name: ct_bands; Type: TABLE DATA; Schema: db_albums; Owner: -
--

COPY db_albums.ct_bands (llband, dsbanda, fcfechacreacion, llmusicalgender, llnationality, boestatus) FROM stdin;
\.


--
-- TOC entry 2917 (class 0 OID 117961)
-- Dependencies: 206
-- Data for Name: ct_labels; Type: TABLE DATA; Schema: db_albums; Owner: -
--

COPY db_albums.ct_labels (lllabel, dslabel, boestatus, fcfechacreacion) FROM stdin;
\.


--
-- TOC entry 2921 (class 0 OID 117973)
-- Dependencies: 210
-- Data for Name: ct_musicalgenders; Type: TABLE DATA; Schema: db_albums; Owner: -
--

COPY db_albums.ct_musicalgenders (llmusicalgender, dsmusicalgender, boestatus) FROM stdin;
\.


--
-- TOC entry 2923 (class 0 OID 117979)
-- Dependencies: 212
-- Data for Name: ct_musicalsubgenders; Type: TABLE DATA; Schema: db_albums; Owner: -
--

COPY db_albums.ct_musicalsubgenders (llmusicalsubgender, dsmusicalsubgender, boestatus) FROM stdin;
\.


--
-- TOC entry 2927 (class 0 OID 117990)
-- Dependencies: 216
-- Data for Name: ct_nationalities; Type: TABLE DATA; Schema: db_albums; Owner: -
--

COPY db_albums.ct_nationalities (llnationality, dsnacionalidad) FROM stdin;
\.


--
-- TOC entry 2997 (class 0 OID 0)
-- Dependencies: 223
-- Name: crc_bandmemberbandroles_llbandmemberbandrole_seq; Type: SEQUENCE SET; Schema: db_albums; Owner: -
--

SELECT pg_catalog.setval('db_albums.crc_bandmemberbandroles_llbandmemberbandrole_seq', 1, false);


--
-- TOC entry 2998 (class 0 OID 0)
-- Dependencies: 219
-- Name: crc_bands_bandmembers_llbandbandmember_seq; Type: SEQUENCE SET; Schema: db_albums; Owner: -
--

SELECT pg_catalog.setval('db_albums.crc_bands_bandmembers_llbandbandmember_seq', 1, false);


--
-- TOC entry 2999 (class 0 OID 0)
-- Dependencies: 213
-- Name: crc_musicalgenders_musicalsubgend_llmusicalgendersubgenders_seq; Type: SEQUENCE SET; Schema: db_albums; Owner: -
--

SELECT pg_catalog.setval('db_albums.crc_musicalgenders_musicalsubgend_llmusicalgendersubgenders_seq', 1, false);


--
-- TOC entry 3000 (class 0 OID 0)
-- Dependencies: 203
-- Name: ct_albums_llalbum_seq; Type: SEQUENCE SET; Schema: db_albums; Owner: -
--

SELECT pg_catalog.setval('db_albums.ct_albums_llalbum_seq', 1, false);


--
-- TOC entry 3001 (class 0 OID 0)
-- Dependencies: 217
-- Name: ct_bandmembers_llbandmember_seq; Type: SEQUENCE SET; Schema: db_albums; Owner: -
--

SELECT pg_catalog.setval('db_albums.ct_bandmembers_llbandmember_seq', 1, false);


--
-- TOC entry 3002 (class 0 OID 0)
-- Dependencies: 221
-- Name: ct_bandroles_llbandrole_seq; Type: SEQUENCE SET; Schema: db_albums; Owner: -
--

SELECT pg_catalog.setval('db_albums.ct_bandroles_llbandrole_seq', 1, false);


--
-- TOC entry 3003 (class 0 OID 0)
-- Dependencies: 207
-- Name: ct_bands_llband_seq; Type: SEQUENCE SET; Schema: db_albums; Owner: -
--

SELECT pg_catalog.setval('db_albums.ct_bands_llband_seq', 1, false);


--
-- TOC entry 3004 (class 0 OID 0)
-- Dependencies: 205
-- Name: ct_labels_lllabel_seq; Type: SEQUENCE SET; Schema: db_albums; Owner: -
--

SELECT pg_catalog.setval('db_albums.ct_labels_lllabel_seq', 1, false);


--
-- TOC entry 3005 (class 0 OID 0)
-- Dependencies: 209
-- Name: ct_musicalgenders_llmusicalgender_seq; Type: SEQUENCE SET; Schema: db_albums; Owner: -
--

SELECT pg_catalog.setval('db_albums.ct_musicalgenders_llmusicalgender_seq', 1, false);


--
-- TOC entry 3006 (class 0 OID 0)
-- Dependencies: 211
-- Name: ct_musicalsubgenders_llmusicalsubgender_seq; Type: SEQUENCE SET; Schema: db_albums; Owner: -
--

SELECT pg_catalog.setval('db_albums.ct_musicalsubgenders_llmusicalsubgender_seq', 1, false);


--
-- TOC entry 3007 (class 0 OID 0)
-- Dependencies: 215
-- Name: ct_nationalities_llnacionalidad_seq; Type: SEQUENCE SET; Schema: db_albums; Owner: -
--

SELECT pg_catalog.setval('db_albums.ct_nationalities_llnacionalidad_seq', 1, false);


--
-- TOC entry 2772 (class 2606 OID 118019)
-- Name: crc_bands_bandmembers pk_crcbndbndmem_bndbndmem; Type: CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.crc_bands_bandmembers
    ADD CONSTRAINT pk_crcbndbndmem_bndbndmem PRIMARY KEY (llbandbandmember);


--
-- TOC entry 2776 (class 2606 OID 118017)
-- Name: crc_bandmember_bandroles pk_crcbndmembndrol_bndmembndrol; Type: CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.crc_bandmember_bandroles
    ADD CONSTRAINT pk_crcbndmembndrol_bndmembndrol PRIMARY KEY (llbandmemberbandrole);


--
-- TOC entry 2766 (class 2606 OID 118021)
-- Name: crc_musicalgenders_musicalsubgenders pk_crcmusgenmussbgen_musgenmussbgen; Type: CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.crc_musicalgenders_musicalsubgenders
    ADD CONSTRAINT pk_crcmusgenmussbgen_musgenmussbgen PRIMARY KEY (llmusicalgendersubgender);


--
-- TOC entry 2756 (class 2606 OID 118023)
-- Name: ct_albums pk_ctalb_alb; Type: CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_albums
    ADD CONSTRAINT pk_ctalb_alb PRIMARY KEY (llalbum);


--
-- TOC entry 2760 (class 2606 OID 118031)
-- Name: ct_bands pk_ctbnd_bdn; Type: CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_bands
    ADD CONSTRAINT pk_ctbnd_bdn PRIMARY KEY (llband);


--
-- TOC entry 2770 (class 2606 OID 118025)
-- Name: ct_bandmembers pk_ctbndmem_bndmem; Type: CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_bandmembers
    ADD CONSTRAINT pk_ctbndmem_bndmem PRIMARY KEY (llbandmember);


--
-- TOC entry 2774 (class 2606 OID 118029)
-- Name: ct_bandroles pk_ctbndrole_bdnrole; Type: CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_bandroles
    ADD CONSTRAINT pk_ctbndrole_bdnrole PRIMARY KEY (llbandrole);


--
-- TOC entry 2758 (class 2606 OID 118033)
-- Name: ct_labels pk_ctlbl_lbl; Type: CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_labels
    ADD CONSTRAINT pk_ctlbl_lbl PRIMARY KEY (lllabel);


--
-- TOC entry 2762 (class 2606 OID 118035)
-- Name: ct_musicalgenders pk_ctmusgnd_musgnd; Type: CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_musicalgenders
    ADD CONSTRAINT pk_ctmusgnd_musgnd PRIMARY KEY (llmusicalgender);


--
-- TOC entry 2764 (class 2606 OID 118037)
-- Name: ct_musicalsubgenders pk_ctmussbgnd_mussbgnd; Type: CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_musicalsubgenders
    ADD CONSTRAINT pk_ctmussbgnd_mussbgnd PRIMARY KEY (llmusicalsubgender);


--
-- TOC entry 2768 (class 2606 OID 118039)
-- Name: ct_nationalities pk_ctnat_nat; Type: CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_nationalities
    ADD CONSTRAINT pk_ctnat_nat PRIMARY KEY (llnationality);


--
-- TOC entry 2784 (class 2606 OID 118070)
-- Name: crc_bands_bandmembers fk_ctbnd_crcbndbndmem_bnd; Type: FK CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.crc_bands_bandmembers
    ADD CONSTRAINT fk_ctbnd_crcbndbndmem_bnd FOREIGN KEY (llband) REFERENCES db_albums.ct_bands(llband);


--
-- TOC entry 2778 (class 2606 OID 118045)
-- Name: ct_albums fk_ctbnd_ctalb_bnd; Type: FK CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_albums
    ADD CONSTRAINT fk_ctbnd_ctalb_bnd FOREIGN KEY (llband) REFERENCES db_albums.ct_bands(llband);


--
-- TOC entry 2785 (class 2606 OID 118075)
-- Name: crc_bands_bandmembers fk_ctbndmem_crcbndbndmem_bndmem; Type: FK CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.crc_bands_bandmembers
    ADD CONSTRAINT fk_ctbndmem_crcbndbndmem_bndmem FOREIGN KEY (llbandmember) REFERENCES db_albums.ct_bandmembers(llbandmember);


--
-- TOC entry 2787 (class 2606 OID 118090)
-- Name: crc_bandmember_bandroles fk_ctbndmem_crcbndmembndrole_bndmem; Type: FK CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.crc_bandmember_bandroles
    ADD CONSTRAINT fk_ctbndmem_crcbndmembndrole_bndmem FOREIGN KEY (llbandmember) REFERENCES db_albums.ct_bandmembers(llbandmember);


--
-- TOC entry 2786 (class 2606 OID 118085)
-- Name: crc_bandmember_bandroles fk_ctbndrole_crcbndmembndrole_bndrole; Type: FK CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.crc_bandmember_bandroles
    ADD CONSTRAINT fk_ctbndrole_crcbndmembndrole_bndrole FOREIGN KEY (llbandrole) REFERENCES db_albums.ct_bandroles(llbandrole);


--
-- TOC entry 2777 (class 2606 OID 118040)
-- Name: ct_albums fk_ctlbl_ctalb_lbl; Type: FK CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_albums
    ADD CONSTRAINT fk_ctlbl_ctalb_lbl FOREIGN KEY (lllabel) REFERENCES db_albums.ct_labels(lllabel);


--
-- TOC entry 2781 (class 2606 OID 118060)
-- Name: crc_musicalgenders_musicalsubgenders fk_ctmusgnd_crcmusgndmussbgnd_musgnd; Type: FK CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.crc_musicalgenders_musicalsubgenders
    ADD CONSTRAINT fk_ctmusgnd_crcmusgndmussbgnd_musgnd FOREIGN KEY (llmusicalgender) REFERENCES db_albums.ct_musicalgenders(llmusicalgender);


--
-- TOC entry 2779 (class 2606 OID 118050)
-- Name: ct_bands fk_ctmusgnd_ctbnd_musgnd; Type: FK CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_bands
    ADD CONSTRAINT fk_ctmusgnd_ctbnd_musgnd FOREIGN KEY (llmusicalgender) REFERENCES db_albums.ct_musicalgenders(llmusicalgender);


--
-- TOC entry 2782 (class 2606 OID 118065)
-- Name: crc_musicalgenders_musicalsubgenders fk_ctmussbgnd_crcmusgndmussbgnd_mussbgnd; Type: FK CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.crc_musicalgenders_musicalsubgenders
    ADD CONSTRAINT fk_ctmussbgnd_crcmusgndmussbgnd_mussbgnd FOREIGN KEY (llmusicalsubgender) REFERENCES db_albums.ct_musicalsubgenders(llmusicalsubgender);


--
-- TOC entry 2780 (class 2606 OID 118055)
-- Name: ct_bands fk_ctnat_ctbnd_nat; Type: FK CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_bands
    ADD CONSTRAINT fk_ctnat_ctbnd_nat FOREIGN KEY (llnationality) REFERENCES db_albums.ct_nationalities(llnationality);


--
-- TOC entry 2783 (class 2606 OID 118080)
-- Name: ct_bandmembers fk_ctnat_ctbndmem_nat; Type: FK CONSTRAINT; Schema: db_albums; Owner: -
--

ALTER TABLE ONLY db_albums.ct_bandmembers
    ADD CONSTRAINT fk_ctnat_ctbndmem_nat FOREIGN KEY (llnationality) REFERENCES db_albums.ct_nationalities(llnationality);


-- Completed on 2021-06-12 17:59:21

--
-- PostgreSQL database dump complete
--

