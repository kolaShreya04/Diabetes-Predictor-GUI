import numpy as np
import pandas as pd #allows us to read and edit the dataset
import sklearn.linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn import linear_model

def cleandata():
    #TODO: Missing Values
    ds = pd.read_csv('framingham.csv')  # insert dataset name move to same folder as this
    ds.dropna(axis=0, how='any', inplace=True)
    ds.dropna(axis=0, how='all')
    print(ds.shape)
    X = ds.drop(columns=['diabetes']) # this is our input set (things we need to check to find our output) TESTING
    Y = ds['diabetes'] #output data set what we ant to get TRAINING
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size=0.2)
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)
    return X_train,X_test,Y_train,Y_test



def randforest(MAXLeafnodes,X_train,X_test,Y_train,Y_test) -> None:
    rfModel = RandomForestClassifier(max_leaf_nodes=MAXLeafnodes)
    rfModel.fit(X_train,Y_train)
    rfPred = rfModel.predict(X_test)
    Score_RF = accuracy_score(Y_test, rfPred)
    mae = mean_absolute_error(Y_test, rfPred)
    print("Randforest mae and accuracy")
    print(mae , "" , Score_RF)


def RANmaxleaftest() -> None: #Checks if overfit or undefit for parametets
    X_train, X_test, Y_train, Y_test = cleandata()
    for max_leaf_nodes in [5, 50, 100, 200, 500]: ##50 or 200 for parameter optimization
        myranfor = randforest(max_leaf_nodes,X_train, X_test, Y_train, Y_test)


def svmodel(X_train,X_test,Y_train,Y_test)->None:
    svcmodel = SVC()
    svcmodel.fit(X_train,Y_train)
    svcpred = svcmodel.predict(X_test)
    svc_score = accuracy_score(Y_test, svcpred)
    mae = mean_absolute_error(Y_test,svcpred)
    print(mae , "" , svc_score)

def SGD(X_train,X_test,Y_train,Y_test)-> None: #Better error wise
    sgdcl = linear_model.SGDClassifier(max_iter = 1000, tol=1e-3,penalty = "elasticnet")
    sgdcl.fit(X_train,Y_train)
    pred = sgdcl.predict(X_test)

    score = accuracy_score(Y_test, pred)
    mae = mean_absolute_error(Y_test, pred)
    print(mae, "", score)


def linerRegress(X_train,X_test,Y_train,Y_test)-> None:
    LR = linear_model.LinearRegression()
    LR.fit(X_train,Y_train)
    LRPred = LR.predict(X_test)

    mae = mean_absolute_error(Y_test, LRPred)
    print(mae)


#todo: Refactor
RANmaxleaftest()
X_train, X_test, Y_train, Y_test = cleandata()
svmodel(X_train, X_test, Y_train, Y_test)
SGD(X_train, X_test, Y_train, Y_test)
linerRegress(X_train, X_test, Y_train, Y_test)