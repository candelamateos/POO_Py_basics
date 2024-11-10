def cifrar(palabra, posiciones):
    palabra_cifrada = ""
    
    for actual in palabra:
        
        if actual == ' ':
            palabra_cifrada = palabra_cifrada + '_'
        elif actual == 'ñ':
            palabra_cifrada += '-'
        else: 
            numero = ord(actual) - ord("a") + posiciones
            numero = numero % 26
            numero += ord('a')
            nueva = chr(numero)
            palabra_cifrada += nueva 
            
    return palabra_cifrada
def descifrar(palabra_cifrada, posiciones):
    palabra_descifrada = "";
    
    for actual in palabra_cifrada:
        if actual == '_':
            palabra_descifrada += ' '
        elif actual == '-':
            palabra_descifrada += 'ñ'
        else:
            nueva = chr((ord(actual) - posiciones - ord('a')) % 26 + ord('a'))
            palabra_descifrada += nueva
            
    
    return palabra_descifrada
def main():
    
    posiciones = int(input("Que clave de cifrado quieres usar?: "))
    palabra = input("Introduce la palabra que quieres cifrar: " )
    palabra_cifrada = cifrar(palabra, posiciones)
    print("Mensaje cifrado:", palabra_cifrada)
    
    palabra_cifrada = input("Introduce una palabra a descifrar: ")
    palabra_descifrada = descifrar(palabra_cifrada, posiciones)
    print("Mensaje descifrado:", palabra_descifrada)
if __name__ == "__main__":
    main()