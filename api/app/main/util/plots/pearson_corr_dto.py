from flask_restx import fields, Namespace


class PearsonCorrDTO:
    api = Namespace("plots")
    data_content = api.model("data_content", {"x": fields.String, "y": fields.Float})
    data = api.model(
        "pearson_corr",
        {"name": fields.String, "data": fields.List(fields.Nested(data_content))},
    )
