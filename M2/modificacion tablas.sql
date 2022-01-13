use proyecto;

alter table usuarios 
add primary key(id_usu),
add unique(id_usu),
add unique(nombre),
modify id_usu int auto_increment,
modify nombre varchar(10) not null,
modify password varchar(12) not null,
modify fechacreacion datetime null,
modify usuariocreacion varchar(10) not null,
modify fechamodificacion datetime null,
modify usuariomodificacion varchar(10) not null;

alter table personajes
add primary key(id_per),
add unique(id_per),
modify id_per int auto_increment,
modify nombre varchar(10) not null,
modify fechacreacion datetime null,
modify usuariocreacion varchar(10) not null,
modify fechamodificacion datetime null,
modify usuariomodificacion varchar(10) not null;

alter table aventura
add primary key(id_aventura),
add unique(id_aventura),
modify id_aventura int auto_increment,
modify nombre_aventura varchar(100) not null,
modify fecha datetime null,
modify id_usu int not null,
modify id_per int not null,
modify fechacreacion datetime null,
modify usuariocreacion varchar(10) not null,
modify fechamodificacion datetime null,
modify usuariomodificacion varchar(10) not null,
add constraint fk_aventura_usuarios
	foreign key (id_usu)
		references usuarios(id_usu),
add constraint fk_aventura_personajes
	foreign key (id_per)
		references personajes(id_per);

alter table pasos
add primary key(id_paso),
add unique(id_paso),
modify id_paso int auto_increment,
modify paso varchar(1000) not null,
modify id_aventura int not null,
modify num_paso int not null,
modify fechacreacion datetime null,
modify usuariocreacion varchar(10) not null,
modify fechamodificacion datetime null,
modify usuariomodificacion varchar(10) not null,
add constraint fk_pasos_aventura
	foreign key (id_aventura)
		references aventura(id_aventura);

alter table respuesta
add primary key(id_respuesta),
add unique(id_respuesta),
modify id_respuesta int auto_increment,
modify respuesta varchar(1000) not null,
modify id_paso int not null,
modify id_aventura int not null,
modify num_respuesta int not null,
modify fechacreacion datetime null,
modify usuariocreacion varchar(10) not null,
modify fechamodificacion datetime null,
modify usuariomodificacion varchar(10) not null,
add constraint fk_respuesta_pasos
	foreign key (id_paso)
		references pasos(id_paso),
add constraint fk_respuesta_aventura
	foreign key (id_aventura)
		references aventura(id_aventura);

alter table repeticiones
add primary key(id_num),
add unique (id_num),
modify id_num int auto_increment,
modify numero int not null,
modify id_aventura int not null,
modify id_usu int not null,
modify fechacreacion datetime null,
modify usuariocreacion varchar(10) not null,
modify fechamodificacion datetime null,
modify usuariomodificacion varchar(10) not null,
add constraint fk_repeticiones_aventura
	foreign key (id_aventura)
		references aventura(id_aventura),
add constraint fk_repeticiones_usuarios
	foreign key (id_usu)
		references usuarios(id_usu);

CREATE unique INDEX indice_usuarios ON usuarios(id_usu);
CREATE unique INDEX indice_aventura ON aventura(id_aventura);
CREATE unique INDEX indice_personajes ON personajes(id_per);
CREATE unique INDEX indice_repeticion ON repeticiones(id_num);
CREATE unique INDEX indice_respuesta ON respuesta(id_respuesta);
CREATE unique INDEX indice_pasos ON pasos(id_paso);



