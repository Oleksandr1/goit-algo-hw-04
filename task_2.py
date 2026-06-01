"""
Завдання 2. Фрактал «сніжинка Коха».

Програма рекурсивно будує сніжинку Коха за допомогою модуля turtle.
Користувач вказує рівень рекурсії з консолі.

Запуск:
    python task_2.py
"""

import turtle


def koch_curve(t: turtle.Turtle, length: float, level: int) -> None:
    """Рекурсивно малює один сегмент кривої Коха."""
    if level == 0:
        t.forward(length)
        return

    length /= 3
    koch_curve(t, length, level - 1)
    t.left(60)
    koch_curve(t, length, level - 1)
    t.right(120)
    koch_curve(t, length, level - 1)
    t.left(60)
    koch_curve(t, length, level - 1)


def draw_snowflake(level: int, size: float = 300) -> None:
    """Малює замкнену сніжинку Коха з трьох кривих."""
    screen = turtle.Screen()
    screen.title(f"Сніжинка Коха — рівень {level}")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.color("navy")
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, size, level)
        t.right(120)

    turtle.done()


def main() -> None:
    raw = input("Вкажіть рівень рекурсії (рекомендовано 0–5): ").strip()
    try:
        level = int(raw)
        if level < 0:
            raise ValueError
    except ValueError:
        print("Потрібне ціле невід'ємне число.")
        return

    draw_snowflake(level)


if __name__ == "__main__":
    main()
