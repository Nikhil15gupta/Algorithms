# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the 
# rotation.


def rotate(matrix):
        n = len(matrix)
        depth = n // 2
        for i in range(depth):
            rlen, opp = n - 2 * i - 1, n - 1 - i
            for j in range(rlen):
                # 4 way swap
                temp = matrix[i][i + j]
                matrix[i][i + j] = matrix[opp - j][i]
                matrix[opp - j][i] = matrix[opp][opp - j]
                matrix[opp][opp - j] = matrix[i + j][opp]
                matrix[i + j][opp] = temp

                
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

rotate(matrix)

print(matrix)

# https://dev.to/seanpgallivan/solution-rotate-image-cpp
