import numpy as np

from sklearn import datasets
from sklearn import svm, linear_model
from sklearn.neighbors import KNeighborsClassifier, \
    RadiusNeighborsClassifier


def knnClassifier(xTrain, yTrain, xTest, yTest):

    # Create KNeighbor & RadiusNeighbor Classifiers
    knnKNeighbors = KNeighborsClassifier()
    knnRadiusNeighbors = RadiusNeighborsClassifier()

    # Fit data
    knnKNeighbors.fit(xTrain, yTrain)
    knnRadiusNeighbors.fit(xTrain, yTrain)

    # Find matches between predicted & actual values
    matchesKNeighbors = [i for i,j in zip(knnKNeighbors.predict(xTest), yTest) if i == j]
    matchesRadiusNeighbors = [i for i,j in zip(knnKNeighbors.predict(xTest), yTest) if i == j]

    print "Accuracy of KNeighbors: ", (float(len(matchesKNeighbors))/len(yTest)) * 100
    print "Accuracy of RadiusNeighbors: ", (float(len(matchesRadiusNeighbors))/len(yTest)) * 100


def linearRegressor(xTrain, yTrain, xTest, yTest):

    # Apply linear regression
    linear_regress = linear_model.LinearRegression()
    linear_regress.fit(xTrain,yTrain)

    # Apply Ridge Regression (An approach can be to
    # try out multiple values using np.logspace and see
    # which alpha returns maximum score.)

    ridge_regress = linear_model.Ridge(alpha=0.01)
    ridge_regress.fit(xTrain,yTrain)

    # Apply Lasso Regression

    lasso_regress = linear_model.Lasso(alpha=0.01)
    lasso_regress.fit(xTrain,yTrain)

    # Calculate regression score: 1 indicates perfect
    # prediction, 0 means there is no relationship
    print "Linear Model Score: ", linear_regress.score(xTest,yTest)
    print "Ridge Model Score: ", ridge_regress.score(xTest,yTest)
    print "Lasso Model Score: ", lasso_regress.score(xTest,yTest)


def logisticRegressor (xTrain, yTrain, xTest, yTest):


    # Apply logistic regression
    logistic_regress = linear_model.LogisticRegression()
    logistic_regress.fit(xTrain,yTrain)

    # Calculate regression score: 1 indicates perfect
    # prediction, 0 means there is no relationship
    print "Logistic Model Score: ", logistic_regress.score(xTest,yTest)


def main():

    # Load IRIS data-set
    iris = datasets.load_iris()
    iris_X = iris.data
    iris_y = iris.target

    # Randomly split data into training and test
    np.random.seed(0)
    indices = np.random.permutation(len(iris_X))

    # Assign all but last 10 indices to training
    iris_X_train = iris_X[indices[:-10]]
    iris_y_train = iris_y[indices[:-10]]
    # Assign last 10 indices to test
    iris_X_test = iris_X[indices[-10:]]
    iris_y_test = iris_y[indices[-10:]]

    # Load Diabetes data-set
    diabetes = datasets.load_diabetes()
    diabetes_X = diabetes.data
    diabetes_y = diabetes.target

    # Randomly split data into training and test
    np.random.seed(0)
    indices = np.random.permutation(len(diabetes_X))

    # Assign all but last 20 indices to training
    diabetes_X_train = diabetes_X[indices[:-20]]
    diabetes_y_train = diabetes_y[indices[:-20]]
    # Assign last 20 indices to test
    diabetes_X_test = diabetes_X[indices[-20:]]
    diabetes_y_test = diabetes_y[indices[-20:]]

    knnClassifier(iris_X_train,iris_y_train,iris_X_test,iris_y_test)
    linearRegressor(diabetes_X_train,diabetes_y_train,diabetes_X_test,diabetes_y_test)
    logisticRegressor(iris_X_train,iris_y_train,iris_X_test,iris_y_test)

if __name__ == '__main__':
    main()