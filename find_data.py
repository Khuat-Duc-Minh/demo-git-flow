"""find_data.py
Binary search on a sorted ascending list.
"""
from typing import List



def binary_search(data: List[int], target: int) -> int:
    """Perform iterative binary search. Assumes `data` is sorted in ascending order.


    Returns index of target if found, otherwise -1.
    """
    if data is None:
        return -1
    lo = 0
    hi = len(data) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    for t in [3, 6, 1]:
        print(t, binary_search(arr, t))