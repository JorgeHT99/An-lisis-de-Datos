import requests
import pandas as pd

#Buscando articulos de Wikipedia que contengan la palabra "astro":
buscar_en_titulo = 'astro'
endpoint = 'https://es.wikipedia.org/w/rest.php/v1/search/title'
params = {
            'q' : buscar_en_titulo,
            'limit': 20
        }
request_wiki = requests.get(endpoint, params=params)
request_wiki.status_code
df = pd.json_normalize(request_wiki.json()['pages'])
df

#Extrayendo los resúmenes:
titulos = df['title'].to_list()
paginas = df['id'].to_list()
LR = []
DR = {}

for k, l in zip(paginas, titulos):
    url = f'https://es.wikipedia.org/w/api.php?action=query&format=json&pageids={k}&prop=extracts&explaintext=True&exintro=True,'
    request_wiki = requests.get(url)
    request_wiki.status_code
    request_wiki.json()['query']['pages']
    data = pd.json_normalize(request_wiki.json()['query']['pages'])
    extract = data.iloc[:, 3][0]
    LR.append(extract)

DR = { 'title' : titulos, 'page_id' : paginas, 'extract' : LR}
df2 = pd.DataFrame(DR)
df2

#Aqui verificamos si los resúmenes contienen la palabra "ciencia" o "fisica"
verificador = []
for index, row in df2.iterrows():
    if 'ciencia' in row['extract'] or 'física' in row['extract']:
        verificador.append(1)
    else:
        verificador.append(0)
       
verificador

#Ahora agregamos la lista anterior al dataframe
verificadorp = pd.Series(verificador)
df3 = pd.concat([df2, verificadorp.rename('contiene_palabra')], axis=1)

print(df3)