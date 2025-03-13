class Binary:
    def __init__(self):
        pass

    def Binary_Search(self,arr,target):
        left,right = 0, len(arr) -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                print("Found!!")
                return
            elif arr[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        print('not found')

    def first_occurance(self,arr,target):
        left, right = 0, len(arr) -1
        res = 0

        while left <= right:
            mid =  left + (right - left) // 2

            if arr[mid] == target:
                res = mid
                right = mid - 1
            elif arr[mid] > target:
                right = mid -1
            else:
                left = mid + 1

        return  res

    def last_occurance(self,arr,target):
        left,right = 0, len(arr) - 1
        res = 0
        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                res = mid
                left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return  res

    def find_ceil(self,arr,target):
        left,right = 0, len(arr) -1
        res = -1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] >= target:
                res = arr[mid]
                right = mid -1
            else:
                left = mid + 1
        return  res

    def find_floor(self,arr,target):
        left,right = 0 , len(arr) - 1
        res = -1

        while left <= right:
            mid = left + (right - left)  // 2

            if arr[mid] <= target:
                res = arr[mid]
                left = mid + 1
            else:
                right = mid - 1

        return  res




Binary = Binary()

arr = [1,2,3,4,5]
Binary.Binary_Search(arr,3)
arr = [1,2,3,4,4,4,4,5,6]
print("*" * 20)
res = Binary.first_occurance(arr,4)
print(res)
print("*" * 20)

res = Binary.last_occurance(arr,4)
print(res)

print("*" *  20)
arr = [1,2,4,5]
res = Binary.find_ceil(arr, 3)

print(res)

print("*" * 20)

res = Binary.find_floor(arr,3)

print(res)

