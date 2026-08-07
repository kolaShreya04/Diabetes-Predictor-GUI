import pandas as pd #allows us to read and edit the dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
# NOTE: we need to import random forest

ds = pd.read_csv('framingham.csv') #insert dataset name move to same folder as this
print(ds['diabetes'].value_counts())  # 0 is no diabetes 1 is diabtetes

#print(ds.isna)
ds.dropna(axis=0,how='any',inplace=True)
print(ds.shape) # this will tell us the size and amount of items in data set

print(ds['diabetes'].value_counts())  # 0 is no diabetes 1 is diabtetes

'''
TODO: IGNORE HERE
#This does the exact same thing as value_counts() but
 if we had to sep stuff thats more than 0 and 1s
 #

bins = (0,1,2)
group_names = ['no_Diabetes','Diabetes']
ds['diabetes'] = pd.cut(ds['diabetes'], bins = bins, labels = group_names)
print(ds['diabetes'].unique())

has_diabetes = LabelEncoder()
ds['diabetes'] = has_diabetes.fit_transform(ds['diabetes'])
print(ds['diabetes'].value_counts())
'''

# Insert cleaning code ex: drop education or n/a rows
#Drop NA
X = ds.drop(columns=['diabetes']) # this is our input set (things we need to check to find our output) TESTING
Y = ds['diabetes'] #output data set what we ant to get TRAINING
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size=0.2) #sets aside 20% of data for testing
#first 2 are input training + testing second 2 are forout teting + trainn
#scales the numbers so things have an equal impact
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

#Model_Df = DecisionTreeClassifier()
#Model_Df.fit(X_train, Y_train) #takes input and ouput set to train set
#Predict_Df = Model_Df.predict(X_test) #must insert users information from non-dropped tables
#Score_Df = accuracy_score(Y_test, Predict_Df) # contains score of 0 to 1

#TODO: SEPERATE IF DIABETES OR NOT TO TRAIN FOR RF
Model_RF = RandomForestClassifier(n_estimators=200) #amount of trees it will build
Model_RF.fit(X_train, Y_train,sample_weight=None)
Predict_RF = Model_RF.predict(X_test)
Score_RF = accuracy_score(Y_test,Predict_RF)


#TODO: uncomment stuff
with open('Diabetes_model','wb') as f:
    pickle.dump(Model_RF, f)


print(Score_RF)


#use y test to see how good x test is
print(classification_report(Y_test, Predict_RF))
'''
Classification Report
 What is the Y_Test: 
    Y_test is the testing input that you use to test the model
    (in short you take an amount from the used csv file and insert it into the model to test it)
    
    
'''


print(confusion_matrix(Y_test,Predict_RF))

'''
How to read confusion matrix:
    The confusion matrix takes the Y_test and Predict_RF
    What is the Y_Test: 
    Y_test is the testing input that you use to test the model
    (in short you take an amount from the used csv file and insert it into the model to test it)
    
    Predict_RF allows us to TODO: Continue explanation 
    
    Top array checks for users that do not have diabetes
    Bottom array checks for users that have diabetes
    
    The left number provides the amount of correctly classified items
    the right number provides the amount of incorrectly classified items
    
'''
#top number for confusion matrix 706 correct for no diabetes 0 inccorect
#bottom 15 correct for diabetes 11 for inccorect
