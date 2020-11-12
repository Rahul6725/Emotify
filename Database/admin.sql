--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2020-11-12 22:21:56

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
-- TOC entry 204 (class 1259 OID 16438)
-- Name: Admin; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Admin" (
    id integer NOT NULL,
    username "char"[],
    password "char"[],
    email "char"[]
);


ALTER TABLE public."Admin" OWNER TO postgres;

--
-- TOC entry 3008 (class 0 OID 16438)
-- Dependencies: 204
-- Data for Name: Admin; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Admin" (id, username, password, email) FROM stdin;
\.


--
-- TOC entry 2877 (class 2606 OID 16445)
-- Name: Admin Admin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Admin"
    ADD CONSTRAINT "Admin_pkey" PRIMARY KEY (id);


-- Completed on 2020-11-12 22:21:57

--
-- PostgreSQL database dump complete
--

