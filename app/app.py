from flask import Flask, render_template, request, redirect, url_for
import os
import tempfile

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tsv_file = request.files["tsv_file"]
        if tsv_file:
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            tsv_file.save(temp_file.name)
            data = read_tsv(temp_file.name)
            os.unlink(temp_file.name)
            counts = find_differences(data)
            return render_template("index.html", counts=counts)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)