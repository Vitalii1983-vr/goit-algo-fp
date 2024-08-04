import turtle
import math

# Функція для малювання дерева Піфагора
def draw_pythagoras_tree(t, branch_length, angle, depth):
    if depth == 0:
        return

    # Малюємо гілку
    t.forward(branch_length)

    # Поворот для малювання правої гілки
    t.left(angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, angle, depth - 1)

    # Поворот назад і малювання лівої гілки
    t.right(2 * angle)
    draw_pythagoras_tree(t, branch_length * math.sqrt(2) / 2, angle, depth - 1)

    # Повертаємося до початкової позиції
    t.left(angle)
    t.backward(branch_length)

# Основна функція для налаштування графіки та запуску малювання
def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Pythagoras Tree")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)

    # Запит користувача на рівень рекурсії
    depth = int(input("Введіть рівень рекурсії: "))

    # Початкові параметри
    branch_length = 100
    angle = 45

    # Початок малювання
    draw_pythagoras_tree(t, branch_length, angle, depth)

    # Завершення малювання
    turtle.done()

if __name__ == "__main__":
    main()
