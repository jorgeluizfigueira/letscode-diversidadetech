-- Musicas em comum
select m.nome as "Nome Música", a.nome from musicas m 
left join musicas_playlist mp using (id_musica)
left join artistas a using (id_artista)
group by id_musica,m.nome,a.nome
HAVING COUNT(id_musica) > 1;

select count(*) as "Músicas", count(distinct(id_musica)) as "Músicas Únicas" from musicas_playlist mp ;

-- Principais artistas
select a.nome, count(id_artista)
FROM musicas m  
left join artistas a using (id_artista)
GROUP BY id_artista, a.nome
HAVING COUNT(id_artista) > 1
order by count(id_artista) desc
LIMIT 10;

select count(*) as "Quantidade de Artistas" from artistas a;

-- duracao das playlist
select us.nome_usuario ,sum(duracao_segundos)/60 as minutos from musicas m 
left join musicas_playlist mp using (id_musica)
left join playlists p using (id_playlist)
left join usuarios_spotify us using (id_usuario)
group by us.nome_usuario
order  by minutos desc;

select us.nome_usuario as "Nome Usuário", count(distinct(id_artista)) as "Artistas Únicos" from musicas m 
left join musicas_playlist mp using (id_musica)
left join playlists p using (id_playlist)
left join usuarios_spotify us using (id_usuario)
group by us.nome_usuario
order  by count(distinct(id_artista)) desc;




