--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2020-11-12 22:23:25

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 16422)
-- Name: Genre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Genre" (
    id integer NOT NULL,
    genre_name "char"[],
    genre_img "char"[],
    description "char"[]
);


ALTER TABLE public."Genre" OWNER TO postgres;

--
-- TOC entry 3008 (class 0 OID 16422)
-- Dependencies: 202
-- Data for Name: Genre; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Genre" (id, genre_name, genre_img, description) FROM stdin;
\.


--
-- TOC entry 2877 (class 2606 OID 16429)
-- Name: Genre Genre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Genre"
    ADD CONSTRAINT "Genre_pkey" PRIMARY KEY (id);


-- Completed on 2020-11-12 22:23:26

--
-- PostgreSQL database dump complete
--

