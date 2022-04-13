import json


class ClassificationResponseVM:
    def __init__(self, method, acc, balanced_acc):
        self.method = str(method)
        self.accuracy = float(acc)
        self.balanced_accuracy = float(balanced_acc)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
