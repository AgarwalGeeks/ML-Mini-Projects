#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess("word_data.pkl","email_authors.pkl")




#########################################################
### your code goes here ###
from sklearn import tree
from sklearn.metrics import accuracy_score
clf=tree.DecisionTreeClassifier(min_samples_split=40)
###Calculating the present time
t0=time()
###Training
clf.fit(features_train,labels_train)
###printing time of training
print("training time:",round(time()-t0,3),"s")
t1=time()
###Predicting
pred=clf.predict(features_test)
###printing time of prediction
print("prediction time:",round(time()-t1,3),"s")
acc=accuracy_score(pred,labels_test)
###priniting  accuracy
print(round(acc,3)*100,"%")
#print(len(features_train[0]))


#########################################################


