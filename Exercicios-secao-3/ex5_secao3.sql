select distinct autor.nome
    from autor
    join livro on autor.codautor = livro.autor
    join editora on livro.editora = editora.codeditora
    join endereco on editora.endereco = endereco.codendereco
    where endereco.estado not in ('SANTA CATARINA', 'RIO GRANDE DO SUL', 'PARANÁ')
    order by autor.nome