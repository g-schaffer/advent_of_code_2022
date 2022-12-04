def main():
    with open('data.txt') as f:
        lines = f.read()
        elves = lines.split("\n\n")
        sum_elves = list()
        for elve in elves:
            s = 0
            for l in elve.split("\n"):
                if l != "":
                    s += int(l)
            sum_elves.append(s)

        return max(sum_elves)
print(main())

