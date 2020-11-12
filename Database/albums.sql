--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2020-11-12 22:22:32

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
-- TOC entry 201 (class 1259 OID 16414)
-- Name: Albums; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Albums" (
    id integer NOT NULL,
    name "char"[],
    genre_id integer,
    artists_id integer,
    album_img "char"[],
    description "char"[],
    song_id integer
);


ALTER TABLE public."Albums" OWNER TO postgres;

--
-- TOC entry 3011 (class 0 OID 16414)
-- Dependencies: 201
-- Data for Name: Albums; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Albums" (id, name, genre_id, artists_id, album_img, description, song_id) FROM stdin;
\.


--
-- TOC entry 2877 (class 2606 OID 16421)
-- Name: Albums Albums_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Albums"
    ADD CONSTRAINT "Albums_pkey" PRIMARY KEY (id);


--
-- TOC entry 2880 (class 2606 OID 16483)
-- Name: Albums album_song_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Albums"
    ADD CONSTRAINT album_song_id_fkey FOREIGN KEY (song_id) REFERENCES public."Songs"(id) NOT VALID;


--
-- TOC entry 2879 (class 2606 OID 16478)
-- Name: Albums albums_artists_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Albums"
    ADD CONSTRAINT albums_artists_id_fkey FOREIGN KEY (artists_id) REFERENCES public."Artists"(id) NOT VALID;


--
-- TOC entry 2878 (class 2606 OID 16473)
-- Name: Albums albums_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Albums"
    ADD CONSTRAINT albums_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES public."Genre"(id) NOT VALID;


-- Completed on 2020-11-12 22:22:33

--
-- PostgreSQL database dump complete
--

