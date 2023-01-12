
CREATE DATABASE musicas;

CREATE TABLE public.artistas (
                id_artista VARCHAR NOT NULL,
                nome VARCHAR NOT NULL,
                CONSTRAINT artistas_pk PRIMARY KEY (id_artista)
);


CREATE TABLE public.musicas (
                id_musica VARCHAR NOT NULL,
                id_artista VARCHAR NOT NULL,
                nome VARCHAR NOT NULL,
                duracao_segundos INTEGER NOT NULL,
                CONSTRAINT musicas_pk PRIMARY KEY (id_musica)
);


CREATE TABLE public.usuarios_spotify (
                id_usuario VARCHAR NOT NULL,
                nome_usuario VARCHAR NOT NULL,
                CONSTRAINT usuarios_spotify_pk PRIMARY KEY (id_usuario)
);


CREATE TABLE public.playlists (
                id_playlist VARCHAR NOT NULL,
                id_usuario VARCHAR NOT NULL,
                nome_playlist VARCHAR NOT NULL,
                CONSTRAINT playlists_pk PRIMARY KEY (id_playlist)
);


CREATE SEQUENCE public.musicas_playlist_id_seq;

CREATE TABLE public.musicas_playlist (
                id INTEGER NOT NULL DEFAULT nextval('public.musicas_playlist_id_seq'),
                id_playlist VARCHAR NOT NULL,
                id_musica VARCHAR NOT NULL,
                CONSTRAINT musicas_playlist_pk PRIMARY KEY (id)
);


ALTER SEQUENCE public.musicas_playlist_id_seq OWNED BY public.musicas_playlist.id;

ALTER TABLE public.musicas ADD CONSTRAINT artistas_musicas_fk
FOREIGN KEY (id_artista)
REFERENCES public.artistas (id_artista)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.musicas_playlist ADD CONSTRAINT musicas_musicas_playlist_fk
FOREIGN KEY (id_musica)
REFERENCES public.musicas (id_musica)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.playlists ADD CONSTRAINT usuarios_spotify_playlists_fk
FOREIGN KEY (id_usuario)
REFERENCES public.usuarios_spotify (id_usuario)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE public.musicas_playlist ADD CONSTRAINT playlists_musicas_playlist_fk
FOREIGN KEY (id_playlist)
REFERENCES public.playlists (id_playlist)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;