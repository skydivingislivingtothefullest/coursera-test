"""Display a spinning doughnut in the terminal."""

import math
import sys
import time

# Angles for rotation around the X and Z axes
A = 0.0
B = 0.0

while True:
    # Clear the screen and move cursor to top left
    sys.stdout.write("\x1b[H")

    z = [0] * 1760
    b = [" "] * 1760

    for j in [i * 0.07 for i in range(0, 90)]:
        for i in [i * 0.02 for i in range(0, 628)]:
            c = math.sin(i)
            l = math.cos(i)
            d = math.cos(j)
            f = math.sin(j)
            g = math.cos(A)
            e = math.sin(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e

            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 0 <= y < 22 and 0 <= x < 80 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[max(N, 0)]

    sys.stdout.write("".join(b))
    sys.stdout.flush()
    A += 0.04
    B += 0.02
    time.sleep(0.03)

