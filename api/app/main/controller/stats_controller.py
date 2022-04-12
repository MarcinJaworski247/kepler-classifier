from flask_restx import Resource

from ..util.stats_dto import StatsDTO
from ..service.stats_service import get_description_stats

api = StatsDTO.api
_data = StatsDTO.data

@api.route('/getDescriptionStats')
class StatsList(Resource):
    @api.doc('list_of_description_stats')
    @api.marshal_list_with(_data, envelope='stats')
    def get(self):
        """List of description stats"""
        return get_description_stats()
