# Genome Project
A web-based tool to analyse and visualise DNA sequence edits. Users upload a TSV file with original and edited sequences, the app identifies edit types (deletion, insertion, mutation), and displays counts and color-coded visualisations. Built with Python, Flask, and D3.js.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Architectural and Design Decisions](#architectural-and-design-decisions)

## Features

- Import TSV files containing DNA sequence data
- Identify and count different types of changes, including deletions, insertions, and mutations
- Display a table of results highlighting the differences between the original and edited sequences
- Generate a chart showing the counts of each edit type

## Installation

1. Clone the repository to your local machine: git clone https://github.com/Jomoregie1/GenomeProject.git
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

## Architectural and Design Decisions

The Genome Project is built using a modular and scalable architecture that consists of the following main components:

- Frontend: Developed using D3.js and Bootstrap, the frontend is responsible for presenting the data and providing interactive visualizations.
- Backend: The Flask web framework is used for handling HTTP requests, processing TSV files, and providing the necessary API endpoints for the frontend.
- Data Model: The `SequenceData` class serves as the main data structure for storing and processing DNA sequence information.
- Utilities: Helper functions, such as `detect_delimiter`, `read_tsv`, and `find_differences`, are used to modularise the code and handle various tasks related to data processing and analysis.

Key design decisions and considerations include:

1. Choosing Flask for its lightweight and easy-to-use nature, which allowed for rapid development and deployment of the application.
2. Using D3.js for creating interactive and visually appealing data visualisations.
3. Implementing the `SequenceData` class to encapsulate the DNA sequence data, making it easier to manage and process the data.
4. Utilising Python's built-in libraries, such as `csv` and `re`, to simplify file parsing and data manipulation.
5. Designing the application with modularity in mind, allowing for easier maintenance, scalability, and the addition of new features in the future.
6. `InvalidDelimiterError` is used to handle cases where an invalid delimiter is detected in the input file. This allows the application to provide more meaningful error messages to the user.

Trade-offs considered during the development process include:

- Balancing code readability with performance, prioritising readability for the current project scope while keeping in mind potential optimisations for future scalability.
- Prioritising the core features of the application, such as DNA sequence comparison and visualisation, over additional features that could be implemented in future iterations.

