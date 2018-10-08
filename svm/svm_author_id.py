#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
features_train, features_test, labels_train, labels_test = preprocess('word_data.pkl','email_authors.pkl')


#########################################################
### your code goes here ###
#labels_train=labels_train[:int(len(labels_train)/100)]
#features_train=features_train[:int(len(features_train)/100)]
from sklearn.svm import SVC
clf=SVC()
t0=time()
clf.fit(features_train,labels_train)
print("Training Time:",round(time()-t0,3),"s")
t1=time()
pred=clf.predict(features_test)
print("Prediction Time:",round(time()-t1,3),"s")
### to find the accuracy
from sklearn.metrics import accuracy_score
print("Accuracy:",abs(accuracy_score(pred,labels_test)*100),"%")

#########################################################


