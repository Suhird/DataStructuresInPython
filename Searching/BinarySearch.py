#program implementing binary search
'''
Complexity if Linear Search on an unordered list is O(n)

'''
__author__ = 'Suhird'

import random

def generate_list():
    b=[]
    for i in range(13):
        b.append(random.randint(1,57))
    return b

def binary_search(element_to_be_searched,l):
    start, end, found = 0, len(l)-  1, False
    x = element_to_be_searched
    while start <= end and not found:
        print(found)
        mid = (start+end)//2
        print(mid)
        if l[mid] == element_to_be_searched:
            found = True
        else:
            if x < l[mid]:
                end = mid - 1
            else:
                first = mid + 1
    
    return found

if __name__=='__main__':
    b = [3, 5, 6, 6, 7, 9, 24, 29, 34, 36, 39, 43, 50]
    print(binary_search(29,b))