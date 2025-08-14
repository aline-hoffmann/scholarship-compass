select
    tbvendedor.nmvdd as vendedor,
    sum(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas,
    round(
        (sum
            (round(tbvendas.qtd, 2) * round(tbvendas.vrunt, 2) * round(tbvendedor.perccomissao, 2))/ 100), 2) as comissao
from tbvendedor
inner join tbvendas on tbvendedor.cdvdd = tbvendas.cdvdd
where tbvendas.status = 'Concluído'
group by tbvendedor.nmvdd, tbvendedor.perccomissao
order by comissao desc