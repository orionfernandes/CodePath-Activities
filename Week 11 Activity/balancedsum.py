def findIndex(arr):
    lsum = []
    rsum = []

    # Iterate from 0 to len(arr)
    i = 0
    while( i < len(arr)):

        # If i is not 0
        if(i):
            lsum.append(lsum[i-1]+arr[i])
            rsum.append(rsum[i-1]+arr[len(arr)-1-i])
        else:
            lsum.append(arr[i])
            rsum.append(arr[len(arr)-1])
        i= i + 1

    # Iterate from 0 to len(arr)    
    i = 0
    while( i <len(arr)):
        if(lsum[i] == rsum[len(arr) - 1 - i ]):
            return(i)
        i+=1
            
    # If no equilibrium index found,then return -1
    return -1

n = int(input())

arr = list(map(int ,input().split()))
print('Index is ',
    findIndex(arr))
