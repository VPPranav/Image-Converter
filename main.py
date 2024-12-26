# pip3 install flask opencv-python
from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import cv2
import os

# Configuration
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'webp', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file is allowed based on its extension."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def processImage(filename, operation):
    """Process the image based on the operation."""
    print(f"Processing {filename} with operation {operation}")
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img = cv2.imread(img_path)
    new_filename = None

    match operation:
        case "cgray":
            img_processed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            new_filename = os.path.join(app.config['PROCESSED_FOLDER'], f"{filename.rsplit('.', 1)[0]}_gray.jpg")
            cv2.imwrite(new_filename, img_processed)
        case "cwebp":
            new_filename = os.path.join(app.config['PROCESSED_FOLDER'], f"{filename.rsplit('.', 1)[0]}.webp")
            cv2.imwrite(new_filename, img)
        case "cjpg":
            new_filename = os.path.join(app.config['PROCESSED_FOLDER'], f"{filename.rsplit('.', 1)[0]}.jpg")
            cv2.imwrite(new_filename, img)
        case "cpng":
            new_filename = os.path.join(app.config['PROCESSED_FOLDER'], f"{filename.rsplit('.', 1)[0]}.png")
            cv2.imwrite(new_filename, img)
        case _:
            flash("Invalid operation selected.")
            return None

    return new_filename

@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

@app.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    """Handle image upload and processing."""
    if request.method == "POST":
        operation = request.form.get("operation")
        if 'file' not in request.files:
            flash('No file part in the request.')
            return render_template("index.html")
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected.')
            return render_template("index.html")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            processed_file_path = processImage(filename, operation)
            if processed_file_path:
                flash(f"Your image has been processed and is available "
                      f"<a href='/{processed_file_path}' target='_blank'>here</a>.", "success")
            else:
                flash("Failed to process the image. Please try again.", "error")
            return render_template("index.html")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
