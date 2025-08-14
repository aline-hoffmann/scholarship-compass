  select
        autor.nome,
        autor.codautor,
        autor.nascimento,
        count(livro.cod) as quantidade
    from autor
    left join livro on autor.codautor = livro.autor
    group by autor.nome, autor.codautor, autor.nascimento
    order by replace (autor.nome, 'Á', 'A')