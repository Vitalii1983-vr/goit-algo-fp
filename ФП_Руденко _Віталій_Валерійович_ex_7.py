import random
import matplotlib.pyplot as plt
import pandas as pd

# Функція для імітації кидків кубиків і підрахунку ймовірностей сум
def monte_carlo_simulation(num_simulations):
    sums = [0] * 13  # Ініціалізуємо список для підрахунку кожної суми від 2 до 12

    for _ in range(num_simulations):
        roll1 = random.randint(1, 6)  # Кидок першого кубика
        roll2 = random.randint(1, 6)  # Кидок другого кубика
        sums[roll1 + roll2] += 1  # Збільшуємо лічильник відповідної суми

    probabilities = [(i, sums[i] / num_simulations) for i in range(2, 13)]  # Обчислюємо ймовірності
    return probabilities

# Функція для побудови таблиці ймовірностей
def create_probability_table(probabilities):
    df = pd.DataFrame(probabilities, columns=['Сума', 'Ймовірність'])
    df['Ймовірність'] = df['Ймовірність'].apply(lambda x: f"{x:.2%} ({int(x * num_simulations)}/{num_simulations})")
    return df

# Функція для побудови графіку ймовірностей
def plot_probabilities(probabilities):
    sums, probs = zip(*probabilities)
    plt.bar(sums, probs, color='skyblue')
    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.show()

# Кількість імітацій
num_simulations = 100000

# Виконуємо симуляцію
probabilities = monte_carlo_simulation(num_simulations)

# Створюємо таблицю ймовірностей
probability_table = create_probability_table(probabilities)
print(probability_table)

# Будуємо графік ймовірностей
plot_probabilities(probabilities)
