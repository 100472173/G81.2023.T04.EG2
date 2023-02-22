# G81.2023.T04.EG2
El directorio raíz incluye:
- .gitignore, .pylintrc, requirements.txt, readme.md
- main.py
- uc3m_logistics, con el codigo proporcionado para la practica
- 6 tests en formato json para probar el validador de codigos EAN13
- imágenes de los códigos de barras EAN13 correctos
- imágenes de los warnings de pylint antes de las modificaciones y la imagen sin warnings
- normativa_de_codigo.pdf, que incluye la normativa de codigo

Descripción de los tests aportados para la práctica:
- Test 1: Código EAN13 correcto, acabado en 0
- Test 2: Código EAN13 incorrecto, último digito no corresponde
- Test 3: Código EAN13 correcto, acabado en numero distinto de 0
- Test 4: Código EAN13 correcto, acabado en numero distinto de 0
- Test 5: Código EAN13 incorrecto, longitud menor de 13 caracteres
- Test 6: Código EAN13 incorrecto, longitud mayor de 13 caracteres
