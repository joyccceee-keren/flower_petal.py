import turtle, math

def bez(p0 , p1, p2, n=20):
    pts = []
    for i in range(n+1):
        f = i / n
        x = (1-f)**2*p0[0] + 2*(1-f)*f*p1[0] + f**2*p2[0]
        y = (1-f)**2*p0[1] + 2*(1-f)*f*p1[1] + f**2*p2[1]
        pts.append((x,y))
    return pts

def petal(ang, L, w, s):
    d = (math.cos(ang),math.sin(ang))
    p = (-math.sin(ang),math.cos(ang))
    tip = (d[0]*L*s, d[1]*L*s)
    c1 = (d[0]*L*.55*s + p[0]*w*s,
          d[1]*L*.55*s + p[1]*w*s)
    cr =  (d[0]*L*.55*s - p[0]*w*s,
          d[1]*L*.55*s - p[1]*w*s) 
    pts = bez((0, 0), c1, tip) + bez(tip, cr , (0, 0))
    return pts

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")

# Create a turtle to draw the flower
t = turtle.Turtle()
t.speed(0)
t.color("yellow", "red")
t.hideturtle()

# Draw 12 petals around the center
num_petals = 12
for i in range(num_petals):
    ang = i * 2 * math.pi / num_petals
    pts = petal(ang, 180, 45, 1.0)
    
    t.penup()
    t.goto(pts[0])
    t.pendown()
    t.begin_fill()
    for pt in pts:
        t.goto(pt)
    t.end_fill()

# Keep the window open
turtle.done()

