#Juan Antonio Lizaola Rubio
#214208712
#Plantilla para el pre procesado de datos - datos categoricos
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
