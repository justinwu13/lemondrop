import numpy as np
from prettytable import PrettyTable

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

x_value_dict = {0: 1} # contains expected values for every game state. start with won game state w/ expected value 1

od_2 = [0] # optimal decisions for rolling 2
od_3 = [0] # optimal decisions for rolling 3
od_4 = [0] # optimal decisions for rolling 4
od_5 = [0] # optimal decisions for rolling 5
od_6 = [0] # optimal decisions for rolling 6
od_7 = [0] # optimal decisions for rolling 7
od_8 = [0] # optimal decisions for rolling 8
od_9 = [0] # optimal decisions for rolling 9
od_10 = [0] # optimal decisions for rolling 10
od_11 = [0] # optimal decisions for rolling 11
od_12 = [0] # optimal decisions for rolling 12

def int_to_bin(int):
    return f'{int:012b}'

def get_x_values(state): # returns the possible x_values for each roll. Index 2 = xValue if a 2 is rolled with the current state, etc.
    drop_state = int_to_bin(state)
    x_values = [0, 0]
    
    # if you roll 2
    if drop_state[1] == '1': # 2 available
        x_values.append(get_x_value(state - 1024))
        od_2.append('2')
    else: # you lose
        x_values.append(0)
        od_2.append('0')
    
    # if you roll 3
    move_names_3 = ['0', '1 2', '3']
    possible_moves_3 = [0]
    if drop_state[0] == '1' and drop_state[1] == '1': # 1 and 2 available
        possible_moves_3.append(get_x_value(state - 3072))
    else:
        possible_moves_3.append(0)

    if drop_state[2] == '1': # 3 available
        possible_moves_3.append(get_x_value(state - 512))
    else:
        possible_moves_3.append(0)

    x_values.append(np.max(possible_moves_3))
    ind3 = possible_moves_3.index(np.max(possible_moves_3))
    od_3.append(move_names_3[ind3])

    # if you roll 4
    move_names_4 = ['0', '1 3', '4']
    possible_moves_4 = [0]
    if drop_state[0] == '1' and drop_state[2] == '1': # 1 and 3 available
        possible_moves_4.append(get_x_value(state - 2560))
    else:
        possible_moves_4.append(0)
        
    if drop_state[3] == '1': # 4 available
        possible_moves_4.append(get_x_value(state - 256))
    else:
        possible_moves_4.append(0)
        
    x_values.append(np.max(possible_moves_4))
    ind4 = possible_moves_4.index(np.max(possible_moves_4))
    od_4.append(move_names_4[ind4])

    # if you roll 5
    move_names_5 = ['0', '1 4', '2 3', '5']
    possible_moves_5 = [0]
    if drop_state[0] == '1' and drop_state[3] == '1': # 1 and 4 available
        possible_moves_5.append(get_x_value(state - 2304))
    else:
        possible_moves_5.append(0)

    if drop_state[1] == '1' and drop_state[2] == '1': # 2 and 3 available
        possible_moves_5.append(get_x_value(state - 1536))
    else:
        possible_moves_5.append(0)

    if drop_state[4] == '1': # 5 available
        possible_moves_5.append(get_x_value(state - 128))
    else:
        possible_moves_5.append(0)

    x_values.append(np.max(possible_moves_5))
    ind5 = possible_moves_5.index(np.max(possible_moves_5))
    od_5.append(move_names_5[ind5])

    # if you roll 6
    move_names_6 = ['0', '1 5', '2 4', '6']
    possible_moves_6 = [0]
    if drop_state[0] == '1' and drop_state[4] == '1': # 1 and 5 available
        possible_moves_6.append(get_x_value(state - 2176))
    else:
        possible_moves_6.append(0)

    if drop_state[1] == '1' and drop_state[3] == '1': # 2 and 4 available
        possible_moves_6.append(get_x_value(state - 1280))
    else:
        possible_moves_6.append(0)

    if drop_state[5] == '1': # 6 available
        possible_moves_6.append(get_x_value(state - 64))
    else:
        possible_moves_6.append(0)

    x_values.append(np.max(possible_moves_6))
    ind6 = possible_moves_6.index(np.max(possible_moves_6))
    od_6.append(move_names_6[ind6])

    # if you roll 7
    move_names_7 = ['0', '1 6', '2 5', '3 4', '7']
    possible_moves_7 = [0]
    if drop_state[0] == '1' and drop_state[5] == '1': # 1 and 6 available
        possible_moves_7.append(get_x_value(state - 2112))
    else:
        possible_moves_7.append(0)

    if drop_state[1] == '1' and drop_state[4] == '1': # 2 and 5 available
        possible_moves_7.append(get_x_value(state - 1152))
    else:
        possible_moves_7.append(0)

    if drop_state[2] == '1' and drop_state[3] == '1': # 3 and 4 available
        possible_moves_7.append(get_x_value(state - 768))
    else:
        possible_moves_7.append(0)
    
    if drop_state[6] == '1': # 7 available
        possible_moves_7.append(get_x_value(state - 32))
    else:
        possible_moves_7.append(0)

    x_values.append(np.max(possible_moves_7))
    ind7 = possible_moves_7.index(np.max(possible_moves_7))
    od_7.append(move_names_7[ind7])

    # if you roll 8
    move_names_8 = ['0', '1 7', '2 6', '3 5', '8']
    possible_moves_8 = [0]
    if drop_state[0] == '1' and drop_state[6] == '1': # 1 and 7 available
        possible_moves_8.append(get_x_value(state - 2080))
    else:
        possible_moves_8.append(0)
    
    if drop_state[1] == '1' and drop_state[5] == '1': # 2 and 6 available
        possible_moves_8.append(get_x_value(state - 1088))
    else:
        possible_moves_8.append(0)

    if drop_state[2] == '1' and drop_state[4] == '1': # 3 and 5 available
        possible_moves_8.append(get_x_value(state - 640))
    else:
        possible_moves_8.append(0)

    if drop_state[7] == '1': # 8 available
        possible_moves_8.append(get_x_value(state - 16))
    else:
        possible_moves_8.append(0)

    x_values.append(np.max(possible_moves_8))
    ind8 = possible_moves_8.index(np.max(possible_moves_8))
    od_8.append(move_names_8[ind8])

    # if you roll 9
    move_names_9 = ['0', '1 8', '2 7', '3 6', '4 5', '9']
    possible_moves_9 = [0]
    if drop_state[0] == '1' and drop_state[7] == '1': # 1 and 8 available
        possible_moves_9.append(get_x_value(state - 2064))
    else:
        possible_moves_9.append(0)

    if drop_state[1] == '1' and drop_state[6] == '1': # 2 and 7 available
        possible_moves_9.append(get_x_value(state - 1056))
    else:
        possible_moves_9.append(0)

    if drop_state[2] == '1' and drop_state[5] == '1': # 3 and 6 available
        possible_moves_9.append(get_x_value(state - 576))
    else:
        possible_moves_9.append(0)

    if drop_state[3] == '1' and drop_state[4] == '1': # 4 and 5 available
        possible_moves_9.append(get_x_value(state - 384))
    else:
        possible_moves_9.append(0)

    if drop_state[8] == '1': # 9 available
        possible_moves_9.append(get_x_value(state - 8))
    else:
        possible_moves_9.append(0)

    x_values.append(np.max(possible_moves_9))
    ind9 = possible_moves_9.index(np.max(possible_moves_9))
    od_9.append(move_names_9[ind9])

    # if you roll 10
    move_names_10 = ['0', '1 9', '2 8', '3 7', '4 6', '10']
    possible_moves_10 = [0]
    if drop_state[0] == '1' and drop_state[8] == '1': # 1 and 9 available
        possible_moves_10.append(get_x_value(state - 2056))
    else:
        possible_moves_10.append(0)

    if drop_state[1] == '1' and drop_state[7] == '1': # 2 and 8 available
        possible_moves_10.append(get_x_value(state - 1040))
    else:
        possible_moves_10.append(0)

    if drop_state[2] == '1' and drop_state[6] == '1': # 3 and 7 available
        possible_moves_10.append(get_x_value(state - 544))
    else:
        possible_moves_10.append(0)

    if drop_state[3] == '1' and drop_state[5] == '1': # 4 and 6 available
        possible_moves_10.append(get_x_value(state - 320))
    else:
        possible_moves_10.append(0)

    if drop_state[9] == '1': # 10 available
        possible_moves_10.append(get_x_value(state - 4))
    else:
        possible_moves_10.append(0)

    x_values.append(np.max(possible_moves_10))
    ind10 = possible_moves_10.index(np.max(possible_moves_10))
    od_10.append(move_names_10[ind10])

    # if you roll 11
    move_names_11 = ['0', '1 10', '2 9', '3 8', '4 7', '5 6', '11']
    possible_moves_11 = [0]
    if drop_state[0] == '1' and drop_state[9] == '1': # 1 and 10 available
        possible_moves_11.append(get_x_value(state - 2052))
    else:
        possible_moves_11.append(0)

    if drop_state[1] == '1' and drop_state[8] == '1': # 2 and 9 available
        possible_moves_11.append(get_x_value(state - 1032))
    else:
        possible_moves_11.append(0)

    if drop_state[2] == '1' and drop_state[7] == '1': # 3 and 8 available
        possible_moves_11.append(get_x_value(state - 528))
    else:
        possible_moves_11.append(0)

    if drop_state[3] == '1' and drop_state[6] == '1': # 4 and 7 available
        possible_moves_11.append(get_x_value(state - 288))
    else:
        possible_moves_11.append(0)
        
    if drop_state[4] == '1' and drop_state[5] == '1': # 5 and 6 available
        possible_moves_11.append(get_x_value(state - 192))
    else:
        possible_moves_11.append(0)

    if drop_state[10] == '1': # 11 available
        possible_moves_11.append(get_x_value(state - 2))
    else:
        possible_moves_11.append(0)

    x_values.append(np.max(possible_moves_11))
    ind11 = possible_moves_11.index(np.max(possible_moves_11))
    od_11.append(move_names_11[ind11])

    # if you roll 12
    move_names_12 = ['0', '1 11', '2 10', '3 9', '4 8', '5 7', '12']
    possible_moves_12 = [0]
    if drop_state[0] == '1' and drop_state[10] == '1': # 1 and 11 available
        possible_moves_12.append(get_x_value(state - 2050))
    else:
        possible_moves_12.append(0)

    if drop_state[1] == '1' and drop_state[9] == '1': # 2 and 10 available
        possible_moves_12.append(get_x_value(state - 1028))
    else:
        possible_moves_12.append(0)

    if drop_state[2] == '1' and drop_state[8] == '1': # 3 and 9 available
        possible_moves_12.append(get_x_value(state - 520))
    else:
        possible_moves_12.append(0)

    if drop_state[3] == '1' and drop_state[7] == '1': # 4 and 8 available
        possible_moves_12.append(get_x_value(state - 272))
    else:
        possible_moves_12.append(0)

    if drop_state[4] == '1' and drop_state[6] == '1': # 5 and 7 available
        possible_moves_12.append(get_x_value(state - 160))
    else:
        possible_moves_12.append(0)

    if drop_state[11] == '1': # 12 available
        possible_moves_12.append(get_x_value(state - 1))
    else:
        possible_moves_12.append(0)

    x_values.append(np.max(possible_moves_12))
    ind12 = possible_moves_12.index(np.max(possible_moves_12))
    od_12.append(move_names_12[ind12])
    
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

# place results into a list and write to a text file
file = open('dropsolver.txt', 'w')
x_val_list = [1]

for i in range(1, 4096):
    x_val_list.append(calc_x_value(i))

# format table
t = PrettyTable(['Drop State', 'Expected Value', 'Dice Sum = 2', 'Dice Sum = 3', 'Dice Sum = 4', 'Dice Sum = 5', 
                 'Dice Sum = 6', 'Dice Sum = 7', 'Dice Sum = 8', 'Dice Sum = 9', 'Dice Sum = 10', 'Dice Sum = 11', 
                 'Dice Sum = 12'])
for j in range(0, 4096):
    i = 4095 - j
    t.add_row([int_to_bin(i), x_val_list[i], od_2[i], od_3[i], od_4[i], od_5[i], od_6[i], od_7[i], od_8[i], 
               od_9[i], od_10[i], od_11[i], od_12[i]])

file.write(str(t))
file.close()