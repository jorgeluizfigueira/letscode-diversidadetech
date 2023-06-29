import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from collections import namedtuple


# banco de dados
from database import *

import re

# Autenticação Spotify
with open('spotify_credentials.txt') as f:
    lines = f.read()
    client_id, client_secret = lines.split('\n')

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret) 

#Create Spotify object 
sp  = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Obtém os dados das músicas da playlist do usuário
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
        
    sql = f"select exists(select 1 from musicas where id_musica = '{id_musica}')"
    musica_cadastrada = bool(con.consultar(sql)[0][0])
    if not(musica_cadastrada):
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
    
    Usuario = namedtuple( 'Usuario', ['nome_usuario', 'id_usuario', 'nome_playlist', 'id_playlist'] )
    
    usuarios = [
    Usuario('Jorge','227olwh4isc7in2k2antkfkxi','Mais tocadas 2022','2DaBOhl0FVRgMuebKTMSD4'),
    Usuario('Dário','dariornj','Mais tocadas 2022','2DwHb7MbOApxeI9bbPnT4U'),
    Usuario('Lucas','12146651973','Mais tocadas 2022','2EsDQ5HR1w6CaZqFFRlvFw'),
    Usuario('Maicon','2y9a4d5p6fxc3awwemt1q4vc0','Mais tocadas 2022','43IeRWiwHHKwJ1LCtQZUUd')
    ]
    
    for usuario in usuarios:
        registra_usuario(con, usuario.id_usuario, usuario.nome_usuario)
        registra_playlist(con, usuario.id_playlist, usuario.id_usuario, usuario.nome_playlist)
        registra_musicas_playlist(con, usuario.id_usuario, usuario.id_playlist)
    
    con.fechar()