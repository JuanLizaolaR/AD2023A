#Regresión lineal simple
#Juan Antonio Lizaola Rubio
#Importar dataset
dataset = read.csv('Salary_Data.csv')
#dataset = dataset[, 2:3]

#dividir los datos en conjunto de entrenamiento y conjunto de test
install.packages("caTools")
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
testing_set = subset(dataset, split == FALSE)

#Ajustar el modelo de regresion linea simple con el conjunto de entrenamiento
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)

summary (regressor) 

#predecir resultados con el conjunto test
y_pred = predict(regressor, newdata = testing_set)

#Visualizacion de los resultados en el conjunto de entrenamiento
#install.packages("ggplot2")
library(ggplot2)
ggplot () + geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
                      colour = "red") + 
  geom_line(aes(x = training_set$YearsExperience, y= predict (regressor, newdata = training_set)), 
            colour = "blue") + 
  ggtitle("Sueldo vs Años de Experiencia (Conjunto de Entrenamiento)")+ 
  xlab("Años de Experiencia
       Juan Antonio Lizaola Rubio")+
  ylab("Sueldo (en $)")

#Visualizacion de los resultados en el conjunto de testing
ggplot () + geom_point(aes(x = testing_set$YearsExperience, y = testing_set$Salary),
                       colour = "red") + 
  geom_line(aes(x = training_set$YearsExperience, y= predict (regressor, newdata = training_set)), 
            colour = "blue") + 
  ggtitle("Sueldo vs Años de Experiencia (Conjunto de Testing)")+ 
  xlab("Años de Experiencia

 Juan Antonio Lizaola Rubio      
       ")+
  ylab("Sueldo (en $)")
