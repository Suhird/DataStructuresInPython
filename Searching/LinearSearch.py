#program implementing linear search
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

def linear_search(element_to_be_searched,l):
    x = element_to_be_searched
    pos = 0
    found = False
    while pos < len(l):
        if x==l[pos]:
            print('Element Found at: ',pos+1)
            found = True
            break
        else:
            pos+=1
    return found


if __name__ == '__main__':
    '''To generate random list uncomment below code'''
    #b = generate_list()            
    b = [9, 50, 5, 24, 43, 6, 7, 36, 34, 39, 29, 6, 3]
    linear_search(29,b)
