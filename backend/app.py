from flask import Flask, request, render_template, redirect, url_for
from convert import ImageCompressor, ImageConverter
import os
import tempfile
import shutil

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


"""
Convert images from a folder to another format and compress them.
This function handles the conversion of images uploaded via a form.
"""


@app.route('/convert', methods=['POST'])
def convert():
    max_weight_mb = request.form.get('max_weight', '1')
    max_weight_bytes = int(float(max_weight_mb) * 1024 * 1024)
    target_format = request.form.get('lot_convert', 'webp')

    # Get the redimension
    red_width = request.form.get('red_width')
    red_height = request.form.get('red_height')

    # Manage Files
    if 'file_orig' not in request.files or 'file_dest' not in request.files:
        return "Archivos no enviados correctamente", 400

    orig_folder = tempfile.mkdtemp()
    dest_folder = tempfile.mkdtemp()

    # Extract folders
    for file in request.files.getlist("file_orig"):
        file_path = os.path.join(orig_folder, file.filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file.save(file_path)

    # Space for proccessing
    compressor = ImageCompressor(max_size=max_weight_bytes)
    converter = ImageConverter(orig_folder, dest_folder, compressor)
    converter.convert_all()

    # Future ZIPS
    return f"Conversión finalizada. Las imágenes están en: {dest_folder}"


if __name__ == "__main__":
    app.run(debug=True)
