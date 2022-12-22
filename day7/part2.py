
#  []
MAX = 70_000_000
total_space = 0
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
    
    global total_space
    total_space = 70_000_000 - price("/", all_dir)      

    price("/", all_dir, True)
def price(path, all_dir, check_size=False):
    sum = 0
    for i in all_dir[path]:
        if "dir " in i:
            sum += price(path + "&"+ i.split('dir ')[1], all_dir, check_size)
        else :
            sum += int(i.split(' ')[0]) 
    global MAX
    global total_space
    print(total_space)
    if check_size and sum + total_space > 30_000_000 and sum < MAX:
        print(path)        
        MAX = sum
    return sum
main()
print(MAX)
