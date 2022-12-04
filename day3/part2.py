VALUE = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()
def main():
    with open('data.txt') as f:
        data = f.read()
    sum = 0

    # reorganize data
    curr_bag = []
    groups = []
    for i in range(len(data.split("\n"))):
        if i % 3 == 0 and len(curr_bag) > 0:
            groups.append(curr_bag)
            curr_bag = []
        curr_bag.append(data.split("\n")[i])
    groups.append(curr_bag)
    for group in groups:
        common_obj = set(group[0]).intersection(group[1]).intersection(group[2])
        letter = list(common_obj)[0]
        
        # print("---------")
        # print(group)
        # print(letter)
        # print(VALUE.index(letter) + 1)
        
        sum += VALUE.index(letter) + 1
    return sum
print(main())

