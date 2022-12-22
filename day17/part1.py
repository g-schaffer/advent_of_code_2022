
# #  []
# def main():
#     with open('data.txt') as f:
#         data = list(f.read())

#     arr = [0, 0, 0, 0, 0, 0, 0]
#     pos = [0, 0, 3, 3, 3, 3, 0]
#     size = 0
#     starting_pos = size + 3
#     curr_obj = 0
#     while data:
#         print(data.pop(0), end=' ')
        
#         if curr_obj_is_touching():
#             # changer curr obj
#             # mettre à jour arr
#             starting_pos = size + 3
#             curr_obj = (curr_obj + 1) % 5
#             arr = change_arr(arr, curr_obj, touching_pos)
#         else:

# main()


#  []
def main():
    with open('data.txt') as f:
        data = list(f.read())

    arr = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    
    while data:
        move = data.pop(0)
        
        if curr_obj_is_touching():
            # changer curr obj
            # mettre à jour arr
            starting_pos = size + 3
            curr_obj = (curr_obj + 1) % 5
            arr = change_arr(arr, curr_obj, touching_pos)
        else:

main()