use projecto;

alter table usuarios 
add primary key(id_usu),
add unique(id_usu),
add unique(nombre),
modify id_usu int auto_increment,
modify nombre varchar(10) not null,
modify password varchar(12) not null;

alter table aventura
add primary key(id_aventura),
add unique(id_aventura),
modify id_aventura int auto_increment,
modify nombre_aventura varchar(100) not null,
modify fecha datetime not null,
modify id_usu int not null,
modify id_per int not null;

alter table pasos
add primary key(id_paso),
add unique(id_paso),
modify id_paso int auto_increment,
modify paso varchar(1000) not null,
modify id_aventura int not null;

alter table respuesta
add primary key(id_respuesta),
add unique(id_respuesta),
modify id_respuesta int auto_increment,
modify respuesta varchar(1000) not null,
modify id_paso int not null;
