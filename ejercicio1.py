f = open('correos.csv','r')
a = 0
b = 0
lista1 = []
nombres = []
qdom = []
dominios = []
dominiosnr = []
Nvocales = []
vocales = ["a","e","i","o","u"]


for i in range (0,24):
    lista1.append(f.readline())

## Estos son los nombres:
for j in range (0,24):
    a = lista1[j].split('@')
    nombres.append(a[0])
    qdom.append(a[1])
    
for k in range (0,24):
    b = qdom[k].split('.')
    dominios.append(b[0])
    
for l in range (len(dominios)):
    if dominios[l] not in dominiosnr:
        dominiosnr.append(dominios[l])

print("La lista de los dominios es:\n")
print(dominiosnr,"\n")

print("La lista de los nombres es:\n")
print(nombres)

for w in range (len(nombres)):
    contador = 0
    for v in range(len(nombres[w])):
        if nombres[w][v] in vocales: 
            contador = contador + 1
    Nvocales.append(contador)
    
print("Vocales por nombre:\n")
print(Nvocales)
    
   
    