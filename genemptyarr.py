#import numpy as np

def genemptyarr(x,y):
    arr = []
    for i in range(y):
        arr.append([None for a in range(x)])
    #x = np.array(arr)
    return arr


def integratewordtoarr(direction, xpos, ypos, word, arr):
    if direction <= 4:
        if direction == 1:
            if xpos + len(word) <= len(arr[ypos]) and checkwordperword(direction, word, xpos, ypos, arr):
                for j,i in enumerate(word):
                    arr[ypos][xpos+j] = i
        if direction == 2:
            if ypos + len(word) <= len(arr) and checkwordperword(direction, word, xpos, ypos, arr):
                pass
      
    if direction >= 5:
        word = word[::-1]
        
    

def checkwordperword(direction, word, xpos, ypos, arr):
    if direction == 1:
        for j,i in enumerate(word):
            if arr[ypos][xpos + j] == word or not arr[ypos][xpos+j]:
                pass
            else:
                return False
    if direction == 2:
        for j,i in enumerate(word):
            if arr[ypos+j][xpos] == word or not arr[ypos][xpos+j]:
                pass
            else:
                return False
            
