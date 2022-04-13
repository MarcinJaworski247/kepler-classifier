from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

from app.main.service.data_service import get_data_frame_to_classify
from app.main.util.classification_response_vm import ClassificationResponseVM


def get_classification_results(params):
    df = get_data_frame_to_classify()
    # class variable
    Y = df.koi_disposition.values
    Y = Y.astype("int")
    # independent variables
    X = df.drop(labels=["koi_disposition"], axis=1)

    rf_acc, rf_balanced_acc = random_forest_classifier(
        df, Y, X, params["testDataPercentage"] / 100, params["numberOfTrees"]
    )
    dt_acc, dt_balanced_acc = decision_tree_classifier(
        df, Y, X, params["testDataPercentage"] / 100
    )
    # svm_acc, svm_balanced_acc = svm_classifier(
    #     df, Y, X, params["testDataPercentage"] / 100
    # )
    knn_acc, knn_balanced_acc = knn_classifier(
        df, Y, X, params["testDataPercentage"] / 100
    )
    return [
        ClassificationResponseVM("rf", rf_acc, rf_balanced_acc),
        ClassificationResponseVM("dt", dt_acc, dt_balanced_acc),
        # ClassificationResponseVM("svm", svm_acc, svm_balanced_acc),
        ClassificationResponseVM("knn", knn_acc, knn_balanced_acc),
    ]


def random_forest_classifier(df, Y, X, testDataPercentage, numberOfTrees):
    # split data into train and test datasets
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=testDataPercentage, random_state=20
    )

    model = RandomForestClassifier(n_estimators=numberOfTrees)
    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    # model metrics
    rf_accuracy = metrics.accuracy_score(Y_test, prediction)
    rf_balanced_accuracy = metrics.balanced_accuracy_score(Y_test, prediction)

    return rf_accuracy, rf_balanced_accuracy


def decision_tree_classifier(df, Y, X, testDataPercentage):
    # split data into train and test datasets
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=testDataPercentage, random_state=20
    )

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    # model metrics
    dt_accuracy = metrics.accuracy_score(Y_test, prediction)
    dt_balanced_accuracy = metrics.balanced_accuracy_score(Y_test, prediction)

    return dt_accuracy, dt_balanced_accuracy


def svm_classifier(df, Y, X, testDataPercentage):
    # split data into train and test datasets
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=testDataPercentage, random_state=20
    )

    model = svm.SVC(kernel="linear")
    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    # model metrics
    svm_accuracy = metrics.accuracy_score(Y_test, prediction)
    svm_balanced_score = metrics.balanced_accuracy_score(Y_test, prediction)

    return svm_accuracy, svm_balanced_score


def knn_classifier(df, Y, X, testDataPercentage):
    # split data into train and test datasets
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=testDataPercentage, random_state=20
    )

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    # model metrics
    knn_accuracy = metrics.accuracy_score(Y_test, prediction)
    knn_balanced_accuracy = metrics.balanced_accuracy_score(Y_test, prediction)

    return knn_accuracy, knn_balanced_accuracy
