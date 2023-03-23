import numpy as np

auxiliar1 = 0
auxiliar2 = 0

#Ejercicio 1 

arreglo1 = np.arange(1,65,1)
A = np.reshape(arreglo1,(8,8))
print(A,"\n")

#Ejercicio 2

B = np.transpose(A)
print(B,"\n")

for i in range(len(B)):
    for j in range(len(B)):
        auxiliar1 = str(B[i][j])
        auxiliar2 = auxiliar1.find('3')
        if auxiliar2 != -1:
            B[i][j] = -99
    
print(B,"\n")

#Ejercicio 3

arreglo2 = np.arange(0.4,0.8,0.01)
C = np.reshape(arreglo2,(8,5))

print(C,"\n")

#Uniendo las matrices C Y B
unionCB = np.append(C,B,axis=1)

print(unionCB,"\n")

#Promedio de cada columna
vp = np.array([])
for k in range(13):
    promedio = np.mean(unionCB[:,k])
    vp = np.append(vp,promedio)
MP = np.vstack([unionCB,vp])

print(MP,"\n")

#Número máximo en cada fila
vm = np.array([])
for l in range(9):
    valormaximo = max(MP[l,:])
    vm = np.append(vm,valormaximo)

MF = np.append(MP,np.array([vm]).transpose(),axis=1)

print(MF)

#Guardando en un archivo
np.savetxt('matrizfinal.txt',MF)





