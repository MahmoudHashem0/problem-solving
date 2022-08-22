
X = "X"
O = "O"
EMPTY = None
board = [[EMPTY, X, EMPTY],
            [EMPTY, X, EMPTY],
            [O, EMPTY, EMPTY]]


arr = [11,3,5,9,7,4,21,8]
max = 0
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]

print(f"max: {max}")