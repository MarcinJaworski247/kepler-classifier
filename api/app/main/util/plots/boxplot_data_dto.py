from flask_restx import fields, Namespace

class BoxPlotDataDTO:
    api = Namespace('plots')
    data = api.model('box_plot', {
        'name': fields.String,
        'data': fields.List(fields.Float)
    })