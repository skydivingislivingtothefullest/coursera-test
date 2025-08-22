"""Display a spinning ASCII doughnut in the terminal."""

import math
import sys
import time

# Rotation angles for the animation
A = 0.0
B = 0.0

while True:
    z = [0] * 1760  # z-buffer
    b = [" "] * 1760  # output buffer

    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            # Convert loop indices to radians
            j_r = j / 100
            i_r = i / 100

            c = math.sin(i_r)
            d = math.cos(j_r)
            e = math.sin(A)
            f = math.sin(j_r)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i_r)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e

            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = x + 80 * y
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 0 <= y < 22 and 0 <= x < 80 and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[max(N, 0)]

    # Move cursor to top-left and render the frame with newlines
    sys.stdout.write("\x1b[H")
    for k in range(1760):
        sys.stdout.write(b[k] if k % 80 else "\n")
    sys.stdout.flush()

    A += 0.04
    B += 0.02
    time.sleep(0.03)

