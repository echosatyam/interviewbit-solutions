def searchMatrix(A, B):
    print(A)
    index_low = 0
    row_low = 0
    row_high = len(A[0])-1
    index_high = len(A)-1
    while(index_low <= index_high and row_low <= row_high):
        mid_index = int((index_low+index_high)/2)
        if(A[mid_index][0] > B):
            index_high = mid_index-1
        elif A[mid_index][len(A[0])-1] < B:
            index_low = mid_index+1
        else:
            mid_row = int((row_low + row_high)/2)
            print(mid_index, mid_row)
            print(A[mid_index][mid_row])
            if(A[mid_index][mid_row] == B):
                return 1
            elif(A[mid_index][mid_row] > B):
                row_high = mid_row-1
            else:
                row_low = mid_row+1

    return 0


print(searchMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 19))
