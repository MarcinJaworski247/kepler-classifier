from flask_restx import fields, Namespace


class ClassificationResponseDTO:
    api = Namespace("classification")
    feature_importance = api.model(
        "feature_importance", {"name": fields.String, "value": fields.Float})
    data = api.model(
        "data",
        {
            "method": fields.String,
            "accuracy": fields.Float,
            "balanced_accuracy": fields.Float,
            "f1_score": fields.Float,
            "brier_score_loss": fields.Float,
            "feature_importance": fields.List(fields.Nested(feature_importance))
        },
    )

    classification_result = api.model(
        "classification_result",
        {
            "kepler_name": fields.String,
            "kepoi_name": fields.String,
            "koi_fpflag_nt": fields.Integer,
            "koi_fpflag_ss": fields.Integer,
            "koi_fpflag_co": fields.Integer,
            "koi_fpflag_ec": fields.Integer,
            "koi_period": fields.Float,
            "koi_time0bk": fields.Float,
            "koi_impact": fields.Float,
            "koi_duration": fields.Float,
            "koi_depth": fields.Float,
            "koi_prad": fields.Float,
            "koi_teq": fields.Integer,
            "koi_insol": fields.Float,
            "koi_model_snr": fields.Float,
            "koi_steff": fields.Integer,
            "koi_slogg": fields.Float,
            "koi_srad": fields.Float,
            "ra": fields.Float,
            "dec": fields.Float,
            "koi_kepmag": fields.Float,
            "RESULT": fields.Integer
        }
    )
