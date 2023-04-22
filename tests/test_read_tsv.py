import unittest
import os
from app.sequence_analysis import read_tsv, SequenceData


class TestReadTsv(unittest.TestCase):
    def test_read_tsv(self):
        # Step 1: Create a test TSV file with known data
        test_tsv_data = "ID\tOriginal_Seq\tResult\n1\tACTTAAGCA\tACTTAAGCA\n"
        test_tsv_file = "test.tsv"
        with open(test_tsv_file, "w") as file:
            file.write(test_tsv_data)

        # Step 2: Call the read_tsv function with the test TSV file
        result = read_tsv(test_tsv_file)

        # Step 3: Compare the returned value against the expected value
        expected_result = [SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTTAAGCA")]
        self.assertEqual(result, expected_result)

        # Clean up: Remove the test TSV file
        os.remove(test_tsv_file)


if __name__ == "__main__":
    unittest.main()
