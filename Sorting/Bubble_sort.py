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
        for j in range(0, n - i - 0):
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


arr = [1,2,5,4]
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



