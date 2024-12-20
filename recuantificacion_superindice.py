import re

# Mapeo de superíndices Unicode a números
superindices_unicode = {
    '⁰': 0, '¹': 1, '²': 2, '³': 3, '⁴': 4,
    '⁵': 5, '⁶': 6, '⁷': 7, '⁸': 8, '⁹': 9
}

# Mapeo inverso de números a superíndices Unicode
numeros_a_superindices = {v: k for k, v in superindices_unicode.items()}

def convertir_a_numero(superindice):
    """Convierte una cadena de superíndices Unicode a un número entero."""
    return int(''.join(str(superindices_unicode[char]) for char in superindice))

def convertir_a_superindice(numero):
    """Convierte un número entero a una cadena de superíndices Unicode."""
    return ''.join(numeros_a_superindices[int(d)] for d in str(numero))

def modificar_superindices(texto, resta=35):
    # Expresión regular para encontrar secuencias de superíndices Unicode
    patron = re.compile(r'[⁰¹²³⁴⁵⁶⁷⁸⁹]+')
    
    def ajustar_superindice(coincidencia):
        superindice_original = coincidencia.group()
        numero = convertir_a_numero(superindice_original)
        nuevo_numero = numero - resta
        # Si el nuevo número es negativo, mantenerlo en 0
        nuevo_numero = max(nuevo_numero, 0)
        return convertir_a_superindice(nuevo_numero)
    
    return patron.sub(ajustar_superindice, texto)

# Leer el archivo de entrada
with open('entrada.txt', 'r', encoding='utf-8') as archivo_entrada:
    contenido = archivo_entrada.read()

# Modificar los superíndices
contenido_modificado = modificar_superindices(contenido)

# Guardar el resultado en el archivo de salida
with open('salida.txt', 'w', encoding='utf-8') as archivo_salida:
    archivo_salida.write(contenido_modificado)

print("El archivo se ha modificado correctamente y se ha guardado como 'salida.txt'.")
