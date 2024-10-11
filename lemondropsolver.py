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

xValueDict = {0: 1} # contains expected values for every game state. start with won game state w/ expected value 1

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

def intToBinary(int):
    return f'{int:012b}'

def getXValues(state): # returns the possible xValues for each roll. Index 2 = xValue if a 2 is rolled with the current state, etc.
    dropState = intToBinary(state)
    xValues = [0, 0]
    
    # if you roll 2
    if dropState[1] == '1': # 2 available
        xValues.append(getXValue(state - 1024))
        od_2.append("2")
    else:
        xValues.append(0)
        od_2.append("0")
    
    # if you roll 3
    movenames3 = ["0", "1 2", "3"]
    possibleMoves3 = [0]
    if dropState[0] == '1' and dropState[1] == '1': # 1 and 2 available
        possibleMoves3.append(getXValue(state - 3072))
    else:
        possibleMoves3.append(0)

    if dropState[2] == '1': # 3 available
        possibleMoves3.append(getXValue(state - 512))
    else:
        possibleMoves3.append(0)

    xValues.append(np.max(possibleMoves3))
    ind3 = possibleMoves3.index(np.max(possibleMoves3))
    od_3.append(movenames3[ind3])

    # if you roll 4
    movenames4 = ["0", "1 3", "4"]
    possibleMoves4 = [0]
    if dropState[0] == '1' and dropState[2] == '1': # 1 and 3 available
        possibleMoves4.append(getXValue(state - 2560))
    else:
        possibleMoves4.append(0)
        
    if dropState[3] == '1': # 4 available
        possibleMoves4.append(getXValue(state - 256))
    else:
        possibleMoves4.append(0)
        
    xValues.append(np.max(possibleMoves4))
    ind4 = possibleMoves4.index(np.max(possibleMoves4))
    od_4.append(movenames4[ind4])

    # if you roll 5
    movenames5 = ["0", "1 4", "2 3", "5"]
    possibleMoves5 = [0]
    if dropState[0] == '1' and dropState[3] == '1': # 1 and 4 available
        possibleMoves5.append(getXValue(state - 2304))
    else:
        possibleMoves5.append(0)

    if dropState[1] == '1' and dropState[2] == '1': # 2 and 3 available
        possibleMoves5.append(getXValue(state - 1536))
    else:
        possibleMoves5.append(0)

    if dropState[4] == '1': # 5 available
        possibleMoves5.append(getXValue(state - 128))
    else:
        possibleMoves5.append(0)

    xValues.append(np.max(possibleMoves5))
    ind5 = possibleMoves5.index(np.max(possibleMoves5))
    od_5.append(movenames5[ind5])

    # if you roll 6
    movenames6 = ["0", "1 5", "2 4", "6"]
    possibleMoves6 = [0]
    if dropState[0] == '1' and dropState[4] == '1': # 1 and 5 available
        possibleMoves6.append(getXValue(state - 2176))
    else:
        possibleMoves6.append(0)

    if dropState[1] == '1' and dropState[3] == '1': # 2 and 4 available
        possibleMoves6.append(getXValue(state - 1280))
    else:
        possibleMoves6.append(0)

    if dropState[5] == '1': # 6 available
        possibleMoves6.append(getXValue(state - 64))
    else:
        possibleMoves6.append(0)

    xValues.append(np.max(possibleMoves6))
    ind6 = possibleMoves6.index(np.max(possibleMoves6))
    od_6.append(movenames6[ind6])

    # if you roll 7
    movenames7 = ["0", "1 6", "2 5", "3 4", "7"]
    possibleMoves7 = [0]
    if dropState[0] == '1' and dropState[5] == '1': # 1 and 6 available
        possibleMoves7.append(getXValue(state - 2112))
    else:
        possibleMoves7.append(0)

    if dropState[1] == '1' and dropState[4] == '1': # 2 and 5 available
        possibleMoves7.append(getXValue(state - 1152))
    else:
        possibleMoves7.append(0)

    if dropState[2] == '1' and dropState[3] == '1': # 3 and 4 available
        possibleMoves7.append(getXValue(state - 768))
    else:
        possibleMoves7.append(0)
    
    if dropState[6] == '1': # 7 available
        possibleMoves7.append(getXValue(state - 32))
    else:
        possibleMoves7.append(0)

    xValues.append(np.max(possibleMoves7))
    ind7 = possibleMoves7.index(np.max(possibleMoves7))
    od_7.append(movenames7[ind7])

    # if you roll 8
    movenames8 = ["0", "1 7", "2 6", "3 5", "8"]
    possibleMoves8 = [0]
    if dropState[0] == '1' and dropState[6] == '1': # 1 and 7 available
        possibleMoves8.append(getXValue(state - 2080))
    else:
        possibleMoves8.append(0)
    
    if dropState[1] == '1' and dropState[5] == '1': # 2 and 6 available
        possibleMoves8.append(getXValue(state - 1088))
    else:
        possibleMoves8.append(0)

    if dropState[2] == '1' and dropState[4] == '1': # 3 and 5 available
        possibleMoves8.append(getXValue(state - 640))
    else:
        possibleMoves8.append(0)

    if dropState[7] == '1': # 8 available
        possibleMoves8.append(getXValue(state - 16))
    else:
        possibleMoves8.append(0)

    xValues.append(np.max(possibleMoves8))
    ind8 = possibleMoves8.index(np.max(possibleMoves8))
    od_8.append(movenames8[ind8])

    # if you roll 9
    movenames9 = ["0", "1 8", "2 7", "3 6", "4 5", "9"]
    possibleMoves9 = [0]
    if dropState[0] == '1' and dropState[7] == '1': # 1 and 8 available
        possibleMoves9.append(getXValue(state - 2064))
    else:
        possibleMoves9.append(0)

    if dropState[1] == '1' and dropState[6] == '1': # 2 and 7 available
        possibleMoves9.append(getXValue(state - 1056))
    else:
        possibleMoves9.append(0)

    if dropState[2] == '1' and dropState[5] == '1': # 3 and 6 available
        possibleMoves9.append(getXValue(state - 576))
    else:
        possibleMoves9.append(0)

    if dropState[3] == '1' and dropState[4] == '1': # 4 and 5 available
        possibleMoves9.append(getXValue(state - 384))
    else:
        possibleMoves9.append(0)

    if dropState[8] == '1': # 9 available
        possibleMoves9.append(getXValue(state - 8))
    else:
        possibleMoves9.append(0)

    xValues.append(np.max(possibleMoves9))
    ind9 = possibleMoves9.index(np.max(possibleMoves9))
    od_9.append(movenames9[ind9])

    # if you roll 10
    movenames10 = ["0", "1 9", "2 8", "3 7", "4 6", "10"]
    possibleMoves10 = [0]
    if dropState[0] == '1' and dropState[8] == '1': # 1 and 9 available
        possibleMoves10.append(getXValue(state - 2056))
    else:
        possibleMoves10.append(0)

    if dropState[1] == '1' and dropState[7] == '1': # 2 and 8 available
        possibleMoves10.append(getXValue(state - 1040))
    else:
        possibleMoves10.append(0)

    if dropState[2] == '1' and dropState[6] == '1': # 3 and 7 available
        possibleMoves10.append(getXValue(state - 544))
    else:
        possibleMoves10.append(0)

    if dropState[3] == '1' and dropState[5] == '1': # 4 and 6 available
        possibleMoves10.append(getXValue(state - 320))
    else:
        possibleMoves10.append(0)

    if dropState[9] == '1': # 10 available
        possibleMoves10.append(getXValue(state - 4))
    else:
        possibleMoves10.append(0)

    xValues.append(np.max(possibleMoves10))
    ind10 = possibleMoves10.index(np.max(possibleMoves10))
    od_10.append(movenames10[ind10])

    # if you roll 11
    movenames11 = ["0", "1 10", "2 9", "3 8", "4 7", "5 6", "11"]
    possibleMoves11 = [0]
    if dropState[0] == '1' and dropState[9] == '1': # 1 and 10 available
        possibleMoves11.append(getXValue(state - 2052))
    else:
        possibleMoves11.append(0)

    if dropState[1] == '1' and dropState[8] == '1': # 2 and 9 available
        possibleMoves11.append(getXValue(state - 1032))
    else:
        possibleMoves11.append(0)

    if dropState[2] == '1' and dropState[7] == '1': # 3 and 8 available
        possibleMoves11.append(getXValue(state - 528))
    else:
        possibleMoves11.append(0)

    if dropState[3] == '1' and dropState[6] == '1': # 4 and 7 available
        possibleMoves11.append(getXValue(state - 288))
    else:
        possibleMoves11.append(0)
        
    if dropState[4] == '1' and dropState[5] == '1': # 5 and 6 available
        possibleMoves11.append(getXValue(state - 192))
    else:
        possibleMoves11.append(0)

    if dropState[10] == '1': # 11 available
        possibleMoves11.append(getXValue(state - 2))
    else:
        possibleMoves11.append(0)

    xValues.append(np.max(possibleMoves11))
    ind11 = possibleMoves11.index(np.max(possibleMoves11))
    od_11.append(movenames11[ind11])

    # if you roll 12
    movenames12 = ["0", "1 11", "2 10", "3 9", "4 8", "5 7", "12"]
    possibleMoves12 = [0]
    if dropState[0] == '1' and dropState[10] == '1': # 1 and 11 available
        possibleMoves12.append(getXValue(state - 2050))
    else:
        possibleMoves12.append(0)

    if dropState[1] == '1' and dropState[9] == '1': # 2 and 10 available
        possibleMoves12.append(getXValue(state - 1028))
    else:
        possibleMoves12.append(0)

    if dropState[2] == '1' and dropState[8] == '1': # 3 and 9 available
        possibleMoves12.append(getXValue(state - 520))
    else:
        possibleMoves12.append(0)

    if dropState[3] == '1' and dropState[7] == '1': # 4 and 8 available
        possibleMoves12.append(getXValue(state - 272))
    else:
        possibleMoves12.append(0)

    if dropState[4] == '1' and dropState[6] == '1': # 5 and 7 available
        possibleMoves12.append(getXValue(state - 160))
    else:
        possibleMoves12.append(0)

    if dropState[11] == '1': # 12 available
        possibleMoves12.append(getXValue(state - 1))
    else:
        possibleMoves12.append(0)

    xValues.append(np.max(possibleMoves12))
    ind12 = possibleMoves12.index(np.max(possibleMoves12))
    od_12.append(movenames12[ind12])
    
    return xValues

def calcXValue(dropState):
    xValues = getXValues(dropState)
    sum = 0
    for i in range(2, 13):
        sum += (prob_dict[i] * xValues[i])
    return sum

def getXValue(dropState): # dropState: an int that represents the current state of the lemondrops when converted to binary
    return xValueDict.get(dropState)

for i in range(1, 4096):
    xValueDict[i] = calcXValue(i)

# place results into a list and write to a text file
file = open("dropsolver.txt", "w")
xValueArray = [1]

for i in range(1, 4096):
    xValueArray.append(calcXValue(i))

# format table
t = PrettyTable(['Drop State', 'Expected Value', 'Dice Sum = 2', 'Dice Sum = 3', 'Dice Sum = 4', 'Dice Sum = 5', 
                 'Dice Sum = 6', 'Dice Sum = 7', 'Dice Sum = 8', 'Dice Sum = 9', 'Dice Sum = 10', 'Dice Sum = 11', 
                 'Dice Sum = 12'])
for j in range(0, 4096):
    i = 4095 - j
    t.add_row([intToBinary(i), xValueArray[i], od_2[i], od_3[i], od_4[i], od_5[i], od_6[i], od_7[i], od_8[i], 
               od_9[i], od_10[i], od_11[i], od_12[i]])

file.write(str(t))
file.close()