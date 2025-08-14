select
    tbestoqueproduto.cdpro,
    tbvendas.nmcanalvendas,
    tbvendas.nmpro,
    sum(tbvendas.qtd) as quantidade_vendas
from tbvendas
join tbestoqueproduto on tbvendas.cdpro = tbestoqueproduto.cdpro
where
    (tbvendas.nmcanalvendas = 'Ecommerce' or tbvendas.nmcanalvendas = 'Matriz') and
    tbvendas.status = 'Concluído'
group by tbestoqueproduto.cdpro, tbvendas.nmcanalvendas
order by quantidade_vendas asc
limit 10