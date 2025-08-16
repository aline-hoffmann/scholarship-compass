-- Criando as tabelas para a modelagem dimensional

-- Criando e visuando Dimensão vendedor

create table dim_vendedor(
	id int primary key,
	nome varchar,
	sexo smallint,
	estado varchar
	)

select *
from dim_vendedor

-- Criando e visuando Dimensão cliente

create table dim_cliente(
	id int primary key,
	nome varchar,
	cidade varchar,
	estado varchar,
	pais varchar
	)

select *
from dim_cliente
	
-- Criando e visuando Dimensão carro
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

select *
from dim_carro

-- Criando a Tabela fato locacao
-- Aqui também realizei uma alteração em relação ao modelo relacional, trazendo os dados de entrega para a tabela fato de locacão. Sendo assim atributos dela.
-- Criei uma chave primária composta, sendo assim, o banco só vai permitir um único registro para cada combinação dos valores idCliente, idVendedor, idCarro e dataLocacao.

create table fato_locacao(
	idCliente int,
	idVendedor int,
	idCarro int,
	dataLocacao datetime,
	horaLocacao time,
	dataEntrega datetime,
	horaEntrega time,
	qntDiaria int,
	vlrDiaria decimal(6,2),
	
	constraint pk_fato_locacao primary key (idCliente, idVendedor, idCarro, dataLocacao)
	
	constraint fk_ft_cliente foreign key (idCliente) references dim_cliente(id),
	
	constraint fk_ft_vendedor foreign key (idVendedor) references dim_vendedor(id),
	
	constraint fk_ft_carro foreign key (idCarro) references dim_carro(id)
	
	)

-- Inserindo dados na tabela dim_vendedor e visualizando

insert into dim_vendedor (id, nome, sexo, estado)
select distinct idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
from vendedor

select *
from dim_vendedor

-- Inserindo dados na tabela dim_cliente e visualizando

insert into dim_cliente (id, nome, cidade, estado, pais)
select distinct idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
from cliente

select *
from dim_cliente

-- Inserindo dados na tabela dim_carro e visualizando

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

select *
from dim_carro

-- Inserindo dados na tabela fato_locacao e visualizando

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
left join entrega_loc as e on l.idLocacao = e.idLocacao 

select *
from fato_locacao




