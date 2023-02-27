from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pandas
i = Image.open('Full_Moon_Luc_Viatour.jpg') 
r, g, b = i.split()
nula = r.point(lambda x: 0)
roja = Image.merge("RGB", (nula, g, b))
verde = Image.merge("RGB", (r, nula, b))
azul = Image.merge("RGB", (r, g, nula))
fig,ax1 = plt.subplots(figsize=(5,5))
ax1.imshow(roja)
fig,ax2 = plt.subplots(figsize=(5,5))
ax2.imshow(verde)
fig,ax3 = plt.subplots(figsize=(5,5))
ax3.imshow(azul)
plt.show()