#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PowerTransformer

dataset = load_boston()
x = dataset.data
t = dataset.target
x_train, x_test, t_train, t_test = train_test_split(x, t, test_size=0.3, random_state=0)
reg_model = LinearRegression()

reg_model.fit(x_train, t_train)
print(reg_model.score(x_train, t_train))

scaler = StandardScaler()
scaler = PowerTransformer()
scaler.fit(x_train)
x_train_scaled = scaler.transform(x_train)
x_test_scaled  = scaler.transform(x_test)
reg_model = LinearRegression()
reg_model.fit(x_train_scaled, t_train)
print(reg_model.score(x_train_scaled, t_train))
print(reg_model.score(x_test_scaled, t_test))

