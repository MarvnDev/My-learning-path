x = 1
y = 1
z = 1
n = 2

newList = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]

# ================================================================================
# for item in range(0, len(newList)):
#     if sum(newList[item]) != n:
#         print(newList[item], end="," if item < (len(newList)-1) else "")
# ================================================================================

lstFinal = []

for item in range(0,len(newList)):
    if sum(newList[item])!=n:
        lstFinal.append(newList[item])

print(lstFinal)


    #[0, 0, 0],[0, 0, 1],[0, 1, 0],[0, 1, 1],[1, 0, 0],[1, 0, 1],[1, 1, 0],[1, 1, 1],

    #[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] OUTPUT DONE

    # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
    # [0, 0, 0],[0, 0, 1],[0, 1, 0],[0, 1, 2],[0, 2, 1],[0, 2, 2],[1, 0, 0],[1, 0, 2],[1, 1, 1],[1, 1, 2],[1, 2, 0],[1, 2, 1],[1, 2, 2],[2, 0, 1],[2, 0, 2],[2, 1, 0],[2, 1, 1],[2, 1, 2],[2, 2, 0],[2, 2, 1],[2, 2, 2]
    # OUTPUT DONE