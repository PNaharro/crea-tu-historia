create database if not exists proyecto;

use proyecto;

create table if not exists usuarios (
id_usu int,
nombre varchar(10),
password varchar(12),
fechacreacion datetime,
usuariocreacion varchar(10),
fechamodificacion datetime,
usuariomodificacion varchar(10)
);

create table if not exists personajes (
id_per int ,
nombre varchar(10),
fechacreacion datetime,
usuariocreacion varchar(10),
fechamodificacion datetime,
usuariomodificacion varchar(10)
);

create table if not exists aventura (
id_aventura int,
nombre_aventura varchar(100),
fecha datetime,
fechacreacion datetime,
usuariocreacion varchar(10),
fechamodificacion datetime,
usuariomodificacion varchar(10),
descripcion varchar(100)
);

create table if not exists pasos (
id_paso int ,
paso varchar(1000),
id_aventura int, 
num_paso int,
final int,
fechacreacion datetime,
usuariocreacion varchar(10),
fechamodificacion datetime,
usuariomodificacion varchar(10)
);

create table if not exists respuesta (
id_respuesta int ,
respuesta varchar(1000) ,
id_paso int,
num_respuesta int,
id_aventura int,
fechacreacion datetime,
usuariocreacion varchar(10),
fechamodificacion datetime,
usuariomodificacion varchar(10)
);

create table if not exists repeticiones (
id_num int,
id_paso int,
id_respuesta int,
id_game int,
fechacreacion datetime,
usuariocreacion varchar(10),
fechamodificacion datetime,
usuariomodificacion varchar(10)
);

create table if not exists game (
idgame int,
id_aventura int,
id_usuario int,
id_personaje int,
fechacreacion datetime,
usuariocreacion varchar(10),
fechamodificacion datetime,
usuariomodificacion varchar(10)
);

savepoint p3;