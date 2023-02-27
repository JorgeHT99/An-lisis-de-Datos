cont = 0
SUMA = 0
SUMA2 = 0
auxiliar = 0
with open('DS.txt') as myfile:
    renglones = sum(1 for line in myfile)

textoce = []
textose = []
textoss = []
PR = []
carunic = []

f = open('DS.txt','r')

for i in range(0,renglones):
    textoce.append(f.readline())
    
for j in textoce:
    if j != "\n":
        cont = cont + 1
        textose.append(j)
    
print("\n En el texto hay",cont,"parrafos\n")

for l in range (len(textose)):
    cont2 = 0
    for m in textose[l]:
        if m == " ":
            cont2 = cont2 + 1
    SUMA = SUMA + (cont2 + 1)
    
print("\n En el texto hay",SUMA,"palabras\n")

#---------------------------------------------------------------------

for g in textose:
    a = g.split()
    for y in a:
        b = y.lower()
        textoss.append(b)
        
for r in range(len(textoss)):
    if textoss[r] not in PR:
        PR.append(textoss[r])
    
print("\n En el texto hay",len(PR),"palabras diferentes\n")

for s in textoss:
    SUMA2 = SUMA2 + len(s)
    
print("\n En el texto hay",SUMA2,"caracteres\n")

for w in textoss:
    for q in w:
        if q not in carunic:
            carunic.append(q)    

print("\n En el texto hay",len(carunic),"caracteres unicos\n")
        
        
    
    
            
        






    
    
    