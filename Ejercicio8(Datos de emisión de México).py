import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("GCB2022v27_MtCO2_flat.csv") 
columnas = df.columns 
filasmex = df.index[36176:36448]
filasglo = df.index[62832:63105]

dfmexico = pd.DataFrame(data=df[36176:36449], index=filasmex, columns=columnas)
dfglobal = pd.DataFrame(data=df[62832:63105], index=filasglo, columns=columnas)

print("Datos de México:\n")
print(dfmexico)

x = range(0,272)
y = range(1750,2022)
col = ['Año','Total México','Total Global']
ind = list(x)
año = list(y)
Totalmex = list(dfmexico['Total'])
Totalwld = list(dfglobal['Total'])

comparacion = pd.DataFrame(list(zip(año,Totalmex,Totalwld)),index=ind, columns =col)
print("Comparación datos México y datos globales:\n")
print(comparacion)

#Graficando la comparación
plt.xlabel('Año') 
plt.ylabel('Emisión')
plt.plot(año,Totalmex,'-',color = 'red',label = 'México')
plt.plot(año,Totalwld,'-',color = 'blue',label = 'Global')
plt.title('Comparación de emisión global y México (1750-2021)')
plt.legend()
plt.show()