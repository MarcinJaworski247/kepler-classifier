from sklearn.linear_model import LinearRegression
from app.main.service.data_service import get_data_frame
import numpy as np
from app.main.util.plots.linear_regression_vm import LinearRegressionVM
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


def get_simple_linear_regression(firstAttr, secondAttr):
    df = get_data_frame()

    attr1 = df[firstAttr].values
    attr2 = df[secondAttr].values

    x = np.array(attr1).reshape((-1, 1))
    y = np.array(attr2).reshape((-1, 1))

    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)

    Y_pred = linear_regressor.predict(x)
    res = LinearRegressionVM(Y_pred.flatten().tolist())

    return res.data
