import math as m
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import matplotlib.style as mpstyle
import numpy as np
from scipy.integrate import solve_ivp

#mpstyle init
mpstyle.use('fast')

#inp values
L=float(input("Enter Effective Length of Pendulum: "))
g=float(input("Enter Acc. due to Gravity: "))
theta0=np.deg2rad(30)
duration=int(input("Enter Video Length: "))
fps=30

#calc of time period
T=2*m.pi*m.sqrt(L/g)
print("Time Period of the Pendulum is", T ,"seconds")  
t = np.linspace(0, duration, fps * duration)
theta = theta0 * np.cos(np.sqrt(g/L) * t)


#animate pendulum
x = L*np.sin(theta)
y = -L*np.cos(theta)


fig, ax = plt.subplots()
ax.set_xlim(-L-0.2, L+0.2)
ax.set_ylim(-L-0.2, L+0.2)
line, = ax.plot(x, y, 'ro-', lw=2 , color='black')

def animate(i):
    line.set_data([0, x[i]], [0, y[i]])


anim = animation.FuncAnimation(fig, animate, frames=len(t), repeat='True')
ffmpeg_writer = animation.FFMpegWriter(fps=30)
anim.save(filename='simplependulum1.gif', writer='ffmpeg', fps=30)
plt.show()