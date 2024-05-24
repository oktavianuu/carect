# Text Extractor Application

This is a Flask-based web application that extracts text from uploaded images using OCR (Optical Character Recognition). The application supports image preprocessing to enhance the quality of text extraction, including contrast enhancement and color inversion for images with dark backgrounds.

## Features

- Upload an image and extract text using OCR.
- Preprocess images to enhance text extraction:
  - Convert RGBA images to RGB.
  - Enhance image contrast.
  - Invert colors for images with dark backgrounds.
- Detect if the background color is white to adjust preprocessing steps.

## Technologies Used

- **Flask**: For creating the web application.
- **Pillow**: For image processing and enhancement.
- **pytesseract**: For text extraction from images using Tesseract OCR.

## Installation

### Prerequisites

- Python 3.6 or higher
- Tesseract OCR installed on your system. You can download it from [here](https://github.com/tesseract-ocr/tesseract).

### Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/textextractor.git
    cd textextractor
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Ensure Tesseract is installed and its executable is in your system's PATH. You can specify the path to the Tesseract executable if it's not in your PATH:

    ```python
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path based on your Tesseract installation.
    ```

## Usage

1. Run the Flask application:

    ```sh
    python app.py
    ```

2. Open a web browser and go to `http://127.0.0.1:5000`.

3. Upload an image file (PNG, JPG, or JPEG) and click the "Extract" button to extract text from the image.

## Application Structure

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML template for the web interface.

## Functions
`is_white(image)`
Checks if the background color of the image is white.

`preprocess_image(image)`
Converts RGBA images to RGB.

`enhance_image(image)`
Enhances the contrast of the image.

`invert_colors(image)`
Inverts the colors of the image to handle dark backgrounds.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Pillow](https://python-pillow.org/)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any inquiries, please contact oktavianuss.misro@gmail.com.
