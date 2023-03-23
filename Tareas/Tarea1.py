import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Convirtiendo el csv a Dataframe
df=pd.read_csv("GCB2022v27_MtCO2_flat.csv")

#Desplegando el nombre de cada columna:
print("Las columnas son: \n")
for i in (df.columns):
  print(i)

#Tipo de dato en cada columna:
print("\nTipo de dato por columna: \n")
print(df.dtypes)

#Contando el número de NaNs por columna:
print("\nNúmero de NaNs por columna: \n")
print(df.isnull().sum())

#Contando cantidad de paises:
paises = []
for j in range (len(df)):
  pais = df['Country'].iloc[j]
  if pais not in paises:
    paises.append(pais)
  if pais == 'Zimbabwe':
    break
print("\nExisten datos de",len(paises),"países diferentes. \n")

#Graficando valores globales:
df.set_index('Country', inplace = True)
fig, ax = plt.subplots(2,4, figsize=(18,8))
fig.suptitle(r'Valores globales' , fontsize=20)
ax[0,0].plot(df['Global':'Global']['Year'], df['Global':'Global']['Total'])
ax[0,0].set_title('Total');
ax[0,1].plot(df['Global':'Global']['Year'], df['Global':'Global']['Coal'])
ax[0,1].set_title('Coal');
ax[0,2].plot(df['Global':'Global']['Year'], df['Global':'Global']['Oil'])
ax[0,2].set_title('Oil');
ax[0,3].plot(df['Global':'Global']['Year'], df['Global':'Global']['Gas'])
ax[0,3].set_title('Gas');
ax[1,0].plot(df['Global':'Global']['Year'], df['Global':'Global']['Cement'])
ax[1,0].set_title('Cement');
ax[1,1].plot(df['Global':'Global']['Year'], df['Global':'Global']['Flaring'])
ax[1,1].set_title('Flaring');
ax[1,2].plot(df['Global':'Global']['Year'], df['Global':'Global']['Other'])
ax[1,2].set_title('Other');
ax[1,3].plot(df['Global':'Global']['Year'], df['Global':'Global']['Per Capita'])
ax[1,3].set_title('Per Capita');

#Graficando valores de México:
fig, bx = plt.subplots(2,4, figsize=(18,8))
fig.suptitle(r'Valores de México' , fontsize=20)
bx[0,0].plot(df['Mexico':'Mexico']['Year'], df['Mexico':'Mexico']['Total'])
bx[0,0].set_title('Total');
bx[0,1].plot(df['Mexico':'Mexico']['Year'], df['Mexico':'Mexico']['Coal'])
bx[0,1].set_title('Coal');
bx[0,2].plot(df['Mexico':'Mexico']['Year'], df['Mexico':'Mexico']['Oil'])
bx[0,2].set_title('Oil');
bx[0,3].plot(df['Mexico':'Mexico']['Year'], df['Mexico':'Mexico']['Gas'])
bx[0,3].set_title('Gas');
bx[1,0].plot(df['Mexico':'Mexico']['Year'], df['Mexico':'Mexico']['Cement'])
bx[1,0].set_title('Cement');
bx[1,1].plot(df['Mexico':'Mexico']['Year'], df['Mexico':'Mexico']['Flaring'])
bx[1,1].set_title('Flaring');
bx[1,2].plot(df['Mexico':'Mexico']['Year'], df['Mexico':'Mexico']['Other'])
bx[1,2].set_title('Other');
bx[1,3].plot(df['Mexico':'Mexico']['Year'], df['Mexico':'Mexico']['Per Capita'])
bx[1,3].set_title('Per Capita');

plt.show()

#Graficando valores G20
G20 = ['Germany','Saudi Arabia','Argentina','Australia','Brazil','Canada','China','USA','France','India','Indonesia','Italy','Japan','United Kingdom','South Korea','Mexico','Russia','South Africa','Turkey']
colores = ['black','grey','lightgray','blue','darkblue','skyblue','cian','red','darkred','green','lightgreen','yellowgreen','darkgreen','yellow','magenta','pink','violet','oragne','brown']
columnas = ['Total','Coal','Oil','Gas','Cement','Flaring','Other','Per Capita']

fig, cx = plt.subplots(8,1, figsize=(10,45))
for k in range (len(columnas)):
  cx[k].set_title(columnas[k], fontsize = 15)
  for l in range (len(G20)):
    cx[k].plot(df[G20[l]:G20[l]]['Year'],df[G20[l]:G20[l]][columnas[k]],label = G20[l])
  cx[k].legend()

plt.show()

#Los tres países que contaminan mas en cada caso
print("A continuación se muestran los tres países que más contaminan en cada caso: \n")
Auxiliar = []
for g in range (len(columnas)):
  print(columnas[g],"\n")
  Auxiliar = []
  for h in range (len(G20)):
    promedio = df[G20[h]:G20[h]][columnas[g]].mean()
    Auxiliar.append(promedio)
  Axuliar2 = pd.Series(data = Auxiliar, index = G20, dtype='float')
  promedios = Axuliar2.dropna() #Aqui se están eliminando los NaNs
  if g == 0:
    mexicototalprom = promedios
  if g == 7:
    mexicopercapitaprom = promedios
  sorted_series = promedios.sort_values(ascending = True)
  y = len(sorted_series)
  print(sorted_series.iloc[y-3:y],"\n")
  
#Porcentaje con el que contribuye México al G20 en total y percapita
print("\nPorcentaje con el que contribuye México al G20 en total y percapita:\n")
contrubuciontotal = (mexicototalprom['Mexico']/mexicototalprom.sum())*100
contribucionpercapita = (mexicopercapitaprom['Mexico']/mexicopercapitaprom.sum())*100
print("México contribuye con un",round(contrubuciontotal,3),"% al Total\n")
print("México contribuye con un",round(contribucionpercapita,3),"% al Per Capita\n")