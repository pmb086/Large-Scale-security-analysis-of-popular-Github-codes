from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn import svm
data = pd.read_csv('train_file.csv', sep=",")
X = data.drop(['Project_url','Project_Name'], axis=1)
X = X.drop(['Language','Created_at'], axis=1)
X = X.drop(['Pushed_at','Subscribers','# of Vuln'], axis=1)
X = X.drop(['Vul-1','Vul-2','Vul-3','Vul-4'], axis=1)
X = X.fillna(X.mean())
Y= data['Vul-1']
Y=Y.astype('str')
test_data = pd.read_csv('test_file.csv', sep=",")
test_X = test_data.drop(['Project_url','Project_Name'], axis=1)
test_X = test_X.drop(['Language','Created_at'], axis=1)
test_X = test_X.drop(['Pushed_at','Github_score','# of Vuln'], axis=1)
test_X = test_X.drop(['Vul-1','Vul-2','Vul-3','Vul-4'], axis=1)
test_X = test_X.fillna(test_X.mean())
test_Y= test_data['Vul-1']
test_Y= test_Y.astype('str')
print(X.shape)
print(Y.shape)
#logistic regression
logist = LogisticRegression()
logist.fit(X, Y)
j=1
for i in range(0,440,55):
	y_pred = logist.predict(test_X.iloc[i:i+55])
	print(str(j)+'th epoch')
	print('The accuracy of Logistic Regression is' + str(metrics.accuracy_score(Y, y_pred)))
	print(y_pred)
	j+=1

'''model = svm.SVC() #select the algorithm
model.fit(X,Y) # we train the algorithm with the training data and the training output
prediction=model.predict(test_X) #now we pass the testing data to the trained algorithm
print('The accuracy of the SVM is:',metrics.accuracy_score(prediction,test_Y))#now we check the accuracy of the algorithm. 
#we pass the predicted output by the model and the actual output'''




