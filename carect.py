from flask import Flask, render_template, request
from PIL import Image, ImageEnhance, ImageOps
import pytesseract

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')
    
    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error="No selected file")
    
    # check if the file extension is allowed:
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return render_template('index.html', error='Invalid file extension')
    
    # read image and perform preprocessing
    image = Image.open(file)
    image = preprocess_image(image) # image enhancement and conversion
    image = enhance_image(image) # Apply image enhancement
    image = invert_colors(image) # invert colors if necessary

    # perform extraction
    text = pytesseract.image_to_string(image)

    return render_template('index.html', text=text)

def preprocess_image(image):
    # convert RGB if image is RGBA
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    return image

def enhance_image(image):
    # enhance contrast
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(2.0)
    return enhanced_image

def invert_colors(image):
    # invert colors to handle dark backgrounds
    inverted_image = ImageOps.invert(image)
    return inverted_image

if __name__ == '__main__':
    app.run(debug=True)

