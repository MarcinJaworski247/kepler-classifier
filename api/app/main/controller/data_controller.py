from flask_restx import Resource

from ..util.data_dto import DataDTO
from ..service.data_service import detect_outliers, get_class_info, get_prepared_data

api = DataDTO.api
_data = DataDTO.data
_outliers = DataDTO.outliers
_class_info = DataDTO.class_info


@api.route("/getPreparedData")
class DataList(Resource):
    @api.doc("list_of_prepared_data")
    @api.marshal_list_with(_data)
    def get(self):
        """List of preparedd data"""
        return get_prepared_data()


@api.route("/getOutliers")
class Outliers(Resource):
    @api.doc("count_and_percentage_of_outliers")
    @api.marshal_with(_outliers)
    def get(self):
        """Count and percentage of outliers"""
        return detect_outliers()


@api.route("/getClassInfo")
class ClassInfo(Resource):
    @api.marshal_with(_class_info)
    def get(self):
        """Count of values 'candidate' and 'false positive' in class variable"""
        return get_class_info()
