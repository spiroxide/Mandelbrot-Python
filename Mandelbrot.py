from math import *

MAX_ITERATIONS = 1000
CUT_OFF = 4


def map_range(f_value, f_start, f_end, t_start, t_end):
    return (t_end - t_start) / (f_end - f_start) * (f_value - f_start) + t_start


def mandelbrot(real, imaginary):
    a = real
    b = imaginary
    i = 0
    while i < MAX_ITERATIONS:
        aa = a * a
        bb = b * b
        ab = a * b

        a = aa - bb + real
        b = 2 * ab + imaginary
        if a * a + b * b > CUT_OFF:
            break
        i += 1
    return i


def main():
    imaginary = 0
    while imaginary < 200:
        real = 0
        while real < 500:
            val = mandelbrot(map_range(real, 0, 500, -3, 3), map_range(imaginary, 0, 200, -3, 3))
            if val <= 0:
                print(' ', end='')
            else:
                print(int(log10(val)), end='')
            real += 1
        print()
        imaginary += 1


main()
