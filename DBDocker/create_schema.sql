CREATE SCHEMA seed;

USE seed;

CREATE TABLE usuarios (
  id int NOT NULL AUTO_INCREMENT,
  nome varchar(255) DEFAULT NULL,
  imagem varchar(255) DEFAULT NULL,
  email varchar(255) NOT NULL,
  senha varchar(255) NOT NULL,
  criado_em datetime DEFAULT NULL,
  atualizado_em datetime DEFAULT NULL,
  PRIMARY KEY (id)
);



CREATE TABLE tarefas (
  id int NOT NULL AUTO_INCREMENT,
  usuario_id int DEFAULT NULL,
  nome varchar(255) DEFAULT NULL,
  descricao varchar(255) DEFAULT NULL,
  concluido tinyint(1) NOT NULL,
  criado_em datetime DEFAULT NULL,
  atualizado_em datetime DEFAULT NULL,
  PRIMARY KEY (id),
  KEY usuario_id (usuario_id),
  CONSTRAINT tarefas_ibfk_1 FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
);