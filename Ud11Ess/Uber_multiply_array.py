def no_division(A):
    total = A.copy()
    left = 1
    for i in range(len(A)):
        right =1
        if i>0:
            left *= A[i-1]
        for j in range(i+1,len(A)):
            right *= A[j]
        total[i] = left * right
    return total

def brute_force(A):
    total = A.copy()
    for i in range(len(A)):
        sum=1
        for j in range(len(A)):
            if i==j:
                continue
            else:
                sum *= A[j]
        total[i] = sum
    return total

def optimized(A):
    total = A.copy()
    mult=1
    for num in A:
        mult *=num
    
    for i in range(len(A)):
        total[i] = mult // A[i]
    return total

print(no_division([-1,1, 2, 3, 4, 5]))