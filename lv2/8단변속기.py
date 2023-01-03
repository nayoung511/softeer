import sys
input = sys.stdin.readline

def checkAscending(num):
    start = num[0]
    for i in range (1, 8):
        if start < num[i]:
            start = num[i]
        else:
            return False

    return True

def checkDescending(num):
    start = num[0]
    for i in range (1, 8):
        if start > num[i]:
            start = num[i]
        else:
            return False

    return True

num = list(map(int, input().split()))

if checkAscending(num): print("ascending")
elif checkDescending(num): print("descending")
else: print("mixed")
