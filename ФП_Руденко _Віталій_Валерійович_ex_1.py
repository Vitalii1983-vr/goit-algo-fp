# Визначаємо структуру вузла однозв'язного списку
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Функція для реверсування однозв'язного списку
def reverse_list(head):
    prev = None  # Ініціалізуємо попередній вузол як None
    current = head  # Починаємо з голови списку
    while current is not None:
        next_node = current.next  # Зберігаємо наступний вузол
        current.next = prev  # Змінюємо посилання наступного вузла на попередній
        prev = current  # Переміщуємо попередній вузол на поточний
        current = next_node  # Переміщуємо поточний вузол на наступний
    return prev  # Повертаємо нову голову списку (останній елемент став першим)

# Алгоритм сортування однозв'язного списку методом злиття
def merge_sort(head):
    if head is None or head.next is None:
        return head  # Якщо список порожній або має один елемент, він вже відсортований

    # Розділення списку на дві половини
    middle = get_middle(head)  # Знаходимо середину списку
    next_to_middle = middle.next  # Зберігаємо наступний вузол після середини
    middle.next = None  # Розділяємо список на дві частини

    # Рекурсивне сортування обох половин
    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    # Злиття двох відсортованих половин
    sorted_list = sorted_merge(left, right)
    return sorted_list

def get_middle(head):
    if head is None:
        return head  # Якщо список порожній, повертаємо None

    slow = head  # Початково обидва вказівники на голові списку
    fast = head

    # Переміщуємо fast на два кроки, а slow на один, щоб знайти середину
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow  # Повертаємо середній вузол

def sorted_merge(a, b):
    result = None

    if a is None:
        return b  # Якщо перший список порожній, повертаємо другий
    if b is None:
        return a  # Якщо другий список порожній, повертаємо перший

    # Вибираємо вузол з меншою значенням і рекурсивно зливаємо інші
    if a.value <= b.value:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)

    return result  # Повертаємо злитий список

# Функція для об'єднання двох відсортованих однозв'язних списків
def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(0)  # Додатковий вузол для спрощення коду
    tail = dummy

    # Порівнюємо вузли з обох списків і додаємо їх у новий список
    while l1 is not None and l2 is not None:
        if l1.value <= l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Додаємо залишки списків, якщо вони є
    if l1 is not None:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next  # Повертаємо об'єднаний список, пропустивши додатковий вузол

# Приклади використання функцій

# Створення списку: 1 -> 2 -> 3 -> None
head = ListNode(1, ListNode(2, ListNode(3)))
# Реверсування списку
reversed_head = reverse_list(head)
print("Реверсований список:")
while reversed_head is not None:
    print(reversed_head.value, end=" -> ")
    reversed_head = reversed_head.next
print("None")

# Створення списку: 3 -> 1 -> 2 -> None
head = ListNode(3, ListNode(1, ListNode(2)))
# Сортування списку
sorted_head = merge_sort(head)
print("Відсортований список:")
while sorted_head is not None:
    print(sorted_head.value, end=" -> ")
    sorted_head = sorted_head.next
print("None")

# Створення першого списку: 1 -> 3 -> 5 -> None
l1 = ListNode(1, ListNode(3, ListNode(5)))
# Створення другого списку: 2 -> 4 -> 6 -> None
l2 = ListNode(2, ListNode(4, ListNode(6)))
# Об'єднання списків
merged_head = merge_two_sorted_lists(l1, l2)
print("Об'єднаний список:")
while merged_head is not None:
    print(merged_head.value, end=" -> ")
    merged_head = merged_head.next
print("None")
