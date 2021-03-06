#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 21:42:33 2017

@author: Christian R. F. Gomes
@title: Support Vector Regression
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#--------------------------------------------------------------------------

# BASES DE DADOS

train = pd.read_csv('~/Documentos/Ciencia da Computacao/Machine Learning/New York City Taxi Trip Duration - Kaggle Competition/Data/train.csv', header=0)
test = pd.read_csv('~/Documentos/Ciencia da Computacao/Machine Learning/New York City Taxi Trip Duration - Kaggle Competition/Data/test.csv', header=0)

#--------------------------------------------------------------------------

# PRE-PROCESSAMENTO

train.dtypes
# One Hot Encoding
train = pd.get_dummies(train, columns=['store_and_fwd_flag'], prefix=['frag'])

# Analise basica sem as colunas id, pickup_datetime e dropoff_datetime
train.drop(train.columns[[0, 2, 3]], axis=1, inplace=True)
train = train[['vendor_id', 'passenger_count', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'frag_N', 'frag_Y', 'trip_duration']]

X = train.iloc[0:100, 0:8].values
y = train.iloc[0:100, 8].values

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = y.reshape(-1, 1)
y = sc_y.fit_transform(y)

#--------------------------------------------------------------------------

# TRAINING AND TEST SET
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 12)

#--------------------------------------------------------------------------

# CRIACAO E AVALIACAO DO MODELO

# Criacao do modelo SVR
from sklearn.svm import SVR
svr_regressor = SVR(kernel='rbf')
y = y.ravel()
svr_regressor.fit(X, y)

from sklearn import model_selection
kfold = model_selection.KFold(n_splits=10, random_state=12)
results = model_selection.cross_val_score(svr_regressor, X, y, cv=kfold, scoring='accuracy')

