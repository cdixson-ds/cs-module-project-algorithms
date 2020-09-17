'''
Input: an integer
Returns: an integer
'''


#create cache for cookies to handle larger numbers

def eating_cookies(n, cache=None):
    
    #base case
    if n == 0:
        return 1
    elif n < 3:
        return n
    #check if in chache
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            #initialize an empty cache
            cache = {i: 0 for i in range(n+1)} #want n itself also in the cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        #Cookie Monster can eat either 1, 2, or 3 cookies at a time
        #return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        return cache[n]
    
    
if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


