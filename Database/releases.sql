--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2020-11-12 22:24:09

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
-- TOC entry 207 (class 1259 OID 16465)
-- Name: Releases; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Releases" (
    id integer NOT NULL,
    album_id integer,
    genre_id integer,
    img "char"[],
    song_id integer,
    description "char"[]
);


ALTER TABLE public."Releases" OWNER TO postgres;

--
-- TOC entry 3011 (class 0 OID 16465)
-- Dependencies: 207
-- Data for Name: Releases; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Releases" (id, album_id, genre_id, img, song_id, description) FROM stdin;
\.


--
-- TOC entry 2877 (class 2606 OID 16472)
-- Name: Releases Releases_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Releases"
    ADD CONSTRAINT "Releases_pkey" PRIMARY KEY (id);


--
-- TOC entry 2878 (class 2606 OID 16508)
-- Name: Releases releases_album_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Releases"
    ADD CONSTRAINT releases_album_id_fkey FOREIGN KEY (album_id) REFERENCES public."Albums"(id) NOT VALID;


--
-- TOC entry 2879 (class 2606 OID 16513)
-- Name: Releases releases_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Releases"
    ADD CONSTRAINT releases_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES public."Genre"(id) NOT VALID;


--
-- TOC entry 2880 (class 2606 OID 16518)
-- Name: Releases releases_song_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Releases"
    ADD CONSTRAINT releases_song_id_fkey FOREIGN KEY (song_id) REFERENCES public."Songs"(id) NOT VALID;


-- Completed on 2020-11-12 22:24:10

--
-- PostgreSQL database dump complete
--

