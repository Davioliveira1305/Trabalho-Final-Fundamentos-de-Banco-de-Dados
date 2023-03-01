/* Professor*/
CREATE TABLE Professores(
    ID_Professor    INTEGER,
    Nome            VARCHAR(30) NOT NULL,
    Email           VARCHAR(20) NOT NULL,
    Formacao        VARCHAR(20) NOT NULL,
    Sexo            VARCHAR(10) NOT NULL,
    data_de_nascimento DATE NOT NULL,
    PRIMARY KEY(ID_Professor)
);

drop table Professores;



/*REITORES*/
CREATE TABLE Reitores(
    ID_Reitor           INTEGER,
    data_de_admissao    DATE NOT NULL,
    PRIMARY KEY(ID_Reitor),
    Foreign Key (ID_Reitor) REFERENCES Professores(ID_Professor)
    ON DELETE CASCADE
);
drop TABLE Reitores;


/*Campus*/
CREATE TABLE Campus(
    ID_Campus       INTEGER,
    Nome            VARCHAR(30) NOT NULL,
    Reitor          INTEGER  NOT NULL,
    Local_Campus    VARCHAR(10) NOT NULL,
    Primary KEY(ID_Campus),
    FOREIGN KEY (Reitor) REFERENCES Reitores ON DELETE CASCADE
);
Drop table Campus;




CREATE TABLE Centros(
    ID_Centro   INTEGER,
    Nome        VARCHAR(30),
    Diretor     INTEGER UNIQUE,
    Campus      INTEGER NOT NULL,
    PRIMARY KEY(ID_Centro),
    Foreign Key (Diretor) REFERENCES Professores ON DELETE CASCADE,
    FOREIGN KEY (Campus) REFERENCES Campus ON DELETE CASCADE
);
DROP TABLE Centros;



/*Cursos*/
CREATE TABLE Cursos(
    ID_Curso    INTEGER,
    Nome        VARCHAR(30),
    Centro      INTEGER NOT NULL,
    Coordenador INTEGER NOT NULL UNIQUE,
    Carga_horaria INTEGER,
    PRIMARY KEY(ID_Curso),
    FOREIGN KEY (Coordenador) REFERENCES Professores ON DELETE CASCADE,
    FOREIGN KEY (Centro) REFERENCES Centros ON DELETE CASCADE
);

drop table Cursos;





CREATE TABLE Prof_Cursos(
    ID_Professor INTEGER,
    ID_Curso     INTEGER,
    Primary Key(ID_Professor,ID_Curso),   
    Foreign Key (ID_Professor) REFERENCES Professores ON DELETE CASCADE,
    Foreign Key (ID_Curso) REFERENCES Cursos ON DELETE CASCADE
);

Drop table Prof_Cursos;

select * from Centros;

/*AlUNOS*/
CREATE Table Alunos(
    Matricula   INTEGER,
    Curso       INTEGER NOT NULL,
    Nome        VARCHAR(10) NOT NULL,
    Sobrenome   VARCHAR(25) NOT NULL,
    Email       VARCHAR(30) NOT NULL,
    Data_de_Nascimento DATE NOT NULL,
    Número      INTEGER NOT NULL,
    Rua         VARCHAR(30) NOT NULL,
    Bairro      VARCHAR(30) NOT NULL,
    Cidade      VARCHAR(20) NOT NULL,
    Estado      VARCHAR(20) NOT NULL,
    Sexo        VARCHAR(10) NOT NULL,
    PRIMARY KEY(Matricula),
    FOREIGN KEY (Curso) REFERENCES Cursos
);

drop table Alunos;




/*DISCIPLINAS*/
CREATE TABLE Disciplinas(
    ID_Disciplina   INTEGER ,
    Nome            CHAR(30) NOT NULL  ,
    Professor       INTEGER NOT NULL   ,
    Ementa          char(800) NOT NULL ,
    Carga_Horaria   INTEGER NOT NULL,
    PRIMARY KEY(ID_Disciplina),
    Foreign Key (Professor) REFERENCES Professores,
    constraint Carga_Horaria check (Carga_Horaria >= 32 and Carga_Horaria <=128)
); 

drop table Disciplinas;



/*Blocos*/
CREATE TABLE Blocos(
    ID_Bloco    INTEGER,
    Centro      INTEGER NOT NULL,
    PRIMARY KEY(ID_Bloco),
    FOREIGN KEY (Centro) REFERENCES Centros ON DELETE CASCADE
);

drop TABLE Blocos;

insert into blocos(ID_Bloco,Centro) values(4557,6789);

/*Locais*/
Create table Locais(
    ID_Local INTEGER,
    Tipo        VARCHAR(20) CHECK(Tipo = 'Bloco' or Tipo = 'Auditório' or Tipo = 'Sala de Aula' 
    or Tipo = 'Laboratório') NOT NULL,
    Bloco       INTEGER,
    Lotacao     integer NOT NULL,
    Nome        VARCHAR(30) NOT NULL,
    Descricao   VARCHAR(500) NOT NULL,
    PRIMARY KEY(ID_Local),
    FOREIGN KEY (Bloco) REFERENCES Blocos
    ON DELETE CASCADE
);

drop TABLE Locais;



/*TURMAS*/
CREATE TABLE Turmas(
    Id_turma        INTEGER,
    Ano             INTEGER NOT NULL,
    Semestre        INTEGER check(semestre >= 1 and semestre <=2 )NOT NULL,
    Disciplina      INTEGER NOT NULL,
    Estado          VARCHAR(20) Check(Estado = 'CONCLUÍDA' or Estado = 'ABERTA') NOT NULL,
    Loca_l          INTEGER NOT NULL,
    Horario_Inicio  TIME NOT NULL,
    Horario_Fim     TIME NOT NULL,
    Vagas           INTEGER NOT NULL,
    Qtde_Matriculados INTEGER NOT NULL,
    PRIMARY KEY(Id_turma),
    Foreign Key (Loca_l) REFERENCES Locais ON DELETE CASCADE,
    Foreign Key (Disciplina) REFERENCES Disciplinas
    ON DELETE CASCADE
);



/*Dias da semana*/
CREATE TABLE Dia_Semana(
    ID_Turma    INTEGER,
    Dia_Semana  VARCHAR(15),
    PRIMARY KEY(ID_Turma,Dia_Semana),
    Foreign Key (ID_Turma) REFERENCES Turmas ON DELETE CASCADE
);
drop TABLE Dia_Semana;


 
/*Relacionamento entre alunos e turmas, ou seja, Matrículas*/
CREATE Table Matriculas(
    Matricula INTEGER ,
    Turma     INTEGER ,
    PRIMARY KEY(Matricula,Turma),
    FOREIGN KEY(Matricula) REFERENCES Alunos ON DELETE CASCADE,
    FOREIGN KEY (Turma) REFERENCES Turmas ON DELETE CASCADE
);
drop TABLE Matriculas;



select * from turmas;

/*Relacionamento entre Alunos e disciplinas*/
CREATE table Avaliacoes(
    Matricula     INTEGER       ,
    Tipo          VARCHAR(20)   ,
    ID_Disciplina INTEGER       ,
    Nota          INTEGER check (Nota >= 0 and Nota <=10) NOT NULL,
    PRIMARY KEY(Matricula,ID_Disciplina,Tipo),
    Foreign Key (Matricula) REFERENCES Alunos,
    Foreign Key (ID_Disciplina) REFERENCES Disciplinas
);

drop TABLE Avaliacoes;
