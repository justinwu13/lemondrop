import numpy as np

# dice roll | prob
# 1         | 0
# 2         | 0.0277
# 3         | 0.0555
# 4         | 0.0833
# 5         | 0.1111
# 6         | 0.1388
# 7         | 0.1666
# 8         | 0.1388
# 9         | 0.1111
# 10        | 0.0833
# 11        | 0.0555
# 12        | 0.0277

prob_dict = {2: 1/36, 
             3: 2/36, 
             4: 3/36, 
             5: 4/36, 
             6: 5/36, 
             7: 6/36, 
             8: 5/36, 
             9: 4/36, 
             10: 3/36, 
             11: 2/36, 
             12: 1/36}

x_value_dict = {0: 1}

def int_to_bin(int): # retrieves the binary representation of game state (1 for available, 0 for unavailable)
    return f'{int:012b}'

def get_x_values(state): # returns the possible x_values (expected values) for each roll. Index 2 = xValue if a 2 is rolled with the current state, etc.
    drop_state = int_to_bin(state)
    x_values = [0, 0]
    
    # if you roll 2
    if drop_state[1] == '1': # 2 available
        x_values.append(get_x_value(state - 1024))
    else:
        x_values.append(0)
    
    # if you roll 3
    possible_moves_3 = [0]
    if drop_state[0] == '1' and drop_state[1] == '1': # 1 and 2 available
        possible_moves_3.append(get_x_value(state - 3072))
    if drop_state[2] == '1': # 3 available
        possible_moves_3.append(get_x_value(state - 512))
    x_values.append(np.max(possible_moves_3))

    # if you roll 4
    possible_moves_4 = [0]
    if drop_state[0] == '1' and drop_state[2] == '1': # 1 and 3 available
        possible_moves_4.append(get_x_value(state - 2560))
    if drop_state[3] == '1': # 4 available
        possible_moves_4.append(get_x_value(state - 256))
    x_values.append(np.max(possible_moves_4))

    # if you roll 5
    possible_moves_5 = [0]
    if drop_state[0] == '1' and drop_state[3] == '1': # 1 and 4 available
        possible_moves_5.append(get_x_value(state - 2304))
    if drop_state[1] == '1' and drop_state[2] == '1': # 2 and 3 available
        possible_moves_5.append(get_x_value(state - 1536))
    if drop_state[4] == '1': # 5 available
        possible_moves_5.append(get_x_value(state - 128))
    x_values.append(np.max(possible_moves_5))

    # if you roll 6
    possible_moves_6 = [0]
    if drop_state[0] == '1' and drop_state[4] == '1': # 1 and 5 available
        possible_moves_6.append(get_x_value(state - 2176))
    if drop_state[1] == '1' and drop_state[3] == '1': # 2 and 4 available
        possible_moves_6.append(get_x_value(state - 1280))
    if drop_state[5] == '1': # 6 available
        possible_moves_6.append(get_x_value(state - 64))
    x_values.append(np.max(possible_moves_6))

    # if you roll 7
    possible_moves_7 = [0]
    if drop_state[0] == '1' and drop_state[5] == '1': # 1 and 6 available
        possible_moves_7.append(get_x_value(state - 2112))
    if drop_state[1] == '1' and drop_state[4] == '1': # 2 and 5 available
        possible_moves_7.append(get_x_value(state - 1152))
    if drop_state[2] == '1' and drop_state[3] == '1': # 3 and 4 available
        possible_moves_7.append(get_x_value(state - 768))
    if drop_state[6] == '1': # 7 available
        possible_moves_7.append(get_x_value(state - 32))
    x_values.append(np.max(possible_moves_7))

    # if you roll 8
    possible_moves_8 = [0]
    if drop_state[0] == '1' and drop_state[6] == '1': # 1 and 7 available
        possible_moves_8.append(get_x_value(state - 2080))
    if drop_state[1] == '1' and drop_state[5] == '1': # 2 and 6 available
        possible_moves_8.append(get_x_value(state - 1088))
    if drop_state[2] == '1' and drop_state[4] == '1': # 3 and 5 available
        possible_moves_8.append(get_x_value(state - 640))
    if drop_state[7] == '1': # 8 available
        possible_moves_8.append(get_x_value(state - 16))
    x_values.append(np.max(possible_moves_8))

    # if you roll 9
    possible_moves_9 = [0]
    if drop_state[0] == '1' and drop_state[7] == '1': # 1 and 8 available
        possible_moves_9.append(get_x_value(state - 2064))
    if drop_state[1] == '1' and drop_state[6] == '1': # 2 and 7 available
        possible_moves_9.append(get_x_value(state - 1056))
    if drop_state[2] == '1' and drop_state[5] == '1': # 3 and 6 available
        possible_moves_9.append(get_x_value(state - 576))
    if drop_state[3] == '1' and drop_state[4] == '1': # 4 and 5 available
        possible_moves_9.append(get_x_value(state - 384))
    if drop_state[8] == '1': # 9 available
        possible_moves_9.append(get_x_value(state - 8))
    x_values.append(np.max(possible_moves_9))

    # if you roll 10
    possible_moves_10 = [0]
    if drop_state[0] == '1' and drop_state[8] == '1': # 1 and 9 available
        possible_moves_10.append(get_x_value(state - 2056))
    if drop_state[1] == '1' and drop_state[7] == '1': # 2 and 8 available
        possible_moves_10.append(get_x_value(state - 1040))
    if drop_state[2] == '1' and drop_state[6] == '1': # 3 and 7 available
        possible_moves_10.append(get_x_value(state - 544))
    if drop_state[3] == '1' and drop_state[5] == '1': # 4 and 6 available
        possible_moves_10.append(get_x_value(state - 320))
    if drop_state[9] == '1': # 10 available
        possible_moves_10.append(get_x_value(state - 4))
    x_values.append(np.max(possible_moves_10))

    # if you roll 11
    possible_moves_11 = [0]
    if drop_state[0] == '1' and drop_state[9] == '1': # 1 and 10 available
        possible_moves_11.append(get_x_value(state - 2052))
    if drop_state[1] == '1' and drop_state[8] == '1': # 2 and 9 available
        possible_moves_11.append(get_x_value(state - 1032))
    if drop_state[2] == '1' and drop_state[7] == '1': # 3 and 8 available
        possible_moves_11.append(get_x_value(state - 528))
    if drop_state[3] == '1' and drop_state[6] == '1': # 4 and 7 available
        possible_moves_11.append(get_x_value(state - 288))
    if drop_state[4] == '1' and drop_state[5] == '1': # 5 and 6 available
        possible_moves_11.append(get_x_value(state - 192))
    if drop_state[10] == '1': # 11 available
        possible_moves_11.append(get_x_value(state - 2))
    x_values.append(np.max(possible_moves_11))

    # if you roll 12
    possible_moves_12 = [0]
    if drop_state[0] == '1' and drop_state[10] == '1': # 1 and 11 available
        possible_moves_12.append(get_x_value(state - 2050))
    if drop_state[1] == '1' and drop_state[9] == '1': # 2 and 10 available
        possible_moves_12.append(get_x_value(state - 1028))
    if drop_state[2] == '1' and drop_state[8] == '1': # 3 and 9 available
        possible_moves_12.append(get_x_value(state - 520))
    if drop_state[3] == '1' and drop_state[7] == '1': # 4 and 8 available
        possible_moves_12.append(get_x_value(state - 272))
    if drop_state[4] == '1' and drop_state[6] == '1': # 5 and 7 available
        possible_moves_12.append(get_x_value(state - 160))
    if drop_state[11] == '1': # 11 available
        possible_moves_12.append(get_x_value(state - 1))
    x_values.append(np.max(possible_moves_12))
    
    return x_values

def calc_x_value(drop_state):
    x_values = get_x_values(drop_state)
    sum = 0
    for i in range(2, 13):
        sum += (prob_dict[i] * x_values[i])
    return sum

def get_x_value(drop_state): # drop_state: an int that represents the current state of the lemondrops when converted to binary
    return x_value_dict.get(drop_state)

for i in range(1, 4096):
    x_value_dict[i] = calc_x_value(i)

file = open("dropsodds.txt", "w")

for i in range(0, 4096):
    file.write(f"{int_to_bin(i)} | {x_value_dict[i]}\n")

file.close()