def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0 , n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j] , arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return  arr
# arr = [1,2,6,8,9]
arr = ["banana", "apple", "cherry", "date"]
res = bubble_sort(arr)
print(res)


def descending_order(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1],arr[j]
                swapped = True

        if not swapped:
            break
    return  arr


def swap_count(arr):
    n = len(arr)
    swapped_count = 0


    for i in range(n):
        swapped = False


        for j in range(0,n - i - 1):
            if arr[j] > arr[j + 1]:
               arr[j],arr[j + 1] = arr[j + 1], arr[j]
               swapped_count += 1
               swapped = True

        if not  swapped:
            break

    return  swapped_count

def sort_array_of_strings(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return  arr

def is_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                return False
                break

    return  True


arr = [1,2,4]
res = is_sort(arr)
print(res)

# Imroved
def is_Sort(arr):
    n = len(arr)

    for i in range(n -1):
        if arr[i] > arr[i + 1]:
            return  False
    return  True

res = is_Sort(arr)
print(res)



def sort_array_of_tuple_by_last_index(arr):
     n = len(arr)
     for i in range(n):
         swapped = False
         for j in range(0, n - i - 1):
             if arr[j][1] > arr[j + 1][1]:
                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
                 swapped = True

         if not swapped:
            break
     return  arr



def optimized_buble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n  - i  -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def cocktail_shaker_sort(arr):
    n = len(arr)             # Get the length of the array
    swapped = True           # Flag to track if any swaps were made
    start = 0                # Starting index for the forward pass
    end = n - 1              # Ending index for the backward pass

    while swapped:           # Continue until no swaps occur
        swapped = False      # Assume no swaps will be needed in this pass

        # 🔼 Forward Pass: Move the largest element to its correct position
        for i in range(start, end):
            if arr[i] > arr[i + 1]:   # Compare current element with next
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap
                swapped = True        # Mark that a swap occurred

        if not swapped:      # If no swaps, array is already sorted
            break              # Exit the loop

        swapped = False      # Reset swapped for the backward pass
        end -= 1             # Reduce the range for the next forward pass

        # 🔽 Backward Pass: Move the smallest element to its correct position
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:   # Compare elements moving backwards
                arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap
                swapped = True        # Mark that a swap occurred

        start += 1           # Increase the range for the next backward pass

    return arr



