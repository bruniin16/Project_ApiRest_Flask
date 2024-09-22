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

def listar_id(param_id):
    aluno = aluno_model.Aluno.query.filter_by(id=param_id).first()
    return aluno

def att_aluno(aluno_bd, aluno_att):
    aluno_bd.nome = aluno_att.nome
    aluno_bd.data_nasc = aluno_att.data_nasc

    db.session.commit() #update

def del_aluno(aluno):
    db.session.delete(aluno)
    db.session.commit()