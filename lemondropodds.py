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

xValueDict = {0: 1}

def intToBinary(int): # retrieves the binary representation of game state (1 for available, 0 for unavailable)
    return f'{int:012b}'

def getXValues(state): # returns the possible xValues (expected values) for each roll. Index 2 = xValue if a 2 is rolled with the current state, etc.
    dropState = intToBinary(state)
    xValues = [0, 0]
    
    # if you roll 2
    if dropState[1] == '1': # 2 available
        xValues.append(getXValue(state - 1024))
    else:
        xValues.append(0)
    
    # if you roll 3
    possibleMoves3 = [0]
    if dropState[0] == '1' and dropState[1] == '1': # 1 and 2 available
        possibleMoves3.append(getXValue(state - 3072))
    if dropState[2] == '1': # 3 available
        possibleMoves3.append(getXValue(state - 512))
    xValues.append(np.max(possibleMoves3))

    # if you roll 4
    possibleMoves4 = [0]
    if dropState[0] == '1' and dropState[2] == '1': # 1 and 3 available
        possibleMoves4.append(getXValue(state - 2560))
    if dropState[3] == '1': # 4 available
        possibleMoves4.append(getXValue(state - 256))
    xValues.append(np.max(possibleMoves4))

    # if you roll 5
    possibleMoves5 = [0]
    if dropState[0] == '1' and dropState[3] == '1': # 1 and 4 available
        possibleMoves5.append(getXValue(state - 2304))
    if dropState[1] == '1' and dropState[2] == '1': # 2 and 3 available
        possibleMoves5.append(getXValue(state - 1536))
    if dropState[4] == '1': # 5 available
        possibleMoves5.append(getXValue(state - 128))
    xValues.append(np.max(possibleMoves5))

    # if you roll 6
    possibleMoves6 = [0]
    if dropState[0] == '1' and dropState[4] == '1': # 1 and 5 available
        possibleMoves6.append(getXValue(state - 2176))
    if dropState[1] == '1' and dropState[3] == '1': # 2 and 4 available
        possibleMoves6.append(getXValue(state - 1280))
    if dropState[5] == '1': # 6 available
        possibleMoves6.append(getXValue(state - 64))
    xValues.append(np.max(possibleMoves6))

    # if you roll 7
    possibleMoves7 = [0]
    if dropState[0] == '1' and dropState[5] == '1': # 1 and 6 available
        possibleMoves7.append(getXValue(state - 2112))
    if dropState[1] == '1' and dropState[4] == '1': # 2 and 5 available
        possibleMoves7.append(getXValue(state - 1152))
    if dropState[2] == '1' and dropState[3] == '1': # 3 and 4 available
        possibleMoves7.append(getXValue(state - 768))
    if dropState[6] == '1': # 7 available
        possibleMoves7.append(getXValue(state - 32))
    xValues.append(np.max(possibleMoves7))

    # if you roll 8
    possibleMoves8 = [0]
    if dropState[0] == '1' and dropState[6] == '1': # 1 and 7 available
        possibleMoves8.append(getXValue(state - 2080))
    if dropState[1] == '1' and dropState[5] == '1': # 2 and 6 available
        possibleMoves8.append(getXValue(state - 1088))
    if dropState[2] == '1' and dropState[4] == '1': # 3 and 5 available
        possibleMoves8.append(getXValue(state - 640))
    if dropState[7] == '1': # 8 available
        possibleMoves8.append(getXValue(state - 16))
    xValues.append(np.max(possibleMoves8))

    # if you roll 9
    possibleMoves9 = [0]
    if dropState[0] == '1' and dropState[7] == '1': # 1 and 8 available
        possibleMoves9.append(getXValue(state - 2064))
    if dropState[1] == '1' and dropState[6] == '1': # 2 and 7 available
        possibleMoves9.append(getXValue(state - 1056))
    if dropState[2] == '1' and dropState[5] == '1': # 3 and 6 available
        possibleMoves9.append(getXValue(state - 576))
    if dropState[3] == '1' and dropState[4] == '1': # 4 and 5 available
        possibleMoves9.append(getXValue(state - 384))
    if dropState[8] == '1': # 9 available
        possibleMoves9.append(getXValue(state - 8))
    xValues.append(np.max(possibleMoves9))

    # if you roll 10
    possibleMoves10 = [0]
    if dropState[0] == '1' and dropState[8] == '1': # 1 and 9 available
        possibleMoves10.append(getXValue(state - 2056))
    if dropState[1] == '1' and dropState[7] == '1': # 2 and 8 available
        possibleMoves10.append(getXValue(state - 1040))
    if dropState[2] == '1' and dropState[6] == '1': # 3 and 7 available
        possibleMoves10.append(getXValue(state - 544))
    if dropState[3] == '1' and dropState[5] == '1': # 4 and 6 available
        possibleMoves10.append(getXValue(state - 320))
    if dropState[9] == '1': # 10 available
        possibleMoves10.append(getXValue(state - 4))
    xValues.append(np.max(possibleMoves10))

    # if you roll 11
    possibleMoves11 = [0]
    if dropState[0] == '1' and dropState[9] == '1': # 1 and 10 available
        possibleMoves11.append(getXValue(state - 2052))
    if dropState[1] == '1' and dropState[8] == '1': # 2 and 9 available
        possibleMoves11.append(getXValue(state - 1032))
    if dropState[2] == '1' and dropState[7] == '1': # 3 and 8 available
        possibleMoves11.append(getXValue(state - 528))
    if dropState[3] == '1' and dropState[6] == '1': # 4 and 7 available
        possibleMoves11.append(getXValue(state - 288))
    if dropState[4] == '1' and dropState[5] == '1': # 5 and 6 available
        possibleMoves11.append(getXValue(state - 192))
    if dropState[10] == '1': # 11 available
        possibleMoves11.append(getXValue(state - 2))
    xValues.append(np.max(possibleMoves11))

    # if you roll 12
    possibleMoves12 = [0]
    if dropState[0] == '1' and dropState[10] == '1': # 1 and 11 available
        possibleMoves12.append(getXValue(state - 2050))
    if dropState[1] == '1' and dropState[9] == '1': # 2 and 10 available
        possibleMoves12.append(getXValue(state - 1028))
    if dropState[2] == '1' and dropState[8] == '1': # 3 and 9 available
        possibleMoves12.append(getXValue(state - 520))
    if dropState[3] == '1' and dropState[7] == '1': # 4 and 8 available
        possibleMoves12.append(getXValue(state - 272))
    if dropState[4] == '1' and dropState[6] == '1': # 5 and 7 available
        possibleMoves12.append(getXValue(state - 160))
    if dropState[11] == '1': # 11 available
        possibleMoves12.append(getXValue(state - 1))
    xValues.append(np.max(possibleMoves12))
    
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

file = open("dropsodds.txt", "w")

for i in range(0, 4096):
    file.write(f"{intToBinary(i)} | {xValueDict[i]}\n")

file.close()