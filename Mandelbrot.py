from numba import jit
import PIL.Image

WIDTH = 512
HEIGHT = 512

MAX_ITERATIONS = 128


@jit
def map_range(f_val, f_start, f_end, t_start, t_end):
    return (t_end - t_start) / (f_end - f_start) * (f_val - f_start) + t_start


@jit
def mandelbrot_value(cmplx, dim):
    c = cmplx
    for i in range(MAX_ITERATIONS):
        if abs(cmplx) > 2:
            return i
        cmplx = cmplx ** dim + c
    return MAX_ITERATIONS


@jit
def mandelbrot_image():
    for i in range(1, 113, 1):
        mandelbrot = []
        for y in range(HEIGHT):
            for x in range(WIDTH):
                val = mandelbrot_value(complex(map_range(x, 0, WIDTH, -2, 2), map_range(y, 0, HEIGHT, -2, 2)), map_range(i, 1, 113, 0, 4))
                r = int((val * abs(map_range(x, 0, WIDTH, 0, 256))) % 256)
                g = int((val * abs(map_range(y, 0, HEIGHT, 0, 256))) % 256)
                b = int((2 * val * i) % 256)
                mandelbrot.append((r, g, b))
        image = PIL.Image.new('RGB', (WIDTH, HEIGHT))
        image.putdata(mandelbrot)
        image.save("images/mandelbrot" + str(i) + ".png")


@jit
def main():
    mandelbrot_image()


main()
