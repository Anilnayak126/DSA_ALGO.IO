class Binary:

    def binary_search(self,arr,target):
        left,right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                print("Found..")
                return
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
    def first_occurance(self,arr,target):
