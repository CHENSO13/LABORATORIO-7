def frecuencia_caracter(cadena):
    frecuencia = {}
    for caracter in cadena: 
        if caracter in frecuencia: # se suma caracteres repetidos y se agrega al diccionario
            frecuencia[caracter] += 1 
        else:
            frecuencia[caracter] = 1 
    print(frecuencia)
    return frecuencia
frecuencia_caracter(cadena='murcielago programacion') 