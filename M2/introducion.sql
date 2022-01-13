use proyecto;

insert into usuarios(nombre,password,usuariocreacion,usuariomodificacion) values ("Pau","Password",user(),user());

insert into personajes(nombre,usuariocreacion,usuariomodificacion) values ("Jose","Naharro","Naharro");

insert into aventura(nombre_aventura,id_usu,id_per,usuariocreacion,usuariomodificacion) values ("Death is Death",
(select id_usu from usuarios where nombre="Pau"),
(select id_per from personajes where nombre="Jose")
,"Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Despiertas tras una pesadilla, la noche es tranquila y intentas relajarte despues de el susto, al conseguir calmarte escuchas ruido fuera de tu piso, Que hace MC:"
,"1","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Ignoras el ruido y intentas volver a dormir,después de un rato consigues dormir.al despertar, miras por la ventana y te encuentras las calles llenas de gente muerta y sangre. Asustado sales de tu habitación a ver si tus padres estan bien. Al revisar la casa entera te das cuenta de que no hay nadie en ella aparte de ti.Que hace MC:"
,"11","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Sales rápido de casa a buscar a tus padres pero nada mas salir te encuentras con alguien caminando de manera errática por los pasillo, al verte grita y corre hacia ti. Que hace MC:"
,"111","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"al intentar pelear la persona te gana en fuerza por lo que te tira al suelo te golpeas la cabeza lo que te deja inconsciente a merced del zombie."
,"1111","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"huilles subiendo las escaleras hasta llegar a la azotea pero al intentar abrir la puerta esta cerrada por lo que el zombie que te perseguía al cual tras el ruido de la carrera ahora no solo es uno, te acorralan contra la puerta, devorándote. tus gritos se escuchan por todo el edificio."
,"1112","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"esperas en casa durante todo el dia pero ello no vuelven, te asomas a la venta para ver si puedes ver algo mas de fuera, al mirar por la ventana ves que la situacin a enpeorado ves gente corriendo y gritando por la calles, al ver esa escena cieras la persiana y , Que hace MC:"
,"112","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Tapas la puerta con lo que puedes pero al hacer ruido moviendo las cosa una gran cantidad de zombies vienen hacia ti, te quedas encerado hay hasta quedarte sin comida, y mueres con el tiempo debido a la desnutrición."
,"1121","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"al pensar que todo esto sigue siendo un sueño, decide acabar con tu vida, pensando que asi te despertaras, asi que vas a la ventana del comedor la mas grande que hay en tu casa y saltas, estrellándose conta el suelo acabando con tu vida."
,"1122","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"antes de salir buscas en tu casa algo para defenderte, coges un cuchillo de la cocina y sales de casa.pero nada mas salir te encuentras con alguien caminando de manera errática por los pasillo, al verte grita y corre hacia ti. Que hace MC:"
,"113","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"al intentar pelear consigues acertas un golpe mortal a la cabeza del zombie lo que hace caer al suelo. al mirar de cerca al zombie te das cuenta que es tu padre. impactado por lo sucedido te arrodillas para abrazar a tu padre ya muerto, el sonido de tus llantos atrae a los zombies, ya sabiendo lo que va a pasar te resignas a morir."
,"1131","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"huilles subiendo las escaleras hasta llegar a la azotea pero al intentar abrir la puerta esta cerrada por lo que el zombie que te perseguía al cual tras el ruido de la carrera ahora no solo es uno, te acorralan contra la puerta, devorándote, mientras intentas defenderte con tu cuchillo si hacer efecto alguno contra tantos de ellos."
,"1132","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"Te levantas de la cama para ir a ver que ha pasado, al salir de tu cuarto encuentras a tu madre y padre despierto llendo a mirar que pasa. Que hace MC:"
,"12","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
,"vas con ellos a mira que ha pasado al salir de casa algo ataca a tu madre , tu y tu padre vais a ayudarla, causando que os noquen a ti y a tu padre, decando a merced de lo que pase a los dos."
,"121","Naharro","Naharro");

insert into pasos(id_paso,id_aventura,paso,num_paso,usuariocreacion,usuariomodificacion) values (id_paso,(select id_aventura from aventura where nombre_aventura="Death is Death")
," decides no ir con ellos, cuando ellos salen los escuchas gritar, pensando que solo se estan peleando con tus vecinos no le tomas mucha importancia, pasado un rato todo queda en silencio, y después de eso escuchas la puerta, mientras que vas quedando dormido. mientras estas dormido alguien entra a tu habitación haciendo ruido inentendibles."
,"122","Naharro","Naharro");

################################


insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
" ignoras el ruido y intentas volver a domir.",11,"Naharro","Naharro",
(select id_paso from pasos where num_paso="11"));

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
" Te levantas de la cama para ir a ver que ha pasado.",12,"Naharro","Naharro",
(select id_paso from pasos where num_paso="12"));

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"Salir rapido de casa a buscarlos.",111,"Naharro","Naharro",
(select id_paso from pasos where num_paso="111"));

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"esperar en casa a que vuelvan a casa.",112,"Naharro","Naharro",
(select id_paso from pasos where num_paso="112"));

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"coger un algo para defenderte y salir a buscarlos.",113,"Naharro","Naharro",
(select id_paso from pasos where num_paso="113"));

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"pelear",1111,"Naharro","Naharro",
(select id_paso from pasos where num_paso="1111"));

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"huir",1112,"Naharro","Naharro",
(select id_paso from pasos where num_paso="1112"));

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"tapar la puerta de tu casa.",1121,"Naharro","Naharro",
(select id_paso from pasos where num_paso="1121"));

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"acabar con tu vida.",1122,"Naharro","Naharro",
(select id_paso from pasos where num_paso="1122"));

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"pelear",1131,"Naharro","Naharro",
(select id_paso from pasos where num_paso="1131"));

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"huir.",1132,"Naharro","Naharro",
(select id_paso from pasos where num_paso="1132"));

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"ir con ellos.",21,"Naharro","Naharro",
(select id_paso from pasos where num_paso="121"));

insert into respuesta(id_respuesta,id_aventura,respuesta,num_respuesta,usuariocreacion,usuariomodificacion,id_paso) values (id_respuesta,(select id_aventura from aventura where nombre_aventura="Death is Death"),
"no ir.",22,"Naharro","Naharro",
(select id_paso from pasos where num_paso="122"));



