def main():
    with open('data.txt') as f:
        data = f.read()

    sum = 0
    for game in data.split("\n"):
        if game == "":
            continue
        game = game.split(" ")
        opponent = game[0]
        your_choice = game[1]

        if your_choice == "X": # ROCK
            sum += 1

            if opponent == "A": # ROCK
                sum += 3 # DRAW
            if opponent == "B": # PAPER
                sum += 0 # LOOSE
            if opponent == "C": # SCISSOR
                sum += 6 # WIN
        elif your_choice == "Y": # PAPER
            sum += 2

            if opponent == "A": # ROCK
                sum += 6 # WIN
            if opponent == "B": # PAPER
                sum += 3 # DRAW
            if opponent == "C": # SCISSOR
                sum += 0 # LOOSE

        elif your_choice == "Z": # SCISSOR
            sum += 3

            if opponent == "A": # ROCK
                sum += 0 # LOOSE
            if opponent == "B": # PAPER
                sum += 6 # WIN
            if opponent == "C": # SCISSOR
                sum += 3 # DRAW

    return sum

print(main())