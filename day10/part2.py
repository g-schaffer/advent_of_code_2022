
#  []
def main():
    with open('data.txt') as f:
        data = f.read()

    moves = [[k.split(" ")[0], int(k.split(" ")[1])] for k in data.split("\n")]

    tail_all_pos = []

    rope = {
        0: {"x": 0, "y": 0},
        1: {"x": 0, "y": 0},
        2: {"x": 0, "y": 0},
        3: {"x": 0, "y": 0},
        4: {"x": 0, "y": 0},
        5: {"x": 0, "y": 0},
        6: {"x": 0, "y": 0},
        7: {"x": 0, "y": 0},
        8: {"x": 0, "y": 0},
        9: {"x": 0, "y": 0},
    }
    rope_length = 10
    
    for move in moves:
        
        
        for i in range(move[1]):
            last_pos = rope[0].copy()
            if move[0] == "R":
                rope[0]["y"] += 1
            elif move[0] == "L":
                rope[0]["y"] -= 1
            elif move[0] == "U":
                rope[0]["x"] += 1
            elif move[0] == "D":
                rope[0]["x"] -= 1
            
            for i in range(0, rope_length - 1):
                if not adjacent(rope[i + 1], rope[i]):
                    rope[i + 1], last_pos = last_pos, rope[i + 1]
                         

            tail_all_pos.append(str(rope[9]["x"]) + " " + str(rope[9]["y"]))


    print(len(list(dict.fromkeys(tail_all_pos))))
            

def adjacent(head, tail):
    return abs(head["x"] - tail["x"]) <= 1 and abs(head["y"] - tail["y"]) <= 1


main()

