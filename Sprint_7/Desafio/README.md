# DESAFIO

Para iniciar a resolução do desafio da Sprint 7, eu organizei os dados da camada Trusted seguindo um modelo em estrela (Star Schema). 

Meu objetivo nessa modelagem foi levar apenas as informações necessárias para responder meus questionamentos, definidos nas sprints anteriores.

Para isso, eu criei uma tabela fato, que concentra as métricas principais, e três dimensões, que armazenam os dados descritivos.

Na tabela fato (fato_avaliação) coloquei informações sobre as avalições dos filmes, como nota média, número de votos e popularidade. Além disso, ela se relaciona com as dimensões de filme, artista e tempo por meio das chaves estrangeiras (id_filme, id_artista, id_tempo).

Quanto às dimensões, criei três, sendo: dim_filme, dim_artista e dim_tempo. A dimensão de filme armazena dados como o título e a duração dos filmes, permitindo observar características e tendências ao longo do tempo. 

A dimensão de artista reúne o nome e o gênero dos artistas, o que possibilita comparar médias de avaliação entre homens e mulheres e identificar os artistas mais recorrentes nas comédias. 

Já a dimensão de tempo organiza os dados por ano de lançamento, servindo de base para analisar a evolução das produções e o comportamento da duração dos filmes ao longo dos anos.

<br>

![imagem](../Evidencias/modelagem-estrela.jpg)

<br>

Com essa modelagem, estruturei a camada Refined de forma mais analítica, levando apenas os dados realmente úteis para as minhas análises.