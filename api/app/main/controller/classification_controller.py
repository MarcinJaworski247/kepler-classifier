from flask import request
from flask_restx import Resource
from app.main.service.classification_service import get_classification_results

from app.main.util.classification_params_dto import ClassificationParamsDTO
from app.main.util.classification_params_vm import ClassificationParamsVM
from app.main.util.classification_response_dto import ClassificationResponseDTO

api = ClassificationParamsDTO.api
_response = ClassificationResponseDTO.data


@api.route("/getClassificationResult")
class DataList(Resource):
    @api.doc("results_of_classification_process")
    @api.marshal_list_with(_response)
    def get(self):
        """Results of classification process"""

        isCrossValidation = request.args.get("isCrossValidation", "")
        testDataPercentage = request.args.get("testDataPercentage", "")
        treesCount = request.args.get("treesCount", "")
        neighboursCount = request.args.get("neighboursCount", "")
        foldsCount = request.args.get("foldsCount", "")

        params = ClassificationParamsVM(
            isCrossValidation, testDataPercentage, treesCount, neighboursCount, foldsCount)

        return get_classification_results(params)
