import math
import time
from threading import Thread
import tkinter as tk
WIDTH = 2560
HEIGHT = 1600

class MyTurtle():
    def __init__(self):
        self.window = tk.Tk("MyTurtle")
        #   initialize initial coordinates as (0, 0)
        self.x = WIDTH/2
        self.y = HEIGHT/2
        #speed of turtle
        self.speed = 0.1
        #   direction in which the cursor is facing, represented by a vector
        #   initially facing right
        self.dir = [1, 0]
        self.theta  = 0
        #   initial line color is black
        self.line_color = f"#{0:02X}{0:02X}{0:02X}"
        self.line_width = 3
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT)
        #   initial background color = white
        self.BGColor(1, 1, 1)
        self.canvas.pack()
        self.current_distance = 0
        #   initial background color = white
                # self.BGColor(1, 1, 1)
        #   initially is pen is up
        self.pen_down = False

    def Init(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
        if(theta <= 0):
            self.Right(-theta)
        else:
            self.Left(theta)

    def BGColor(self, r, g, b):
        self.BG_COLOR = [int(r*255), int(g*255), int(b*255)]
        bg_color = f"#{self.BG_COLOR[0]:02X}{self.BG_COLOR[1]:02X}{self.BG_COLOR[2]:02X}"
        self.window.configure(bg=bg_color)
        self.canvas.configure(bg=bg_color)

    def find_final(self, curr_x, curr_y, distance):
        final_x = self.dir[0]*distance + curr_x
        final_y = self.dir[1]*distance + curr_y
        return (final_x, final_y)

    def Draw(self, distance):
        self.current_distance = 0
        self.__draw_step(distance)

    def __draw_step(self, distance_to_draw):
        curr_x = self.x
        curr_y = self.y
        while(self.current_distance < distance_to_draw):
            final_x, final_y = self.find_final(curr_x, curr_y, self.speed) 
            if(self.canvas):
                self.canvas.create_line(curr_x, curr_y, final_x, final_y, fill=self.line_color, width=self.line_width) 
            curr_x = final_x
            curr_y = final_y
            self.current_distance += self.speed 
            self.canvas.update()
    def Forward(self, distance):
        #   check if pen is down
        if(self.pen_down):
            self.Draw(distance)
        self.x, self.y = self.find_final(self.x, self.y, distance)
    #   alpha is the angle by which we are rotating

    def Left(self, alpha):
        self.theta = self.theta + alpha
        radians = self.__degrees_to_radians__(self.theta)
        self.dir[0] = math.cos(radians)
        self.dir[1] = math.sin(radians)

    def Right(self, alpha):
        self.theta = self.theta - alpha
        radians = self.__degrees_to_radians__(self.theta)
        self.dir[0] = math.cos(radians)
        self.dir[1] = math.sin(radians)

    def Backward(self, distance):
        if(self.pen_down):
            self.Draw(distance)
        self.x, self.y = self.find_final(self.x, self.y, distance)

    def PenDown(self, isDown):
        self.pen_down = isDown


    def calculate_distance(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1

        squared_distance = dx**2 + dy**2

        distance = math.sqrt(squared_distance)

        return distance

    def GoTo(self, x, y):
        if(self.pen_down):
            distance = self.calculate_distance(self.x, self.y, x, y)
            self.Draw(distance)
        self.x = x
        self.y = y

    def LineColor(self, r, g, b):
        red = int(r * 255)
        blue = int(b * 255)
        green = int(g * 255)
        line_color = f"#{red:02X}{green:02X}{blue:02X}"
        self.line_color = line_color 

    def LineWidth(self, width):
        self.line_width = width
    def Speed(self, speed):
        self.speed = speed

    def ResetPosition(self):
        self.x = 0
        self.y = 0
        self.theta = 0
        self.dir = [0,0]
    def __degrees_to_radians__(self, degrees):
        return degrees * (math.pi / 180)
    def GetWidth(self):
        return WIDTH
    def GetHeight(self):
        return HEIGHT

    def ClearScreen(self):
        self.canvas.delete("all")
    #   destructor
    def mainloop(self):
        self.window.mainloop()

