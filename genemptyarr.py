#import numpy as np

def genemptyarr(x,y):
    arr = []
    for i in range(y):
        arr.append([None for a in range(x)])
    #x = np.array(arr)
    return arr

def integrate_horizontally(xpos, ypos, word, arr):
    if checkwordperword(1, word, xpos, ypos, arr):
        for position,letter in enumerate(word):
            arr[ypos][xpos+position] = letter
##            print(letter)
    else:
##        print("integration failed")
        return False

def integrate_vertically(xpos, ypos, word, arr):
    if checkwordperword(2, word, xpos, ypos, arr):
        for position, letter in enumerate(word):
            arr[ypos+position][xpos] = letter
##            print(letter)
    else:
##        print("integration failed")
        return False


def integrate_diagonally(xpos, ypos, word, arr, downwards=True):
    if downwards:
        if checkwordperword(3, word, xpos, ypos, arr):
            for position, letter in enumerate(word):
                arr[ypos + position][xpos + position] = letter
##                print(letter)
        else:
##            print("integration failed")
            return False
    else:
        if checkwordperword(4, word, xpos, ypos, arr):
            for position, letter in enumerate(word):
                arr[ypos - position][xpos + position] = letter
##                print(letter)
        else:
##            print("integration failed")
            return False



def checkwordperword(direction, word, xpos, ypos, arr):
    if direction == 1:
##        print(ypos,xpos)
        if len(word)+xpos > len(arr[0]):
            return False
        for j,i in enumerate(word):
##            print(xpos, j, arr[ypos][xpos])
            next_position = arr[ypos][xpos + j]
##            print(j, next_position, i)
            if not (next_position == i or next_position == None):
                return False
        return True
        
    if direction == 2:
        if len(word)+ypos > len(arr):
            return False
        for position, letter in enumerate(word):
            next_position = arr[ypos+position][xpos]
##            print(position, next_position, letter)
            if not (next_position == letter or next_position == None):
                return False
        return True    
    if direction == 3:
        if len(word)+ypos > len(arr) or len(word)+xpos > len(arr[0]):
            return False
        for position, letter in enumerate(word):
            next_position = arr[ypos+position][xpos+position]
##            print(position, next_position, letter)
            if next_position == letter or next_position == None:
                pass
            else:
                return False
        return True
    if direction == 4:
        if ypos - (len(word)-1) < 0 or len(word)+xpos > len(arr[0]):
            return False
        for position, letter in enumerate(word):
##            print(position, ypos-position,xpos+position, letter)
            next_position = arr[ypos-position][xpos+position]
            if next_position == letter or next_position == None:
                pass
            else:
                return False
        return True
        
