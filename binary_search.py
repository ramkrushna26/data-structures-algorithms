'''
Binary Search Algorithm: find the position of a target value within a sorted array
'''

def binary_search(arr, num):
    left = 0
    right = len(arr) - 1
    mid = len(arr) // 2
    if num > arr[right]:
            return -1
    
    while left < right:
        if arr[mid] == num:
            return mid
        elif num < arr[mid]:
            right = mid
            mid = right // 2
        elif num > arr[mid]:
            left = mid
            mid = (left+right+1) // 2

    return -1


def binary_search_recursive(arr, left, right, num):
    if left <= right:
        mid = (left+right) // 2
        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            return binary_search_recursive(arr, mid+1, right, num)
        else:
            return binary_search_recursive(arr, left, mid-1, num)
    else:
        return -1


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    num = 6

    print(binary_search(arr, num))

    print(binary_search_recursive(arr, 0, len(arr)-1, num))
