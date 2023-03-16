#Juan Antonio Lizaola Rubio
#214208712
#Plantilla para el pre procesado de datos - datos faltantes
#importar dataset
dataset = read.csv('C:/Users/juanr/examenAnalitica/Data.csv')


#Tratamiento de los valores N/A
dataset$Age = ifelse (is.na(dataset$Age),
                      ave(dataset$Age, FUN = function(x) mean (x, na.rm = TRUE)),
                      dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean (x, na.rm = TRUE)),
                        dataset$Salary)

#importar dataset
dataset = read.csv('C:/Users/juanr/examenAnalitica/Data.csv', stringsAsFactors = F)

str(dataset)
#codificar las variables categoricas
dataset$Country = factor(dataset$Country,
                         levels = c ("France", "Spain", "Germany"),
                         labels =c (1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c ("No", "Yes"),
                           labels =c (0,1))

str(dataset)

#importar el dataset
dataset = read.csv('C:/Users/juanr/examenAnalitica/Data.csv')

#Dividir los datos en conjunto de entrenamiento y conjunto de test 
#install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split (dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)


