
#  []
def main():
    with open('data.txt') as f:
        data = f.read()

    # create stacks obj
    rows = data.split("\n\n")[0].split("\n")
    stacks = [[] for k in range(9)]

    for j in range(len(rows) - 1):
        row = rows[j]
        letters = [row[k] for k in [1, 5, 9, 13, 17, 21, 25, 29, 33]]
        for i in range(len(letters)):
            letter = letters[i]
            if letter != " ":
                stacks[i].append(letter)
    for i in stacks:
        i.reverse()

    moves = data.split("\n\n")[1].split("\n")
    tmp_moves = list()
    for move in moves:
        if len(move) > 0:
            tmp_moves.append([int(move.split(" ")[1]), int(move.split(" ")[3]), int(move.split(" ")[5])])
    moves = tmp_moves

    for move in moves:
        for _ in range(move[0]):
            stacks = modif_stack(stacks, move[1] - 1, move[2] - 1)

    for i in stacks:
        # print last elemnet of i
        print(i[-1], end="")
        
    print("")
    return True



def modif_stack(stacks,  i, j):
    # print(stacks, i , j)

    stacks[j].append(stacks[i].pop())
    return stacks

main()