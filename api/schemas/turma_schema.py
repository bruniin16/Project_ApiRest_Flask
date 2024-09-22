from api import ma
from ..models import turma_model
from marshmallow import fields

class TurmaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = turma_model.TurmaModel
        load_instance = True
        fields = ("id", "nome", "desc", "data_inic", "data_fim")

    nome = fields.String(required=True)
    desc = fields.String(required=True)
    data_inic = fields.Date(required=True)
    data_fim = fields.Date(required=True)