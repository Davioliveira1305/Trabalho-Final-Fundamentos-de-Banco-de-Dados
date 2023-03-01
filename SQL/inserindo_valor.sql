/*Inserção de tuplas em professores*/
insert into professores(ID_Professor, Nome, Email, Formacao,Sexo,data_de_nascimento) 
values(534,'Ricardo','Ricardo@UFC','Doutorado','Masculino','1991-06-23');
insert into professores(ID_Professor, Nome, Email, Formacao,Sexo,data_de_nascimento) 
values(568,'Monalisa','Monalisa@UFC','Doutorado','Feminini','1982-03-07');
insert into professores(ID_Professor, Nome, Email, Formacao,Sexo,data_de_nascimento) 
values(890,'Jobson','Jobson@UFC','Mestrado','Masculino','1995-11-03');
insert into professores(ID_Professor, Nome, Email, Formacao,Sexo,data_de_nascimento) 
values(333,'Marielly','Marielly@UFC','Mestrado','Feminino','1997-01-01');


/*Inserção de tuplas em reitores*/
insert into reitores(ID_Reitor,data_de_admissao) values(534,'05-12-2016');


/*Inserção de tuplas em Campus*/
insert into campus(ID_Campus,Nome,Reitor,Local_Campus) values(4578,'Campus do Pici',534,'Fortaleza');


/*Inserção de tuplas em Centros*/
insert into centros(ID_Centro,Nome,Diretor,Campus) values(6789,'Centro de Ciências',Null,4578);
insert into centros(ID_Centro,Nome,Diretor,Campus) values(7000,'Centro de Humanas',Null,4578);

/*Curso*/
insert into cursos(ID_Curso,Nome,Centro,Coordenador,Carga_horaria)
values(5609,'Ciência de Dados',6789,890,3002);
insert into cursos(ID_Curso,Nome,Centro,Coordenador,Carga_horaria)
values(5765,'Física',6789,568,3072);
insert into cursos(ID_Curso,Nome,Centro,Coordenador,Carga_horaria)
values(2111,'Letras',7000,534,3072);
select * from cursos c ;

/*Prof cusos*/
insert into Prof_Cursos(ID_Professor,ID_Curso) values(890,5609);
insert into Prof_Cursos(ID_Professor,ID_Curso) values(568,5609);


/*Inserção de tuplas em Alunos*/
insert into alunos(Matricula,Curso,Nome,Sobrenome,Email,Data_de_Nascimento,Número,Rua,Bairro,Cidade,Estado,Sexo)
values(493463,5609,'Davi','Oliveira','davipo1305@UFC','2001-05-13',222,'Pedro Ortega','Pici','Fortaleza','Ceará','Masculino');
insert into alunos(Matricula,Curso,Nome,Sobrenome,Email,Data_de_Nascimento,Número,Rua,Bairro,Cidade,Estado,Sexo)
values(50000,5609,'Joba','Assada','Joba@UFC','2003-04-13',456,'Mister Hull','Kennedy','Fortaleza','Ceará','Masculino');
insert into alunos(Matricula,Curso,Nome,Sobrenome,Email,Data_de_Nascimento,Número,Rua,Bairro,Cidade,Estado,Sexo)
values(70000,5609,'jefim','Barbosa','jefim@UFC','2002-05-13',346,'Rua das Flores','Lagamar','Fortaleza','Ceará','Masculino');



/*Inserção de tuplas em disciplinas*/
insert into disciplinas(ID_Disciplina,Nome,Professor,Ementa,Carga_Horaria) values (56,'Cálculo 1',568 ,'fhgfggh',96);
insert into disciplinas(ID_Disciplina,Nome,Professor,Ementa,Carga_Horaria) values (57,'Cálculo 3',568,'fhgfggh',96);
insert into disciplinas(ID_Disciplina,Nome,Professor,Ementa,Carga_Horaria) values (58,'Cálculo 4',568,'fhgfggh',96);
insert into disciplinas(ID_Disciplina,Nome,Professor,Ementa,Carga_Horaria) values (59,'Geometria Espacial',568,'fhgfggh',96);
insert into disciplinas(ID_Disciplina,Nome,Professor,Ementa,Carga_Horaria) values (12,'Cálculo 8',534,'fhgfggh',96);


/*LOCAIS*/
insert into locais(ID_Local,Tipo,Bloco,Lotacao,Nome,Descricao) values(45,'Bloco',4557,67,'gyg','hjggcgcfgxfgcf');
insert into locais(ID_Local,Tipo,Bloco,Lotacao,Nome,Descricao) values(34,'Sala de Aula',4557,40,'Sala-915','hjggcgcfgxfgcf');


/*turmas*/
insert into Turmas(ID_Turma,Semestre,Ano,Disciplina,Estado,Loca_l,Vagas,Qtde_Matriculados) 
values(123,1,2022,12,'CONCLUÍDA',34,40,0);
insert into Turmas(ID_Turma,Semestre,Ano,Disciplina,Estado,Loca_l,Vagas,Qtde_Matriculados) 
values(456,2,2022,12,'ABERTA',34,39,0);

/*Dias*/
insert into Dia_Semana(ID_Turma,Dia_Semana) values(123,'Segunda');
insert into Dia_Semana(ID_Turma,Dia_Semana) values(123,'Terça');
insert into Dia_Semana(ID_Turma,Dia_Semana) values(123,'Quarta');


/*matriculas*/
insert into matriculas(Matricula,Turma) values (493463,123);
Insert into matriculas(Matricula,Turma) values (493463,456);
insert into matriculas(Matricula,Turma) values (50000,123);
insert into matriculas(Matricula,Turma) values (50000,456);


/*
insert into Avaliacoes(Matricula,Tipo,ID_Disciplina,Nota) values (493463,'AP1',12,10);
insert into Avaliacoes(Matricula,Tipo,ID_Disciplina,Nota) values (50000,'AP1',12,10);
*/