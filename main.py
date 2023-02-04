def solveSudoku(board) -> None:
    l = list()
    al = list()
    for i in range(1, 10):
        l.append(i)
    for i in range(81):
        t1 = i // 9
        t2 = i % 9
        if board[t1][t2] == '.':
            p = l.copy()
            al.append(p)
        else:
            al.append([])

    rand = -1
    number = 0
    count = 100
    counts = 10
    sohr1 = list()
    sohr2 = list()
    tor = 0
    ex = 0
    while count != 0:
        counts = count
        for i in range(81):
            if len(al[i]) == 1:
                t1 = i // 9
                t2 = i % 9
                board[t1][t2] = str(al[i][0])
        for i in range(9):
            for k in range(1, 10, 1):
                if str(k) in board[i]:
                    for j in range(9):
                        if k in al[i * 9 + j]:
                            al[i * 9 + j].remove(k)

        for i in range(9):
            p = list()
            for j in range(9):
                if board[j][i] != '.':
                    p.append(int(board[j][i]))
            for j in range(9):
                for k in p:
                    if k in al[j * 9 + i]:
                        al[j * 9 + i].remove(k)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    t1 = i // 3
                    t2 = j // 3
                    for k in range(t1 * 3, t1 * 3 + 3, 1):
                        for t in range(t2 * 3, t2 * 3 + 3, 1):
                            if int(board[i][j]) in al[k * 9 + t]:
                                al[k * 9 + t].remove(int(board[i][j]))

        for i in range(9):
            for k in range(1, 10, 1):
                if str(k) not in board[i]:
                    co = 0
                    t = -1
                    for j in range(9):
                        if k in al[i * 9 + j]:
                            co += 1
                            t = j
                    if co == 1:
                        board[i][t] = str(k)
                        al[i * 9 + t].clear()

        for i in range(9):
            for k in range(1, 10, 1):
                lik = 0
                for tiz in range(9):
                    if board[tiz][i] == str(k):
                        lik += 1
                if lik == 0:
                    co = 0
                    t = -1
                    for j in range(9):
                        if k in al[j * 9 + i]:
                            co += 1
                            t = j
                    if co == 1:
                        board[t][i] = str(k)
                        al[t * 9 + i].clear()

        for i in range(3):
            for j in range(3):
                for k in range(1, 10, 1):
                    lik = 0
                    non = 0
                    t1 = -1
                    t2 = -1
                    for t in range(3 * i, 3 * i + 3, 1):
                        for p in range(3 * j, 3 * j + 3, 1):
                            if k in al[9 * t + p]:
                                lik += 1
                                t1 = t
                                t2 = p
                            if str(k) == board[t][p]:
                                non += 1
                    if non == 0 and lik == 1:
                        board[t1][t2] = str(k)
                        al[t1 * 9 + t2].clear()

        if ex == 1:
            for i in range(9):
                for k in range(1, 10, 1):
                    if board[i].count(str(k)) > 1:
                        tor = 1
                        break
                if tor == 1:
                    break
            if tor == 0:
                for i in range(9):
                    for k in range(1, 10, 1):
                        counters = 0
                        for j in range(9):
                            if board[j][i] == str(k):
                                counters += 1
                        if counters > 1:
                            tor = 1
                            break
                    if tor == 1:
                        break
            if tor == 0:
                for i in range(3):
                    for j in range(3):
                        for k in range(1, 10, 1):
                            counters = 0
                            for lam in range(3 * i, 3 * i + 3, 1):
                                for t in range(3 * j, 3 * j + 3, 1):
                                    if board[lam][t] == str(k):
                                        counters += 1
                            if counters > 1:
                                tor = 1
                                break
                        if tor == 1:
                            break
                    if tor == 1:
                        break

        count = 0
        for i in range(81):
            for j in al[i]:
                count += 1

        if counts == count or tor != 0:
            ex = 1
            count = 10
            tor = 0
            if rand < 0:
                for i in range(81):
                    sohr1.append(al[i].copy())
                for i in range(9):
                    sohr2.append(board[i].copy())
                for i in range(rand + 1, 81, 1):
                    if len(al[i]) != 0:
                        rand = i
                        number = 0
                        board[i // 9][i % 9] = str(al[i][0])
                        al[i] = []
                        break
            else:
                al.clear()
                board.clear()
                for i in range(81):
                    al.append(sohr1[i].copy())
                for i in range(9):
                    board.append(sohr2[i].copy())
                if len(al[rand]) - 1 != number:
                    number += 1
                    board[rand // 9][rand % 9] = str(al[rand][number])
                    al[rand] = []
                else:
                    for i in range(rand + 1, 81, 1):
                        if len(al[i]) != 0:
                            rand = i
                            number = 0
                            board[i // 9][i % 9] = str(al[i][0])
                            al[i] = []
                            break

print("Enter your Sudoku. Enter one line at a time without spaces between characters, the omissions are indicated by the symbol '.':")
li = list()
for i in range(9):
    s = input()
    p = list()
    for j in range(9):
        p.append(s[j])
    li.append(p)
solveSudoku(li)
print()
print("A ready-made solution to your Sudoku")
for i in range(9):
    for j in range(9):
        print(li[i][j], end=" ")
        if j == 2 or j == 5:
            print('|', end=" ")
    print()
    if i == 2 or i == 5:
        for j in range(11):
            print('-', end=" ")
        print()
