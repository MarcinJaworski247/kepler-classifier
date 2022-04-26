from sklearn.model_selection import cross_validate, train_test_split
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

    rf_acc, rf_balanced_acc, rf_brier, rf_f1 = random_forest_classifier(
        Y, X, int(params.testDataPercentage) /
        100, int(params.treesCount), params.isCrossValidation, params.foldsCount
    )
    dt_acc, dt_balanced_acc, dt_brier, dt_f1 = decision_tree_classifier(
        Y, X, int(params.testDataPercentage) /
        100, params.isCrossValidation, params.foldsCount
    )
    svm_acc, svm_balanced_acc, svm_brier, svm_f1 = svm_classifier(
        Y, X, int(params.testDataPercentage) / 100, params.isCrossValidation, params.foldsCount)
    knn_acc, knn_balanced_acc, knn_brier, knn_f1 = knn_classifier(
        Y, X, int(params.testDataPercentage) / 100, params.neighboursCount, params.isCrossValidation, params.foldsCount)

    return [
        ClassificationResponseVM("Random forest", round(
            rf_acc, 4), round(rf_balanced_acc, 4), round(rf_brier, 4), round(rf_f1, 4)),
        ClassificationResponseVM("Decision tree", round(
            dt_acc, 4), round(dt_balanced_acc, 4), round(dt_brier, 4), round(dt_f1, 4)),
        ClassificationResponseVM(
            "Support Vector Machine", round(svm_acc, 4), round(svm_balanced_acc, 4), round(svm_brier, 4), round(svm_f1, 4)),
        ClassificationResponseVM(
            "K-nearest neighbours", round(knn_acc, 4), round(knn_balanced_acc, 4), round(knn_brier, 4), round(knn_f1, 4)),
    ]


def random_forest_classifier(Y, X, testDataPercentage, treesCount, isCrossValidation, foldsCount):
    # split data into train and test datasets
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=testDataPercentage, random_state=20
    )

    model = RandomForestClassifier(n_estimators=treesCount)
    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    # model metrics
    rf_accuracy = metrics.accuracy_score(Y_test, prediction)
    rf_balanced_accuracy = metrics.balanced_accuracy_score(Y_test, prediction)
    rf_brier_score_loss = metrics.brier_score_loss(Y_test, prediction)
    rf_f1_score = metrics.f1_score(Y_test, prediction)

    return rf_accuracy, rf_balanced_accuracy, rf_brier_score_loss, rf_f1_score


def decision_tree_classifier(Y, X, testDataPercentage, isCrossValidation, foldsCount):
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
    dt_brier_score_loss = metrics.brier_score_loss(Y_test, prediction)
    dt_f1_score = metrics.f1_score(Y_test, prediction)

    return dt_accuracy, dt_balanced_accuracy, dt_brier_score_loss, dt_f1_score


def svm_classifier(Y, X, testDataPercentage, isCrossValidation, foldsCount):
    # split data into train and test datasets
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=testDataPercentage, random_state=20
    )

    model = svm.LinearSVC()
    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    # model metrics
    svm_accuracy = metrics.accuracy_score(Y_test, prediction)
    svm_balanced_score = metrics.balanced_accuracy_score(Y_test, prediction)
    svm_brier_score_loss = metrics.brier_score_loss(Y_test, prediction)
    svm_f1_score = metrics.f1_score(Y_test, prediction)

    return svm_accuracy, svm_balanced_score, svm_brier_score_loss, svm_f1_score


def knn_classifier(Y, X, testDataPercentage, neighboursCount, isCrossValidation, foldsCount):
    # split data into train and test datasets
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=testDataPercentage, random_state=20
    )

    model = KNeighborsClassifier(n_neighbors=int(neighboursCount))

    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    # model metrics
    accuracy = metrics.accuracy_score(Y_test, prediction)
    balanced_accuracy = metrics.balanced_accuracy_score(Y_test, prediction)
    brier_score_loss = metrics.brier_score_loss(Y_test, prediction)
    f1_score = metrics.f1_score(Y_test, prediction)

    return accuracy, balanced_accuracy, brier_score_loss, f1_score
