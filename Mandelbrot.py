from string import *

WIDTH = 960
HEIGHT = 540
ASCI = digits + ascii_letters + punctuation
MAX_ITERATIONS = len(ASCI) - 1
CUT_OFF = 4


def map_range(f_val, f_range, t_range):
    """
    returns the value of f_val from f_range converted to t_range
    :param f_val: value to convert from
    :param f_range: range to convert from
    :param t_range: range to convert to
    :return: the value of f_val from f_range converted to t_range
    """
    return (t_range[len(t_range) - 1] - t_range[0]) / (f_range[len(f_range) - 1] - f_range[0]) * (f_val - f_range[0]) + t_range[0]


def mandelbrot(real, imaginary):
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


def main():
    file = open("C:\\Users\\Erich Ostendarp\\Workspace\\PyCharmProjects\\Mandelbrot\\mandelbrot.txt", 'w')
    for imaginary in range(HEIGHT):
        for real in range(WIDTH):
            val = mandelbrot(map_range(real, range(WIDTH), range(-2, 3)), map_range(imaginary, range(HEIGHT), range(-2, 3)))
            if val <= 0:
                file.write(' ')
            else:
                file.write(ASCI[val])
        file.write('\n')
    file.close()


main()
