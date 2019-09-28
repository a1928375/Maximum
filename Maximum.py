l = ['Barbara', 'kingsolver', 'wrote', 'The', 'Poisonwood','Bible']
f = len


def findMax(arr, func):
    
    max = 0
    
    result = ""
    
    for i in arr:
        
        if func(i) >= max:
            
            max = func(i)
            
            result = i
    
    return result 


print(findMax(l, f))

l = [1,-2,3,-4]
f = abs

print(findMax(l, f))
