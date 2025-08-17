# DESAFIO

## [**ETAPA 1**](https://github.com/aline-hoffmann/scholarship-compass/tree/main/Sprint_1/Desafio/Etapa-1)

Inicialmente, após fazer download e descompactar o arquivo “concessionaria.sqlite”, abri o mesmo com auxílio do DBeaver para visualizar sua estrutura.

Em um primeiro momento, verifiquei que todos os dados estavam concentrados em uma única tabela, nomeada de “tb_locacao”. Assim, visando uma melhor organização, optei por realizar a normalização da base de dados, utilizando as três formas normais.

Iniciei alterando o nome da tabela de "tb_locacao" para "tb_original".

```sql
    alter table tb_locacao rename to tb_original
```

De acordo com a **1ª FORMA NORMAL**, cada campo da tabela deve conter apenas um valor atômico, evitando dados compostos ou repetidos em uma mesma coluna.

Sendo assim, dividi os dados da "tb_original" em outras seis tabelas específicas, sendo elas: [**cliente**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-desafio/tab-cliente.jpg), [**vendedor**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-desafio/tab-vendedor.jpg), [**carro**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-desafio/tab-carro.jpg), [**combustivel**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-desafio/tab-combustivel.jpg), [**locacao**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-desafio/tab-locacao.jpg) e [**entrega_loc**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-desafio/tab-entrega-loc.jpg). Dessa forma, cada atributo passou a armazenar apenas uma informação clara e direta.

Exemplo de criação da tabela "cliente":

```sql
    create table cliente(
	idCliente int primary key,
	nomeCliente varchar,
	cidadeCliente varchar,
	estadoCliente varchar,
	paisCliente varchar
	)
```

Ademais, a **2ª FORMA NORMAL** exige que todos os atributos não-chave dependam totalmente da chave primária da tabela. Nesse sentido, garanti que cada tabela armazene apenas informações próprias da sua entidade.

Por exemplo, na tabela "cliente", atributos como "cidadeCliente" e "paisCliente" dependem exclusivamente do idCliente.

Posteriormente, utilizei a **3ª FORMA NORMAL**, cujo objetivo é eliminar dependências transitivas, evitando que um atributo não-chave dependa de outro atributo não-chave.

Para aplicar essa forma, por exemplo, separei os dados de combustível em uma tabela própria chamada "combustivel". Antes, o tipo de combustível poderia se repetir dentro de "carro", mas agora cada carro aponta para um "idCombustivel" e o tipo do combustível fica específico na sua tabela.

```sql
    create table combustivel(
	idCombustivel int primary key,
	tipoCombustivel varchar
	)
```

Além disso, realizei mais algumas alterações para melhor visualização e entendimento dos dados, sendo elas:

- Alterei o formato das datas para o padrão YYYY-MM-DD. Fiz isso para padronizar os valores, deixando as datas mais claras e inteligíveis, garantindo consistência e facilitando consultas e comparações futuras.

```sql
    update entrega_loc
    set dataEntrega = substring(dataEntrega, 1, 4) || '-' || substring(dataEntrega, 5, 2) || '-' || substring(dataEntrega, 7, 2)
```

- Usei uma subquery para garantir que cada carro tivesse apenas um registro na tabela carro, selecionando sempre a maior quilometragem registrada. Isso evita duplicidades, mantém consistência e assegura que cada veículo esteja representado de forma única e atualizada.

```sql
    insert into carro(idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
    select distinct idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel
    from tb_original
    where kmCarro = (
	    select(kmCarro)
	    from tb_original as maxKm
	    where maxkm.idCarro = tb_original.idCarro
    ) group by idCarro
```

<br>

Essa normalização seguiu [**esses passos**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Desafio/Etapa-1/etapa1.sql) e resultou [**nesse diagrama relacional**.](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-desafio/mod-relacional.jpg)

<br>
<br>

## [**ETAPA 2**](https://github.com/aline-hoffmann/scholarship-compass/tree/main/Sprint_1/Desafio/Etapa-2)

Após a normalização, foi necessário criar a modelagem dimensional dos dados. Sendo assim, criei as tabelas Fato e Dimensão:

- [**Tabela Fato "fato_locacao";**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-desafio/tab-fato-locacao.jpg)<br>

- [**Tabela Dimensão "dim_vendedor";**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-desafio/tab-dim-vendedor.jpg)<br>

- [**Tabela Dimensão "dim_cliente";**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-desafio/tab-dim-cliente.jpg)<br>

- [**Tabela Dimensão "dim_carro";**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-desafio/tab-dim-carro.jpg)

Essa modelagem seguiu [**esses passos**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Desafio/Etapa-2/etapa2.sql) e resultou nesse [**diagrama dimensional**](https://github.com/aline-hoffmann/scholarship-compass/blob/main/Sprint_1/Evidencias/Evidencias-desafio/mod-dimensional.jpg).
