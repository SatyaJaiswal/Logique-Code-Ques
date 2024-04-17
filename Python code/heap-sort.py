def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # create map heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # swapping here 
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)

    return arr

# Example :
arr = [14, 25, 13, 5, 6, 7,2,8,18]
sorted_arr = heap_sort(arr)
print("Sorted array:", sorted_arr)

