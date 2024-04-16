# This is a sample Python script.
def generate_pascal_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

def print_pascal_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))

def main():
    n = int(input("Введите количество строк треугольника Паскаля: "))

    # Генерируем треугольник Паскаля и выводим его
    pascal_triangle = generate_pascal_triangle(n)
    print("Треугольник Паскаля:")
    print_pascal_triangle(pascal_triangle)

if __name__ == "__main__":
    main()
    