def queen(A, cur=0):
    # use backtracking to solve 8Queens
    if cur == len(A):
        # print(A)
        return 0
    for col in range(len(A)):
        A[cur], flag = col, True
        for row in range(cur):
            if A[row] == col or abs(col - A[row]) == cur - row:
                flag = False
                break
        if flag:
            queen(A, cur+1)


if __name__ == '__main__':
    queen([None]*8)