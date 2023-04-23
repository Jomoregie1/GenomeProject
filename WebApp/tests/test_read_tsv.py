import unittest
import os
from WebApp.app.sequence_analysis import read_tsv, SequenceData, detect_delimiter,InvalidDelimiterError


class TestReadTsv(unittest.TestCase):
    def test_read_tsv(self):
        """
        Test the read_tsv function to ensure it reads TSV data correctly and creates a list
        of SequenceData objects as expected.

        """

        # Create a test TSV file with known data
        test_tsv_data = "ID\tOriginal_Seq\tResult\n1\tACTTAAGCA\tACTTAAGCA\n"
        test_tsv_file = "test.tsv"
        with open(test_tsv_file, "w") as file:
            file.write(test_tsv_data)

        # Call the read_tsv function with the test TSV file
        result = read_tsv(test_tsv_file)

        # Compare the returned value against the expected value
        expected_result = [SequenceData(id=1, original_seq="ACTTAAGCA", edited_seq="ACTTAAGCA")]
        self.assertEqual(result, expected_result)

        # Clean up: Removes the test TSV file
        os.remove(test_tsv_file)


class TestDetectDelimiter(unittest.TestCase):
    """
        Test suite for the detect_delimiter function, which checks if the function
        correctly detects the delimiter used in the header string.

        Tests include detecting:
        - Tab delimiter
        - Space delimiter
        - Unsupported delimiter
    """

    def test_detect_tab_delimiter(self):
        header = "ID\tOriginal_Seq\tResult"
        self.assertEqual(detect_delimiter(header), '\t')

    def test_detect_space_delimiter(self):
        header = "ID Original_Seq Result"
        self.assertEqual(detect_delimiter(header), r'\s+')

    def test_detect_unsupported_delimiter(self):
        header = "ID,Original_Seq,Result"
        with self.assertRaises(InvalidDelimiterError):
            detect_delimiter(header)


if __name__ == "__main__":
    unittest.main()
