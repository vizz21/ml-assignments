# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 21:30:00 2022

@author: User
"""

#importing libraries 
import numpy as np
import pandas as pd

#impoorting dataset
dataset=pd.read_csv('Data.csv')
dataset=pd.read_csv('Data.csv')
#pd.read_csv is a predefined method in pandas to import dataset


X=dataset.iloc[:,:-1].values   #independent variable matrix
y=dataset.iloc[:,3].values   #dependent variable vector 
# .iloc is a method to import desired columns



"""
to handle missing data values we use sklearn to compute the missing values 
with its mean
"""
#handling missing data
from sklearn.impute import SimpleImputer  #imputer is the class
imputer= SimpleImputer(missing_values ='nan',strategy='mean')                  
#imputer variable is the object of class Imputer 
imputer=imputer.fit(X[:,1:3])    
X[:,1:3]=imputer.transform(X[:,1:3])


