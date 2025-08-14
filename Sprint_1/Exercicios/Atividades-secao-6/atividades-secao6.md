## <p align="center"> ATIVIDADES - SEÇÃO 6</p>

**Etapa 1.** Para apresentar o resultado solicitado, utilizei o "AS" para renomear as colunas no resultado. O "LEFT JOIN" foi usado para combinar os valores solicitados das tabelas "autor" e "editora" com os da tabela "livro".

    select
        livro.cod as CodLivro,
        livro.titulo as Titulo,
        autor.codautor as CodAutor,
        autor.nome as NomeAutor,
        livro.valor as Valor,
        editora.codeditora as CodEditora,
        editora.nome as NomeEditora

    from livro
    left join autor on livro.autor = autor.codautor
    left join editora on livro.editora = editora.codeditora
    order by valor desc
    limit 10

- [Link do arquivo .csv](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Exercicios/Atividades-secao-6/atividade1_s6.csv)

<br>

**Etapa 2.** Para obter o resultado solicitado, utilizei novamente o "AS" para renomear as colunas no resultado. Dessa vez foi usado o "INNER JOIN" para unir apenas as linhas em que o código da tabela "editora" coincide com o valor da coluna "editora" na tabela "livro".

    select
        editora.codeditora as CodEditora,
        editora.nome as NometEditora,
        count(livro.cod) as QuantidadeLivros
    from editora
    inner join livro on editora.codeditora = livro.editora
    group by editora.codeditora, editora.nome
    order by QuantidadeLivros desc
    limit 5

- [Link do arquivo .csv](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Exercicios/Atividades-secao-6/atividade2_s6.csv)
