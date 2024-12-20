# recuantificacion_superindice

Este script toma cada superíndice, le resta 36 y lo convierte a la notación correspondiente en superíndice.

Explicación:
superindice_map: Mapea los números 0-9 a sus respectivos superíndices.
numero_a_superindice: Convierte un número entero a su representación en superíndice.
convertir_superindices: Busca todos los superíndices en el texto. Si un superíndice es 37, se convierte en 2, si es 38, se convierte en 3, etc. Esto se logra restando 36 al número original del superíndice.
procesar_archivo: Lee el archivo de entrada, convierte los superíndices según lo especificado y guarda el resultado en un archivo de salida.

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
