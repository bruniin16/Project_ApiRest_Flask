from flask_restful import Resource
from api import api


class AlunoController(Resource):
    def get(self):
        return "Teste aluno"
    
api.add_resource(AlunoController,"/aluno")