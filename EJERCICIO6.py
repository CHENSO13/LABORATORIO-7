def remplzo_subcadena(cadena, sub_cadena, nueva_cadena):
    print("Cadena")
    print(cadena + sub_cadena)
    return cadena.replace(sub_cadena, nueva_cadena) #remplaza la subcadena por una nueva cadena

remplzo_subcadena(cadena="voy a cenar ", sub_cadena="noche", nueva_cadena="arroz")
