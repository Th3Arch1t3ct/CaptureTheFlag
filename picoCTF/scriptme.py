#!/usr/bin/python

def maxDepth(S):
    curMax = 0
    finMax = 0
    n = len(S)

    for i in xrange(n):
        if S[i] == '(':
            curMax = curMax + 1
            if curMax > finMax:
                finMax = curMax
        elif S[i] == ')':
            if curMax > 0:
                curMax = curMax - 1
            else:
                return -1
    if curMax != 0:
        return -1
    return finMax

def calcResult(equation):
    i = 0
    for j in range(0, len(equation)-1):
        leftCount = maxDepth(equation[i])
        rightCount = maxDepth(equation[i+1])
        if(leftCount == rightCount):
            equation[i+1] = equation[i]+equation[i+1]
            del equation[i]
        elif (leftCount < rightCount):
            equation[i+1] = '(' + equation[i] + equation[i+1][1:]
            del equation[i]
        else:
            equation[i+1] = equation[i][:-1] + equation[i+1] + ')'
            del equation[i]
        i = 0
    return equation

def main():
    # Write your code here!


if__name__== "__main__":
    main()