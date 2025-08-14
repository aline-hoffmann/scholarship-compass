select
    tbdependente.cddep,
    tbdependente.nmdep,
    tbdependente.dtnasc,
    sum(tbvendas.qtd * tbvendas.vrunt) as valor_total_vendas
from tbvendedor
left join tbdependente on tbvendedor.cdvdd = tbdependente.cdvdd
left join tbvendas on tbvendedor.cdvdd = tbvendas.cdvdd
where tbvendas.status = 'Concluído'
group by tbdependente.cddep, tbdependente.nmdep, tbdependente.dtnasc
having valor_total_vendas > 0
order by valor_total_vendas
limit 1