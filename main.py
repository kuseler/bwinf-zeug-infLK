import genemptyarr
import random
text = """
40 32
77
ABRUFDATUM
ABSATZ
ACHTUNG
ALLMUSIC
ARCHIV
ARCHIVBOT
ARCHIVIERUNG
AUS
AUT
AUTOARCHIV
BABEL
BAUSTELLE
BBKL
BEGRIFFSKLÄRUNG
BEGRIFFSKLÄRUNGSHINWEIS
BEL
BELEGE
BENUTZER
BGR
BIBRECORD
BOOLAND
CAN
CENTER
CHARTS
COL
COMMONS
COMMONSCAT
COORDINATE
COORDINATEMAP
DDB
DEU
DISKUSSIONSSEITE
DOI
ERLEDIGT
FARBLEGENDE
FILM
FN
FNZ
FOLGENLEISTE
FRA
FUSSBALLDATEN
GEOQUELLE
GER
GNIS
HÖHE
IMDB
INFO
INFORMATION
INTERNETQUELLE
IPA
KALENDERSTIL
KASTEN
KATEGORIEGRAPH
LANG
LITERATUR
LIZENZUMSTELLUNG
MEDAILLENSPIEGEL
MULTILINGUAL
MUSIKCHARTS
NAVFRAME
NAVIGATIONSLEISTE
NOCOMMONS
ÖSTERREICHBEZOGEN
PERSONENLEISTE
PING
POSITIONSKARTE
PRO
SMILEY
SORT
TAXOBOX
TEXT
WAPPENRECHT
WEBARCHIV
WIKIDATA
WIKISOURCE
WIKTIONARY
ZITATION
"""
liste = text.split("\n")
liste = [ i for i in liste if i]
x,y = int(liste[0].split()[0]), int(liste[0].split()[1])
rechteck = genemptyarr.genemptyarr(x,y)
wortliste = liste[2:]

def random_number(lower, upper):
    if upper < 0:
        return False
    else:
        return random.randint(lower, upper)

def fill_random(array):
    for y_iter,q in enumerate(array):
        for x_iter,p in enumerate(array[y_iter]):
            if not array[y_iter][x_iter]:
                array[y_iter][x_iter]= random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return array

def fill_1(array, wortliste):
    remaining = wortliste
    for i in remaining:
        while True:
            if random.randint(0,1) == 0:
                x_word,y_word = random_number(0, x-len(i)-1), random_number(0,y-1)
                if genemptyarr.integrate_horizontally(x_word, y_word, i, array) != False:
##                    print(i, x_word, y_word)
                    break
                else:
                    pass
            else:
                x_word,y_word = random_number(0, x-1), random_number(0,y-len(i)-1)
                if genemptyarr.integrate_vertically(x_word, y_word, i, array) != False:
##                    print(i, x_word, y_word)
                    break
                else:
                    pass
    fill_random(array)
    return array
            

def fill_2(array, wortliste):
    remaining = wortliste
    for i in remaining:
        while True:
            chosen = random.randint(0,2)
            if chosen == 0:
                x_word,y_word = random_number(0, x-len(i)-1), random_number(0,y-1)
                if genemptyarr.integrate_horizontally(x_word, y_word, i, array) != False:
                    #print(i, x_word, y_word)
                    break
                else:
                    pass
            elif chosen == 1:
                x_word,y_word = random_number(0, x-1), random_number(0,y-len(i)-1)
                if genemptyarr.integrate_vertically(x_word, y_word, i, array) != False:
                    #print(i, x_word, y_word)
                    break
                else:
                    pass
            else:
                if random.randint(0,1) == 0:
                    x_word,y_word = random_number(0, x-len(i)-1), random_number(0,y-len(i)-1)
                    if genemptyarr.integrate_diagonally(x_word, y_word, i, array) != False:
                        #print(i, x_word, y_word)
                        break
                    else:
                        pass
                else:
                    x_word,y_word = random_number(0, x-len(i)-1), random_number(0,y-len(i)-1)
                    if genemptyarr.integrate_diagonally(x_word, y_word, i, array, False) != False:
                        #print(i, x_word, y_word)
                        break
                    else:
                        pass
                    
    fill_random(array)
    return array
                


def fill_3(array, wortliste):
    remaining = wortliste
    for i in remaining:
        while True:
            chosen = random.randint(0,7)
            if chosen >= 4:
                i = i[::-1]
                chosen -= 4
                if chosen == 0:
                    x_word,y_word = random_number(0, x-len(i)-1), random_number(0,y-1)
                    if genemptyarr.integrate_horizontally(x_word, y_word, i, array) != False:
                        #print(i, x_word, y_word)
                        break
                    else:
                        pass
                elif chosen == 1:
                    x_word,y_word = random_number(0, x-1), random_number(0,y-len(i)-1)
                    if genemptyarr.integrate_vertically(x_word, y_word, i, array) != False:
                        #print(i, x_word, y_word)
                        break
                    else:
                        pass
                else:
                    if random.randint(0,1) == 0:
                        x_word,y_word = random_number(0, x-len(i)-1), random_number(0,y-len(i)-1)
                        if genemptyarr.integrate_diagonally(x_word, y_word, i, array) != False:
                            #print(i, x_word, y_word)
                            break
                        else:
                            pass
                    else:
                        x_word,y_word = random_number(0, x-len(i)-1), random_number(0,y-len(i)-1)
                        if genemptyarr.integrate_diagonally(x_word, y_word, i, array, False) != False:
                            #print(i, x_word, y_word)
                            break
                        else:
                            pass
    fill_random(array)
    return array





            
fill_3(rechteck, wortliste)
for i in rechteck:
    print(i)
    
