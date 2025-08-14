select autor.nome
from autor
left join livro on autor.codautor = livro.autor
where livro.cod is null
order by autor.nome