#Juan Antonio Lizaola Rubio
#214208712
#Plantilla para el pre procesado de datos - datos faltantes
dataset = read.csv('C:/Users/juanr/examenAnalitica/Data.csv')


#Tratamiento de los valores N/A
dataset$Age = ifelse (is.na(dataset$Age),
                      ave(dataset$Age, FUN = function(x) mean (x, na.rm = TRUE)),
                      dataset$Age)
dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary, FUN = function(x) mean (x, na.rm = TRUE)),
                        dataset$Salary)
