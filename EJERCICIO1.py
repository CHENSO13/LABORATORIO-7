def palindromo():
    palabra = input("Ingrese una palabra: ")
    n = len(palabra) 
    for i in range(n//2): #divine la cadena en dos partes 
        if palabra[i] != palabra[n-i-1]: #compara la cadena y si es palindromo imprime No es palindromo
            print("No es palindromo")
            return False
        print("Si es palindromo")  #Si son iguales devuelve "Si es palindromo"
palindromo()