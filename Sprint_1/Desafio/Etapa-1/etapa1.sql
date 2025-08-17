--Visualizando a tabela original (tb_locacao)

select *
from tb_locacao

-- Renomeando e visualizando a tabela original

alter table tb_locacao rename to tb_original

select *
from tb_original

-- Criando e visualizando a tabela vendedor

create table vendedor(
	idVendedor int primary key,
	nomeVendedor varchar,
	sexoVendedor smallint,
	estadoVendedor varchar
	)

select *
from vendedor
	
-- Criando e visualizando a tabela cliente
	
create table cliente(
	idCliente int primary key,
	nomeCliente varchar,
	cidadeCliente varchar,
	estadoCliente varchar,
	paisCliente varchar
	)

select *
from cliente
	
-- Criando e visualizando a tabela combustivel
	
create table combustivel(
	idCombustivel int primary key,
	tipoCombustivel varchar
	)

select *
from combustivel
	
-- Criando e visualizando a tabela carro
	
create table carro(
	idCarro int primary key,
	kmCarro int,
	chassiCarro int,
	marcaCarro varchar,
	modeloCarro varchar,
	anoCarro int,
	idCombustivel int references combustivel(idCombustivel)
	)

select *
from carro
	
-- Criando e visualizando a tabela locacao
	
create table locacao(
	idLocacao int primary key,
	dataLocacao datetime,
	horaLocacao time,
	qntDiaria int,
	vlrDiaria decimal(6,2),
	idVendedor int references vendedor(idVendedor),
	idCiente int references cliente(idCliente),
	idCarro int references carro(idCarro)
	)

select *
from locacao


-- Criando e visualizando a tabela entrega_loc

create table entrega_loc(
	idLocacao int primary key references locacao(idLocacao),
	dataEntrega datetime,
	horaEntrega time
	)

select *
from entrega_loc

-- Inserindo dados na tabela vendedor

insert into vendedor(idVendedor,nomeVendedor, sexoVendedor, estadoVendedor)
select distinct idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
from tb_original 

-- Visualizando a tabela vendedor

select *
from vendedor

-- Inserindo dados na tabela cliente

insert into cliente(idCliente, nomeCliente, CidadeCliente, estadoCliente, paisCliente)
select distinct idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
from tb_original 

-- Visualizando a tabela cliente

select *
from cliente

-- Inserindo dados na tabela combustivel

insert into combustivel (idCombustivel, tipoCombustivel)
select distinct idcombustivel, tipoCombustivel
from tb_original 

-- Visualizando a tabela combustivel

select *
from combustivel

-- Inserindo dados na tabela carro

insert into carro(idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
select distinct idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel 
from tb_original 

-- Ocorreu um erro nessa inserção de dados, então verifiquei que existem carros com mais de uma quilometragem. Sendo assim, optei por selecionar apenas a máxima quilometragem de cada carro, deixando a query assim:

insert into carro(idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
select distinct idCarro, kmCarro, chassiCarro, marcaCarro, modeloCarro, anoCarro, idcombustivel 
from tb_original 
where kmCarro = (
	select(kmCarro)
	from tb_original as maxKm
	where maxkm.idCarro = tb_original.idCarro
) group by idCarro

-- Visualizando a tabela carro

select *
from carro 

-- Inserindo dados na tabela locacao

insert into locacao(idLocacao, dataLocacao, horaLocacao, qntDiaria, vlrDiaria, idVendedor, idCiente, idCarro)
select distinct idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, idVendedor, idCliente, idCarro
from tb_original 

-- Houve um erro nessa inserção. Verifiquei que houve um erro de digitação na coluna "IdCiente" e realizei a correção. Após isso, utilizei a mesma query para inserir os dados na tabela.

alter table locacao rename column idCiente to idCliente 

insert into locacao(idLocacao, dataLocacao, horaLocacao, qntDiaria, vlrDiaria, idVendedor, idCiente, idCarro)
select distinct idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, idVendedor, idCliente, idCarro
from tb_original 

-- Visualizando a tabela locacao

select *
from locacao 

-- Inserindo dados na tabela entrega_loc

insert into entrega_loc(idLocacao, dataEntrega, horaEntrega)
select distinct idLocacao, dataEntrega, horaEntrega
from tb_original

-- Verifiquei que as datas não estavam no formato padrão, ficando pouco inteligíveis. Dessa forma, optei por alterar para o formato YYYY-MM-DD.

-- Alterando o formato das datas na tabela entrega_loc

update entrega_loc
set dataEntrega = substring(dataEntrega, 1, 4) || '-' || substring(dataEntrega, 5, 2) || '-' || substring(dataEntrega, 7, 2)

-- Visualizando a mudança na tabela entrega_loc

select *
from entrega_loc

-- Alterando o formato das datas na tabela locacao 

update locacao
set dataLocacao = substring(dataLocacao, 1, 4) || '-' || substring(dataLocacao, 5, 2) || '-' || substring(dataLocacao, 7, 2)

--  Visualizando a mudança na tabela locacao

select *
from locacao

-- Excluindo a tb_original

drop table tb_original