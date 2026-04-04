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
thetadot0=0


#calc of time period
T=2*m.pi*m.sqrt(L/g)
print("Time Period of the Pendulum is", T ,"seconds")  



#diff. eq
def pendulum_ODE(t, y):
    return(y[1], -g*np.sin(y[0])/L)

#solve
sol=solve_ivp(pendulum_ODE, [0,5], (theta0, thetadot0),
    t_eval=np.linspace(0,5,30*5))

#output of solve
theta=sol.y[0]
thetadot=sol.y[1]
t=sol.t
nframes = len(t)

#rad to deg
thetad=np.rad2deg(sol.y[0])
thetadotd=np.rad2deg(sol.y[1])

# theta was calculated as sol.y[0]
x = L * np.sin(theta)
y = -L * np.cos(theta) # Negative because the pendulum hangs down

fig, ax = plt.subplots()
ax.set_aspect('equal') # Keep the circle from looking like an oval
ax.set_xlim(-L-0.2, L+0.2)
ax.set_ylim(-L-0.2, 0.2)

# Create the parts of the pendulum
line, = ax.plot([], [], 'o-', lw=2, color='blue') 

def init():
    line.set_data([], [])
    return line,

def animate(i):
    # Set the line from the origin (0,0) to the current (x, y)
    line.set_data([0, x[i]], [0, y[i]])
    return line,

# interval=1000/30 means 33.3ms per frame, matching your 30fps data
anim = animation.FuncAnimation(fig, animate, init_func=init, 
                               frames=len(t), interval=1000/30, blit=True)

# To save correctly at the right speed
anim.save(filename='simple_pendulum.gif', writer='ffmpeg', fps=30)
plt.show()