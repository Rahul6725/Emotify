--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2020-11-12 22:24:30

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
-- TOC entry 205 (class 1259 OID 16446)
-- Name: Songs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Songs" (
    id integer NOT NULL,
    album_id integer,
    genre_id integer,
    name "char"[],
    singer_id integer,
    length integer[]
);


ALTER TABLE public."Songs" OWNER TO postgres;

--
-- TOC entry 3011 (class 0 OID 16446)
-- Dependencies: 205
-- Data for Name: Songs; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Songs" (id, album_id, genre_id, name, singer_id, length) FROM stdin;
\.


--
-- TOC entry 2877 (class 2606 OID 16453)
-- Name: Songs Songs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Songs"
    ADD CONSTRAINT "Songs_pkey" PRIMARY KEY (id);


--
-- TOC entry 2878 (class 2606 OID 16523)
-- Name: Songs songs_album_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Songs"
    ADD CONSTRAINT songs_album_id_fkey FOREIGN KEY (album_id) REFERENCES public."Albums"(id) NOT VALID;


--
-- TOC entry 2879 (class 2606 OID 16528)
-- Name: Songs songs_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Songs"
    ADD CONSTRAINT songs_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES public."Genre"(id) NOT VALID;


--
-- TOC entry 2880 (class 2606 OID 16533)
-- Name: Songs songs_singer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Songs"
    ADD CONSTRAINT songs_singer_id_fkey FOREIGN KEY (singer_id) REFERENCES public."Artists"(id) NOT VALID;


-- Completed on 2020-11-12 22:24:30

--
-- PostgreSQL database dump complete
--

