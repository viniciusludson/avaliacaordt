#importando a biblioteca matplotlib
import matplotlib.pyplot as plt #para gerar gráficos
import numpy as np
'''

x= np.linspace(6, 0, 100)  #linspace é espaço de linha
y= -x**2 +4*x+2

#fazer um gráfico com concavidade para baixo
plt.plot(x, y)
plt.title("Meu primeiro gráfico! ")
plt.xlabel("Eixo X ")
plt.ylabel("Eixo Y ")
plt.grid(True)
plt.show() #para o gráfico aparecer
'''
#fazer um gráfico com a função cos seno
import math
x=[]
y=[]
#sin: seno,cos: coseno

for angulo in range(0, 361):
    x.append(angulo)
    y.append(math.cos(math.radians(angulo)))
plt.plot(x, y)
plt.title("Meu primeiro gráfico! ")
plt.xlabel("Eixo X ")
plt.ylabel("Eixo Y ")
plt.grid(True)
plt.show()