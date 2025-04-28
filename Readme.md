# 🖼️ ImageConverter - Compresor y Convertidor de Imágenes a WebP

Este script te permite **convertir imágenes a formato WebP** y **comprimirlas automáticamente** para que no superen un tamaño máximo (por defecto, 1 MB). Mantiene la estructura de carpetas del origen y guarda las imágenes comprimidas en una carpeta de destino.

---

## 📦 Características

- Soporta imágenes `.jpg`, `.jpeg`, `.png`, `.gif`
- Convierte a `.webp`
- Comprime ajustando la calidad para no superar un tamaño máximo
- Mantiene la estructura de carpetas del directorio de origen
- Admite imágenes GIF animadas (procesa solo el primer frame)
- Código estructurado en clases (POO) y documentado

---

## 🚀 Requisitos

- Python 3.7 o superior
- Librería [`Pillow`](https://pillow.readthedocs.io/en/stable/)

Instalación de dependencias:

```bash
pip install Pillow
```

---

## 🛠️ Uso

### 1. Estructura esperada

Crea dos carpetas:

```
project/
├── orig/     ← Aquí colocas tus imágenes
├── dest/     ← Aquí se guardarán las imágenes .webp convertidas
├── convert.py
└── README.md
```

### 2. Ejecuta el script

```bash
python convert.py
```

Esto convertirá y comprimirá todas las imágenes de `orig/` hacia `dest/`, manteniendo la estructura de carpetas.

---

## ⚙️ Personalización

Puedes modificar los parámetros en el archivo `convert.py`:

```python
compressor = ImageCompressor(max_size=500_000, step=10)  # Comprimir a máximo 500 KB reduciendo de 10 en 10 la calidad
```

---

## 📚 Ejemplo

Si tienes esta estructura:

```
orig/
├── producto1/
│   └── imagen.jpg
└── producto2/
    └── banner.png
```

El script generará:

```
dest/
├── producto1/
│   └── imagen.webp
└── producto2/
    └── banner.webp
```

---

## 🧼 Buenas prácticas

- El código sigue principios de programación orientada a objetos (POO).
- Se utilizan docstrings estilo Google.
- Los errores están manejados con mensajes informativos y no se interrumpe la ejecución.

---

## 📜 Licencia

MIT. Úsalo como gustes y si mejoras algo, ¡compártelo! 😊

---

## 👤 Desarrollador

- **Nickname:** Elemento
- **Nombre:** Raúl Ferreyra
- **Email:** [raul.ferreyra@urasweb.com](mailto:raul.ferreyra@urasweb.com)

---

```bash
#@@Ñ@#################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
@@Ñ@####@#@##########@@@@@@@#@@@@@@@@@@@@@@@@@@@@@#@#
@@Ñ@##################@##@@@@@@@@@@@@@@@@@@@@@@@@@###
@@@@######################@@@@@@@@@@@@@@@@@@@@@#@####
@@@@00####################@@@@@@@@@@@@@@@@@@@@@@@####
@@@#00###################@@@@@@@@@@@@@@@@@@@@@@@@####
@@@#00##################@#@@@##@@@@@@@@@@@@@@@@@@####
@@@#00##################@#########@@@@@@@@#@@@@@@@###
@@@#00#################@@#########@@@@@@@@#@@@@@@@###
#@@#00##################@@#########@@@@@@@##@@@@#####
#@@#000#################@@#10########@@@#@###@@##@###
#@@#0000################@##110######@@@@@@##@@@@@@###
#@@00000#################0000000####@@@@@@@@@@@@#####
#@@00000################00000000##0#@@@@@@##@@#######
#@@00000#############00011000001000############00##0#
#@#000000##0#########001rrr111rr1000#######0#0000000#
#@#00000000000###0000011rrrr01r11100#######000100011#
#@#0000000000000000000111rr101r11000#####00111100111#
#@#000000000000000000010001100000010###0011111000111#
#@#0000000100000000001r1001111100110000011r110001111#
#@0001111111111111111111111rrr11111100111r1100001111#
##0000011rrrr111111111r11111r11111111111r1##00011111#
##1100000110000000000011111rrr11111101rrr0#000111111#
##111000000############1r11rrr1111011rrr1#0001111r11#
##rr110000000##########0rr11111110#0111100011111rr10#
##rrr110000000##########rr11111110######0011111rrr1##
##1rrr11000000000#######1rrrrrrrr0######0011111rr10##
##0rjrr111000000000#####0rrrrrrrr10##0##001111rrr0###
##00rjrr1111100000000###1rrrrrrrr11000#001111rrr1####
##000rjrr1111111000000#0rrrrrrr110000#001111rrr10####
##0000rjrrr111110000000111111110000##00011rrrrr0#####
##00000rrrrr11110000000000000000####000111rrrr1######
#00000001rrrr1110000000000000000####0001111rr1#######
#000000001rjrrr10000000000##000#####00011111r0#######
#0000000001rjjr1000000000#0000#####0000111111########
#00000000001rjr100#000#0#0000######0000111110########
#000000000001rr10##0000##0000#000000000011110########
#0000000000001r00###00##0000001r100000011111######00#
#0000000000001110##000##000000rr100001111110###0##00#
00001111111111r100000000000111rr11111111111000000000#
0111111111111rjr1000000000011rrrr11111111110000##000#
01111rrrrrrr1rjrr111000000001rrrrrrr11111r1110000000#
0r1111rrrrrr1rjjrr100000000001rrrrr11111r11111000000#
1rrrrrrrrrrr1rjjj110000000000011rr111111r11111100000#
1rrrrrrrrrr11rjjr1000000000000011111111rr11111110000#
1rrrrrrrrr111rjr11000000000000011111111rr11111111000#
1rrrrrrrr11111jr11100001000000011111111r1111111111100
1rrrrrrrrr1111jr1110000100000011111111rr1111111111110
1rrrrrrrrrrrrrjr1111001110000011111111rr1111111111110
rrrrrrrrrrrrrrjrr11111111111111111111rrr1111111111110
rrrrrrrrrrrrrrjrr11111111111111111111rr11111111111110
rrrrrrrrrrrrrrrrrr111111111111111111rrr11111111111110
rrrrrrrrrrrrrrrrrrr11111111111111111rrr11111000001111
rrrrrrrrrrrrrrrrrrr11111111111111111rrr11111000000011
rrrrrrrrrrrrrrrrrrr11111111111111111rrr11111100000011
rrrrrrrrrrrrrrrrrrrrrrr11111111111111rrr1111110000001
rrrrrrrrrrrrrrjrrrrrrrrr1111111111111r1111r1100000001
1rrrrrrrrrrrrrrrrrrrrrrr11111111111111111111111110011
111rrrrrrrrrrrrrrrr1rrrr1111111111111111111r111111111
11111rrrrrrrrrrrrr111rjr111111111111111111rr111111111
1111111rrrrrrrrrrr1111r1111111111111111111rrr11111111
11111111rrrrrrrrrr1111111111111111111111rrrrrr1111111
1111111111rrrrrrrrrr1111rrrrr111111111rrrrrrrrrrr1rr1
11111111111rrrrrrrrrrrrrrrrrrrrrr111rrrrrrrrrrrrrr1r1
11111111111rrrrrrrrrrjjjrrrrrrrrrrrrrrrrrrrrrrrrr1111
11111111111rjjjjjjjjjjjjjjjjjrrrrrrrrrrrrrrrrrrr1r111
11111111111rjjjjjjjjjjjjjjjjjjjjjrrrrrrrrrrrrrrrrr111
11111111111rjjjjjjjjjjjjjjjjjjjjjrrrrrrrrrrrrrrrrr111
11111111111rrjjjjjjjjjjjjjjjjjjjjrrrrrrrrrrrrrrrrrrr1
11111111111rrrrjjjjjjjjjjjjjjjjrrrrrrrrrrrrrrrrrrrrr1
1111111111rjrrrrjjjjjjjjjjjjjjjrrrrrjrrrrrrrrrrrrrrr1
1111111111jjjjrrjjjjjrrrrrrjjjjrrjjjrrrrrrrrrrrrrrrr1
1111111111rrjjjrjjjjrrrrrrrjjjjjjjrrrrrrrrrrrrrrrrrr0
111111111rrrrrrrjjjjjjjjjjjjjjjjjrrr11rrrrrrrrrrrrrr1
r11111111rrrrrrrrjjjjjjjjjjjjjjjrrr11rrrrrrrrrrrrrrr1
111111111jrrr111rjjjjjjjjjjjjjjjrrrrrrrrrrrrrrrrrrrr1
11111111rjrrr111rrjddddddddddjjrrrrrrrrrrrrrrrrrrrrr1
1111111rrjrrr111rrjddddTTddddjrrrrrrrrrrrrrrrrrrrrrr1
111111rrjjrrrr11rrrjdTTTTTTTdjrrrrrrrrrrrrjjrrrrrrrr1
111111rrjjjrrrrrrrrrdTUUUTTTjrrrrrrrrrrrrrjjrrrrrrrr1
11111rrrjjjrrrrrrrrrjTUUUUUdjrrrrrrrrrrrrjjjrrrrrrrr1
1111rrrrjjjrrrrrrrrrrdTUUUUdjrrrrrrrrrrrrjjjrrrrrrrr1
1rrrjrrrjjjjrrrrrrrrrjdTUUTjjjrrrrrrrrrrjjjjjrrrrrrr1
rrrrrrrrjjjjrrrrrrrrrjjTUUTjjjjrrrrrrrrrjjjjrrrrrrrr1
1111rrrrdjjjjrrrrrrrjjjdTUdjjjjjrrrrrrrrjjjjrrrrrrrr1
r111rrrrdjjjjrrrrrrjjjjdTUdjjjjjjrrrrrjjjjjjrrrrrrr11
r11rrrrrdjjjjrrrrrjjjjjdTUddjjjjjjjjjjjjjjjjrrrrrrr11
1rrrrrrrddjjjjjjjjjjjjjdTUTddjjjjjjjjjjjjjjjrrrrrrr11
1rrrrrrrddjjjjjjjjjjjjjdTUTdddjjjjjjjjjjjjjjjrrrrrr1r
11rrrrrrjdjjjjjjjjjjjjjdTUTTdddjjjjjjjjjjjjjjjjjrrr1r
11rrrrrrjdjjjjjjjjjjjjjdTTTTdddddjjjjjjjjjjjjjjjrrr11
111rrrrrjdjjjjjjjjjjjjjdTTdTdddddjjjjjjjjjjjjjjrrrr11
001111rrjdjjjjjjjjjjjjddTTdTddddddjjjjjjjddjjjjjrrr1
```