# zip

alpha = ['a', 'b', 'c']
index = [1, 2, 3]
alpha_index = list(zip(alpha, index))
print(alpha_index)    
# [('a', 1), ('b', 2), ('c', 3)]

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(list(zip(*arr)))  
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]