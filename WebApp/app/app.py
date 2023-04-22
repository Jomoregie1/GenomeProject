from flask import render_template, request
from sequence_analysis import read_tsv, find_differences, determine_change
from WebApp.app import create_app
import os
import tempfile

app = create_app()


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Index route to handle the file upload and processing of TSV files containing DNA sequences.
    """
    if request.method == "POST":
        tsv_file = request.files["tsv_file"]

        if tsv_file:
            # Save the uploaded file to a temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            tsv_file.save(temp_file.name)
            temp_file.close()  # Close the file after saving

            # Read the data from the TSV file
            data = read_tsv(temp_file.name)

            # Remove the temporary file
            os.unlink(temp_file.name)

            # Process the data
            counts = find_differences(data)
            change_messages = [determine_change(sequence_data) for sequence_data in data]

            # Render the template with the processed data
            return render_template("index.html", counts=counts, data=data, data_and_changes=zip(data, change_messages))

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
