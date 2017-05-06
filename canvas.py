#!/usr/bin/env python3

import sys

def main():
    canvas = Canvas()
    do_art(canvas)
    canvas.print()

def do_art(canvas):
    canvas.box(20, 50, 10, 5)
    canvas.line(4, 10, 27, 21)
    canvas.line(35, 46, 40, 23)
    canvas.triangle(3, 6, 6, 9, 9, 3)

class Canvas:
    def __init__(self):
        self.area = [ ["\N{FULL BLOCK}"] * 75 for row in range(60) ]

    def print(self):
        print(self.get_image())

    def get_image(self):
        return "\n".join([ "".join(row) for row in self.area])
        
    def box(self, x, y, width, height):
        for yy in range(y, y + height):
            for xx in range(x, x + width):
                self.dab(xx, yy)

    def oval(self, x, y, width, height):
        a = (width - 1) / 2
        b = (height - 1) / 2
        x0 = x + a
        y0 = y + b
        for yy in range(y, y + height):
            for xx in range(x, x + width):
                if ((xx - x0) / a)**2 + ((yy - y0) / b)**2 <= 1:
                    self.dab(xx, yy)

    def triangle(self, x1, y1, x2, y2, x3, y3):
        self.line(x1, y1, x2, y2)
        self.line(x2, y2, x3, y3)
        self.line(x3, y3, x1, y1)

    def line(self, xb, yb, xe, ye):
        if abs(xe - xb) > abs(ye - yb):
            for x in range(xb, xe, step(xe - xb)):
                y = int(yb + (x - xb) * (ye - yb) / (xe - xb) + 0.5)
                self.dab(x, y)
        else:
            for y in range(yb, ye, step(ye - yb)):
                x = int(xb + (y - yb) * (xe - xb) / (ye - yb) + 0.5)
                self.dab(x, y)

    def dab(self, x, y):
        self.area[-y - 1][x] = " "

def step(x):
    if x >= 0:
        return 1
    return -1
    
if __name__ == "__main__":
    main()


