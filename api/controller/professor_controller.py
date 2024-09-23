from flask import request, make_response, jsonify
from flask_restful import Resource
from api import api
from ..schemas import professor_schema
from ..dto import professor_dto
from ..service import professor_service

class ProfessorController(Resource):
    
    def get(self):
        professores = professor_service.listar_professores()
        validate = professor_schema.ProfessorSchema(many=True)
        return make_response(validate.jsonify(professores), 200)
    
    def post(self):
        professorSchema = professor_schema.ProfessorSchema()
        validate = professorSchema.validate(request.json)

        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            data_nasc = request.json["data_nasc"]
            novoProfessor = professor_dto.ProfessorDTO(nome=nome, data_nasc=data_nasc)
            retorno = professor_service.cadastrar_professor(novoProfessor)
            professor_json = professorSchema.jsonify(retorno)

            return make_response(professor_json, 201)
    
    def put(self, id):
        professor = professor_service.listar_id(id)
        if professor is None:
            return make_response(jsonify("Professor não encontrado"), 404)
        else:
            professorSchema = professor_schema.ProfessorSchema()
            validate = professorSchema.validate(request.json)

            if validate:
                make_response(jsonify(validate), 400)
            else:
                nome = request.json["nome"]
                data_nasc = request.json["data_nasc"]
                professor_att = professor_dto.ProfessorDTO(nome, data_nasc)
                professor_service.att_professor(professor, professor_att)
                professor_atualizado = professor_service.listar_id(id)

                return make_response(professorSchema.jsonify(professor_atualizado), 200)

    def delete(self, id):
        professor = professor_service.listar_id(id)
        if professor is None:
            return make_response(jsonify("Professor não encontrado"), 404)
        else:
            professor_service.del_professor(professor)
            return make_response(jsonify("Professor excluído com sucesso."), 204)


class ProfessorDetailController(Resource):
    
    def get(self, id):
        professor = professor_service.listar_id(id)
        if professor is None:
            return make_response(jsonify("Professor não encontrado."), 404)
        else:
            validate = professor_schema.ProfessorSchema()
            return make_response(validate.jsonify(professor), 200)



api.add_resource(ProfessorController,"/professor")
api.add_resource(ProfessorController,"/professor/<int:id>", endpoint="alterar e excluir", methods=["PUT", "DELETE"])
api.add_resource(ProfessorDetailController,"/professor/<int:id>")