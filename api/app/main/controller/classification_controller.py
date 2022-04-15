from flask import request
from flask_restx import Resource
from app.main.service.classification_service import get_classification_results

from app.main.util.classification_params_dto import ClassificationParamsDTO
from app.main.util.classification_response_dto import ClassificationResponseDTO

api = ClassificationParamsDTO.api
_params = ClassificationParamsDTO.params
_response = ClassificationResponseDTO.data


@api.route("/getClassificationResult")
class DataList(Resource):
    @api.doc("results_of_classification_process")
    @api.marshal_list_with(_response, envelope="data")
    @api.expect(_params)
    def get(self):
        """Results of classification process"""
        params = request.json
        return get_classification_results(params)
