import copy

# 'w' = wall
# 'f' = floor
# 'B' = FIRE (like Bonfire)
# 'C' = CAKE
# 'D' = DUNUT
# 'O' = ONI
the_map = [
    [['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]]],
    [['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['D', 3], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]]],
    [['f', [0.0, 0.0, 0.0, 0.0]], ['w', -1], ['w', -1], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]]],
    [['f', [0.0, 0.0, 0.0, 0.0]], ['B', -5], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['w', -1], ['w', -1], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]]],
    [['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['w', -1], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]]],
    [['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['w', -1], ['w', -1], ['w', -1], ['f', [0.0, 0.0, 0.0, 0.0]], ['C', 10], ['f', [0.0, 0.0, 0.0, 0.0]]],
    [['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['O', -10], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]]],
    [['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]], ['f', [0.0, 0.0, 0.0, 0.0]]]
]
gamma = 0.8

def print_the_map():
    print("+--------+--------+--------+--------+--------+--------+--------+--------+")
    for i in the_map:
        printed_string = "|"
        for j in i:
            if j[0] == 'w':
                printed_string += " ###### |"
            elif j[0] == 'f':
                printed_string += " %6.3f" % max(j[1]) + " |"
            elif j[0] == 'B':
                printed_string += "   FIRE |"
            elif j[0] == 'D':
                printed_string += "  DUNUT |"
            elif j[0] == 'C':
                printed_string += "   CAKE |"
            elif j[0] == 'O':
                printed_string += "    ONI |"
        print(printed_string)
    print("+--------+--------+--------+--------+--------+--------+--------+--------+")
    return


def print_policy():
    print("+--------+--------+--------+--------+--------+--------+--------+--------+")
    for i in the_map:
        printed_string = "|"
        for j in i:
            if j[0] == 'w':
                printed_string += " ###### |"
            elif j[0] == 'f':
                optimal = max(j[1])
                if j[1].index(optimal) == 0:
                    printed_string += "   ^    |"
                elif j[1].index(optimal) == 1:
                    printed_string += "   <    |"
                elif j[1].index(optimal) == 2:
                    printed_string += "   V    |"
                elif j[1].index(optimal) == 3:
                    printed_string += "   >    |"
            elif j[0] == 'B':
                printed_string += "   FIRE |"
            elif j[0] == 'D':
                printed_string += "  DUNUT |"
            elif j[0] == 'C':
                printed_string += "   CAKE |"
            elif j[0] == 'O':
                printed_string += "    ONI |"
        print(printed_string)
    print("+--------+--------+--------+--------+--------+--------+--------+--------+")

    return


def ValueIterate(n):
    global the_map
    for k in range(n):
        new_map = copy.deepcopy(the_map)
        for r in range(len(the_map)):
            for c in range(len(the_map[r])):
                for i in range(0, 4):
                    if the_map[r][c][0] == 'f':
                        # check upwards
                        uptmp = Prob((r - 1, c), (r, c), '^') * Value(r - 1, c)  # Up
                        uptmp += Prob((r, c - 1), (r, c), '^') * Value(r, c - 1)  # Left
                        uptmp += Prob((r, c + 1), (r, c), '^') * Value(r, c + 1)  # Right
                        uptmp += Prob((r + 1, c), (r, c), '^') * Value(r + 1, c)  # Down
                        new_map[r][c][1][0] = ExpRewards([r, c], '^') + gamma * uptmp
                        # valtmp = [uptmp, '^']

                        # check leftwards
                        lefttmp = Prob((r - 1, c), (r, c), '<') * Value(r - 1, c)  # Up
                        lefttmp += Prob((r, c - 1), (r, c), '<') * Value(r, c - 1)  # Left
                        lefttmp += Prob((r, c + 1), (r, c), '<') * Value(r, c + 1)  # Right
                        lefttmp += Prob((r + 1, c), (r, c), '<') * Value(r + 1, c)  # Down
                        new_map[r][c][1][1] = ExpRewards([r, c], '<') + gamma * lefttmp
                        # if valtmp[0] < lefttmp:
                        #     valtmp[0] = lefttmp
                        #     valtmp[1] = '<'

                        # check downwards
                        downtmp = Prob((r - 1, c), (r, c), 'V') * Value(r - 1, c)  # Up
                        downtmp += Prob((r, c - 1), (r, c), 'V') * Value(r, c - 1)  # Left
                        downtmp += Prob((r, c + 1), (r, c), 'V') * Value(r, c + 1)  # Right
                        downtmp += Prob((r + 1, c), (r, c), 'V') * Value(r + 1, c)  # Down
                        new_map[r][c][1][2] = ExpRewards([r, c], 'V') + gamma * downtmp
                        # if valtmp[0] < downtmp:
                        #     valtmp[0] = downtmp
                        #     valtmp[1] = 'V'

                        # check rightwards
                        righttmp = Prob((r - 1, c), (r, c), '>') * Value(r - 1, c)  # Up
                        righttmp += Prob((r, c - 1), (r, c), '>') * Value(r, c - 1)  # Left
                        righttmp += Prob((r, c + 1), (r, c), '>') * Value(r, c + 1)  # Right
                        righttmp += Prob((r + 1, c), (r, c), '>') * Value(r + 1, c)  # Down
                        new_map[r][c][1][3] = ExpRewards([r, c], '>') + gamma * righttmp
                        # if valtmp[0] < righttmp:
                        #     valtmp[0] = righttmp
                        #     valtmp[1] = '>'


                        # Record new optimized values
                        # new_map[r][c][1] = valtmp[0]
                        # new_map[r][c][2] = valtmp[1]
                        # new_map[r][c][i] = valtmp

        # OVerwrite previous map
        the_map = new_map

    return


def Prob(new_state, current_state, action):
    p = 0.0
    # if moving upwards
    if action == '^':
        if current_state[0] == new_state[0] + 1:
            p = 0.82
        elif current_state[1] == new_state[1] - 1 or current_state[1] == new_state[1] + 1:
            p = 0.09

    # if moving downwards
    elif action == 'V':
        if current_state[0] == new_state[0] - 1:
            p = 0.82
        elif current_state[1] == new_state[1] - 1 or current_state[1] == new_state[1] + 1:
            p = 0.09

    # if moving leftwards
    elif action == '<':
        if current_state[1] == new_state[1] + 1:
            p = 0.82
        elif current_state[0] == new_state[0] - 1 or current_state[0] == new_state[0] + 1:
            p = 0.09

    # if moving rightwards
    elif action == '>':
        if current_state[1] == new_state[1] - 1:
            p = 0.82
        elif current_state[0] == new_state[0] - 1 or current_state[0] == new_state[0] + 1:
            p = 0.09

    return p


def Value(r, c):
    if -1 < r < 8 and -1 < c < 8:
        # if the_map[r][c][1] > 0.0:  # and the_map[r][c][0] == 'f'
        #     return the_map[r][c][1]
        # else:
        #     return 0.0
        if the_map[r][c][0] != 'f':
            return the_map[r][c][1]
        else:
            return max(the_map[r][c][1])
    else:
        return -1.0


def ExpRewards(current_state, action):
    res = 0.0
    res += Prob([current_state[0] - 1, current_state[1]], current_state, action) * Reward([current_state[0] - 1, current_state[1]])
    res += Prob([current_state[0] + 1, current_state[1]], current_state, action) * Reward([current_state[0] + 1, current_state[1]])
    res += Prob([current_state[0], current_state[1] - 1], current_state, action) * Reward([current_state[0], current_state[1] - 1])
    res += Prob([current_state[0], current_state[1] + 1], current_state, action) * Reward([current_state[0], current_state[1] + 1])
    return res


def Reward(new_state):
    if new_state[0] < 0 or new_state[0] > 7 or new_state[1] < 0 or new_state[1] > 7:
        return -1.0
    elif the_map[new_state[0]][new_state[1]][0] == 'C':
        return 10.0
    elif the_map[new_state[0]][new_state[1]][0] == 'D':
        return 3.0
    elif the_map[new_state[0]][new_state[1]][0] == 'B':
        return -5.0
    elif the_map[new_state[0]][new_state[1]][0] == 'O':
        return -10.0
    elif the_map[new_state[0]][new_state[1]][0] == 'w':
        return -1.0
    else:
        return 0.0


if __name__ == "__main__":
    count = 0
    print("CS-5001: HW#2")
    print("Programmer: Peter Dolan")
    print("Discount Gamma = {}\r\n".format(gamma))
    n = int(input("Enter No of Iterations: "))
    while n > 0:
        ValueIterate(n)
        count += n
        print("\r\nValues after {0} iterations:\r\n".format(count))
        print_the_map()
        n = int(input("\r\nEnter No of Iterations: "))
    print("\r\nPolicy:\r\n")
    print_policy()
