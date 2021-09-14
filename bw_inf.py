from random import randint

datei= open("worte0.txt","r").readlines()

x_raster, y_raster = datei[0].split(" ")

worte = [ ele.rstrip() for ele in datei[2:] ]

def erstelle_raster(x,y,schwierigkeit):
    richtung = randint(1,schwierigkeit)
    if richtung == 1: #horizontal
        pass
