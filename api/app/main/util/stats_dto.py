from flask_restx import fields, Namespace

class StatsDTO:
    api = Namespace('stats')
    data = api.model('data', {
        '_attribute': fields.String(required=True),
        '_min': fields.Float(required=True),
        '_max': fields.Float(required=True),
        '_avg': fields.Float(required=True),
        '_stdv': fields.Float(required=True),
        '_median': fields.Float(required=True),
        '_iqr': fields.Float(required=True),
        '_q1': fields.Float(required=True),
        '_q3': fields.Float(required=True)
    })