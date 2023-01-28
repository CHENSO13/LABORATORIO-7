def longitud_digitos(cadena):
    subcadena = cadena.split(" ") # divide la cadena en una lista 
    longitud = 0 # creamos la variable la longitud maxima
    for subcadena in subcadena: # usamos el ciclo para recorre la cadena
        if subcadena.isdigit(): # isdigit sirve para verificar si la subcadena tiene digitos
            longitud = max(longitud, len(subcadena)) # comparamos si la subcadena  es mayor que la longitud maxima
    print("la longitud de la subcadena " + subcadena + " es " + str(longitud))
    
    return longitud

longitud_digitos(cadena="la clase 12345675655")
