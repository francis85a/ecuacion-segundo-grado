import math

def raiz_ecuacion_segundo_grado(a, b, c):
    
    if a == 0:
        return None
    if b == c == 0:
        return 0
    
    if c == 0:
        x = 0
        y = -b / a
        return x, y
    
    discriminante = b ** 2 - 4 * a * c
    
    if discriminante <= 0:
        return None
    if discriminante >= 0:
        x = -b + math.sqrt(discriminante) / (2 * a)
        y = -b - math.sqrt(discriminante) / (2 * a)
        return x, y
    else:
        return None