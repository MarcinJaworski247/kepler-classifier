from flask_restx import fields, Namespace

class DataDTO:
    api = Namespace('data')
    data = api.model('data', {
        'kepid': fields.Integer,
        'kepoi_name': fields.String,
        'kepler_name': fields.String,
        'koi_disposition': fields.Integer,
        'koi_fpflag_nt': fields.Integer,
        'koi_fpflag_ss': fields.Integer,
        'koi_fpflag_co': fields.Integer,
        'koi_fpflag_ec': fields.Integer,
        'koi_period': fields.Float,
        'koi_time0bk': fields.Float,
        'koi_impact': fields.Float,
        'koi_duration': fields.Float,
        'koi_depth': fields.Float,
        'koi_prad': fields.Float,
        'koi_teq': fields.Integer,
        'koi_insol': fields.Float,
        'koi_model_snr': fields.Float,
        'koi_steff': fields.Integer,
        'koi_slogg': fields.Float,
        'koi_srad': fields.Float,
        'ra': fields.Float,
        'dec': fields.Float,
        'koi_kepmag': fields.Float
    })

    outliers = api.model('outliers', {
        'count': fields.Integer,
        'percentage': fields.Float
    })