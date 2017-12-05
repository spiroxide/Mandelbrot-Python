from numba import jit
import PIL.Image

WIDTH = 512
HEIGHT = 512

MAX_ITERATIONS = 128


@jit
def map_range(f_val, f_start, f_end, t_start, t_end):
    return (t_end - t_start) / (f_end - f_start) * (f_val - f_start) + t_start


@jit
def mandelbrot_value(real, imaginary):
    a = real
    b = imaginary

    i = 0
    while i < MAX_ITERATIONS:
        ab = a * b

        a = a * a - b * b + real
        b = 2 * ab + imaginary

        if a * a + b * b > 4:
            break
        i += 1
    return i


@jit
def mandelbrot_image():
    mandelbrot = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            val = mandelbrot_value(map_range(x, 0, WIDTH, -2.5, 1.5), map_range(y, 0, WIDTH, -2, 2))
            r = int(val) % 256
            g = int(val) % 256
            b = int(val) % 256
            mandelbrot.append((r, g, b))
    image = PIL.Image.new('RGB', (WIDTH, HEIGHT))
    image.putdata(mandelbrot)
    image.save("mandelbrot.png")


@jit
def main():
    mandelbrot_image()


main()
