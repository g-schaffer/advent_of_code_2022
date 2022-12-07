def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
    sum = 0
    for i in range(len(data)):
        data[i] = [data[i].split(",")[0], data[i].split(",")[1]]
        data[i][0] = [k for k in range(int(data[i][0].split(",")[0].split("-")[0]), int(data[i][0].split(",")[0].split("-")[1]) + 1 )]
        data[i][1] = [k for k in range(int(data[i][1].split(",")[0].split("-")[0]), int(data[i][1].split(",")[0].split("-")[1]) + 1 )]
        print(data[i])
        inter = 0 < len(intersection_of_2_list_of_integer(data[i][0], data[i][1]))
        if inter:
            sum += 1
    print(sum)
def intersection_of_2_list_of_integer(list_of_integer_1, list_of_integer_2):
    return [i for i in list_of_integer_1 if i in list_of_integer_2]
main()

