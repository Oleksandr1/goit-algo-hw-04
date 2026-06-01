"""
Завдання 3. Порівняння алгоритмів сортування за часом виконання.

Порівнюються:
  - сортування вставками (insertion sort), O(n^2);
  - сортування злиттям (merge sort), O(n log n);
  - вбудований Timsort (sorted), O(n log n) — гібрид merge + insertion.

Час вимірюється модулем timeit на випадкових масивах різного розміру.
Висновки оформлено у файлі README.md.

Запуск:
    python task_3.py
"""

import random
import timeit


def insertion_sort(arr: list) -> list:
    a = list(arr)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return list(arr)
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def timsort(arr: list) -> list:
    return sorted(arr)


def benchmark(func, data: list, number: int) -> float:
    """Середній час одного запуску func(data) у секундах."""
    total = timeit.timeit(lambda: func(data), number=number)
    return total / number


def main() -> None:
    sizes = [100, 1000, 5000, 10000]
    algorithms = {
        "Insertion": insertion_sort,
        "Merge": merge_sort,
        "Timsort": timsort,
    }

    header = f"{'Розмір':>8} | {'Insertion (с)':>15} | {'Merge (с)':>12} | {'Timsort (с)':>13}"
    print(header)
    print("-" * len(header))

    for size in sizes:
        data = [random.randint(0, size) for _ in range(size)]
        row = {}
        for name, func in algorithms.items():
            # повільні/великі кейси проганяємо меншу кількість разів
            if name == "Insertion" and size >= 5000:
                number = 1
            elif size >= 5000:
                number = 5
            else:
                number = 20
            row[name] = benchmark(func, data, number)

        print(
            f"{size:>8} | {row['Insertion']:>15.6f} | "
            f"{row['Merge']:>12.6f} | {row['Timsort']:>13.6f}"
        )


if __name__ == "__main__":
    main()
