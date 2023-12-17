def multiplicacion_vectores(vector1, vector2):
    vector3 = []
    for x in vector1:
        acumulador = 0
        for y in vector2:
            acumulador = acumulador + (x*y)
        vector3.append(acumulador)
    return vector3
