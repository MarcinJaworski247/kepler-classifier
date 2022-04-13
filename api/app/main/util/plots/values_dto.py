from flask_restx import fields, Namespace


class ValuesDTO:
    api = Namespace("plots")
    data = api.model(
        "values", {"name": fields.String, "data": fields.List(fields.Float)}
    )
