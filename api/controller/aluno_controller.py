from flask import request, make_response, jsonify
from flask_restful import Resource
from api import api
from ..schemas import aluno_schema
from ..dto import aluno_dto
from ..service import aluno_service

class AlunoController(Resource):
    def get(self):
        return "Teste aluno"
    
    def post(self):
        alunoSchema = aluno_schema.AlunoSchema()
        validate = alunoSchema.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            data_nasc = request.json["data_nasc"]
            novoAluno = aluno_dto.AlunoDTO(nome=nome, data_nasc=data_nasc)
            retorno = aluno_service.cadastrar_aluno(novoAluno)
            aluno_json = alunoSchema.jsonify(retorno)

            return make_response(aluno_json, 201)
    
api.add_resource(AlunoController,"/aluno")