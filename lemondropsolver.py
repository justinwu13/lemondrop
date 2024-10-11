from prettytable import PrettyTable

target_name = 'dropsolver.txt' # name of results file that will be written to

# dictionary of probabilities of rolling each sum of two dice. will be used as weights to calculate expected values of each state
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

# a 2d list of all optimal decisions for each roll. optimal_decisions[roll] = list of optimal decisions for that roll
# optimal_decisions[roll][state] = optimal decision for a specific state and roll
optimal_decisions = [] 

for i in range(0, 13): # first two lists will stay empty as you cannot roll 0 or 1. next 11 lists will contain optimal decisions for rolls 2-12
    optimal_decisions.append([[0]]) # add [0] move at pos 0 to all lists as the finished game state (state = 0) is won

def get_valid_moves(roll): # returns a list of all possible moves for a given roll. each element is a valid move, represented as a list of either 1 or 2 ints
    moves = [[0], [roll]] # [0] move exists in case there are no other valid moves - if it's the only move, you lose
    i = 1
    while i < roll / 2:
        j = roll - i
        moves.append([i, j])
        i += 1
    return moves

def int_to_bin(int):
    return f'{int:012b}'

def calc_x_value(drop_state):
    x_values = get_x_values(drop_state)
    sum = 0
    for i in range(2, 13): # calculate expected value of a state with weighted sum of probabilities and expected values after each roll
        sum += (prob_dict[i] * x_values[i])
    return sum

def get_x_value(drop_state): # drop_state: an int that represents the current state of the lemondrops when converted to binary
    return x_value_dict.get(drop_state)

def get_x_values(state): # returns a list of expected values for each roll. Index 2 = x_value if a 2 is rolled with the current state, etc.
    drop_state = int_to_bin(state)
    x_values = [0, 0] # not possible to roll 0 or 1, so set those values to 0
    
    for roll in range(2, 13):
        valid_moves = get_valid_moves(roll)
        possible_moves = [] # expected values of all possible moves for roll
        for move in valid_moves:
            if move == [0]: # expected value for a lost position = 0
                possible_moves.append(0)
                continue
            move_valid = True 
            for i in move: # check validity by checking if any number needed is unavailable (corresponding bit in drop_state = 0)
                if drop_state[i - 1] == '0': # move is invalid
                    possible_moves.append(0)
                    move_valid = False
                    break
            if move_valid:
                next_state = state
                for i in move: # determine the next state if you play this move: reset corresponding bits of state
                    next_state = next_state - 2**(12 - i) 
                possible_moves.append(get_x_value(next_state)) # get expected value by checking expected value of next state
        x_values.append(max(possible_moves)) # take max to get the expected value of the optimal move for the roll
        optimal_decisions[roll].append(valid_moves[possible_moves.index(max(possible_moves))])

    return x_values

# iterate through all possible game states, starting from next simplest after the win state
for i in range(1, 4096): 
    x_value_dict[i] = calc_x_value(i)

# make a table and write results into a text file
file = open(target_name, 'w')

def format_move(move):
    move_str = ''
    for i in move:
        move_str += str(i) + ' '
    return move_str

t = PrettyTable(['Drop State', 'Expected Value', 'Dice Sum = 2', 'Dice Sum = 3', 'Dice Sum = 4', 'Dice Sum = 5', 
                 'Dice Sum = 6', 'Dice Sum = 7', 'Dice Sum = 8', 'Dice Sum = 9', 'Dice Sum = 10', 'Dice Sum = 11', 
                 'Dice Sum = 12'])
for j in range(0, 4096):
    i = 4095 - j # go through game states from most complex to simplest
    t.add_row([int_to_bin(i), x_value_dict[i]] + [format_move(optimal_decisions[k][i]) for k in range(2, 13)])

file.write(str(t))
file.close()
