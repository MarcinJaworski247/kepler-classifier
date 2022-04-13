import json


class StatsVM:
    def __init__(self, _attribute, _min, _max, _avg, _stdv, _median, _iqr, _q1, _q3):
        self._attribute = _attribute
        self._min = _min
        self._max = _max
        self._avg = _avg
        self._stdv = _stdv
        self._median = _median
        self._iqr = _iqr
        self._q1 = _q1
        self._q3 = _q3

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
