from ..models import professor_model
from api import db


def cadastrar_professor(professor):
    professor_bd = professor_model.Professor(nome=professor.nome, data_nasc=professor.data_nasc)
    db.session.add(professor_bd)
    db.session.commit()
    
    return professor_bd

def listar_professores():
    professores = professor_model.Professor.query.all()
    return professores

def listar_id(param_id):
    professor = professor_model.Professor.query.filter_by(id=param_id).first()
    return professor

def att_professor(professor_bd, professor_att):
    professor_bd.nome = professor_att.nome
    professor_bd.data_nasc = professor_att.data_nasc

    db.session.commit()

def del_professor(professor):
    db.session.delete(professor)
    db.session.commit()