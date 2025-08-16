select *
from tb_locacao

alter table tb_locacao rename to tb_original

select *
from tb_original

update tb_original
set dataLocacao = substring(dataLocacao, 1, 4) || '-' || substring(dataLocacao, 5, 2) || '-' || substring(dataLocacao, 7, 2),
	dataEntrega = substring(dataEntrega , 1, 4) || '-' || substring(dataEntrega , 5, 2) || '-' || substring(dataEntrega , 7, 2)
	
select *
from tb_original

-- Criando a tabela vendedor

create table vendedor(
	idVendedor int primary key,
	nomeVendedor varchar,
	sexoVendedor smallint,
	estadoVendedor varchar
	)
	
-- Criando a tabela cliente
	
create table cliente(
	idCliente int primary key,
	nomeCliente varchar,
	cidadeCliente varchar,
	estadoCliente varchar,
	paisCliente varchar
	)
	
-- Criando a tabela combustivel
	
create table combustivel(
	idCombustivel int primary key,
	tipoCombustivel varchar
	)
	
-- Criando a tabela carro
	
create table carro(
	idCarro int primary key,
	kmCarro int,
	chassiCarro int,
	marcaCarro varchar,
	modeloCarro varchar,
	anoCarro int,
	idCombustivel int references combustivel(idCombustivel)
	)
	
-- Criando a tabela locacao
	
create table locacao(
	idLocacao int primary key,
	dataLocacao date,
	horaLocacao time,
	qntDiaria int,
	vlrDiaria decimal(6,2),
	idVendedor int references vendedor(idVendedor),
	idCiente int references cliente(idCliente),
	idCarro int references carro(idCarro)
	)


-- Criando a tabela entrega_loc

create table entrega_loc(
	idLocacao int primary key references locacao(idLocacao)
	dataEntrega date,
	horaEntrega time
	)


	-- Inserindo dados na tabela vendedor

insert into vendedor(idVendedor,nomeVendedor, sexoVendedor, estadoVendedor)
select distinct idVendedor,nomeVendedor, sexoVendedor, estadoVendedor
from tb_original 

-- Visualizando e criando um "apelido" para a tabela vendedor

select *
from vendedor as vend

-- Inserindo dados na tabela cliente

insert into cliente(idCliente, nomeCliente, CidadeCliente, estadoCliente, paisCliente)
select distinct idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
from tb_original 

-- Visualizando e criando um "apelido" para a tabela cliente

select *
from cliente as cli

-- Inserindo dados na tabela combustivel

insert into combustivel (idCombustivel, tipoCombustivel)
select distinct idcombustivel, tipoCombustivel
from tb_original 

-- Visualizando e criando um "apelido" para a tabela combustivel

select *
from combustivel as comb

-- Inserindo dados na tabela carro

insert into carro(idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
select distinct idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel 
from tb_original 

-- Visualizando e criando um "apelido" para a tabela carro

select *
from carro as car

-- Ocorreu um erro, pois existem carros com mais de uma kilometragem. Sendo assim, optei por selecionar apenas a máxima kilometragem do carro, deixando a query assim:

insert into carro(idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
select distinct idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel 
from tb_original 
where kmCarro = (
	select(kmCarro)
	from tb_original as maxKm
	where maxkm.idCarro = tb_original.idCarro
) group by idCarro

-- Inserindo dados na tabela locacao

insert into locacao(dataLocacao, horaLocacao, qntDiaria, vlrDiaria, idVendedor, idCiente, idCarro)
select distinct dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, idVendedor, idCliente, idCarro
from tb_original 

-- Visualizando e criando um "apelido" para a tabela locacao

select *
from locacao as loc

-- Verifiquei que houve um erro de digitação na coluna "IdCiente" e realizei a correção

alter table locacao rename column idCiente to idCliente

-- Inserindo dados na tabela entrega_loc

insert into entrega_loc(idLocacao, dataEntrega, horaEntrega)
select distinct idLocacao, dataEntrega, horaEntrega
from tb_original

-- Excluindo a tb_original

drop table tb_original