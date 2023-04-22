from flask import Flask, render_template, request
from sequence_analysis import read_tsv, find_differences, determine_change
import os
import tempfile

app = Flask(__name__, static_folder='C:/Users/Joseph/PycharmProjects/GenomicProject/WebApp/static',
            template_folder='C:/Users/Joseph/PycharmProjects/GenomicProject/WebApp/templates')


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tsv_file = request.files["tsv_file"]
        if tsv_file:
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            tsv_file.save(temp_file.name)
            temp_file.close()  # Close the file after saving
            data = read_tsv(temp_file.name)
            os.unlink(temp_file.name)
            counts = find_differences(data)
            change_messages = [determine_change(sequence_data) for sequence_data in data]
            return render_template("index.html", counts=counts, data=data, data_and_changes=zip(data, change_messages))
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
