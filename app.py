import base64
import io
import uuid
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from flask import Flask, request, redirect, url_for, render_template
from PIL import Image

from check_model import get_predict
from text_on_image import get_text_bbox

UPLOAD_DIR = 'upload'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

STEPS = [
    {'id': 1, 'name': 'Загрузите изображение'},
    {'id': 2, 'name': 'Обрежьте по тексту'},
    {'id': 3, 'name': 'Получите результат'}
]

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

app = Flask(__name__)


@app.route("/")
def redirect_to_upload():
    return redirect(request.url + 'upload')


@app.route("/upload")
def get_upload():
    return render_template('upload.html', steps=STEPS, actual_step=1)


@app.route("/crop", methods=['POST'])
def post_upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        img, path = save_img_to_upload_dir(file.read())
        bbox = get_text_bbox(path)

        buffered = io.BytesIO()
        img.save(buffered, format='JPEG')
        image_string = base64.b64encode(buffered.getvalue()).decode('utf-8')

        os.remove(path)
        return render_template(
            'crop.html',
            steps=STEPS,
            actual_step=2,
            image_string=image_string,
            bbox=bbox)
    else:
        return redirect('/upload')


@app.route("/result", methods=['POST'])
def post_result():
    image = request.form.get('crop_img')

    _, path = save_img_to_upload_dir(base64.b64decode(image))
    predict_fonts = get_predict(path)
    os.remove(path)

    return render_template('result.html', steps=STEPS, actual_step=3, fonts=predict_fonts)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_img_to_upload_dir(image):

    img = Image.open(io.BytesIO(image))
    img = img.convert('L')

    path = f'{UPLOAD_DIR}/{str(uuid.uuid4())}.jpg'
    img.save(path, 'jpeg')

    return img, path
