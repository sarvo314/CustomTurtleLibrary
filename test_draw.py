from myTurtle import MyTurtle as mt

cursor = mt.MyTurtle()
cursor.Init(250, 250, 0)
cursor.BGColor(0, 0, 0)
cursor.LineColor(1, 1, 1)
cursor.PenDown(False)
cursor.Forward(50)
cursor.Left(90)
cursor.PenDown(True)
cursor.Forward(50)
cursor.Left(90)
cursor.Forward(100)
cursor.Left(90)
cursor.Forward(100)
cursor.Left(90)
cursor.Forward(100)
cursor.Left(90)
cursor.Forward(50)


cursor.mainloop()
