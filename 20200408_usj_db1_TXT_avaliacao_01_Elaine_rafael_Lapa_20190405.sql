Elaine Mattje / Rafael Lapa
Avalia��o 01 - 05/04/2019

#1 - 1,0pt
CREATE DATABASE avaliacao_01_Elaine_Rafael_Lapa;
USE avaliacao_01_Elaine_Rafael_Lapa;


#2 - 2,0pt
CREATE TABLE IF NOT EXISTS empresa (
id int(11) NOT NULL AUTO_INCREMENT,
nome varchar(50) NOT NULL,
ano_fundacao tinyint(4) NOT NULL,
ramo_atuacao varchar(30) DEFAULT 'nao informado',
capital decimal(10,2),
PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS funcionario (
id int(11) NOT NULL AUTO_INCREMENT,
nome varchar(50) NOT NULL,
nascimento date NOT NULL,
ano_inicio_trabalho tinyint(4),
funcao varchar(30) NOT NULL,
empresa int(11) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (empresa) REFERENCES empresa(id)
);


#3 - 1,0pt

ALTER TABLE empresa MODIFY COLUMN ano_fundacao smallint(4) NOT NULL;

ALTER TABLE funcionario MODIFY COLUMN ano_inicio_trabalho smallint(4);


#4 - 1,5 erro no valor da empresa ao inserir funcionario

INSERT INTO empresa (nome, ano_fundacao, ramo_atuacao, capital) VALUE ('google', 2001, 'busca internet', 10500.55 );
INSERT INTO empresa (nome, ano_fundacao, ramo_atuacao, capital) VALUE ('facebook', 2005, 'redes sociais', 7600.45);
INSERT INTO empresa (nome, ano_fundacao, ramo_atuacao, capital) VALUE ('youtube', 2002, 'streaming videos', 5900.00);
INSERT INTO empresa (nome, ano_fundacao, ramo_atuacao, capital) VALUE ('whatsapp', 2010, 'chat', 8000.00);
INSERT INTO empresa (nome, ano_fundacao, ramo_atuacao, capital) VALUE ('telegram', 2015, 'chat', 2000.50);

#SELECT * FROM empresa;

INSERT INTO funcionario (nome, nascimento, ano_inicio_trabalho, funcao, empresa) VALUE ('Pedro', '1985-05-01', 2017, 'programador', 17);
INSERT INTO funcionario (nome, nascimento, ano_inicio_trabalho, funcao, empresa) VALUE ('Maria', '1991-04-16',2005,'analista', 13);
INSERT INTO funcionario (nome, nascimento, ano_inicio_trabalho, funcao, empresa) VALUE ('Joao','1982-10-31',2011,'suporte',16);
INSERT INTO funcionario (nome, nascimento, ano_inicio_trabalho, funcao, empresa) VALUE ('Steve','2001-04-05',2006,'analista',15);
INSERT INTO funcionario (nome, nascimento, ano_inicio_trabalho, funcao, empresa) VALUE ('Bill','1977-12-25',2002,'gerente',13);
INSERT INTO funcionario (nome, nascimento, ano_inicio_trabalho, funcao, empresa) VALUE ('Rafael','1983-01-24',2009,'gerente',14);
INSERT INTO funcionario (nome, nascimento, ano_inicio_trabalho, funcao, empresa) VALUE ('Marc','1993-09-11',2018,'testador',17);
INSERT INTO funcionario (nome, nascimento, ano_inicio_trabalho, funcao, empresa) VALUE ('William','1975-09-01',2011,'programador',13);
INSERT INTO funcionario (nome, nascimento, ano_inicio_trabalho, funcao, empresa) VALUE ('Teodoro','1979-01-23',2008,'suporte',14);
INSERT INTO funcionario (nome, nascimento, ano_inicio_trabalho, funcao, empresa) VALUE ('Thiago','2001-09-11',2004,'analista',15);
INSERT INTO funcionario (nome, nascimento, ano_inicio_trabalho, funcao, empresa) VALUE ('Elaine','1985-12-11',2001,'programador',13);
INSERT INTO funcionario (nome, nascimento, ano_inicio_trabalho, funcao, empresa) VALUE ('Rafael Lapa','1995-12-11',2019,'programador',17);

#SELECT * FROM funcionario;


#5 - 0,5pt

SELECT DISTINCT funcao FROM funcionario;


#6  - 1,0pt

SELECT funcao, COUNT(*) FROM funcionario GROUP BY funcao ORDER BY funcao;


#7 - 0,5

SELECT * FROM empresa WHERE nome LIKE '%e';


#8 - 0,3pt - erro no tipo de dado do ano de fundacao

SELECT COUNT(*), SUM(capital) FROM empresa WHERE ano_fundacao > '2004-01-01';


#9 - 0,5pt

SELECT DISTINCT ramo_atuacao, COUNT(*) FROM empresa GROUP BY ramo_atuacao;


#10 - 0,5pt

SELECT * FROM funcionario WHERE (YEAR(CURDATE()) - YEAR(nascimento)) > 20;


#11 - 0,3 ano_inicio_trabalho é um valor numérico

UPDATE funcionario SET funcao = 'gerente' WHERE ano_inicio_trabalho = '2019-01-01';

#SELECT * FROM funcionario WHERE ano_inicio_trabalho = '2019';




