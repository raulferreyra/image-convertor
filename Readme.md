# 🖼️ ImageConverter - Compresor y Convertidor de Imágenes a WebP

Este proyecto permite **convertir imágenes a formato WebP** y **comprimirlas automáticamente** para optimizar su peso, manteniendo la estructura de carpetas original. El proyecto está dividido en tres partes principales:

- `frontend/`: Aplicación web desarrollada en Vue.js.
- `backend/`: Lógica de procesamiento de imágenes en Python.
- `electron/`: Aplicación de escritorio basada en Electron.

---

## 📦 Características

- Soporte para `.jpg`, `.jpeg`, `.png`, `.gif`
- Conversión a `.webp` y `.avif` con compresión automática
- Preserva la estructura de carpetas del directorio original
- Procesamiento de imágenes GIF animadas (solo el primer frame)
- Código backend organizado en clases y documentado
- Interfaz web con Drag & Drop y limitador de carga (en desarrollo)
- Aplicación multiplataforma (Windows, Linux, macOS) con Electron

---

## 🗂️ Estructura del proyecto

```
project/****
├── backend/  ← Lógica de conversión de imágenes (convert.py)
│ └── convert.py
├── frontend/ ← Interfaz web (Vue.js)
│ ├── components/
│ ├── assets/
│ └── ...
├── electron/ ← Aplicación de escritorio (Electron + Vue)
│ ├── main.js
│ └── preload.js
│ └── README.md
├── LICENSE.md
└── README.md
```

---

## 🚀 Requisitos

### Backend

- Python 3.7 o superior
- Librería [`Pillow`](https://pillow.readthedocs.io/en/stable/)

Instalación de dependencias:

```bash
pip install Pillow
```

### FrontEnd

- Node.js 16+
- Vue 3

Instalación de dependencias:

```bash
cd frontend
npm install
```

### Electron

- Node.js 16+
- Electron

Instalación de dependencias:

```bash
cd electron
npm install
```

---

## 🛠️ Uso

### Ejecutar el conversor en consola (modo backend)

```bash
cd backend
python convert.py
```

### Ejecutar la app web (modo desarrollo)

```bash
cd frontend
npm run dev
```

### Ejecutar la app de escritorio (modo Electron)

```bash
cd electron
npm run start
```

---

## ⚙️ Personalización del backend

Puedes modificar los parámetros de compresión en convert.py:


```bash
compressor = ImageCompressor(max_size=500_000, step=10)
```

Esto define un límite de 500 KB, ajustando la calidad de 10 en 10.

---

## 📚 Ejemplo de uso (backend)

Si tienes esta estructura:

```
backend/
├── orig/
│   └── imagen.png
├── dest/
└── convert.py
```

El script generará:

```
backend/
├── dest/
│   └── imagen.webp
```

---

## 🌐 Funcionalidades futuras del frontend

- 🖱️ Área de Drag & Drop para imágenes
- ⏱️ Límite de carga de 5 imágenes por envío
- 📤 Conversión vía backend o API
- 📥 Descarga automática de imágenes procesadas

---

## 🧼 Buenas prácticas

- Código organizado en clases y funciones reutilizables
- Documentación en formato Google Docstring
- Manejo de errores informativo y sin interrupciones
- Separación clara entre frontend, backend y escritorio

---

## 📜 Licencia

MIT. Libre para usar, modificar y compartir. Si mejoras algo, ¡sería genial recibir tu aporte! 😊

---

## 👤 Desarrollador

- **Nickname:** Elemento
- **Nombre:** Raúl Ferreyra
- **Email:** [raul.ferreyra@urasweb.com](mailto:raul.ferreyra@urasweb.com)

---

😘