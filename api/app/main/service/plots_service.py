from app.main.service.data_service import get_data_frame
from app.main.util.plots.values_vm import ValuesVM
from app.main.util.plots.pearson_corr_vm import PearsonCorrVM


def get_pearson_corr():
    df = get_data_frame()
    correlations = df.corr()

    result = []
    columns = correlations.columns

    for col in columns:
        name = col
        data = []

        for val in correlations[col].values:
            data.append({"x": "", "y": round(val, 4)})

        for i in range(0, len(data)):
            data[i]["x"] = columns[i]

        result.append(PearsonCorrVM(name, data))

    return result


def get_values(attribute):
    df = get_data_frame()
    res = ValuesVM(attribute, df[attribute].values)
    return res
