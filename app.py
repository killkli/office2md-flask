# app.py
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from markitdown import MarkItDown
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')  # Use environment variable

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'xls', 'docx', 'pptx', 'pdf'}  # Add more as needed

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB limit

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '' or file.filename == None:
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            try:
                markitdown = MarkItDown()
                result = markitdown.convert(file_path)
                markdown_text = result.text_content

                # Optionally, remove the uploaded file after processing
                os.remove(file_path)

                return render_template('result.html', markdown=markdown_text)
            except Exception as e:
                flash(f'An error occurred while processing the file: {str(e)}')
                return redirect(request.url)
        else:
            flash('Unsupported file type')
            return redirect(request.url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
