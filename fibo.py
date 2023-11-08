#Author : Logan Markley
#Due Date : 11 / 7 / 2023
#Course : CS 2500 (Algorithms)
#Semester : Fall 2023
#Professor : Dr. Morales

def fiboRecursive(n: int) -> int:
    fiboCalculationsArray[n] += 1
    if n <= 1:
        return n
    else:
        return (fiboRecursive(n-1) + fiboRecursive(n-2))

def fiboMatrixMult(n: int) -> tuple[int, int]:
    startingMatrix =    [[1,1],
                        [1,0]]
    currentMatrix =     [[1,1],
                        [1,0]]
    numOfMultiplcations = 0

    for i in range(1,n):    # multiplies the matrix n times in order to achieve our final fibonacci matrix
        zeroZero = currentMatrix[0][0] * startingMatrix[0][0] + currentMatrix[0][1] * startingMatrix[1][0]  # have to calculate the values before updating the array
        zeroOne = currentMatrix[0][0] * startingMatrix[0][1] + currentMatrix[0][1] * startingMatrix[1][1]
        oneZero = currentMatrix[1][0] * startingMatrix[0][0] + currentMatrix[1][1] * startingMatrix[1][0]
        oneOne = currentMatrix[1][0] * startingMatrix[0][1] + currentMatrix[1][1] * startingMatrix[1][1]
        numOfMultiplcations += 8    # every iteration does 8 multiplications.

        currentMatrix[0][0] = zeroZero
        currentMatrix[0][1] = zeroOne
        currentMatrix[1][0] = oneZero
        currentMatrix[1][1] = oneOne

    return currentMatrix[0][1], numOfMultiplcations # returns a tuple with the fibonacci number and the num of multiplications needed to calculate it.

inputNum = int(input())
fiboCalculationsArray = [0] * (inputNum+1)  # an array to hold each number of fibo uses from the recursive method.

print(fiboRecursive(inputNum))  # print the fibo number at n

for index, num in enumerate(fiboCalculationsArray): # print the uses of each fibo number from the recursive method
    print(f"fibo({index}) : {num}")

print(fiboMatrixMult(inputNum)[1])  # print how many multiplications it would take to get that fibo number using the naive matrix multiplication method
