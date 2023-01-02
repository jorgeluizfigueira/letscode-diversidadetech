-- Questao 1
select municipio  from reflorestamento where area > 200000


-- Questao 2
select municipio, uf from reflorestamento where area > 150000


-- Questao 3

-- Questao 4
select municipio, especie_florestal  from reflorestamento where area > 30000 and uf = 'BA'


-- Questao 5
create view vw_tabela_reflorestamento as (
	select *
	from reflorestamento 
)

create materialized view vwm_tabela_reflorestamento as (
	select *
	from reflorestamento 		
)

select * from vw_tabela_reflorestamento

select * from vwm_tabela_reflorestamento 