import csv
import re
from dataclasses import dataclass
from typing import List
from exceptions import InvalidDelimiterError


@dataclass
class SequenceData:
    id: int
    original_seq: str
    edited_seq: str


def detect_delimiter(header: str) -> str:
    """
    Detect the delimiter used in the header.

    :param header: The header string.
    :return: The detected delimiter.
    :raises ValueError: If an unsupported delimiter is detected.
    """
    if '\t' in header:
        return '\t'
    elif re.match(r"ID\s+Original_Seq\s+Result", header):
        return r'\s+'
    else:
        raise InvalidDelimiterError("Unsupported delimiter detected in the header.")


def read_tsv(file_path: str) -> List[SequenceData]:
    """
    Reads the TSV file and returns a list of SequenceData objects.

    :param file_path: The path to the TSV file.
    :return: A list of SequenceData objects.
    """
    data = []

    with open(file_path, "r") as file:
        # Read header and detect delimiter
        header = file.readline()
        delimiter = detect_delimiter(header)

        file.seek(0)  # Reset file pointer to the start

        if delimiter == r'\s+':
            # Handle space-separated values using regular expressions
            for line in file:
                if not line.strip():
                    continue  # Skip empty lines

                # Split line using delimiter
                row = re.split(delimiter, line.strip())

                # Extract data and append to the list
                try:
                    id, original_seq, edited_seq = int(row[0]), row[1], row[2]
                    data.append(SequenceData(id, original_seq, edited_seq))
                except (ValueError, IndexError):
                    print(f"Error processing row: {row}")
        else:
            # Handle tab-separated values using csv.reader
            tsv_reader = csv.reader(file, delimiter=delimiter)
            next(tsv_reader)  # Skip the header row

            for row in tsv_reader:
                # Extract data and append to the list
                try:
                    id, original_seq, edited_seq = int(row[0]), row[1], row[2]
                    data.append(SequenceData(id, original_seq, edited_seq))
                except (ValueError, IndexError):
                    print(f"Error processing row: {row}")

    return data


def find_differences(data: List[SequenceData]) -> dict:
    """Finds differences among the sequences and reports the counts of each edit type."""
    counts = {"deletion": 0, "insertion": 0, "mutation": 0}

    for sequence_data in data:
        original_seq, edited_seq = sequence_data.original_seq, sequence_data.edited_seq
        i, j = 0, 0

        while i < len(original_seq) and j < len(edited_seq):
            if original_seq[i] == edited_seq[j]:
                i += 1
                j += 1
            elif len(original_seq) > len(edited_seq):
                counts["deletion"] += 1
                i += 1
            elif len(original_seq) < len(edited_seq):
                counts["insertion"] += 1
                j += 1
            else:
                counts["mutation"] += 1
                i += 1
                j += 1

    return counts


def determine_change(sequence_data: SequenceData) -> str:
    """
    Determines the changes between an original and edited DNA sequence.
    """
    original_seq, edited_seq = sequence_data.original_seq, sequence_data.edited_seq
    i, j = 0, 0
    deletion, insertion, mutation = 0, 0, 0

    while i < len(original_seq) and j < len(edited_seq):
        if original_seq[i] == edited_seq[j]:
            i += 1
            j += 1
        elif len(original_seq) > len(edited_seq):
            deletion += 1
            i += 1
        elif len(original_seq) < len(edited_seq):
            insertion += 1
            j += 1
        else:
            mutation += 1
            i += 1
            j += 1

    change_message = ""
    if deletion > 0:
        change_message += f"{deletion} Deletion(s) detected. "
    if insertion > 0:
        change_message += f"{insertion} Insertion(s) detected. "
    if mutation > 0:
        change_message += f"{mutation} Mutation(s) detected. "
    if not change_message:
        change_message = "No change detected."

    return change_message.strip()
