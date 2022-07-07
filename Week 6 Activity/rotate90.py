import numpy as np

def rotate_matrix(m):
    arr1 = np.array(m)

    print(f'Input :\n{arr1}')

    output = np.rot90(arr1)        

    print(f'Output:\n{output}')




#Test Cases:

# m = [ [1, 2, 3],[4, 5, 6], [7, 8, 9]]
# m =  [ [ 5, 1, 9,11], [ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]

rotate_matrix(m)
