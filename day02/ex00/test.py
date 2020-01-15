from ft_filter import ft_filter
from ft_map import ft_map
from ft_reduce import ft_reduce

from functools import reduce

# filter 1
lst = range(30)
new_lst = ft_filter(lambda x: x > 18, lst)
print(new_lst)
# filter 2
def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']  
filtered = ft_filter(fun, sequence) 
print('The filtered letters are:') 
for s in filtered: 
    print(s) 

# Map 1
h, m, s = ft_map(int, '8:19:22'.split(':'))
print(h,m,s)

# Map 2
def addition(n): 
    return n + n 
numbers = (1, 2, 3, 4) 
result = ft_map(addition, numbers) 
print(list(result)) 
'''
# Map 3
numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
result = ft_map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) 
'''
# Reduce 1
print(reduce(lambda a, b: a * b, range(1, 11)))

# Reduce 2
print(ft_reduce(lambda a, b: a * b, range(1, 5)))

lis = [ 1 , 3, 5, 6, 2, ] 

# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (ft_reduce(lambda a,b : a+b,lis)) 

# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (ft_reduce(lambda a,b : a if a > b else b,lis)) 
