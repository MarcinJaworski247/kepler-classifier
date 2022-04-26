import json


class ClassificationResponseVM:
    def __init__(self, method, acc, balanced_acc, brier_score_loss, f1_score):
        self.method = str(method)
        self.accuracy = float(acc)
        self.balanced_accuracy = float(balanced_acc)
        self.brier_score_loss = float(brier_score_loss)
        self.f1_score = float(f1_score)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
