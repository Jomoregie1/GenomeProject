import unittest
from WebApp.app.sequence_analysis import find_differences, SequenceData, determine_change


class TestFindDifferences(unittest.TestCase):

    def test_no_edits(self):
        """
        Test the find_differences function with no edits between the original and edited sequences.
        """
        data = [
            SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTTAAGCA")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 0, "insertion": 0, "mutation": 0}
        self.assertEqual(result, expected_result)

    def test_single_deletion(self):
        """
        Test the find_differences function with a single deletion in the edited sequence.
        """
        data = [
            SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTAAGCA")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 1, "insertion": 0, "mutation": 0}
        self.assertEqual(result, expected_result)

    def test_multiple_deletions(self):
        """
        Test the find_differences function with multiple deletions in the edited sequence.
        """
        data = [
            SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACAGCA")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 3, "insertion": 0, "mutation": 0}
        self.assertEqual(result, expected_result)

    def test_single_insertion(self):
        """
        Test the find_differences function with a single insertion in the edited sequence.
        """
        data = [
            SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTCTAAGCA")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 0, "insertion": 1, "mutation": 0}
        self.assertEqual(result, expected_result)

    def test_multiple_insertions(self):
        """
        Test the find_differences function with multiple insertions in the edited sequence.
        """
        data = [
            SequenceData(1, "ACGTACGT", "ACGTGACGT")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 0, "insertion": 1, "mutation": 0}
        self.assertEqual(result, expected_result)

    def test_single_mutation(self):
        """
        Test the find_differences function with a single mutation in the edited sequence.
        """
        data = [
            SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTTGAGCA")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 0, "insertion": 0, "mutation": 1}
        self.assertEqual(result, expected_result)

    def test_multiple_mutations(self):
        """
        Test the find_differences function with multiple mutations in the edited sequence.
        """
        data = [
            SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACGTCAGGA")
        ]
        result = find_differences(data)
        expected_result = {"deletion": 0, "insertion": 0, "mutation": 3}
        self.assertEqual(result, expected_result)


class TestDetermineChange(unittest.TestCase):

    def test_no_edits(self):
        """
        Test the determine_change function with no edits between the original and edited sequences.
        """
        sequence_data = SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTTAAGCA")
        result = determine_change(sequence_data)
        expected_result = "No change detected."
        self.assertEqual(result, expected_result)

    def test_single_deletion(self):
        """
        Test the determine_change function with a single deletion in the edited sequence.
        """
        sequence_data = SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTAAGCA")
        result = determine_change(sequence_data)
        expected_result = "1 Deletion(s) detected."
        self.assertEqual(result, expected_result)

    def test_multiple_deletions(self):
        """
        Test the determine_change function with multiple deletions in the edited sequence.
        """
        sequence_data = SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACAGCA")
        result = determine_change(sequence_data)
        expected_result = "3 Deletion(s) detected."
        self.assertEqual(result, expected_result)

    def test_single_insertion(self):
        """
        Test the determine_change function with a single insertion in the edited sequence.
        """
        sequence_data = SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTCTAAGCA")
        result = determine_change(sequence_data)
        expected_result = "1 Insertion(s) detected."
        self.assertEqual(result, expected_result)

    def test_multiple_insertions(self):
        """
        Test the determine_change function with multiple insertions in the edited sequence.
        """
        sequence_data = SequenceData(1, "ACGTACGT", "ACGTGACGT")
        result = determine_change(sequence_data)
        expected_result = "1 Insertion(s) detected."
        self.assertEqual(result, expected_result)

    def test_single_mutation(self):
        """
        Test the determine_change function with a single mutation in the edited sequence.
        """
        sequence_data = SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTTGAGCA")
        result = determine_change(sequence_data)
        expected_result = "1 Mutation(s) detected."
        self.assertEqual(result, expected_result)

    def test_multiple_mutations(self):
        """
        Test the determine_change function with multiple mutations in the edited sequence.
        """
        sequence_data = SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACGTCAGGA")
        result = determine_change(sequence_data)
        expected_result = "3 Mutation(s) detected."
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
