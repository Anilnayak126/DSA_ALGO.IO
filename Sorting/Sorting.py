input = [1,2,3,4]
# [24, 12, 8, 6]


def multiplication(arr):
    n = len(arr)
    mul = []
    for i in range(n):
        multi =  1
        for j in arr:
            if arr[i] == j:
                pass
            else:
               multi *= j
        mul.append(multi)
    return mul

print(multiplication(input))










