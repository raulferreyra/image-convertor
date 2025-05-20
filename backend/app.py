from flask import Flask, request, render_template
from convert import ImageCompressor, ImageConverter
import os
import tempfile
import shutil

app = Flask(__name__)


"""
Convert images from a folder to another format and compress them.
This function handles the conversion of images uploaded via a form.
"""


@app.route('/convert', methods=['POST'])
def convert():
    max_weight_mb = request.form.get('max_weight', '1')
    max_weight_bytes = int(float(max_weight_mb) * 1024 * 1024)
    target_format = request.form.get('lot_convert', 'webp')
    dest_path = request.form.get('dest_path')

    # Get the redimension
    red_width = request.form.get('red_width')
    red_height = request.form.get('red_height')

    # Manage Files
    if 'file_orig' not in request.files:
        return "No se enviaron archivos correctamente", 400

    orig_folder = tempfile.mkdtemp()

    # Extract folders
    for file in request.files.getlist("file_orig"):
        rel_path = file.filename  # incluye subcarpetas si se subió así
        file_path = os.path.join(orig_folder, rel_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file.save(file_path)

    os.makedirs(dest_path, exist_ok=True)

    # Space for proccessing
    compressor = ImageCompressor(max_size=max_weight_bytes)
    converter = ImageConverter(
        orig_folder, dest_path, compressor, format=target_format)

    if red_width and red_height:
        try:
            converter.set_resize(int(red_width), int(red_height))
        except ValueError:
            return "Dimensiones inválidas", 400

    converter.convert_all()
    shutil.rmtree(orig_folder)

    # Future ZIPS
    return f"Conversión finalizada. Las imágenes están en: {dest_path}"


if __name__ == "__main__":
    app.run(debug=True)
