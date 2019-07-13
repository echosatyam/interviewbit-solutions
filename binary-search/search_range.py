
def First(A, B, low, high):
    while(low <= high):
        mid = int((low+high)/2)
        if(mid == 0 or B > A[mid-1]) and A[mid] == B:
            return mid
        elif A[mid] < B:
            low = mid+1
        else:
            high = mid-1
    return -1


def Last(A, B, low, high):
    while(low <= high):
        mid = int((low+high)/2)
        if(mid == len(A)-1 or B < A[mid+1]) and A[mid] == B:
            return mid
        elif A[mid] > B:
            high = mid-1
        else:
            low = mid+1
    return -1


def searchRange(A, B):
    first = First(A, B, 0, len(A)-1)
    last = Last(A, B, 0, len(A)-1)
    return [first, last]


print(searchRange([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6,
                   6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 10))
