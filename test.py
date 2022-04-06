import re

c = "A Famous Saying: Much Ado About Nothing (2012/8)."


def solution(str):
    tokens = []
    t = 0
    for i in range(len(str)):
        if str[i] == " ":
            tokens.append(str[t:i])
            t = i
    if str[i].isalpha():
        tokens.append(str[t:i+1])
    lens = 0
    for token in tokens:
        lens = len(token)

    return lens

A = input()
result = solution(A)

print(result)
