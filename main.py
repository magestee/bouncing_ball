import matplotlib.pyplot as plt
import matplotlib.animation as animation

g = 0

# coefficient of retituation -v_up / v_down
cor = 0.6

xmax = 10

dt = 0.005

x0, y0 = 0, 3
vx0, vy0 = 1, 0

def get_position(t=0):
    x, y, vx ,vy = x0 ,y0, vx0, vy0
    while x < xmax:
        t += dt
        x += vx * dt
        y += vy * dt
        vy -= g * dt
        if y < 0:
            y = 0
            vy = -vy * cor
        yield x, y


def init():
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, 5)
    line.set_data(xdata, ydata)
    ball.set_center((x0, y0))
    return line, ball

def animate(pos):
    x, y = pos
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    ball.set_center((x,y))
    return line, ball

fig, ax = plt.subplots()
ax.set_aspect('equal')

line, = ax.plot([], [], lw=2)
ball = plt.Circle((x0, y0), 0.08)
ax.add_patch(ball)
xdata, ydata = [], []

interval = 1000*dt

ani = animation.FuncAnimation(fig,
                              animate,
                              get_position,
                              blit = True,
                              repeat = False,
                              interval = interval,
                              init_func = init
                              )

plt.show()