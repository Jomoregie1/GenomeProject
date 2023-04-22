import csv
from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class SequenceData:
    id: int
    original_seq: str
    edited_seq: str


def read_tsv(file_path: str) -> List[SequenceData]:
    """Reads the TSV file and returns a list of SequenceData objects."""
    data = []
    with open(file_path, "r") as file:
        tsv_reader = csv.reader(file, delimiter='\t')
        next(tsv_reader)  # Skip the header row
        for row in tsv_reader:
            id, original_seq, edited_seq = int(row[0]), row[1], row[2]
            data.append(SequenceData(id, original_seq, edited_seq))

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


