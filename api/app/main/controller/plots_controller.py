from flask import request, jsonify
from flask_restx import Resource
from flask_restx import Namespace
from app.main.service.plots_service import get_pearson_corr, get_simple_linear_regression, get_values
from app.main.util.plots.pearson_corr_dto import PearsonCorrDTO
from app.main.util.plots.values_dto import ValuesDTO

api = Namespace("plots")
_data = PearsonCorrDTO.data
_values_data = ValuesDTO.data


@api.route("/getPearsonCorr")
class PearsonCorrList(Resource):
    @api.doc("list_of_pearson_correlations")
    @api.marshal_list_with(_data)
    def get(self):
        """List of pearson correlation between attributes"""
        return get_pearson_corr()


@api.route("/getValues")
class BoxPlotData(Resource):
    @api.doc("list_of_attributes_with_values")
    @api.marshal_list_with(_values_data)
    def get(self):
        """List of atributes data to box plots"""

        attribute = request.args.get("attribute", "")

        return get_values(attribute)


@api.route("/getSimpleLinearRegression")
class SimpleLinearRegression(Resource):
    @api.doc("simple_linear_regression_of_two_attributes")
    def get(self):
        """Simple linear regression between two attributes"""

        firstAttribute = request.args.get("firstAttribute", "")
        secondAttribute = request.args.get("secondAttribute", "")

        res = get_simple_linear_regression(firstAttribute, secondAttribute)
        return res
