from flask import Flask, render_template, request, make_response
from utils.runner import run_code
from utils.file_manager import save_code_to_file, save_upload, save_history, load_history
from utils.syntax_highlight import highlight_python

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"

@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    output = ""
    highlighted_code = ""
    uploaded_file_name = ""

    if request.method == "POST":
        code = request.form.get("code", "")

        # Clear Editor
        if "clear_editor" in request.form:
            code = ""
            output = ""

        # Run Code
        if "run_code" in request.form:
            output = run_code(code)
            save_history(code)

        # Download File
        if "download_file" in request.form:
            filename = request.form.get("filename", "").strip()
            if not filename:
                filename = "script.py"
            response = make_response(code)
            response.headers["Content-Disposition"] = f"attachment; filename={filename}"
            response.headers["Content-Type"] = "text/plain"
            return response

        # Download Output
        if "download_output" in request.form:
            filename = request.form.get("output_filename", "").strip()
            if not filename:
                filename = "output.txt"
            response = make_response(output)
            response.headers["Content-Disposition"] = f"attachment; filename={filename}"
            response.headers["Content-Type"] = "text/plain"
            return response

        # Upload File
        if "upload_file" in request.form:
            file = request.files.get("upload_file_input")
            if file:
                uploaded_file_name = file.filename
                path = save_upload(file)
                with open(path, "r") as f:
                    code = f.read()

    highlighted_code = highlight_python(code)

    history = load_history()

    return render_template(
        "index.html",
        code=code,
        output=output,
        highlighted_code=highlighted_code,
        uploaded_file_name=uploaded_file_name,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)

