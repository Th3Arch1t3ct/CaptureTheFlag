#!/usr/bin/env python3
import socket

def maxDepth(S):
    curMax = 0
    finMax = 0
    n = len(S)

    for i in range(n):
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
    return equation[0]

def main():
    # Write your code here!
    HOST = '2018shell1.picoctf.com'
    PORT = 61344

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        for i in range(0,4):
            data = s.recv(4096) # Rules:
            print(data)
            # This takes all the rules etc and the example. Splits it into list. Does all data cleanup
            data = s.recv(8192).split(b'\n')[-3].decode('utf-8')[0:-6].split(" + ")
            print(data)
            answer = calcResult(data)
            s.sendall((answer + '\n').encode('utf-8'))
        data = s.recv(4096) # Correct!
        data = s.recv(4096) # First part
        data = data + s.recv(4096) # Second Part:
        data = data.split(b'\n')[-3].decode('utf-8')[0:-6].split(" + ")
        answer = calcResult(data)
        s.sendall((answer + '\n').encode('utf-8'))
        data = s.recv(4096) # Correct
        data = s.recv(4096) # Flag!:
        print(data)


if __name__== "__main__":
    main()