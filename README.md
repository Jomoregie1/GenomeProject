# Genome Project
A web-based tool to analyse and visualise DNA sequence edits. Users upload a TSV file with original and edited sequences, the app identifies edit types (deletion, insertion, mutation), and displays changes, counts and color-coded visualisations. Built with Python, Flask, and D3.js.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Architectural and Design Decisions](#architectural-and-design-decisions)
- [Testing Strategy](#testing-strategy)
- [Future Improvements](#future-improvements)


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

### The Genome Project is built using a modular and scalable architecture that consists of the following main components:

- Frontend: Developed using D3.js and Bootstrap, the frontend is responsible for presenting the data and providing interactive visualisations.
- Backend: The Flask web framework is used for handling HTTP requests, processing TSV files, and providing the necessary API endpoints for the frontend.
- Data Model: The `SequenceData` class serves as the main data structure for storing and processing DNA sequence information.
- Utilities: Helper functions, such as `detect_delimiter`, `read_tsv`, and `find_differences`, are used to modularise the code and handle various tasks related to data processing and analysis.

### Key design decisions and considerations include:

1. Choosing Flask for its lightweight and easy-to-use nature, which allowed for rapid development and deployment of the application.
2. Using D3.js for creating interactive and visually appealing data visualisations.
3. Implementing the `SequenceData` class to encapsulate the DNA sequence data, making it easier to manage and process the data.
4. Utilising Python's built-in libraries, such as `csv` and `re`, to simplify file parsing and data manipulation.
5. Designing the application with modularity in mind, allowing for easier maintenance, scalability, and the addition of new features in the future.
6. `InvalidDelimiterError` is used to handle cases where an invalid delimiter is detected in the input file. This allows the application to provide more meaningful error messages to the user.

### Trade-offs considered during the development process include:

- Balancing code readability with performance, prioritising readability for the current project scope while keeping in mind potential optimisations for future scalability.
- Prioritising the core features of the application, such as DNA sequence comparison and visualisation, over additional features that could be implemented in future iterations.
- Error Handling, I used a custom exception for handling invalid delimiters and provided basic error handling, but more advanced error handling and input validation could be implemented to further improve the application's robustness.
- I chose to perform most data processing tasks on the server-side, while using client-side JavaScript (D3.js) to handle the visualization. This decision allows for better separation of concerns and offloads some processing to the client, but it may require more server resources for large datasets.

## Testing Strategy

The testing strategy for the Genome Project consists of unit tests to ensure the correct functionality of the core components, such as file parsing, delimiter detection, and DNA sequence comparison. The tests are written using Python's built-in `unittest` library. The test cases cover a range of scenarios, including various types of edits (insertions, deletions, and mutations) and edge cases.

To run the tests, execute the following command in the terminal:

```bash
python -m unittest discover -s WebApp/tests -p "test_*.py"
```
### Test Cases

The test suite is divided into several test cases that focus on specific functions within the application:

- **TestReadTsv**: Tests the `read_tsv` function to ensure it reads TSV data correctly and creates a list of `SequenceData` objects as expected.

- **TestDetectDelimiter**: Tests the `detect_delimiter` function to check if it correctly detects the delimiter used in the header string. This suite includes tests for detecting tab and space delimiters, as well as unsupported delimiters.

- **TestFindDifferences**: Tests the `find_differences` function to ensure it correctly identifies the differences between the original and edited DNA sequences, such as insertions, deletions, and mutations. The test cases include scenarios with no edits, single and multiple edits of each type.

- **TestDetermineChange**: Tests the `determine_change` function to ensure it generates the correct summary message based on the detected changes in the DNA sequences. The test cases cover the same scenarios as the TestFindDifferences test suite.

## Future Improvements

There are several enhancements and new features that could be implemented in future iterations of the Genome Project:

1. **Parallel processing:** Improve performance for large datasets by implementing parallel processing techniques, such as multi-threading or utilising GPU resources.
2. **Advanced error handling and input validation:** Enhance the application's robustness by implementing more comprehensive error handling and input validation techniques.
3. **Support for additional file formats:** Allow users to upload DNA sequence data in other common formats, such as FASTA, GenBank, or EMBL.
4. **Multiple sequence alignment:** Implement an algorithm for multiple sequence alignment, allowing users to compare more than two DNA sequences at a time.
5. **Visualisation enhancements:** Improve the data visualisation by adding more interactivity, customisation options, and support for different types of visualisations (e.g., heatmaps, phylogenetic trees, etc.).
6. **Integration with external APIs:** Integrate the application with external APIs, such as those provided by NCBI or Ensembl, to retrieve additional sequence data or annotations.
7. **User authentication and data storage:** Implement user authentication to allow users to save their data and analysis results for future access.
8. **Automated tests for frontend components:** Expand the test suite to cover frontend components and interactions, improving the overall reliability and maintainability of the application.
