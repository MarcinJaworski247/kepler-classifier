from flask_restx import Resource

from ..util.data_dto import DataDTO
from ..service.data_service import get_prepared_data

api = DataDTO.api
_data = DataDTO.data

@api.route('/getPreparedData')
class DataList(Resource):
    @api.doc('list_of_prepared_data')
    @api.marshal_list_with(_data, envelope='data')
    def get(self):
        """List of preparedd data"""
        return get_prepared_data()