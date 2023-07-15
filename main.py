g = 9.81

# coefficient of retituation -v_up / v_down
cor = 0.4

xmax = 10

dt = 0.001

x0, y0 = 0, 5
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
        

