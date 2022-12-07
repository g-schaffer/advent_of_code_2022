
#  []
def main():
    with open('data.txt') as f:
        data = f.read()
    print(data)
    sub = data[0:14]
    print(sub)
    for i in range(13, len(data)):
        print(sub)
        sub = data[i-13:i+1]
        if unique(sub):
            print(i + 1)
            break
    return True

def unique(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True

def modif_stack(stacks,  i, j):
    # print(stacks, i , j)

    stacks[j].append(stacks[i].pop())
    return stacks

main()