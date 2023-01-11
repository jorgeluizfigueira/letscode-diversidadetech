-- Questao 1
select count (distinct(municipio)) as municipios_unicos from reflorestamento;

-- Questao 2
select sum (area) as total_area_ha from reflorestamento;

-- Questao 3
select especie_florestal, sum (area) as total_area_especie from reflorestamento group by especie_florestal;

-- Questao 4
select ano, sum (area) as total_area_ano from reflorestamento group by ano;

-- Questao 5
select ano, count (municipio) as municipios_ano from reflorestamento group by ano;

-- Questao 6
select ano, municipio, r.uf, area, media_area_uf, area - media_area_uf  as diferenca_area_media 
from reflorestamento r left join (select uf, round(avg (area)) as media_area_uf from reflorestamento group by uf)
as t on r.uf = t.uf;

-- Questão 7
select regiao, sum (area) as total_area_regiao, rank() over (order by sum(area) desc) from reflorestamento group by regiao;






