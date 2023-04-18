
#  []
def main():
    with open('data.txt') as f:
        data = f.read().split('\n')

    n_cycle = 0
    sum = 0
    register = 1

    for operation in data:
        n_cycle += 1

        if n_cycle in [20, 60, 100, 140, 180, 220]:
            sum += n_cycle * register
            print(n_cycle)

        if "addx" in operation:

            n_cycle += 1
            # fast & ugly
            if n_cycle in [20, 60, 100, 140, 180, 220]:
                sum += n_cycle * register
                print(n_cycle)

            register += int(operation.split(" ")[1])

    print(sum)
main()