import random
import time

def partition_lomuto(arr, low, high):
    if low < high:
        start = low - 1
        pivot = high
        for i in range(low, high):
            if arr[i] <= arr[pivot]:
                start += 1
                arr[start], arr[i] = arr[i], arr[start]
        arr[start + 1], arr[high] = arr[high], arr[start + 1]
        p = start + 1
        partition_lomuto(arr, low, p - 1)
        partition_lomuto(arr, p + 1, high)
        
def partition_lomuto_random(arr, low, high):
    if low < high:
        k = random.randint(low, high)
        arr[k], arr[high] = arr[high], arr[k]
        start = low - 1
        pivot = high
        for i in range(low, high):
            if arr[i] <= arr[pivot]:
                start += 1
                arr[start], arr[i] = arr[i], arr[start]
        arr[start + 1], arr[high] = arr[high], arr[start + 1]
        p = start + 1
        partition_lomuto_random(arr, low, p - 1)
        partition_lomuto_random(arr, p + 1, high)
        
def partition_hoare(arr, low, high):
    if low < high:
        start = low
        i = high
        pivot = low
        while start < i:
            while arr[start] <= arr[pivot] and start < high:
                start += 1
            while arr[i] > arr[pivot]:
                i -= 1
            if start < i:
                arr[start], arr[i] = arr[i], arr[start]
        arr[i], arr[pivot] = arr[pivot], arr[i]
        partition_hoare(arr, low, i - 1)
        partition_hoare(arr, i + 1, high)
        
def partition_hoare_random(arr, low, high):
    if low < high:
        k = random.randint(low, high)
        arr[k], arr[low] = arr[low], arr[k]
        start = low
        i = high
        pivot = low
        while start < i:
            while arr[start] <= arr[pivot] and start < high:
                start += 1
            while arr[i] > arr[pivot]:
                i -= 1
            if start < i:
                arr[start], arr[i] = arr[i], arr[start]
        arr[i], arr[pivot] = arr[pivot], arr[i]
        partition_hoare_random(arr, low, i - 1)
        partition_hoare_random(arr, i + 1, high)

random_array = [i for i in range(500)[::-1]]
random_array1 = random_array.copy()
random_array2 = random_array.copy()
random_array3 = random_array.copy()
# Timing Lomuto Quicksort
start_time = time.time()
partition_lomuto(random_array, 0, len(random_array) - 1)
i_time = time.time()
print("Lomuto Quicksort Time:", i_time - start_time)

# Timing Lomuto Quicksort with random pivot selection
start_time = time.time()
partition_lomuto_random(random_array1, 0, len(random_array1) - 1)
i_time = time.time()
print("Lomuto Quicksort with Random Pivot Selection Time:", i_time - start_time)

# Timing Hoare Quicksort
start_time = time.time()
partition_hoare(random_array2, 0, len(random_array2) - 1)
i_time = time.time()
print("Hoare Quicksort Time:", i_time - start_time)

# Timing Hoare Quicksort with random pivot selection
start_time = time.time()
partition_hoare_random(random_array3, 0, len(random_array3) - 1)
i_time = time.time()
print("Hoare Quicksort with Random Pivot Selection Time:", i_time - start_time)
