from flask_restx import fields, Namespace


class StatsDTO:
    api = Namespace("stats")
    data = api.model(
        "data",
        {
            "_attribute": fields.String,
            "_min": fields.Float,
            "_max": fields.Float,
            "_avg": fields.Float,
            "_stdv": fields.Float,
            "_median": fields.Float,
            "_iqr": fields.Float,
            "_q1": fields.Float,
            "_q3": fields.Float,
        },
    )
