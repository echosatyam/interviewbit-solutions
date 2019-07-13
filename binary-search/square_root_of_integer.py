def sqrt(A):
    if(A == 0 or A == 1):
        return A
    low = 2
    high = int(A/2)+1
    while(low <= high):
        mid = int((low+high)/2)
        if(mid*mid <= A and (mid+1)*(mid+1) > A):
            return mid
        elif mid*mid > A:
            high = mid-1
        else:
            low = mid+1
    return -1


res = sqrt(930675566)
print(res)
