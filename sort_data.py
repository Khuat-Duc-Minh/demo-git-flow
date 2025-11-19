"""sort_data.py
Provide sorting functionality. Default method is 'bubble'.
Supported methods: 'bubble', 'quick', 'merge'.
"""
from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def quick_sort(arr: List[int]) -> List[int]:
    # recursive quicksort (not in-place)
    if len(arr) <= 1:
        return arr.copy()
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr.copy()


    def merge(left: List[int], right: List[int]) -> List[int]:
        i = j = 0
        out = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
            out.extend(left[i:])
            out.extend(right[j:])
        return out


    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def sort_data(data: List[int], choice: str = "bubble") -> List[int]:
    """Sort the given list of integers using the chosen algorithm.


    Args:
    data: list of integers (will not be modified)
    choice: one of 'bubble', 'quick', 'merge'


    Returns:
    sorted list of integers
    """
    if data is None:
        raise ValueError("data must be a list")


    choice = choice.lower()
    if choice == "bubble":
        return bubble_sort(data)
    if choice == "quick":
        return quick_sort(data)
    if choice == "merge":
        return merge_sort(data)
    raise ValueError(f"Unknown sort choice: {choice}. Supported: bubble, quick, merge")                         


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print("bubble:", sort_data(sample, "bubble"))
    print("quick: ", sort_data(sample, "quick"))
    print("merge: ", sort_data(sample, "merge"))