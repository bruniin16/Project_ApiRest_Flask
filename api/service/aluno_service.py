from ..models import aluno_model
from api import db


def cadastrar_aluno(aluno):
    aluno_bd = aluno_model.Aluno(nome=aluno.nome, data_nasc=aluno.data_nasc)
    db.session.add(aluno_bd)  #insert into aluno(nome, data_nasc)
    db.session.commit()
    
    return aluno_bd

def listar_alunos():
    alunos = aluno_model.Aluno.query.all() #select * from aluno
    return alunos

def listar_id(parm_id):
    aluno = aluno_model.Aluno.query.filter_by(id=parm_id).first()
    return aluno