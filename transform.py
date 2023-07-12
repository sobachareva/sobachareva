array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = list(zip(*array))
print(transposed) 
>>> [('a', 'c', 'e'), ('b', 'd', 'f')]
