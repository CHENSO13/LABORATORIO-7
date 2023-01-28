def longitud(x):
    cadenalarga = 0
    subcadena = ''
    for i in x: #recorremos cada caracter 
        if i not in subcadena: #se agrega el caracter a la cadena si no esta dicho caracter
            subcadena += i
        else:
            if cadenalarga < len(subcadena): 
                cadenalarga = len(subcadena)
            subcadena = subcadena.split(i)[-1] + i
    if cadenalarga < len(subcadena):
        cadenalarga = len(subcadena)
    print("La longitud de la cadena mas larga es: " + str(cadenalarga))
    return cadenalarga
longitud(x = 'python en un lenguaje de programacion')
