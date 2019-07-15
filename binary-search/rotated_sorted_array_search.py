
def pivot(A, B):
    low = 0
    high = len(A)-1
    if(low == high):
        return low
    elif high == low+1 and A[low] <= A[high]:
        return low
    elif high == low+1 and A[low] > A[high]:
        return high
    while(low <= high):
        mid = (high+low)//2
        if mid > 0 and mid < len(A)-1 and A[mid] < A[mid+1] and A[mid] < A[mid-1]:
            return mid
        elif A[mid] > A[len(A)-1]:
            low = mid + 1
        else:
            high = mid-1


def binSearch(A, B, low, high):
    if(low <= high):
        mid = (low+high)//2
        if(A[mid] == B):
            return mid
        elif A[mid] > B:
            return binSearch(A, B, low, mid-1)
        else:
            return binSearch(A, B, mid+1, high)
    return -1


def search(A, B):
    p = pivot(A, B)
    print(p)
    one = binSearch(A, B, 0, p+1)
    two = binSearch(A, B, p, len(A)-1)
    if(one != -1):
        return one
    if(two != -1):
        return two
    return -1


print(search([180, 181, 182, 183, 184, 187, 188, 189, 191, 192, 193, 194, 195, 196, 201, 202, 203, 204, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16, 17, 18, 19, 23, 26, 27, 28, 29, 32, 33, 36, 37, 38, 39, 41, 42, 43, 45, 48, 51, 52, 53, 54, 56, 62, 63, 64, 67, 69, 72, 73, 75, 77, 78, 79, 83, 85,
              87, 90, 91, 92, 93, 96, 98, 99, 101, 102, 104, 105, 106, 107, 108, 109, 111, 113, 115, 116, 118, 119, 120, 122, 123, 124, 126, 127, 129, 130, 135, 137, 138, 139, 143, 144, 145, 147, 149, 152, 155, 156, 160, 162, 163, 164, 166, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177], 42))
