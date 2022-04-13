import json

class ValuesVM:
    def __init__(self, name, data):
        self.name = name
        self.data = data
    
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)