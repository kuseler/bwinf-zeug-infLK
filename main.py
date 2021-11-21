import genemptyarr
import random
text = """
6 6
6
EIN
DA
ER
INFO
DU
UND
"""
liste = text.split("\n")
liste = [ i for i in liste if i]
x,y = int(liste[0].split()[0]), int(liste[0].split()[1])
rechteck = genemptyarr.genemptyarr(x,y)
wortliste = liste[2:]

def fill_1(array, wortliste):
    remaining = wortliste
    for i in remaining:
        while True:
            if random.randint(0,1) == 0:
                x_word,y_word = random.randint(0, x-len(i)-1), random.randint(0,y-1)
                if genemptyarr.integrate_horizontally(x_word, y_word, i, array) != False:
                    print(i, x_word, y_word)
                    break
                else:
                    pass
            else:
                x_word,y_word = random.randint(0, x-1), random.randint(0,y-len(i)-1)
                if genemptyarr.integrate_horizontally(x_word, y_word, i, array) != False:
                    print(i, x_word, y_word)
                    break
                else:
                    pass
    for y_iter,q in enumerate(array):
        for x_iter,p in enumerate(array[y_iter]):
            if not array[y_iter][x_iter]:
                array[y_iter][x_iter]= random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                print(i)
    return array
            
        

fill_1(rechteck, wortliste)
