# Визначаємо вхідні дані
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 100

# Функція жадібного алгоритму
def greedy_algorithm(items, budget):
    # Створюємо список страв з їхніми характеристиками
    item_list = [(name, details['cost'], details['calories']) for name, details in items.items()]
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    item_list.sort(key=lambda x: x[2] / x[1], reverse=True)

    total_calories = 0
    selected_items = []

    # Проходимо по відсортованому списку і додаємо страви, поки бюджет дозволяє
    for name, cost, calories in item_list:
        if budget >= cost:
            budget -= cost
            total_calories += calories
            selected_items.append(name)

    return selected_items, total_calories

# Функція алгоритму динамічного програмування
def dynamic_programming(items, budget):
    # Ініціалізуємо таблицю dp, де dp[i] - максимальна калорійність для бюджету i
    dp = [0] * (budget + 1)
    item_list = [(name, details['cost'], details['calories']) for name, details in items.items()]

    # Проходимо по кожній страві
    for name, cost, calories in item_list:
        for b in range(budget, cost - 1, -1):
            dp[b] = max(dp[b], dp[b - cost] + calories)

    # Визначаємо обрані страви
    total_calories = dp[budget]
    selected_items = []
    b = budget

    for name, cost, calories in sorted(item_list, key=lambda x: -x[2]):
        if b >= cost and dp[b] == dp[b - cost] + calories:
            selected_items.append(name)
            b -= cost

    return selected_items, total_calories

# Використання жадібного алгоритму
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм вибрав:", selected_items_greedy)
print("Загальна калорійність:", total_calories_greedy)

# Використання алгоритму динамічного програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("Алгоритм динамічного програмування вибрав:", selected_items_dp)
print("Загальна калорійність:", total_calories_dp)
