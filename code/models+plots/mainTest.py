import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.model_selection import train_test_split, KFold
from sklearn.linear_model import Lasso, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def measurements(name, ytest, predictions):
    mse = mean_squared_error(ytest, predictions)
    rmse = sqrt(mse)
    mae = mean_absolute_error(ytest, predictions)
    r_squared = r2_score(ytest, predictions)
    print(name + "MSE: " + str(round(mse,5)) + "\nRMSE: " + str(round(rmse,5)) + "\nMAE: " + str(round(mae,5)) + "\nR^2: " + str(round(r_squared,5)) + "\n")

def read_file():
    global df, X, y, X1, X2
    df = pd.read_csv(r'./Data/AllData.txt', sep=" ", header=None)
    print(df)
    X1 = df.iloc[:, 0]
    X2 = df.iloc[:, 1]
    X = np.column_stack((X1, X2))
    y = df.iloc[:, 2]


def lasso_reg(xtrain,xtest,ytrain,ytest):
    c=1
    penalty = 1 / (2 * c)
    lasso_model = Lasso(alpha=penalty)
    lasso_model.fit(xtrain,ytrain)
    predictions = lasso_model.predict(xtest)
    measurements("LASSO Model Measurements\n", ytest, predictions)
    plt.scatter(xtest[:,0], ytest, color='blue', marker='o')
    plt.scatter(xtest[:,0], predictions, color='red', marker='x')  # plot predictions on actual answers
    plt.title("Lasso model predictions vs actual output")
    plt.xlabel("Favourite card")
    plt.ylabel("Win %")
    plt.show()

def ridge_reg(xtrain,xtest,ytrain,ytest):
    c=0.00001
    penalty = 1 / (2 * c)
    ridge_model = Ridge(alpha=penalty)
    ridge_model.fit(xtrain,ytrain)
    predictions = ridge_model.predict(xtest)
    measurements("RIDGE Model Measurements\n", ytest, predictions)
    plt.scatter(xtest[:,0], ytest, color='blue', marker='o')
    plt.scatter(xtest[:,0], predictions, color='red', marker='x') # predictions
    plt.title("Ridge model predictions vs actual output")
    plt.xlabel("Favourite card")
    plt.ylabel("Win %")
    plt.show()

def knn_reg(xtrain,xtest,ytrain,ytest):
    n=15
    knn_model = KNeighborsRegressor(n_neighbors=n, weights='uniform')
    knn_model.fit(xtrain, ytrain)
    predictions = knn_model.predict(xtest)
    measurements("KNN Model Measurements\n", ytest, predictions)
    plt.scatter(xtest[:,0], ytest, color='blue', marker='o')
    plt.scatter(xtest[:,0], predictions, color='red', marker='x')  #  predictions
    plt.title("KNN model predictions vs actual output")
    plt.xlabel("Favourite card")
    plt.ylabel("Win %")
    plt.show()

def calc_mean(xtrain, xtest, ytrain, ytest):
    sum=0.0
    for i in y:
        sum+=i
    avg = round(sum/float(len(y)),2)
    print("\nmean is ",avg)
    i=0
    lister=[]
    for i in range(len(ytest)):
        lister.append(avg)

    measurements("Baseline Measurements\n", ytest, lister)
    plt.scatter(xtest[:, 0], ytest, color='blue', marker='o')
    plt.scatter(xtest[:, 0], lister, color='red', marker='x')  #  predictions
    plt.title("Baseline model predictions vs actual output")
    plt.xlabel("Favourite card")
    plt.ylabel("Win %")
    plt.show()

if __name__ == '__main__':
    read_file()
    xtrain, xtest, ytrain, ytest = train_test_split(X,y, test_size=0.3)

    calc_mean(xtrain, xtest, ytrain, ytest) #mean for baseline predictor
    lasso_reg(xtrain, xtest, ytrain, ytest)
    ridge_reg(xtrain, xtest, ytrain, ytest)
    knn_reg(xtrain, xtest, ytrain, ytest)

