from flask_restx import fields, Namespace

class DataDTO:
    api = Namespace('data')
    data = api.model('data', {
        'kepid': fields.Integer(required=True, description='Identifier'),
        'kepoi_name': fields.String(required=True, description=''),
        'kepler_name': fields.String(required=True, description=''),
        'koi_disposition': fields.Integer(required=True, description=''),
        'koi_fpflag_nt': fields.Integer(required=True, description=''),
        'koi_fpflag_ss': fields.Integer(required=True, description=''),
        'koi_fpflag_co': fields.Integer(required=True, description=''),
        'koi_fpflag_ec': fields.Integer(required=True, description=''),
        'koi_period': fields.Float(required=True, description=''),
        'koi_time0bk': fields.Float(required=True, description=''),
        'koi_impact': fields.Float(required=True, description=''),
        'koi_duration': fields.Float(required=True, description=''),
        'koi_depth': fields.Float(required=True, description=''),
        'koi_prad': fields.Float(required=True, description=''),
        'koi_teq': fields.Integer(required=True, description=''),
        'koi_insol': fields.Float(required=True, description=''),
        'koi_model_snr': fields.Float(required=True, description=''),
        'koi_steff': fields.Integer(required=True, description=''),
        'koi_slogg': fields.Float(required=True, description=''),
        'koi_srad': fields.Float(required=True, description=''),
        'ra': fields.Float(required=True, description=''),
        'dec': fields.Float(required=True, description=''),
        'koi_kepmag': fields.Float(required=True, description='')
    })

    outliers = api.model('outliers', {
        'count': fields.Integer(required=True),
        'percentage': fields.Float(required=True)
    })