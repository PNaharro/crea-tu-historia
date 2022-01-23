use proyecto;

insert into usuarios(nombre,password,usuariocreacion) values ("Pau","Password",user());
insert into usuarios(nombre,password,usuariocreacion) values ("a","a",user());

insert into personajes(nombre,usuariocreacion) values ("Jose",user());
insert into personajes(nombre,usuariocreacion) values ("Laura",user());

insert into aventura(nombre_aventura,usuariocreacion,usuariomodificacion,descripcion) values ("Death is Death"
,"Naharro","Naharro","Descubre de donde proceden los sonidos");

insert into aventura(nombre_aventura,usuariocreacion,descripcion) values ("Life is Death"
,user(),"TExto de ejemplo tan ejemplar que ejemplo ejemplo");

insert into aventura(nombre_aventura,usuariocreacion,descripcion) values ("Ejemplo 1"
,user(),"TExto de ejemplo tan ejemplar que ejemplo ejemplo");

insert into aventura(nombre_aventura,usuariocreacion,descripcion) values ("Ejemplo 2"
,user(),"TExto de ejemplo tan ejemplar que ejemplo ejemplo");

insert into aventura(nombre_aventura,usuariocreacion,descripcion) values ("Ejemplo 3"
,user(),"TExto de ejemplo tan ejemplar que ejemplo ejemplo");


insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion, final) 
values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Despiertas tras una pesadilla, la noche es tranquila y intentas relajarte despues de el susto, al conseguir calmarte escuchas ruido fuera de tu piso. Que hace MC:"
,"1","Naharro","Naharro","1");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion, final) 
values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Ignoras el ruido y intentas volver a dormir,después de un rato consigues dormir. Al despertar, miras por la ventana y te encuentras las calles llenas de gente muerta y sangre. Asustado sales de tu habitación a ver si tus padres estan bien. Al revisar la casa entera te das cuenta de que no hay nadie en ella aparte de ti. Que hace MC:"
,"11","Naharro","Naharro","1");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion, final) 
values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Sales rápido de casa a buscar a tus padres pero nada mas salir te encuentras con alguien caminando de manera errática por los pasillo, al verte grita y corre hacia ti. Que hace MC:"
,"111","Naharro","Naharro","1");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion, final) 
values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Al intentar pelear la persona te gana en fuerza por lo que te tira al suelo te golpeas la cabeza lo que te deja inconsciente a merced del zombie."
,"1111","Naharro","Naharro","0");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion, final) 
values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Huilles subiendo las escaleras hasta llegar a la azotea pero al intentar abrir la puerta esta cerrada por lo que el zombie que te perseguía al cual tras el ruido de la carrera ahora no solo es uno, te acorralan contra la puerta, devorándote. Tus gritos se escuchan por todo el edificio."
,"1112","Naharro","Naharro","0");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion, final) 
values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Esperas en casa durante todo el dia pero ello no vuelven, te asomas a la venta para ver si puedes ver algo mas de fuera, al mirar por la ventana ves que la situacion ha empeorado ves gente corriendo y gritando por la calles, al ver esa escena cieras la persiana. Que hace MC:"
,"112","Naharro","Naharro","1");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion,final) 
values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Tapas la puerta con lo que puedes pero al hacer ruido moviendo las cosa una gran cantidad de zombies vienen hacia ti, te quedas encerado hay hasta quedarte sin comida, y mueres con el tiempo debido a la desnutrición."
,"1121","Naharro","Naharro","0");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion,final) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"al pensar que todo esto sigue siendo un sueño, decide acabar con tu vida, pensando que asi te despertaras, asi que vas a la ventana del comedor la mas grande que hay en tu casa y saltas, estrellándose conta el suelo acabando con tu vida."
,"1122","Naharro","Naharro","0");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion,final) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"antes de salir buscas en tu casa algo para defenderte, coges un cuchillo de la cocina y sales de casa.pero nada mas salir te encuentras con alguien caminando de manera errática por los pasillo, al verte grita y corre hacia ti. Que hace MC:"
,"113","Naharro","Naharro","1");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion,final) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"al intentar pelear consigues acertas un golpe mortal a la cabeza del zombie lo que hace caer al suelo. al mirar de cerca al zombie te das cuenta que es tu padre. impactado por lo sucedido te arrodillas para abrazar a tu padre ya muerto, el sonido de tus llantos atrae a los zombies, ya sabiendo lo que va a pasar te resignas a morir."
,"1131","Naharro","Naharro","0");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion,final) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"huilles subiendo las escaleras hasta llegar a la azotea pero al intentar abrir la puerta esta cerrada por lo que el zombie que te perseguía al cual tras el ruido de la carrera ahora no solo es uno, te acorralan contra la puerta, devorándote, mientras intentas defenderte con tu cuchillo si hacer efecto alguno contra tantos de ellos."
,"1132","Naharro","Naharro","0");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion,final) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Te levantas de la cama para ir a ver que ha pasado, al salir de tu cuarto encuentras a tu madre y padre despierto llendo a mirar que pasa. Que hace MC:"
,"12","Naharro","Naharro","1");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion,final) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"vas con ellos a mira que ha pasado al salir de casa algo ataca a tu madre , tu y tu padre vais a ayudarla, causando que os noquen a ti y a tu padre, decando a merced de lo que pase a los dos."
,"121","Naharro","Naharro","0");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion,final) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
," decides no ir con ellos, cuando ellos salen los escuchas gritar, pensando que solo se estan peleando con tus vecinos no le tomas mucha importancia, pasado un rato todo queda en silencio, y después de eso escuchas la puerta, mientras que vas quedando dormido. mientras estas dormido alguien entra a tu habitación haciendo ruido inentendibles."
,"122","Naharro","Naharro","0");

################################


insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Ignoras el ruido y intentas volver a domir.",11,"Naharro","Naharro","1");

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Te levantas de la cama para ir a ver que ha pasado.",12,"Naharro","Naharro","1");

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Salir rapido de casa a buscarlos.",111,"Naharro","Naharro","2");

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Esperar en casa a que vuelvan a casa.",112,"Naharro","Naharro","2");

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Coger un algo para defenderte y salir a buscarlos.",113,"Naharro","Naharro","2");

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Pelear",1111,"Naharro","Naharro","3");

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Huir",1112,"Naharro","Naharro","3");

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Tapar la puerta de tu casa.",1121,"Naharro","Naharro","6");

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Acabar con tu vida.",1122,"Naharro","Naharro","6");

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Pelear",1131,"Naharro","Naharro","9");

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Huir.",1132,"Naharro","Naharro","9");

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Ir con ellos.",121,"Naharro","Naharro","12");

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"No ir.",122,"Naharro","Naharro","12");



