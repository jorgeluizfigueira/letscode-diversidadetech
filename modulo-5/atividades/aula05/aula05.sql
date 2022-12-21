/*
Aula 5 - Consulta simples e manipulação de dados nas tabelas (CRUD)
Prof. Tiago Dias
Aluno Jorge Luiz Figueira da Silva Junior
*/

-- Questão 1 - Criar uma base de dados no Postgres com o nome de CINEMA e uma tabela de nome FILMES conforme exemplo abaixo.

create database CINEMA

-- criando uma sequencia para codigo do aluno

create sequence seq_id_filme start 1

-- criando  a tabela FILMES

create table filmes (
	id		integer default nextval('seq_id_filme'),
	nome	varchar,
	categoria	varchar,
	duracao		integer,
	lancamento		date,
	primary key (id)
)

-- Questão 2 - Inserir apenas um registro na tabela FILMES, informando todos os atributos indicando a coluna ID = 6.

insert into filmes values (6, 'Pinóquio de Guillermo del Toro', 'fantasia', 117, '2022-11-24');

-- Questão 3 - Inserir na tabela FILMES, todos os registros do exemplo abaixo.

insert into filmes values (default, 'Como eu era Antes de Você', 'drama', 110, '2016-06-16');
insert into filmes values (default, 'Para Sempre', 'romance', 104, '2012-06-07');
insert into filmes values (default, 'Arremessando Alto', 'drama', 117, '2022-06-03');
insert into filmes values (default, 'King Richard: Criando Campeãs', 'drama', 144, '2021-12-02');
insert into filmes values (default, 'No Ritmo do Coração', 'drama', 111, '2021-09-23');

-- Questão 4 - Deletar na tabela FILMES, apenas a linha com o ID = 6.

delete from filmes where id = 6;

-- Questão 5 - Adicionar uma coluna com nome de VERIFICAR do tipo booleano e 
-- atualizar os registros com categoria = drama como True na coluna VERIFICAR.

alter table filmes add column verificar bool default False;

update filmes set verificar = True where categoria = 'drama';

-- Questão 6 - Construa um SELECT que retorne os dados conforme imagem abaixo.

select id, nome, categoria from filmes;

-- Questão 7 - Construa um SELECT que retorne os dados conforme imagem abaixo.

select nome from filmes;

-- Questão 8 - Construa um SELECT que retorne os dados conforme imagem abaixo.

select * from filmes where categoria = 'romance';

