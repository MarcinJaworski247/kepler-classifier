import json


class ClassificationResponseVM:
    def __init__(self, method, acc, balanced_acc, brier_score_loss, f1_score, feature_importance):
        self.method = str(method)
        self.accuracy = float(acc)
        self.balanced_accuracy = float(balanced_acc)
        self.brier_score_loss = float(brier_score_loss)
        self.f1_score = float(f1_score)
        self.feature_importance = feature_importance

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class FeatureImportanceVM:
    def __init__(self, name, value):
        self.name = name
        self.value = value
