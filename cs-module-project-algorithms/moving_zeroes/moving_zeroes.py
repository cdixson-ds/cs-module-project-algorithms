'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    #count = 0
 
    for index, i in enumerate(arr):  #keep track of index
        if arr[index] != 0:                       
            arr.insert(0, arr.pop(index))

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")