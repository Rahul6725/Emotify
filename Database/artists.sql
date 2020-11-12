--
-- PostgreSQL database dump
--

-- Dumped from database version 13.0
-- Dumped by pg_dump version 13.0

-- Started on 2020-11-12 22:23:02

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
-- TOC entry 206 (class 1259 OID 16457)
-- Name: Artists; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Artists" (
    id integer NOT NULL,
    user_id integer,
    name "char"[],
    genre_id integer,
    description "char"[],
    artist_img "char"[],
    song_id integer
);


ALTER TABLE public."Artists" OWNER TO postgres;

--
-- TOC entry 3011 (class 0 OID 16457)
-- Dependencies: 206
-- Data for Name: Artists; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Artists" (id, user_id, name, genre_id, description, artist_img, song_id) FROM stdin;
\.


--
-- TOC entry 2877 (class 2606 OID 16464)
-- Name: Artists Artists_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Artists"
    ADD CONSTRAINT "Artists_pkey" PRIMARY KEY (id);


--
-- TOC entry 2879 (class 2606 OID 16493)
-- Name: Artists artists_genre_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Artists"
    ADD CONSTRAINT artists_genre_id_fkey FOREIGN KEY (genre_id) REFERENCES public."Genre"(id) NOT VALID;


--
-- TOC entry 2880 (class 2606 OID 16498)
-- Name: Artists artists_song_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Artists"
    ADD CONSTRAINT artists_song_id_fkey FOREIGN KEY (song_id) REFERENCES public."Songs"(id) NOT VALID;


--
-- TOC entry 2878 (class 2606 OID 16488)
-- Name: Artists artists_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Artists"
    ADD CONSTRAINT artists_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."Users"(id) NOT VALID;


-- Completed on 2020-11-12 22:23:02

--
-- PostgreSQL database dump complete
--

