import pandas as pd
import numpy as np

from app.main.service.data_service import get_data_frame
from app.main.util.stats_vm import StatsVM

def get_description_stats():
    df = get_data_frame()
    result = []
    for col in df.columns:
        result.append(StatsVM(
            _attribute = col,
            _min = round(float(df[col].min()), 2),
            _max = round(float(df[col].max()), 2),
            _avg = round(float(df[col].mean()), 2),
            _stdv = round(float(df[col].std()), 2),
            _median = round(float(df[col].median())  , 2),
            _q1 = round(float(np.quantile(df[col], 0.25)), 2),
            _q3 = round(float(np.quantile(df[col], 0.75)), 2),
            _iqr = round(float(np.quantile(df[col], 0.75)) - np.quantile(df[col], 0.25), 2)
        ))
    for item in result:
        item = item.to_json()
    return result