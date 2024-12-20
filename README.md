# recuantificacion_superindice

Este script toma cada superíndice, le resta 36 y lo convierte a la notación correspondiente en superíndice.

Explicación del Script
Diccionarios:

superindices_unicode para mapear los caracteres superíndices Unicode a números enteros.
numeros_a_superindices para convertir números enteros de vuelta a superíndices Unicode.
Funciones:

convertir_a_numero: Convierte una cadena de superíndices Unicode a un número entero.
convertir_a_superindice: Convierte un número entero a una cadena de superíndices Unicode.
modificar_superindices: Busca superíndices en el texto y resta 36 de su valor.
Expresión Regular: Se utiliza re.compile(r'[⁰¹²³⁴⁵⁶⁷⁸⁹]+') para identificar secuencias de superíndices Unicode.

## Uso

1. Instalar el programa

   ```sh
   git clone https://github.com/victorbondaruk/recuantificacion_superindice.git
   ```

2. Asignar texto

Insertar en el archivo `entrada.txt` el texto.

```sh
moja!³⁶
Palabra³⁷
Otra³⁸
```

3. Ejecutar programa

En la consola, dentro de la misma ubicacion de este proyecto, ejecutar el script:

```sh
python3 recuantificacion_superindice.py
```

4. Resultado

El texto formateado se almacenara en el archivo `salida.txt`

```sh
moja!¹
Palabra²
Otra³
```
