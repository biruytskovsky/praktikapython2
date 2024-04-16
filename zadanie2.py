def draw_sierpinski_triangle(n, x, y, size):
    if n == 0:
        # Выводим треугольник по заданным координатам и размеру
        for i in range(size):
            print(" " * (size - i - 1) + "*" * (2 * i + 1))
    else:
        # Рекурсивно вызываем функцию для каждого из трех подтреугольников
        draw_sierpinski_triangle(n - 1, x, y, size // 2)  # Левый подтреугольник
        draw_sierpinski_triangle(n - 1, x + size // 2, y, size // 2)  # Правый подтреугольник
        draw_sierpinski_triangle(n - 1, x + size // 4, y + size // 2, size // 2)  # Верхний подтреугольник


def main():
    # Вводим количество итераций для построения треугольника Серпинского
    iterations = int(input("Введите количество итераций (минимум 3): "))

    if iterations < 3:
        print("Ошибка: Количество итераций должно быть не менее 3.")
        return

    # Размер исходного треугольника
    size = 2 ** (iterations - 1) * 3

    # Начальные координаты для вывода треугольника
    x = 0
    y = 0

    # Выводим треугольник Серпинского
    draw_sierpinski_triangle(iterations, x, y, size)


if __name__ == "__main__":
    main()