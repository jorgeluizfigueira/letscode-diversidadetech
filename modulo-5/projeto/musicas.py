import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# banco de dados
from database import *

import re

# Autenticação Spotfy
with open('spotify_credentials.txt') as f:
    lines = f.read()
    client_id, client_secret = lines.split('\n')

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret) 

#Create Spotify object 
sp  = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# 

def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def registra_usuario(con,id_usuario,nome_usuario):
    sql = f"insert into usuarios_spotify values ('{id_usuario}','{nome_usuario}');"
    con.manipular(sql)
    
def registra_playlist(con,id_playlist,id_usuario,nome_playlist):
    sql = f"insert into playlists values ('{id_playlist}','{id_usuario}','{nome_playlist}');"
    con.manipular(sql)

def registra_musica(con,id_artista,id_musica,id_playlist,
                    nome_artista,nome_musica,duracao_ms):
    sql = f"select exists(select 1 from artistas where id_artista = '{id_artista}')"
    artista_cadastrado = bool(con.consultar(sql)[0][0])
    if not(artista_cadastrado):
        sql = f"insert into artistas values ('{id_artista}','{nome_artista}');"
    con.manipular(sql)
    sql = f"insert into musicas values ('{id_musica}','{id_artista}','{nome_musica}','{duracao_ms}');"
    con.manipular(sql)
    sql = f"insert into musicas_playlist values (default,'{id_playlist}','{id_musica}');"
    con.manipular(sql)
    

def registra_musicas_playlist(con,id_usuario,id_playlist):
    tracks = get_playlist_tracks(username=id_usuario,playlist_id=id_playlist)

    for track in tracks:
        id_artista = track["track"]["artists"][0]['id']
        id_musica = track["track"]["id"]
        nome_artista = track["track"]["artists"][0]["name"]
        nome_musica = track["track"]["name"]
        nome_musica = re.sub('[\W_]+', ' ', nome_musica)
        duracao_ms = round((track["track"]['duration_ms'])/1000)

        registra_musica(con,id_artista,id_musica,id_playlist,
                        nome_artista,nome_musica,duracao_ms)
    
if __name__ == '__main__':
    params = config()
    con=Conexao(**params)
    registra_usuario(con=con,id_usuario='227olwh4isc7in2k2antkfkxi',nome_usuario='Jorge Luiz')
    registra_playlist(con=con,id_playlist='2DaBOhl0FVRgMuebKTMSD4',id_usuario='227olwh4isc7in2k2antkfkxi',nome_playlist='Top 100 2022')
    registra_musicas_playlist(con=con,id_usuario='227olwh4isc7in2k2antkfkxi',id_playlist='2DaBOhl0FVRgMuebKTMSD4')
    con.fechar()