import os, sys
from PIL import Image, UnidentifiedImageError


class ImageCompressor:
    """
    Clase para comprimir imágenes al formato WebP sin exceder un tamaño máximo.

    Args:
        max_size (int): Tamaño máximo en bytes (por defecto 1 MB).
        step (int): Valor por el cual se reduce la calidad en cada intento.
    """

    def __init__(self, max_weight_mb: float = 1.0, step: int = 5):
        """
        max_weight_mb: peso máximo en MB (por defecto 1MB si no se indica)
        step: reducción por paso de calidad
        """
        self.max_size = max_weight_mb * 1024 * 1024  # Convertir MB a bytes
        self.step = step

    def convert_format(self, image: Image.Image, dest_path: str, target_format: str) -> bool:
        """
        Guarda la imagen como WebP ajustando la calidad para no superar el tamaño máximo.

        Args:
            image (PIL.Image.Image): Imagen a comprimir.
            dest_path (str): Ruta de destino donde se guardará la imagen comprimida.
            target_format (str): Formato al que se convertirá (por ejemplo: "WEBP", "JPG").

        Returns:
            bool: True si la imagen se guardó exitosamente por debajo del tamaño límite, False en caso contrario.
        """
        quality = 100
        image = self._prepare_image(image)

        # Agrega la extensión al nombre del archivo de salida
        ext_map = {
            'jpg': 'JPEG',
            'jpeg': 'JPEG',
            'png': 'PNG',
            'gif': 'GIF',
            'webp': 'WEBP',
            'avif': 'AVIF'
        }
        format_upper = ext_map.get(
            target_format.lower(), target_format.upper())
        dest_path_with_ext = f"{dest_path}.{target_format.lower()}"

        if format_upper in ['JPEG', 'WEBP', 'AVIF']:
            while quality > 10:
                try:
                    image.save(dest_path_with_ext, format=format_upper,
                               quality=quality, lossless=False)
                    if os.path.getsize(dest_path_with_ext) <= self.max_size:
                        return True
                except Exception as e:
                    print(f"[ERROR] No se pudo guardar {dest_path}: {e}")
                    return False

                quality -= self.step

            print(
                f"[ADVERTENCIA] No se pudo comprimir {dest_path} por debajo de {self.max_size / 1024:.2f} KB")
            return False
        else:
            try:
                image.save(dest_path_with_ext, format=format_upper)
                if os.path.getsize(dest_path_with_ext) <= self.max_size:
                    return True
                else:
                    print(
                        f"[ADVERTENCIA] {dest_path_with_ext} excede el tamaño máximo permitido.")
                    return False
            except Exception as e:
                print(f"[ERROR] No se pudo guardar {dest_path_with_ext}: {e}")
                return False

    def _prepare_image(self, image: Image.Image) -> Image.Image:
        """
        Prepara la imagen para la compresión: convierte el modo y toma el primer cuadro si es animada.

        Args:
            image (PIL.Image.Image): Imagen original.

        Returns:
            PIL.Image.Image: Imagen preparada para ser comprimida.
        """
        if image.mode == "P":
            image = image.convert("RGBA")
        elif image.mode not in ("RGBA", "LA"):
            image = image.convert("RGB")

        if image.format == "GIF" and getattr(image, "is_animated", False):
            image.seek(0)

        return image


class ImageConverter:
    """
    Clase para convertir y comprimir imágenes desde una carpeta de origen a una de destino.

    Args:
        orig_folder (str): Carpeta de origen con imágenes.
        dest_folder (str): Carpeta de destino para guardar las imágenes comprimidas.
        compressor (ImageCompressor): Instancia de la clase ImageCompressor.
    """

    VALID_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif')

    def __init__(self, orig_folder: str, dest_folder: str, compressor: ImageCompressor):
        self.orig_folder = orig_folder
        self.dest_folder = dest_folder
        self.compressor = compressor

    def convert_all(self):
        """
        Convierte y comprime todas las imágenes válidas en la carpeta de origen.
        """
        if not os.path.exists(self.dest_folder):
            os.makedirs(self.dest_folder)

        for root, _, files in os.walk(self.orig_folder):
            for file in files:
                if file.lower().endswith(self.VALID_EXTENSIONS):
                    self._convert_single_image(root, file)

    def _convert_single_image(self, root: str, file: str):
        """
        Convierte y comprime una sola imagen, manteniendo la estructura de carpetas.

        Args:
            root (str): Ruta actual dentro de la carpeta de origen.
            file (str): Nombre del archivo de imagen.
        """
        orig_path = os.path.join(root, file)
        relative_path = os.path.relpath(root, self.orig_folder)
        dest_subfolder = os.path.join(self.dest_folder, relative_path)
        os.makedirs(dest_subfolder, exist_ok=True)

        dest_file = os.path.splitext(file)[0] + ".webp"
        dest_path = os.path.join(dest_subfolder, dest_file)

        try:
            with Image.open(orig_path) as img:
                if self.compressor.convert_format(img, dest_path):
                    size_kb = os.path.getsize(dest_path) / 1024
                    print(
                        f"[OK] {orig_path} -> {dest_path} ({size_kb:.2f} KB)")
        except UnidentifiedImageError:
            print(f"[ERROR] No se pudo identificar la imagen: {orig_path}")
        except Exception as e:
            print(f"[ERROR] Falló el procesamiento de {orig_path}: {e}")


if __name__ == "__main__":
    orig_folder = "orig"
    dest_folder = "dest"

    compressor = ImageCompressor(max_size=1_048_576, step=5)
    converter = ImageConverter(orig_folder, dest_folder, compressor)
    converter.convert_all()
