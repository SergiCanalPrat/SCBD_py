# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:41:22 2019
@author: cilia
"""
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
#from sklearn.impute import IterativeImputer
#from sklearn.ensemble import RandomForestRegressor

##Cargar base de datos
data = pd.read_csv('dataset1.csv')
print(data)
print(data.dtypes)
print('------------NULL VALUES----------------')
print(data.isnull().sum()) ##muestra la cantidad de valores nulos de la tablaç

# añadimos a new todas la columnnas de data para tener un copia y modificar esta
new = data.dropna(how='all')
##Usar la sustitucion con los valores nuls de la tabla 
#Sustituye el valor por la media
new.loc[:,'ClasicalDiningRoom'] = data['ClasicalDiningRoom'].replace(np.nan, data['ClasicalDiningRoom'].mean()) 
new.loc[:,'Other'] = data['Other'].replace(np.nan, data['Other'].mean()) 

# Backward fill
new.loc[:,'ClasicalDish'] = data['ClasicalDish'].fillna(method='bfill')
new.loc[:,'PremiumDiningRoom'] = data['PremiumDiningRoom'].fillna(method='bfill')

# Forward fill
new.loc[:,'FFDinigRoom'] = data['FFDinigRoom'].fillna(method='ffill')
new.loc[:,'PremiumDish'] = data['PremiumDish'].fillna(method='ffill')

# Using sklearn.impute.SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
new.loc[:,'FFDish'] = imputer.fit_transform(new[['FFDish']])


# Using sklearn.impute.SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
new.loc[:,'Price'] = imputer.fit_transform(new[['Price']])
#Using sklearn.impute.IterativeImputer
# only available in scikit-learn 0.21, released as a developer version, not as stable.
#imp = IterativeImputer(RandomForestRegressor(), max_iter=10, random_state=0)
#new = pd.DataFrame(imp.fit_transform(data), columns=data.columns)

print('------------NULL VALUES----------------')
print(new.isnull().sum()) ##muestra la cantidad de valores nulos de la tablaç