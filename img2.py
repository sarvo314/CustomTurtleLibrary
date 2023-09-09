import random
from myTurtle import MyTurtle as mt
def draw2():
    t = mt.MyTurtle()
    
    t.BGColor(0, 0, 0)
    
    t.Speed(10)
    t.LineWidth(2)
    t.LineColor(1, 1, 1)
    
    t.Init(t.GetWidth()/4, t.GetHeight()/3, 270)
    
    colors = ["red", "blue", "green", "gray", "orange", "black"]
    t.PenDown(True)
    r = 1
    g = 1
    b = 1
    for i in range(0, 1000):
        t.Forward(20+i/10)
        t.Left(30 - (i/10)/1.5)
        r = random.random()
        g = random.random()
        b = random.random()
    
        t.LineColor(r, g, b)
    
    
    t.mainloop()
