import math

def seno(angulo):
    if(angulo == 0):
        return 0
    elif angulo == 30:
        return 0.5
    elif angulo == 45:
        return math.sqrt(2)/2
    elif angulo == 60:
        return math.sqrt(3)/2
    elif angulo == 90:
        return 1
    else:
        return -1

def coseno(angulo):
    if(angulo == 0):
        return 1
    elif angulo == 30:
        return math.sqrt(3)/2
    elif angulo == 45:
        return math.sqrt(2)/2
    elif angulo == 60:
        return 0.5
    elif angulo == 90:
        return 0
    else:
        return -1

def tangente(angulo):
    if(angulo == 0):
        return 0
    elif angulo == 30:
        return math.sqrt(3)/3
    elif angulo == 45:
        return 1
    elif angulo == 60:
        return math.sqrt(3)
    elif angulo == 90:
        return -1
    else:
        return -1