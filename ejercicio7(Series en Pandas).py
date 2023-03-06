import numpy as np
import pandas as pd

#Parte1
numeros = []
l = []
letras = list(map(chr, range(ord('a'), ord('z')+1)))

for i in range (10,len(letras)+10):
  if i >= 10:
    numeros.append(i)

S1 = pd.Series(data=numeros, index=letras, dtype='float')
print(S1,'\n')

#Parte2
letrasinvertidas= list(reversed(letras))

S2 = pd.Series(data=letrasinvertidas, index=numeros, dtype='str')
print(S2,"\n")

#Parte3

for i in range (27,32+1):
  print(S2[i])
print("\n")
for j in range (3,9):
  print(S1.iloc[j])
