import random
c1,c2 = 0,0
def randomizedqs(arr):
    # print(arr)
    global c1
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = []
        right = []
        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
                c1+=1
            elif arr[i] > pivot:
                right.append(arr[i])
                c1+=1
        # print(left,pivot,right)
        return randomizedqs(left) + [pivot] + randomizedqs(right)

def quicksort(arr):
    global c2
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
                c2+=1
            else:
                right.append(arr[i])
                c2+=1
        # print(left,pivot,right)
        return quicksort(left) + [pivot] + quicksort(right)
        # pivot = arr[0]
        # left =  [i for i in arr if i< pivot]
        # right = [i for i in arr if i>pivot]
        # c2 += len(left) +len(right)
        # print(left,quicksort(left),pivot,right,quicksort(right))
        # return quicksort(left) + [pivot] + quicksort(right)
        
arr = [i for i in range(50)]
print('Normal Quicksort')
print("Sorted Array:", quicksort(arr))
print("Number of Comparisons:", c2)
print("Randomized QS")
print("Sorted Array:", randomizedqs(arr))
print("Number of Comparisons:", c1)


