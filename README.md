
# CVE-2023-22518 - Vulnerabilidad en Confluence

## Descripción
Este repositorio contiene un script para detectar la vulnerabilidad CVE-2023-22518 en instancias de Confluence. La vulnerabilidad permite a los atacantes realizar acciones de destrucción de datos sin necesidad de autenticación.

## Uso del Script
El script `checker.py` se utiliza para verificar si una instancia específica de Confluence es vulnerable a CVE-2023-22518.

### Requisitos
- Python 3
- Biblioteca Requests (instalable vía pip)

### Ejecución
Para ejecutar el script, usa el siguiente comando en tu terminal:

## POC
En este sencillo video puedes ver como ejecutar el script para verificar si tu Confluence es vulnerable.

[![Ver Video](https://img.youtube.com/vi/zv2C-2RWOqw/0.jpg)](https://youtu.be/zv2C-2RWOqw)



```
python3 checker.py <url_de_tu_instancia_confluence>
```
## ¿Cómo contribuir?
¡Toda contribución es bienvenida! Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios.
3. Haz tus cambios.
4. Envía un pull request.

