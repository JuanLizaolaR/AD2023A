
#Juan Antonio Lizaola Rubio
#214208712
#Plantilla para el pre procesado de datos
#importar el dataset
dataset = read.csv('C:/Users/juanr/examenAnalitica/Data.csv')
dataset = dataset [, 2:3]

#Dividir los datos en conjunto de entrenamiento y conjunto de test 
#install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split (dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split== TRUE)
testing_set = subset(dataset, split== FALSE)
