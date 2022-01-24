# coding: utf-8
import sys


def maxRectangle(input, n):
    """
    Function maxRectangle to find maximal defect-free rectangle.
    Input: binary matrix and number of length lines of matrix.
    Output: Maximal defect-free rectangle.
    """
    # Check input binary matrix
    if not input:
        return 0
    if (len(input) != len(input[0])):
        return 0

    # Height histogram of defect-free rectangle
    height = [0 for i in range(n+1)]
    maxArea = 0  # variable save maximal defect-free rectangle

    for i in range(n):
        for j in range(n):
            height[j] = 0 if input[i][j] == 0 else height[j] + 1
            # get maximal defect-free rectangle
        maxArea = max(maxArea, findMaxArea(height))
    return maxArea


def findMaxArea(height):
    """
    Function findMaxArea to find the maximum defect-free rectangle rectangle
    of ​​each line.
    Input: Height histogram of defect-free rectangle.
    Output: maximal defect-free rectangle.
    """
    stack = []  # create empty stack contains the positions of height
    maxAreaTemp = 0

    for i in range(len(height)):
        """
        If the stack is not empty and the value of
        the list at the position peaked from the stack is not less than
        the value of the row at i, perform the algorithm to find the largest
        area inside the loop.
        """
        while((len(stack)) and (height[stack[-1]] > height[i])):
            """
                Get value at the position are pop ra from stack and alignment it
                for height.
            """
            heightTemp = height[stack.pop()]
            if (not len(stack)):
                w = i
            else:
                w = i - stack[-1] - 1
            # update new maximal defect-free rectangle
            maxAreaTemp = max(maxAreaTemp, w * heightTemp)
        stack.append(i)  # push index i into stack
    return maxAreaTemp


if __name__ == "__main__":
    # Create readfile input and file output
    inputFile = open(sys.argv[1], 'r')
    outputFile = open(sys.argv[2], 'w')

    # Create matrix binary from file input
    input = []

    # read n lines from in.txt
    n = int(inputFile.readline())

    # read matrix from file in.txt
    for line in inputFile.readlines():
        input.append([int(x) for x in line.split(' ')])

    # write maximal defect-free rectangle value into output file
    outputFile.write(str(maxRectangle(input, n)))

    inputFile.close()
    outputFile.close()
