from flask import Flask, request, render_template, redirect, url_for
from convert import ImageCompressor, ImageConverter
import os
import tempfile
import shutil

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
