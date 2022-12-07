def main():
    with open("data.txt") as f:
        data = f.read().splitlines()
    sum = 0
    for i in range(len(data)):
        data[i] = [data[i].split(",")[0], data[i].split(",")[1]]
        data[i][0] = [k for k in range(int(data[i][0].split(",")[0].split("-")[0]), int(data[i][0].split(",")[0].split("-")[1]) + 1 )]
        data[i][1] = [k for k in range(int(data[i][1].split(",")[0].split("-")[0]), int(data[i][1].split(",")[0].split("-")[1]) + 1 )]

        if check_if_list_of_integer_is_contained_in_list_of_integer(data[i][0], data[i][1]) or check_if_list_of_integer_is_contained_in_list_of_integer(data[i][1], data[i][0]):
            sum += 1
    print(sum)
def check_if_list_of_integer_is_contained_in_list_of_integer(list_of_integer_1, list_of_integer_2):
    for i in list_of_integer_1:
        if i not in list_of_integer_2:
            return False
    return True
main()