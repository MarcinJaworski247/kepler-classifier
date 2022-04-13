from flask_restx import Resource
from flask_restx import Namespace
from app.main.service.plots_service import get_pearson_corr, get_values
from app.main.util.plots.pearson_corr_dto import PearsonCorrDTO
from app.main.util.plots.values_dto import ValuesDTO

api = Namespace("plots")
_data = PearsonCorrDTO.data
_values_data = ValuesDTO.data


@api.route("/getPearsonCorr")
class PearsonCorrList(Resource):
    @api.doc("list_of_pearson_correlations")
    @api.marshal_list_with(_data, envelope="pearson_corr")
    def get(self):
        """List of pearson correlation between attributes"""
        return get_pearson_corr()


@api.route("/getValues")
class BoxPlotData(Resource):
    @api.doc("list_of_attributes_with_values")
    @api.marshal_list_with(_values_data, envelope="values")
    def get(self):
        """List of atributes data to box plots"""
        return get_values()
