/* Trigger que atualiza a Qtde_Matriculados de uma turma*/
/*Trigger já testada*/
CREATE OR REPLACE FUNCTION atualiza_vagas() RETURNS TRIGGER
AS	
$$
DECLARE 
   qtde_vagas INTEGER;
   qtde_m INTEGER;
BEGIN
    select vagas from turmas where ID_Turma = New.Turma into qtde_vagas;
    select Qtde_Matriculados from turmas where ID_Turma = New.turma into qtde_m;
    IF(qtde_m = qtde_vagas) THEN
        raise exception 'Número limite de Vagas atingido!!!!';
    Elsif(TG_OP = 'INSERT') then
        update Turmas set Qtde_Matriculados = Qtde_Matriculados + 1
        where ID_Turma = NEW.turma;
    Elsif(TG_OP = 'DELETE') THEN
        update Turmas set Qtde_Matriculados = Qtde_Matriculados - 1
        where ID_Turma = OLD.Turma;   
	end IF;
	return new;
END
$$LANGUAGE plpgsql;

CREATE TRIGGER t_atualiza_vagas
AFTER INSERT OR DELETE ON matriculas
FOR EACH ROW
EXECUTE PROCEDURE atualiza_vagas();


/*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/

/*Trigger que assegura que alunos só podem se cadastrar em uma turma por disciplina*/
/*TRIGGER JÁ TESTADA!!!!*/
CREATE OR REPLACE FUNCTION verifica_turma() RETURNS TRIGGER
AS	
$$
DECLARE 
    comp1 integer;
BEGIN
 select T.Disciplina from Turmas T, Matriculas M
 where T.ID_Turma = M.turma and M.matricula = New.Matricula
 intersect 
 select Disciplina from Turmas 
 where  ID_turma = New.Turma
 into comp1;
   if (comp1 > 0) THEN
       raise exception 'Aluno já cadastrado em uma turma dessa disciplina';
	end if;
	return new;
END
$$LANGUAGE plpgsql;

CREATE TRIGGER t_verifica_turma
BEFORE INSERT OR UPDATE ON matriculas
FOR EACH ROW
EXECUTE PROCEDURE verifica_turma();

/*++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/

/*Trigger que verificar se o tipo de um local é um bloco*/
/*JÁ TESTADA!!!!*/
CREATE OR REPLACE FUNCTION verifica_bloco() RETURNS TRIGGER
AS	
$$
DECLARE
verifica VARCHAR;
BEGIN
    if(New.tipo = 'Bloco' and New.Bloco  > 0) THEN
      raise exception'O Registro do bloco precisa ser nulo';
	end if;
	return new;
END
$$LANGUAGE plpgsql;

CREATE TRIGGER t_verifica_bloco
BEFORE INSERT OR UPDATE ON locais
FOR EACH ROW
EXECUTE PROCEDURE verifica_bloco();

/*++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/

/*Trigger que limita em 4 o número máximo de disciplinas que um professor pode lecionar*/
/*TRIGGER JÁ TESTADA!!!!*/
CREATE OR REPLACE FUNCTION verifica_disciplina() RETURNS TRIGGER
AS	
$$
DECLARE
qtde_disciplinas integer;
BEGIN
    select count(ID_Disciplina)
    from disciplinas
    where professor = New.Professor into qtde_disciplinas;   
    if(qtde_disciplinas = 4) THEN
       raise exception'ESSE PROFESSOR JÁ ATINGIU O NÚMERO MÁXIMO DE DISCIPLINAS A SEREM LECIONADAS!!!!';
    end if;
	return new;
END
$$LANGUAGE plpgsql;

CREATE TRIGGER t_verifica_disciplina
BEFORE INSERT OR UPDATE ON Disciplinas
FOR EACH ROW
EXECUTE PROCEDURE verifica_disciplina();

/*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/

/*Trigger que alocar um professor pra ser diretor de um centro pertencente ao ser curso*/
/*Trigger já testada*/
CREATE OR REPLACE FUNCTION verifica_diretor() RETURNS TRIGGER
AS	
$$
DECLARE
verifica integer;
novo_diretor integer;
criterio integer;
BEGIN
    select Centro from Cursos where ID_Curso = new.ID_Curso into criterio;
    select diretor from Centros CE, Cursos C
        where C.centro = CE.ID_Centro and C.ID_Curso = New.ID_curso into verifica;
    select PF.ID_Professor from Professores P, Cursos C, Prof_Cursos PF
        where PF.ID_Curso = C.ID_Curso and PF.ID_Professor = P.ID_Professor and C.ID_Curso = new.ID_Curso and C.Centro = criterio
    into novo_diretor;
    if(verifica is null) THEN
       update Centros set diretor = novo_diretor
       where ID_Centro = criterio;
    end if;
	return new;
END
$$LANGUAGE plpgsql;

CREATE TRIGGER t_verifica_diretor
AFTER INSERT ON Prof_Cursos
FOR EACH ROW
EXECUTE PROCEDURE verifica_diretor();

/*++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/

/*Trigger que verifica se coordenador já dirige um centro */
/*TRIGGER JÁ TESTADA!!!!*/
CREATE OR REPLACE FUNCTION verifica_coordenador() RETURNS TRIGGER
AS	
$$
DECLARE
verifica integer;
BEGIN
    select diretor from Centros where diretor = new.coordenador into verifica;
    if (verifica > 0) THEN
        raise exception 'Esse Professor já dirige um centro';
    end if;
	return new;
END
$$LANGUAGE plpgsql;

CREATE TRIGGER t_verifica_coordenador
BEFORE INSERT OR UPDATE ON Cursos
FOR EACH ROW
EXECUTE PROCEDURE verifica_coordenador();

/*++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/

/*Trigger que verifica se o aluno está matriculado em uma turma de uma disciplina
a fim de atribuir uma avaliação para ele*/
/*TRIGGER TESTADA!!!!*/
CREATE OR REPLACE FUNCTION verifica_avaliacao() RETURNS TRIGGER
AS	
$$
DECLARE
   verifica INTEGER;
BEGIN
    SELECT M.Matricula from Matriculas M, Turmas T
    where M.Turma = T.ID_Turma AND M.Matricula = New.Matricula And T.Disciplina = New.ID_Disciplina into verifica;
    if(verifica is null) THEN
        raise exception'Aluno não matrículado em uma turma dessa disciplina';
	end IF;
	return new;
END
$$LANGUAGE plpgsql;

CREATE TRIGGER t_verifica_avaliacao
BEFORE INSERT OR UPDATE ON Avaliacoes
FOR EACH ROW
EXECUTE PROCEDURE verifica_avaliacao();

/*+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*/

/*Trigger que verifica se o local da turma tem espaço suficiente para a 
Qtde de vagas da turma */
/*TRIGGER  JÁ TESTADA!!!!*/
CREATE OR REPLACE FUNCTION verifica_lotacao() RETURNS TRIGGER
AS	
$$
DECLARE 
   verifica INTEGER;
BEGIN
    SELECT lotacao from locais where ID_Local = new.Loca_l into verifica;
    IF(New.vagas > verifica) THEN
        raise exception 'ESSE LOCAL NÃO POSSUI ESPAÇO SUFICIENTE PARA A TURMA!!!!'; 
	end IF;
	return new;
END
$$LANGUAGE plpgsql;

CREATE TRIGGER t_verifica_lotacao
BEFORE INSERT OR UPDATE ON Turmas
FOR EACH ROW
EXECUTE PROCEDURE verifica_lotacao();
