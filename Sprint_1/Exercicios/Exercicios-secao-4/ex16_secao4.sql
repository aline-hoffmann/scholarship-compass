select
    tbvendas.estado,
    tbvendas.nmpro,
    round(avg(tbvendas.qtd), 4) as quantidade_media
from tbvendas
join tbestoqueproduto on tbvendas.cdpro = tbestoqueproduto.cdpro
where tbvendas.status = 'Concluído'
group by tbvendas.estado, tbvendas.nmpro
order by tbvendas.estado, tbvendas.nmpro