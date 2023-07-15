g = 9.81

# coefficient of retituation -v_up / v_down
cor = 0.4

xmax = 10

dt = 0.001

def get_position(t=0):
    x, y, vx ,vy = 0 ,0, 0, 0
    while x < xmax:
        t += dt
        x = vx * dt
        y = vy * dt
        vy -= g * dt
