#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
employee_list=[]
poi_list=[]
features=[]
count=0
enron_data = pickle.load(open("final_project_dataset.pkl", "rb"))
#print("Number of employees",len(enron_data))
for i in enron_data:
    employee_list.append(i)
#print("Employee list",employee_list)
#print("Number of Features in each person",len(enron_data[employee_list[0]]))
#features=enron_data[employee_list[0]].keys()
#print("Features",list(features))
for employee in enron_data:
    if(enron_data[employee]['poi']==True):
        count=count+1
        poi_list.append(employee)

#print("Number of POI's",count,"\n",poi_list)
#print("Total stock value belong to James Prentice",enron_data['PRENTICE JAMES']['total_stock_value'])
#print("From this person to poi",enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
#print("stock options exercise",enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
p_list=['LAY KENNETH L','SKILLING JEFFREY K','FASTOW ANDREW S']
'''for person in p_list:
    print(person,":",enron_data[person]['total_payments'])
    '''
quant=0
email=0
import math
for employee in employee_list:
    if(math.isnan(float(enron_data[employee]['salary']))==False):
          quant=quant+1
    if(enron_data[employee]['email_address']!="NaN"):
          email=email+1
    
#print("No. of quanitified salary",quant)
#print("No. of known email address",email)
x=0
y=0
'''for employee in employee_list:
    if(enron_data[employee]['total_payments']=="NaN"):
        x=x+1
    
print(x)
print((x/146)*100)
'''
z=0
for poi in poi_list:
    if(enron_data[poi]['total_payments']=="NaN"):
        z=z+1
    
print(z)
print((z/18)*100)

