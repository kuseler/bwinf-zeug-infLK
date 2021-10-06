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
            if xpos + len(word) <= len(arr[ypos]) and not checkwordperword(direction, word, xpos, ypos, arr):
                for j,i in enumerate(word):
                    arr[ypos][xpos+j] = i
                    print(i)
            
        if direction == 2:
            if ypos + len(word) <= len(arr) and checkwordperword(direction, word, xpos, ypos, arr):
                pass
      
    if direction >= 5:
        word = word[::-1]
        
    

def checkwordperword(direction, word, xpos, ypos, arr):
    if direction == 1:
        for j,i in enumerate(word):
            print(j, arr[ypos][xpos + j], i)
            if arr[ypos][xpos + j] == i or arr[ypos][xpos+j] == None:
                pass
            else:
                return True
        
    if direction == 2:
        for j,i in enumerate(word):
            print(j, arr[ypos + j][xpos], i)
            if arr[ypos][xpos + j] == i or arr[ypos][xpos] == None:
                pass
            else:
                return True

            
    if direction == 3:
        pass
