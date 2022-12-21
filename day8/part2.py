
#  []
def main():
    with open('data.txt') as f:
        data = f.read()
    data = [list(k) for k in data.split("\n")]
    
    res = [[calculate_score(data, k, j) for k in range(len(data))] for j in range(len(data))]
    
    print(max([max(k) for k in res]))

def calculate_score(data, x, y):
    up = 0
    down = 0
    right = 0
    left = 0
    
    # up
    for i in range(x + 1, len(data)):
        up += 1
        
        if int(data[i][y]) >= int(data[x][y]):
            break
    # down
    for i in range(x - 1, -1, -1):
        down += 1
        
        if int(data[i][y]) >= int(data[x][y]):
            break

    # right
    for i in range(y + 1, len(data)):
        right += 1
        
        if int(data[x][i]) >= int(data[x][y]):
            break
    # left
    for i in range(y - 1, -1, -1):
        left += 1
        
        if int(data[x][i]) >= int(data[x][y]):
            break

    return up * down * right * left
main()