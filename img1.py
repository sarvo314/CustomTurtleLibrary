from myTurtle import MyTurtle as mt

def draw1():
    cursor = mt.MyTurtle()
    
    cursor.BGColor(0, 0, 0)
    
    cursor.LineWidth(2)
    
    r, g, b = 1, 0, 0
    cursor.PenDown(True)
    cursor.Speed(100)
    cursor.Init(cursor.GetWidth()/3.8, cursor.GetHeight()/4, 0)
    cursor.LineColor(0.1, 0.1, 0.1)
    for i in range(255*2):
        if i<255//3:
            g+=3/255
        elif i<255*2//3:
            r-=3/255
        elif i<255:
            b+=3/255
        elif i<255*4//3:
            g-=3/255
        elif i<255*5//3:
            r+=3/255
        else:
            b-=3/255
        cursor.Forward(50 + i)
        cursor.Left(91)
        cursor.LineColor(r, g, b)
    cursor.mainloop()
