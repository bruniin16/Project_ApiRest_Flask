from flask import request, make_response, jsonify
from flask_restful import Resource
from api import api
from ..schemas import aluno_schema
from ..dto import aluno_dto
from ..service import aluno_service

class AlunoController(Resource):
    
    def get(self):
        alunos = aluno_service.listar_alunos()
        validate = aluno_schema.AlunoSchema(many=True)
        return make_response(validate.jsonify(alunos), 200)
    
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
    
    def put(self, id):
        aluno = aluno_service.listar_id(id)
        if aluno is None:
            return make_response(jsonify("Aluno não encontrado"), 404)
        else:
            alunoSchema = aluno_schema.AlunoSchema()
            validate = alunoSchema.validate(request.json)

            if validate:
                make_response(jsonify(validate), 400)
            else:
                nome = request.json["nome"]
                data_nasc = request.json["data_nasc"]
                aluno_att = aluno_dto.AlunoDTO(nome, data_nasc)
                aluno_service.att_aluno(aluno, aluno_att)
                aluno_atualizado = aluno_service.listar_id(id)

                return make_response(alunoSchema.jsonify(aluno_atualizado), 200)

    def delete(self, id):
        aluno = aluno_service.listar_id(id)
        if aluno is None:
            return make_response(jsonify("Aluno não encontrado"), 404)
        else:
            aluno_service.del_aluno(aluno)
            return make_response(jsonify("Aluno excluído com sucesso."), 204)


class AlunoDetailController(Resource):
    
    def get(self, id):
        aluno = aluno_service.listar_id(id)
        if aluno is None:
            return make_response(jsonify("Aluno não encontrado."), 404)
        else:
            validate = aluno_schema.AlunoSchema()
            return make_response(validate.jsonify(aluno), 200)



api.add_resource(AlunoController,"/aluno")
api.add_resource(AlunoController,"/aluno/<int:id>", endpoint="alterar_excluir", methods=["PUT", "DELETE"])
api.add_resource(AlunoDetailController,"/aluno/<int:id>")