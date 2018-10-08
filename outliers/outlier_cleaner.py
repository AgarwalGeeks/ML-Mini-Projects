#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    print("function invoked")
    cleaned_data = []
    age_list=[]
    net_worth_list=[]
    #age_list=[]
    #error_list=[]
    ### your code goes here
    i=0
    error_list=[]
    for num in range(0,len(ages)):
        error_list.append(abs(int(predictions[i]-net_worths[i])))
        age_list.append(int(ages[i]))
        net_worth_list.append(int(net_worths[i]))
        i=i+1
    print("loop1")
    for i in range(0,9):
        ind=error_list.index(max(error_list))
        error_list.remove(error_list[ind])
        age_list.remove(age_list[ind])
        net_worth_list.remove(net_worth_list[ind])
    print("loop2")
    z=0
    for x in range(0,81):
        cleaned_data.append((age_list[z],net_worth_list[z],error_list[z]))
        z=z+1
    print("loop3")
    
    return cleaned_data

