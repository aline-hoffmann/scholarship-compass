select cdpro, nmpro
from tbvendas
where dtven between '2014-02-03' and '2018-02-02' and status = 'Concluído'
group by qtd
order by qtd desc
limit 1