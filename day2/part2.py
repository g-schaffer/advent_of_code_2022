def main():
    with open('data.txt') as f:
        data = f.read()

    sum = 0
    for game in data.split("\n"):
        if game == "":
            continue
        game = game.split(" ")
        opponent = game[0]
        your_score = game[1]

        if your_score == "X": # YOU LOOSE
            sum += 0

            if opponent == "A": # ROCK
                sum += 3 # YOU PLAYED SCISSOR
            if opponent == "B": # PAPER
                sum += 1 # YOU PLAYED ROCK
            if opponent == "C": # SCISSOR
                sum += 2 # YOU PLAYED PAPER
        elif your_score == "Y": # YOU DRAW
            sum += 3

            if opponent == "A": # ROCK
                sum += 1 # YOUR PLAYED ROCK
            if opponent == "B": # PAPER
                sum += 2 # YOU PLAYED PAPER
            if opponent == "C": # SCISSOR
                sum += 3 # YOU PLAYED SCISSOR

        elif your_score == "Z": # YOU WIN
            sum += 6

            if opponent == "A": # ROCK
                sum += 2 # YOU PLAYED PAPER
            if opponent == "B": # PAPER
                sum += 3 # YOU PLAYED SCISSOR
            if opponent == "C": # SCISSOR
                sum += 1 # YOU PLAYED ROCK

    return sum

print(main())