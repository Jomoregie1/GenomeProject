import unittest
from WebApp.app.sequence_analysis import find_differences, SequenceData, determine_change


class TestFindDifferences(unittest.TestCase):

    def test_no_edits(self):
        data = [
            SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTTAAGCA")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 0, "insertion": 0, "mutation": 0}
        self.assertEqual(result, expected_result)

    def test_single_deletion(self):
        data = [
            SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTAAGCA")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 1, "insertion": 0, "mutation": 0}
        self.assertEqual(result, expected_result)

    def test_multiple_deletions(self):
        data = [
            SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACAGCA")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 3, "insertion": 0, "mutation": 0}
        self.assertEqual(result, expected_result)

    def test_single_insertion(self):
        data = [
            SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTCTAAGCA")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 0, "insertion": 1, "mutation": 0}
        self.assertEqual(result, expected_result)

    def test_multiple_insertions(self):
        data = [
            SequenceData(1, "ACGTACGT", "ACGTGACGT")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 0, "insertion": 1, "mutation": 0}
        self.assertEqual(result, expected_result)

    def test_single_mutation(self):
        data = [
            SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTTGAGCA")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 0, "insertion": 0, "mutation": 1}
        self.assertEqual(result, expected_result)

    def test_multiple_mutations(self):
        data = [
            SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACGTCAGGA")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 0, "insertion": 0, "mutation": 3}
        self.assertEqual(result, expected_result)


class TestDetermineChange(unittest.TestCase):

    def test_no_edits(self):
        sequence_data = SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTTAAGCA")
        result = determine_change(sequence_data)
        expected_result = "No change detected."
        self.assertEqual(result, expected_result)

    def test_single_deletion(self):
        sequence_data = SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTAAGCA")
        result = determine_change(sequence_data)
        expected_result = "1 Deletion(s) detected."
        self.assertEqual(result, expected_result)

    def test_multiple_deletions(self):
        sequence_data = SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACAGCA")
        result = determine_change(sequence_data)
        expected_result = "3 Deletion(s) detected."
        self.assertEqual(result, expected_result)

    def test_single_insertion(self):
        sequence_data = SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTCTAAGCA")
        result = determine_change(sequence_data)
        expected_result = "1 Insertion(s) detected."
        self.assertEqual(result, expected_result)

    def test_multiple_insertions(self):
        sequence_data = SequenceData(1, "ACGTACGT", "ACGTGACGT")
        result = determine_change(sequence_data)
        expected_result = "1 Insertion(s) detected."
        self.assertEqual(result, expected_result)

    def test_single_mutation(self):
        sequence_data = SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTTGAGCA")
        result = determine_change(sequence_data)
        expected_result = "1 Mutation(s) detected."
        self.assertEqual(result, expected_result)

    def test_multiple_mutations(self):
        sequence_data = SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACGTCAGGA")
        result = determine_change(sequence_data)
        expected_result = "3 Mutation(s) detected."
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
