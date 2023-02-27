from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pandas
imagen = Image.open('Full_Moon_Luc_Viatour.jpg') 
im_datos = np.array(imagen)
im_datos.ndim
im_datos.dtype
im_datos.shape
p = imagen.convert('RGBA')
d = np.array(p)
red, green, blue, alpha = d.T
an = (red==0)&(blue==0)&(green==0)
d[..., :-1][an.T] = (0,250,0)
imf=Image.fromarray(d)
fig,ax = plt.subplots(figsize=(10,10))
ax.imshow(imf)