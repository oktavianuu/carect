from flask import Flask, render_template, request
from PIL import Image
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
    
    # read image and perform OCR
    image = Image.open(file)
    text = pytesseract.image_to_string(image)

    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
    
