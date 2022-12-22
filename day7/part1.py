
#  []
BIGSUM = 0
def main():
    with open('data.txt') as f:
        data = f.read()
    
    all_dir = dict()
    last_dir = list()
    last_dir_path = list()
    for line in data.split('\n'):

        if '$' in line:
            if last_dir:
                all_dir['&'.join(last_dir_path)] = last_dir
                last_dir = list()

        if '$ cd ..' in line:
            last_dir_path.pop()
        elif '$ cd ' in line:
            last_dir_path.append(line.split('$ cd ')[1])
        elif '$ ls' in line:
            continue
        else:
            last_dir.append(line)
    all_dir['&'.join(last_dir_path)] = last_dir
                
    price("/", all_dir)

def price(path, all_dir):
    sum = 0
    for i in all_dir[path]:
        if "dir " in i:
            sum += price(path + "&"+ i.split('dir ')[1], all_dir)

        else :
            sum += int(i.split(' ')[0]) 

    if sum <= 100_000:
        # print(path, sum)
        global BIGSUM
        BIGSUM += sum
    return sum
main()
print(BIGSUM)