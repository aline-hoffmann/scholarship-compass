**E01.** Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas. Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma.

    select *
    from livro
    where publicacao > '2014-12-31'
    order by cod

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex1_secao3.jpg)

<br>

**E02.** Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente. Atenção às colunas esperadas no resultado final: titulo, valor.

    select titulo, valor
    from livro
    order by valor desc
    limit 10

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex2_secao3.jpg)

<br>

**E03.** Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

    select
        count(livro.cod) as quantidade,
        editora.nome,
        endereco.estado,
        endereco.cidade
    from livro
    left join editora on livro.editora = editora.codeditora
    left join endereco on editora.endereco = endereco.codendereco
    group by editora.nome, endereco.estado, endereco.cidade
    order by quantidade desc
    limit 5

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex3_secao3.jpg)

<br>

**E04.** Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

Dica para ordenação: Utilize Replace.

    select
        autor.nome,
        autor.codautor,
        autor.nascimento,
        count(livro.cod) as quantidade
    from autor
    left join livro on autor.codautor = livro.autor
    group by autor.nome, autor.codautor, autor.nascimento
    order by replace (autor.nome, 'Á', 'A')

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex4_secao3.jpg)

<br>

**E05.** Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

    select distinct autor.nome
    from autor
    join livro on autor.codautor = livro.autor
    join editora on livro.editora = editora.codeditora
    join endereco on editora.endereco = endereco.codendereco
    where endereco.estado not in ('SANTA CATARINA', 'RIO GRANDE DO SUL', 'PARANÁ')
    order by autor.nome

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex5_secao3.jpg)

<br>

**E06.** Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

    select
        autor.codautor,
        autor.nome,
        count(livro.cod) as quantidade_publicacoes
    from autor
    left join livro on autor.codautor = livro.autor
    group by autor.codautor, autor.nome
    order by quantidade_publicacoes desc
    limit 1

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex6_secao3.jpg)

<br>

**E07.** Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

    select autor.nome
    from autor
    left join livro on autor.codautor = livro.autor
    where livro.cod is null
    order by autor.nome

- [Link para evidência](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-exercicios/ex7_secao3.jpg)

<br>
