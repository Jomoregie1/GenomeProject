# GenomeProject
A web-based tool to analyze and visualize DNA sequence edits. Users upload a TSV file with original and edited sequences, the app identifies edit types (deletion, insertion, mutation), and displays counts and color-coded visualizations. Built with Python, Flask, and D3.js.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Features

- Import TSV files containing DNA sequence data
- Identify and count different types of changes, including deletions, insertions, and mutations
- Display a table of results highlighting the differences between the original and edited sequences
- Generate a chart showing the counts of each edit type

## Installation

1. Clone the repository to your local machine: git clone https://github.com/your-username/dna-sequence-editor.git
2. Navigate to the project directory
3. Install the required dependencies
4. Run the Flask application
5. Open a web browser and navigate to `http://localhost:5000` to use the application.

## Usage

1. Click on the "Select a TSV file" button to choose a TSV file containing DNA sequence data.
2. Click on the "Upload" button to submit the file.
3. The application will process the file and display a table containing the original sequences, edited sequences, and the changes detected.
4. Click on the "Show/Hide Chart" button to view a chart summarising the counts of each edit type.

## Dependencies

- Flask
- D3.js
- Bootstrap
