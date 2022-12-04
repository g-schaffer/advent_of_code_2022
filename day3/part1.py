VALUE = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()
def main():
    with open('data.txt') as f:
        data = f.read()
    sum = 0
    for bag in data.split("\n"):
        bag1 = bag[:len(bag)//2]
        bag2 = bag[len(bag)//2:]

        common_obj = set(bag1).intersection(bag2)
        letter = list(common_obj)[0]
        
        # print("------------")
        # print(letter)
        # print(VALUE.index(letter))
        
        sum += VALUE.index(letter) + 1
    return sum
print(main())

