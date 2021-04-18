maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]


def search(pos: (int, int), maze: list):
    maze_str = []
    for string in maze:
        maze_str.append(list(string))

    def get(position: (int, int), lab: list):
        return lab[position[1]][position[0]]

    def set(position: (int, int), lab: list, value):
        lab[position[1]][position[0]] = value

    if pos[0] < 0 or pos[0] >= len(maze_str) or pos[1] < 0 or pos[1] >= len(maze_str[0]) or get(pos, maze_str) == '#':
        print('Не верные координаты')
        return

    exits = []

    def search_req(pos: (int, int), lab: list):
        cell = get(pos, lab)
        if cell == '#':
            return
        if cell == ' ':
            new_maze_str = lab.copy()
            set(pos, new_maze_str, '#')
            search_req((pos[0] + 1, pos[1]), new_maze_str)
            search_req((pos[0] - 1, pos[1]), new_maze_str)
            search_req((pos[0], pos[1] + 1), new_maze_str)
            search_req((pos[0], pos[1] - 1), new_maze_str)
            return
        exits.append(cell)

    search_req(pos, maze_str)

    if len(exits) > 0:
        for i in exits:
            print(i, end=' ')
        print()
    else:
        print('Выхода нет')


x, y = map(int, input("Введите данные: ").split(' '))
search((x, y), maze)
