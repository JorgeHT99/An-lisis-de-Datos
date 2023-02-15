lista1 = []
lista2 = []
lista3 = []
lista4 = []
nombres = []
k = 0
arroba = "@"
punto = "."
auxiliar = 0
auxiliar2 = 0
suma = ""
dominios = []


file = open('correos.csv','r')

for i in range (0,24):
    lista1.append(file.readline())

print(lista1)

for j in lista1:
    lista2.append(j.split('@'))
    
for k in range (0,24): 
    nombres.append(lista2[k][0])

"""print("Lista de nombres: ",end = "\n")
print(nombres)"""

for h in range (0,24):
    lista3.append(lista2[k][1])


for l in lista3:
    lista4.append(l.split('.'))
    
for g in range (0,24):
    dominios.append(lista4[g][0])

##print(lista3)

    
    
        
        
            
        
        
    
    




