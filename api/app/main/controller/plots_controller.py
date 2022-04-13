from flask_restx import Resource

from app.main.service.plots_service import get_pearson_corr
from app.main.util.plots.pearson_corr_dto import PearsonCorrDTO

api = PearsonCorrDTO.api
_data = PearsonCorrDTO.data

@api.route('/getPearsonCorr')
class PearsonCorrList(Resource):
    @api.doc('list_of_pearson_correlations')
    @api.marshal_list_with(_data, envelope='data')
    def get(self):
        """List of pearson correlation between attributes"""
        return get_pearson_corr()