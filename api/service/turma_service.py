from ..models import turma_model
from api import db

def cadastrar_turma(turma):
    turma_bd = turma_model.TurmaModel(nome=turma.nome, desc=turma.desc, data_inic=turma.data_inic, data_fim=turma.data_fim)
    db.session.add(turma_bd)
    db.session.commit()
    
    return turma_bd

def listar_turmas():
    turmas = turma_model.TurmaModel.query.all()

    return turmas

def listar_id(param_id):
    turma = turma_model.TurmaModel.query.filter_by(id=param_id).first()
    return turma

def att_turma(turma_bd, turma_att):
    turma_bd.nome = turma_att.nome
    turma_bd.desc = turma_att.desc
    turma_bd.data_inic = turma_att.data_inic
    turma_bd.data_fim = turma_att.data_fim

    db.session.commit()

def del_turma(turma):
    db.session.delete(turma)
    db.session.commit()