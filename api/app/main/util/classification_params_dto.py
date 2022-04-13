from flask_restx import fields, Namespace


class ClassificationParamsDTO:
    api = Namespace("classification")
    params = api.model(
        "params",
        {
            "isCrossValidation": fields.Boolean,
            "testDataPercentage": fields.Float,
            "numberOfTrees": fields.Integer,
        },
    )
