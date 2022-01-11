create database if not exists projecto;

use projecto;

savepoint P1;


create table if not exists usuarios (
id_usu int auto_increment unique primary key,
nombre varchar(10) not null unique,
password varchar(12) not null
);

create table if not exists aventura (
id_aventura int auto_increment unique primary key,
nombre_aventura varchar(100) not null,
fecha datetime not null,
id_usu int not null,
constraint id_usu
foreign key (id_usu)
	references usuarios(id_usu),
id_per int not null,
constraint id_per
foreign key (id_per)
	references personajes(id_per)
);

create table if not exists pasos (
id_paso int auto_increment unique primary key,
paso varchar(1000) not null,
id_aventura int not null,
constraint id_aventura
foreign key (id_aventura)
	references aventura(id_aventura)
);

create table if not exists respuesta (
id_respuesta int auto_increment unique primary key,
respuesta varchar(1000) not null,
id_paso int not null,
constraint id_paso
foreign key (id_paso)
	references pasos(id_paso)
);

create table if not exists repeticiones (
id_num int auto_increment unique primary key,
numero int not null,
id_aventura int not null,
constraint id_aventura_rep
foreign key (id_aventura)
	references aventura(id_aventura),
id_usu int not null,
constraint id_usu_rep
foreign key (id_usu)
	references usuarios(id_usu)
);

create table if not exists personajes (
id_per int auto_increment unique primary key,
nombre varchar(10) not null
);



