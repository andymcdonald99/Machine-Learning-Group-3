import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from sklearn.linear_model import Lasso, Ridge
from sklearn.neighbors import KNeighborsRegressor


def read_file():
    global df, X, y, X1, X2
    df = pd.read_csv(r'./Data/AllData.txt', sep=" ", header=None)
    X1 = df.iloc[:, 0]
    X2 = df.iloc[:, 1]
    X = np.column_stack((X1, X2))
    y = df.iloc[:, 2]


def data_scatter_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[:, 0], X[:, 1], y)
    plt.xlabel("Card")
    plt.ylabel("Trophy")
    ax.set_zlabel('Win %')
    plt.title('3D Scatter Plot of Data')
    plt.show()


def second_scatter_plot():
    count=1
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    r=0.1
    g=0.1
    b=0.1
    colors=cm.rainbow(np.linspace(0,1,106))
    while (count<=106):
        i=0
        sum=0
        for i in range(22277):
            card = X[i,0]
            if int(card)==count:
                ax.scatter(X[i, 0], X[i, 1], y[i], color=colors[count-1])
        count+=1

    plt.xlabel("Card")
    plt.ylabel("Trophy")
    ax.set_zlabel('Win %')
    plt.title('3D Scatter Plot of Input Data')
    plt.gcf().set_size_inches((20, 20))

    plt.show()


def lasso_regression_for_C():
    standard_devs = []
    means = []
    c_arr = [0.00001, 0.01, 1, 5, 10, 50, 100,1000,10000]
    for c in c_arr:
        penalty = 1 / (2 * c)
        lasso_model = Lasso(alpha=penalty)
        five_fold = KFold(n_splits=5, shuffle=False)
        estimates_mean_sq_err = []

        for train_index, test_index in five_fold.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
            lasso_model.fit(X_train, y_train)
            y_pred = lasso_model.predict(X_test)
            estimates_mean_sq_err.append(mean_squared_error(y_test, y_pred))

        means.append(np.mean(estimates_mean_sq_err))
        standard_devs.append(np.std(estimates_mean_sq_err))

    plt.errorbar(c_arr, means, yerr=standard_devs, ecolor='r', linewidth=2, capsize=5)
    plt.title('5 Fold Lasso with various C values')
    plt.xlabel('C')
    plt.ylabel('Mean Square Error (blue) / Standard Deviation (red)')
    plt.show()


def ridge_regression_for_C():
    standard_devs = []
    means = []
    c_arr = [0.00001, 0.01, 1, 5, 10, 50, 100,1000,10000]
    for c in c_arr:
        penalty = 1 / (2 * c)
        ridge_model = Ridge(alpha=penalty)
        five_fold = KFold(n_splits=5, shuffle=False)
        estimates_mean_sq_err = []

        for train_index, test_index in five_fold.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
            ridge_model.fit(X_train, y_train)
            y_pred = ridge_model.predict(X_test)
            estimates_mean_sq_err.append(mean_squared_error(y_test, y_pred))

        means.append(np.mean(estimates_mean_sq_err))
        standard_devs.append(np.std(estimates_mean_sq_err))

    plt.errorbar(np.log10(c_arr), means, yerr=standard_devs, ecolor='r', linewidth=2, capsize=5)
    plt.title('5 Fold Ridge with various C values')
    plt.xlabel('log10(C)')
    plt.ylabel('Mean Square Error (blue) / Standard Deviation (red)')
    plt.show()


def knn_regression_for_k():
    # Training kNN classifier with cross-validation
    neighbours = [1, 3, 5, 7, 9, 11, 15, 21, 51, 101]
    standard_devs = []
    means = []
    for n in neighbours:
        knn_model = KNeighborsRegressor(n_neighbors=n, weights='uniform')
        five_fold = KFold(n_splits=5, shuffle=False)
        estimates_mean_sq_err = []
        for train_index, test_index in five_fold.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
            knn_model.fit(X_train, y_train)
            y_pred = knn_model.predict(X_test)
            estimates_mean_sq_err.append(mean_squared_error(y_test, y_pred))

        means.append(np.mean(estimates_mean_sq_err))
        standard_devs.append(np.std(estimates_mean_sq_err))

    plt.errorbar(neighbours, means, yerr=standard_devs, ecolor='r', linewidth=2, capsize=5)
    plt.title('kNN for Different Neighbours')
    plt.xlabel('Neighbours')
    plt.ylabel('Mean Square Error (blue) / Standard Deviation (red)')
    plt.show()


def knn_regression_for_w():
    weights = ['uniform', 'distance']
    standard_devs = []
    means = []
    for w in weights:
        knn_model = KNeighborsRegressor(n_neighbors=15, weights=w)
        five_fold = KFold(n_splits=5, shuffle=False)
        estimates_mean_sq_err = []
        for train_index, test_index in five_fold.split(X):
            X_train, X_test, y_train, y_test = X[train_index], X[test_index], y[train_index], y[test_index]
            knn_model.fit(X_train, y_train)
            y_pred = knn_model.predict(X_test)
            estimates_mean_sq_err.append(mean_squared_error(y_test, y_pred))

        means.append(np.mean(estimates_mean_sq_err))
        standard_devs.append(np.std(estimates_mean_sq_err))

    plt.errorbar(weights, means, yerr=standard_devs, ecolor='r', linewidth=2, capsize=5)
    plt.title('kNN for Different Weights')
    plt.xlabel('Weight')
    plt.ylabel('Mean Square Error (blue) / Standard Deviation (red)')
    plt.show()


if __name__ == '__main__':
    read_file()
    data_scatter_plot()
    second_scatter_plot()
    lasso_regression_for_C()
    ridge_regression_for_C()
    knn_regression_for_k()
    knn_regression_for_w()
