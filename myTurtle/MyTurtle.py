import tkinter as tk
class MyTurtle():
    def __init__(self):
        self.window = tk.Tk()
        #   initialize initial coordinates as (0, 0)
        self.x = 0
        self.y = 0
        #direction in which the cursor is facing
        self.dir = 0
        self.BG_COLOR = [255, 255, 255]

    def Init(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
        #   Set bg color
    def BGColor(self, r, g, b):
        self.BG_COLOR = [r, g, b]
    def Forward(self, distance):
        pass
    def __del__(self):
        self.window.mainloop()

