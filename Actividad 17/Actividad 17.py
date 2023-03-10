# -*- coding: utf-8 -*-
# Regresión lineal simple modelo de entrenamiento
#JUAN ANTONIO LIZAOLA RUBIO
#09 de Marzo del 2023

#importar librerias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importar dataset
dataset = pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

#dividir el dataset en conjunto de entrenamiento y conjunto testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state = 0)

#crear modelo de regresión lineal simple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression .fit(X_train, y_train)

#predecir el conjunto de test
y_pred = regression.predict(X_test)

#visualizar los resultaodos del entrenamiento
plt.scatter(X_train, y_train, color="red")
plt.plot(X_train, regression.predict(X_train),color = "blue")
plt.title("Sueldo vs Años de Experiencia (Conjunto de entrenamiento)")
plt.xlabel("Años de Experiencia   JUAN ANTONIO LIZAOLA RUBIO")
plt.ylabel("Sueldo (en $")
plt.show()

#visualizar los resultados del test
plt.scatter(X_test, y_test, color="red")
plt.plot(X_train, regression.predict(X_train),color = "blue")
plt.title("Sueldo vs Años de Experiencia (Conjunto de Testing)")
plt.xlabel("Años de Experiencia   JUAN ANTONIO LIZAOLA RUBIO")
plt.ylabel("Sueldo (en $")
plt.show()





