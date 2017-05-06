#!/usr/bin/env python3

import sys
import time
import canvas
import matrix

def main():
    P = [[40],
         [40]]
    V0 = [[30],
          [30]]
    V1 = [[40],
          [70]]
    V2 = [[50],
          [30]]
    points = [V0, V1, V2]
    aspect_correct = [[1, 0],
                      [0, 4/7]]
    home = "\N{escape}[H"
    wakeup_time = time.time()
    print(home + "\N{escape}[J\N{escape}[?25l")
    t = 0
    try:
        while True:
            kanvas = canvas.Canvas()
            rot = matrix.rotate_2D(t * 0.5)
            r_points = [] 
            for point in points:
                C = matrix.sub(point, P)
                C = matrix.mult(rot, C)
                C = matrix.add(P, C)
                C = matrix.mult(aspect_correct, C)
                r_points.append(C)
            t += 1
            kanvas.triangle(round(r_points[0][0][0]),
                            round(r_points[0][1][0]),
                            round(r_points[1][0][0]),
                            round(r_points[1][1][0]),
                            round(r_points[2][0][0]),
                            round(r_points[2][1][0]))
            image = home + kanvas.get_image()
            print(image)
            wakeup_time += 0.05
            time.sleep(max(0, wakeup_time - time.time()))
    finally:
        print(home + "\N{escape}[J \N{escape}[?25h")

def round(x):
    return int(x + 0.5)

if __name__ == "__main__":
    main()


