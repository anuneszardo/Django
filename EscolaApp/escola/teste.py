from escola.models import Aluno, Curso, Matricula

def verifyAlunoIsMatriculado(Aluno, Matricula):
    if(matricula.aluno.id == aluno.id):
        return True;
    else:
        return False;


Aluno.id = 1
Matricula.id = 1
assert verifyAlunoIsMatriculado(Aluno, Matricula)
