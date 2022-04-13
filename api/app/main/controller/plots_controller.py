from flask_restx import Resource
from flask_restx import Namespace
from app.main.service.plots_service import get_boxplot_data, get_pearson_corr
from app.main.util.plots.boxplot_data_dto import BoxPlotDataDTO
from app.main.util.plots.pearson_corr_dto import PearsonCorrDTO

api = Namespace('plots')
_data = PearsonCorrDTO.data
_boxplot_data = BoxPlotDataDTO.data

@api.route('/getPearsonCorr')
class PearsonCorrList(Resource):
    @api.doc('list_of_pearson_correlations')
    @api.marshal_list_with(_data, envelope='data')
    def get(self):
        """List of pearson correlation between attributes"""
        return get_pearson_corr()

@api.route('/getBoxPlotData')
class BoxPlotData(Resource):
    @api.doc('list_of_data_to_box_plots')
    @api.marshal_list_with(_boxplot_data, envelope='boxplot_data')
    def get(self):
        """List of atributes data to box plots"""
        return get_boxplot_data()