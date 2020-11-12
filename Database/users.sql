--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2020-11-12 22:24:54

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
-- TOC entry 200 (class 1259 OID 16406)
-- Name: Users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Users" (
    id integer NOT NULL,
    username "char" NOT NULL,
    password "char" NOT NULL,
    email "char",
    country "char",
    gender character(1),
    user_img text[]
);


ALTER TABLE public."Users" OWNER TO postgres;

--
-- TOC entry 3008 (class 0 OID 16406)
-- Dependencies: 200
-- Data for Name: Users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Users" (id, username, password, email, country, gender, user_img) FROM stdin;
\.


--
-- TOC entry 2877 (class 2606 OID 16413)
-- Name: Users Users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Users"
    ADD CONSTRAINT "Users_pkey" PRIMARY KEY (id);


-- Completed on 2020-11-12 22:24:55

--
-- PostgreSQL database dump complete
--

