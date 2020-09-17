'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    s = set()

    for num in arr:
        #sets are similar to dicts
        #they don't associate value with keys
        #they're useful when you the uniqueness
        #property of dicts
        if num in arr:
            if num in s:
                s.remove(num)  
            else:
                s.append(num)

    return s.pop()


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")