# goit-algo-fp

# Аналіз результатів моделювання кидання кубиків методом Монте-Карло (Завдання 7)

## Вступ
Це дослідження має на меті проаналізувати результати моделювання кидання двох кубиків за допомогою методу Монте-Карло та порівняти їх з аналітичними розрахунками ймовірностей сум.

## Опис симуляції
Було виконано моделювання 100000 кидків двох кубиків. Для кожного кидка обчислювалася сума чисел на гранях обох кубиків, після чого підраховувалась частота появи кожної можливої суми від 2 до 12.

## Аналітичні розрахунки
Аналітичні ймовірності для кожної суми від 2 до 12 були обчислені на основі теоретичного розподілу ймовірностей:

| Сума | Імовірність (аналітична) |
|------|-------------------------|
| 2    | 2.78% (1/36)            |
| 3    | 5.56% (2/36)            |
| 4    | 8.33% (3/36)            |
| 5    | 11.11% (4/36)           |
| 6    | 13.89% (5/36)           |
| 7    | 16.67% (6/36)           |
| 8    | 13.89% (5/36)           |
| 9    | 11.11% (4/36)           |
| 10   | 8.33% (3/36)            |
| 11   | 5.56% (2/36)            |
| 12   | 2.78% (1/36)            |

## Результати симуляції
Результати моделювання методом Монте-Карло були наступними:

| Сума | Імовірність (Монте-Карло) |
|------|---------------------------|
| 2    | 2.75%                     |
| 3    | 5.50%                     |
| 4    | 8.25%                     |
| 5    | 11.02%                    |
| 6    | 13.91%                    |
| 7    | 16.70%                    |
| 8    | 13.87%                    |
| 9    | 11.05%                    |
| 10   | 8.36%                     |
| 11   | 5.48%                     |
| 12   | 2.81%                     |

## Висновки
Результати, отримані за допомогою методу Монте-Карло, дуже близькі до аналітичних розрахунків. Відхилення для кожної суми не перевищує 0.5%, що підтверджує правильність проведеного моделювання. Метод Монте-Карло успішно відтворює теоретичний розподіл ймовірностей для сум чисел при киданні двох кубиків.
