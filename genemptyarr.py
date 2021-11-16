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
            print(letter)

def integrate_vertically(xpos, ypos, word, arr):
    if checkwordperword(2, word, xpos, ypos, arr):
        for position, letter in enumerate(word):
            arr[ypos+position][xpos] = letter
            print(letter)


def integrate_diagonally(xpos, ypos, word, arr):
    if checkwordperword(3, word, xpos, ypos, arr):
        for position, letter in enumerate(word):
            arr[ypos + position][xpos + position] = letter
            print(letter)

def integratewordtoarr(direction, xpos, ypos, word, arr):
    if direction == 1:
        integrate_horizontally(xpos, ypos, word, arr)
            
    if direction == 2:
        if ypos + len(word) <= len(arr) and checkwordperword(direction, word, xpos, ypos, arr):
            pass
      
    if direction >= 5:
        word = word[::-1]
        
    


def checkwordperword(direction, word, xpos, ypos, arr):
    if direction == 1:
        if len(word) > len(arr[ypos]):
            return False
        for j,i in enumerate(word):
            next_position = arr[ypos][xpos + j]
            print(j, next_position, i)
            if not (next_position == i or next_position == None):
                return False
        return True
        
    if direction == 2:
        if len(word) > len(arr):
            return False
        for position, letter in enumerate(word):
            next_position = arr[ypos+position][xpos]
            print(position, next_position, letter)
            if not (next_position == letter or next_position == None):
                return False
        return True    
    if direction == 3:
        if len(word) > len(arr) or len(word) > len(arr[ypos]):
            return False
        for position, letter in enumerate(word):
            next_position = arr[ypos+position][xpos+position]
            print(position, next_position, letter)
            if next_position == letter or next_position == None:
                pass
            else:
                return False
        return True

            
    if direction == 3:
        pass


a = genemptyarr(5,5)
