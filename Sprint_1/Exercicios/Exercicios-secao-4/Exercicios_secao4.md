**E08.** Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

    select tbvendedor.cdvdd, tbvendedor.nmvdd
    from tbvendedor
    inner join tbvendas on tbvendedor.cdvdd = tbvendas.cdvdd
    where tbvendas.status = 'Concluído'
    group by tbvendedor.cdvdd, tbvendedor.nmvdd
    order by count(tbvendas.cdven) desc
    limit 1

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Evidencias-exercicios/ex1_secao3.jpg)

<br>

**E09.** Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

    select cdpro, nmpro
    from tbvendas
    where dtven between '2014-02-03' and '2018-02-02' and status = 'Concluído'
    group by qtd
    order by qtd desc
    limit 1

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Evidencias-exercicios/ex1_secao3.jpg)

<br>

**E10.** A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

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

**Nesse exercício utilizei a função "ROUND" para arrendondar as casas decimais, conforme solicitado.**

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Evidencias-exercicios/ex1_secao3.jpg)

<br>

**E11.** Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

    select
        tbvendas.cdcli,
        tbvendas.nmcli,
        sum(tbvendas.qtd * tbvendas.vrunt) as gasto
    from tbvendas
    where tbvendas.status = 'Concluído'
    group by tbvendas.cdcli, tbvendas.nmcli
    order by gasto desc
    limit 1
    
- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Evidencias-exer)

<br>

**E12.** Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.

Observação: Apenas vendas com status concluído.

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

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Evidencias-exer)

<br>

**E13.** Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

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

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Evidencias-exer)

<br>

**E14.** Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

Observação: Apenas vendas com status concluído.

    select
        tbvendas.estado,
        round(avg(tbvendas.qtd * tbvendas.vrunt), 2) as gastomedio
    from tbvendas
    where tbvendas.status = 'Concluído'
    group by  tbvendas.estado
    order by gastomedio desc

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Evidencias-exer)

<br>

**E15.** Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

    select tbvendas.cdven
    from tbvendas
    where tbvendas.deletado = 1
    order by tbvendas.cdven

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Evidencias-exer)

<br>

**E16.** Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).

Obs: Somente vendas concluídas.

    select
        tbvendas.estado,
        tbvendas.nmpro,
        round(avg(tbvendas.qtd), 4) as quantidade_media
    from tbvendas
    join tbestoqueproduto on tbvendas.cdpro = tbestoqueproduto.cdpro
    where tbvendas.status = 'Concluído'
    group by tbvendas.estado, tbvendas.nmpro
    order by tbvendas.estado, tbvendas.nmpro

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Evidencias-exer)