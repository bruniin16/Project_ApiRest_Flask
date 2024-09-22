from ..models import aluno_model
from api import db


def cadastrar_aluno(aluno):
    aluno_bd = aluno_model.Aluno(nome=aluno.nome, data_nasc=aluno.data_nasc)
    db.session.add(aluno_bd)  #insert into aluno(nome, data_nasc)
    db.session.commit()
    
    return aluno_bd