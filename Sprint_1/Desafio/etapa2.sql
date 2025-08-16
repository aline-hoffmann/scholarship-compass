-- Criando as tabelas para a modelagem dimensional

-- Dimensão vendedor

create table dim_vendedor(
	id int primary key,
	nome varchar,
	sexo smallint,
	estado varchar
	)

-- Dimensão cliente

create table dim_cliente(
	id int primary key,
	nome varchar,
	cidade varchar,
	estado varchar,
	pais varchar
	)

	
-- Dimensão carro
-- Alterei os dados de combustível, trazendo os mesmos para a dimensão carro, sendo assim um atributo.

create table dim_carro(
	id int primary key,
	km int,
	chassi int,
	marca varchar,
	modelo varchar,
	ano int,
	idCombustivel int,
	tipoCombustivel varchar
	)

-- Criando a Tabela fato locacao
-- Aqui também realizei uma alteração em relação ao modelo relacional, trazendo os dados de entrega para a tabela fato de locacão. Sendo assim atributos dela.
-- Criei uma chave primária composta, sendo assim, o banco só vai permitir um único registro para cada combinação dos valores idCliente, idVendedor, idCarro e dataLocacao.

create table fato_locacao(
	idCliente int references cliente(id),
	idVendedor int references vendedor(id),
	idCarro int references carro(id),
	dataLocacao date,
	horaLocacao time,
	dataEntrega date,
	horaEntrega time,
	qntDiaria int,
	vlrDiaria decimal(6,2),
	
	constraint pk_fato_locacao primary key (idCliente, idVendedor, idCarro, dataLocacao)
	
	)

-- Inserindo dados na tabela dim_vendedor

insert into dim_vendedor (id, nome, sexo, estado)
select distinct idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
from vendedor

-- Inserindo dados na tabela dim_cliente

insert into dim_cliente (id, nome, cidade, estado, pais)
select distinct idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
from cliente

-- Inserindo dados na tabela dim_carro

insert into dim_carro(id, km, chassi, marca, modelo, ano, idCombustivel, tipoCombustivel)
select distinct 
	c.idCarro, 
	c.kmCarro,
	c.chassiCarro,
	c.marcaCarro,
	c.modeloCarro,
	c.anoCarro,
	c.idCombustivel,
	cm.tipoCombustivel
from carro as c
join combustivel cm on c.idCombustivel = cm.idCombustivel

-- Inserindo dados na tabela fato_locacao

insert into fato_locacao (idCliente, idVendedor, idCarro, dataLocacao, horaLocacao, dataEntrega, horaEntrega, qntDiaria, vlrDiaria)
select distinct 
    l.idCliente,
    l.idVendedor,
    l.idCarro,
    l.dataLocacao,
    l.horaLocacao,
    e.dataEntrega,
    e.horaEntrega,
    l.qntDiaria,
    l.vlrDiaria
from locacao as l
join entrega_loc as e on l.idLocacao = e.idLocacao



