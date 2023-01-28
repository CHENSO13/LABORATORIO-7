def dividir(cadena, caracter):
    subcadena = cadena.split(caracter) # extraemos los carateres de la cadena 
    print(subcadena)
    return subcadena

x = 'Hola mundo, me gusta programar, hola mundo, etc'
y = ','
dividir(cadena=x,caracter=y)
