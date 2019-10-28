def sum(numbers):
    s = 0
    l = len(numbers)
    if l == 0:
        return s
    s = numbers[l-1] + sum(numbers[0:l-1])
    return s

def newsum(numbers):
    s = 0
    l = len(numbers)
    if l == 0:
        return s
    s = numbers[0] + newsum(numbers[1:])
    return s
    
def newnewsum(numbers):
    l = len(numbers)
    if l == 0:
        return 0
    return numbers[0] + newnewsum(numbers[1:])

#numbers = list(range(0,10))
#print(newnewsum(numbers))

def flatten(lst):
    y = []
    if isinstance(lst, list):
        for i in lst:
            y = y + flatten(i)
    else:
        y.append(lst)    
    return y

#x = [[1,2,3],[5,6,7]]
x = [9, [[1, 2], [3, 4]], [5], 6]
print(flatten(x))
