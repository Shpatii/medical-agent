from flask import Flask, request, render_template_string
from flask_cors import CORS
import os
from logic.extract import extract_text_from_pdf, generate_medical_chronology

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

UPLOAD_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Medical PDF Upload</title></head>
<body>
  <h1>Upload Medical PDF</h1>
  <form method="POST" action="/upload" enctype="multipart/form-data">
    <input type="file" name="pdf" />
    <button type="submit">Submit</button>
  </form>
</body>
</html>
"""

RESULT_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Summary</title></head>
<body>
  <h1>Medical Summary</h1>
  <pre>{{ summary }}</pre>
  <a href="/">⬅️ Back</a>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(UPLOAD_PAGE)

@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        file = request.files.get("pdf")
        if not file:
            return "No file uploaded", 400

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        text = extract_text_from_pdf(file_path)
        chronology = generate_medical_chronology(text)

        return render_template_string(RESULT_PAGE, summary=chronology)

    except Exception as e:
        return f"Server Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)