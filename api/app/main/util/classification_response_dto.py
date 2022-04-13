from flask_restx import fields, Namespace


class ClassificationResponseDTO:
    api = Namespace("classification")
    data = api.model(
        "classification_reponse",
        {
            "method": fields.String,
            "accuracy": fields.Float,
            "balanced_accuracy": fields.Float,
        },
    )
