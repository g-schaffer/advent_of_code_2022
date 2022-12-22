
#  []
def main():
    with open('data.txt') as f:
        data = f.read()
    data = [list(k) for k in data.split("\n")]
    
    res = [[0 for k in range(len(data))] for j in range(len(data))]

    


    for i in range(len(data) - 1, -1, -1):

        m = 0
        for j in range(len(data) - 1, 0, -1):
         
            if j == len(data) - 1:
                res[i][j] = 1
                
            elif int(data[i][j]) > m:
                res[i][j] = 1
            
            m = max(m, int(data[i][j]))

    for i in range(0, len(data)):
        m = 0
        for j in range(0, len(data)):
         
            if j == 0:
                res[i][j] = 1
                
            elif int(data[i][j]) > m:
                res[i][j] = 1
            
            m = max(m, int(data[i][j]))


    for j in range(len(data) - 1, -1, -1):
        m = 0
        for i in range(len(data) - 1, 0, -1):
         
            if i == len(data) - 1:
                res[i][j] = 1
                
            elif int(data[i][j]) > m:
                res[i][j] = 1
            
            m = max(m, int(data[i][j]))

    for j in range(0, len(data)):
        m = 0
        for i in range(0, len(data)):
         
            if i == 0:
                res[i][j] = 1
                
            elif int(data[i][j]) > m:
                res[i][j] = 1
            
            m = max(m, int(data[i][j]))


    r = ""
    sum = 0
    for i in res:
        for j in i:
            if int(j) == 1:
                sum += 1
        r += "".join([str(k) for k in i]) +"\n"

    print(r)
    print(sum)
main()