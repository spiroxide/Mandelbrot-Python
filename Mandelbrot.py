from numba import jit
import PIL.Image

WIDTH = 1080
HEIGHT = 1080

x_translate = .5
y_translate = 0
zoom = 1

MAX_ITERATIONS = 25
CUT_OFF = 4

COLOR_CAP = 255
RAIN_RINGS = 7
CHUNK = MAX_ITERATIONS / RAIN_RINGS

RED = (COLOR_CAP, 0, 0)
ORANGE = (COLOR_CAP, COLOR_CAP / 2, 0)
YELLOW = (COLOR_CAP, COLOR_CAP, 0)
GREEN = (0, COLOR_CAP, 0)
BLUE = (0, 0, COLOR_CAP)
INDIGO = (COLOR_CAP / 3, 0, COLOR_CAP / 2)
VIOLET = (COLOR_CAP / 2, 0, COLOR_CAP)
BLACK = (0, 0, 0)


@jit
def map_range(f_val, f_start, f_end, t_start, t_end):
    return (t_end - t_start) / (f_end - f_start) * (f_val - f_start) + t_start


@jit
def mandelbrot_value(real, imaginary):
    """
    returns the number of iterations it takes to reach the CUT_OFF
    :param real: real portion of a complex number
    :param imaginary: imaginary portion of a complex number
    :return: number of iterations it took to reach the CUT_OFF
    """
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
def color_fade(start, end, i, scope):
    """

    :param start:
    :param end:
    :param i:
    :param scope:
    :return:
    """
    return int(start[0] + (i * (end[0] - start[0]) / scope)), \
           int(start[1] + (i * (end[1] - start[1]) / scope)), \
           int(start[2] + (i * (end[2] - start[2]) / scope))


@jit
def mandelbrot_image():
    """

    :return:
    """
    mandelbrot = []
    for imaginary in range(HEIGHT):
        for real in range(WIDTH):
            val = mandelbrot_value(map_range(real, 0, WIDTH, -2 / zoom - x_translate, 2 / zoom - x_translate),
                                   map_range(imaginary, 0, HEIGHT, -2 / zoom - y_translate, 2 / zoom - y_translate))
            if val <= CHUNK:
                mandelbrot.append(color_fade(RED, ORANGE, val, CHUNK))  # Red to Orange
            elif val <= 2 * CHUNK:
                mandelbrot.append(color_fade(ORANGE, YELLOW, val - CHUNK, CHUNK))  # Orange to Yellow
            elif val <= 3 * CHUNK:
                mandelbrot.append(color_fade(YELLOW, GREEN, val - 2 * CHUNK, CHUNK))  # Yellow to Green
            elif val <= 4 * CHUNK:
                mandelbrot.append(color_fade(GREEN, BLUE, val - 3 * CHUNK, CHUNK))  # Green to Blue
            elif val <= 5 * CHUNK:
                mandelbrot.append(color_fade(BLUE, INDIGO, val - 4 * CHUNK, CHUNK))  # Blue to Indigo
            elif val <= 6 * CHUNK:
                mandelbrot.append(color_fade(INDIGO, VIOLET, val - 5 * CHUNK, CHUNK))  # Indigo to Violet
            elif val <= 7 * CHUNK:
                mandelbrot.append(color_fade(VIOLET, BLACK, val - 6 * CHUNK, CHUNK))  # Violet to Black
    image = PIL.Image.new('RGB', (WIDTH, HEIGHT))
    image.putdata(mandelbrot)
    image.save("mandelbrot.gif")


# x_current = -1
# y_current = -1
#
#
# def left_press(event):
#     """
#
#     :param event:
#     :return:
#     """
#     global x_current, y_current
#     x_current = event.x
#     y_current = event.y
#
#
# def left_release(event):
#     """
#
#     :param event:
#     :return:
#     """
#     global x_translate, y_translate
#     x_translate += (event.x - x_current) / zoom
#     y_translate += (event.y - y_current) / zoom
#
#
# def mouse_wheel(event):
#     """
#
#     :param event:
#     :return:
#     """
#     global zoom
#     zoom += event.delta / 1200


def main():
    mandelbrot_image()
    # root = Tk()
    # root.title("Mandelbrot")
    # root.bind_all("<Button-1>", left_press)
    # root.bind_all("<ButtonRelease-1>", left_release)
    # root.bind_all("<MouseWheel>", mouse_wheel)
    # image = PhotoImage(file="mandelbrot.gif")
    # label = Label(root, image=image)
    # label.pack()
    #
    # root.mainloop()


main()
