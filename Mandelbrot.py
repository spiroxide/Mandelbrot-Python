from numba import jit
import PIL.Image

WIDTH = 256
HEIGHT = 256

MAX_ITERATIONS = 128
CUT_OFF = 4


@jit
def map_range(f_val, f_start, f_end, t_start, t_end):
    return (t_end - t_start) / (f_end - f_start) * (f_val - f_start) + t_start


@jit
def mandelbrot_value(real, imaginary):
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


@jit
def mandelbrot_image():
    for i in range(0, 256, 4):
        mandelbrot = []
        for y in range(HEIGHT):
            for x in range(WIDTH):
                # val = mandelbrot_value(map_range(x, 0, WIDTH, -2.5, 1.5), map_range(y, 0, HEIGHT, -2, 2))
                r = int() % 256
                g = int() % 256
                b = int() % 256
                mandelbrot.append((r, g, b))
        image = PIL.Image.new('RGB', (WIDTH, HEIGHT))
        image.putdata(mandelbrot)
        image.save("mandelbrot/mandelbrot" + str(i) + ".gif")


@jit
def main():
    mandelbrot_image()


main()
