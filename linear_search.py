'''
Linear Search Algorithm
'''

def linear_search(arr, num):
    sequence = arr
    num_to_search = num

    for i in range(len(sequence)):
        if num_to_search == sequence[i]:
            return i
    
    return -1

if __name__ == '__main__':
    arr = [1,2,10,4,9,6,7,13,8,12,15,]
    num = 10

    print(linear_search(arr, num))