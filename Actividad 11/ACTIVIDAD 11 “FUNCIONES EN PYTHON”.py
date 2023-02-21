#!/usr/bin/env python
# coding: utf-8

# <h4> Juan Antonio Lizaola Rubio </h4>
# <h4> 214208712 </h4>
# <h4> 20/02/23 </h4>
# <h4> Actividad 11 Analítica de Datos 2023-A LTIN</h4>

# <h1>Hello World (Hola Mundo)</h1>

# In[2]:


print("Hello World")


# In[3]:


"Hello World"


# <h1>Tipos de datos</h1>

# <h3>Integer / Float</h3>

# In[7]:


#permite ver el tipo de dato de un objeto
type(1)


# In[8]:


type(2.3)


# <h3>Operaciones</h3>

# <li> Adicion + </li>
# <li> Substraccion - </li>
# <li> Multiplicación * </li>
# <li> División / </li>
# <li> Exponente **</li>
# <li> Residuo % </li>
# <li> División entera //</li>

# In[9]:


1 + 2


# In[11]:


3 ** 2


# <h1> Boolean </h1>

# In[13]:


type(True)


# <h1> String (Cadena de texto) </h1>

# In[14]:


type("Hello World")


# <h3> String metodos </h3>

# In[21]:


# cambiar miniscula, mayuscula, etc.
print("Hello World".upper())
print("Hello World".lower())
print("Hello World".title())

# contar letras
print("Hello World".count("l"))
# reemplazar letras
print("Hello World".replace('o', 'u'))


# <h1> Variables </h1>

# In[39]:


message_1 = "Estoy aprendiendo Python"


# In[40]:


message_1


# In[41]:


message_2 = "y es divertido :) "


# In[42]:


message_2


# In[43]:


message_1 + message_2


# In[44]:


message_1 + " " + message_2


# In[45]:


message = f'{message_1}{message_2}'
message


# <h1> Listas </h1>

# In[49]:


countries = ['United States','India','China','Brazil']


# In[50]:


countries


# In[51]:


countries[0]


# In[52]:


countries[1]


# In[53]:


countries[3]


# In[54]:


countries[-1]


# In[55]:


countries[-4]


# <h1> Rebanada / Slicing </h1>

#  <h3> nombre_lista[star:stop] </h3>

# In[56]:


countries


# In[57]:


countries[0:3]


# In[58]:


countries[1:]


# In[59]:


countries[:2]


# <h1> Operaciones y Metodos </h1>

# In[60]:


countries


# In[62]:


countries.append('Canada')


# In[63]:


countries


# In[64]:


countries.insert(0, 'Argentina')


# In[65]:


countries


# In[66]:


countries_2 = ['UK','Alemania','Australia']


# In[67]:


countries + countries_2


# In[68]:


nueva_lista = [countries, countries_2]


# In[69]:


nueva_lista


# <h1> Eliminar elementos </h1>

# In[72]:


countries.remove('Canada')


# In[73]:


countries


# In[74]:


countries.pop(0)


# In[75]:


countries


# In[76]:


del countries[0]


# In[77]:


countries


# <h1> Ordenar una lista </h1>

# In[78]:


numbers = [4,3,10,7,1,2]


# In[79]:


numbers


# In[80]:


numbers.sort()


# In[81]:


numbers


# In[82]:


numbers.sort(reverse=True)


# In[83]:


numbers


# In[84]:


numbers[0] = 1000


# In[85]:


numbers


# <h1> Copiar una lista </h1>

# In[86]:


countries.append('Argentina')


# In[87]:


countries


# In[88]:


nueva_lista_3 = countries


# In[89]:


nueva_lista_3


# In[90]:


nueva_lista = countries.copy()


# In[91]:


nueva_lista


# In[92]:


nueva_lista_2 = countries[:]


# In[93]:


nueva_lista_2


# <h1> Diccionarios </h1>

# In[94]:


mi_diccionario = {'key1':'value1', 'key2':'value2'}


# In[95]:


my_data = {'nombre': 'Frank','edad':26}


# In[96]:


my_data


# In[97]:


my_data ['nombre']


# In[98]:


my_data.keys()


# In[99]:


my_data.values()


# In[100]:


my_data.items()


# <h1> Agregar / Actualizar elementos </h1>

# In[102]:


my_data = {'nombre':'Frank', 'edad':26}


# In[103]:


my_data['estatura'] = 1.7


# In[104]:


my_data


# In[105]:


my_data.update({'estatura':1.9,'lenguages':['ingles','español']})


# In[106]:


my_data


# <h1> Copiar un diccionario </h1>

# In[107]:


nuevo_diccionario = my_data.copy()


# In[108]:


nuevo_diccionario


# <h1> Eliminar elementos </h1>

# In[110]:


my_data


# In[111]:


my_data.pop('estatura')


# In[112]:


my_data


# In[113]:


del my_data ['lenguages']


# In[114]:


my_data


# In[115]:


my_data.clear()


# In[116]:


my_data


# <h1> Condicional IF </h1>

# In[117]:


edad = 24

if edad>= 18:
    print("Eres mayor de edad")
elif edad>=13:
    print("Eres un adolescente")
else:
    print("Eres un niño")


# In[118]:


countries = ['United States','India','China','Brazil']


# In[119]:


if "Colombia" in countries:
    print("Pais esta en la lista")
else:
    print("Pais no esta en la lista")


# <h1> For loop (bucle for)</h1>

# In[120]:


for pais in  countries:
    print(pais)


# In[121]:


for pais in countries:
    if pais == "United States":
        print(pais)


# In[122]:


for numero, pais in enumerate(countries):
    print(numero)
    print(pais)


# In[123]:


my_data = {'nombre':'Frank','edad':26}


# In[124]:


my_data


# In[125]:


my_data.items()


# In[126]:


for key, value in my_data.items():
    print(key)
    print(value)


# <h1> Funciones </h1>

# <h3> Funciones pre-fabricadas </h3>

# In[128]:


countries


# In[129]:


len(countries)


# In[130]:


max([16,83,32,1,10])


# In[131]:


min([16,83,32,1,10])


# In[132]:


type(countries)


# In[133]:


type(my_data)


# In[134]:


round(2.333,2)


# In[135]:


for i in range(1,10,2):
    print(i)


# <h1> Crear una función </h1>

# In[136]:


def sumar_numeros(a,b):
    suma_final = a + b
    return suma_final


# In[137]:


sumar_numeros(10,5)


# <h1> Modulos </h1>

# <h1> Modulos OS </h1>

# In[140]:


import os


# In[142]:


os.getcwd()


# In[143]:


os.listdir()


# In[144]:


os.makedirs("Nueva carpeta")


# In[145]:


os.listdir()


# In[ ]:




