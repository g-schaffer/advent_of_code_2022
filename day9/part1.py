
#  []
def main():
    with open('data.txt') as f:
        data = f.read()

    moves = [[k.split(" ")[0], int(k.split(" ")[1])] for k in data.split("\n")]
    head = {"x": 0, "y": 0}
    tail = {"x": 0, "y": 0}
    tail_all_pos = []
    for move in moves:
        for i in range(move[1]):
            last_pos_head = head.copy()
            if move[0] == "R":
                head["y"] += 1
            elif move[0] == "L":
                head["y"] -= 1
            elif move[0] == "U":
                head["x"] += 1
            elif move[0] == "D":
                head["x"] -= 1
            
            if not is_adjacent(head, tail):
                tail = last_pos_head

            tail_all_pos.append(str(tail["x"]) + " " + str(tail["y"]))
    
    # remove duplicates from tail_all_pos
    tail_all_pos = list(dict.fromkeys(tail_all_pos))
            

    print(len(tail_all_pos))
def is_adjacent(head, tail):
    return abs(head["x"] - tail["x"]) <= 1 and abs(head["y"] - tail["y"]) <= 1

main()