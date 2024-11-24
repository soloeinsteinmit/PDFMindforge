import unittest
from pdfmindforge.core import PDFSplitter

class TestPDFSplitter(unittest.TestCase):
    def setUp(self):
        self.splitter = PDFSplitter()
    
    def test_initialization(self):
        self.assertIsNotNone(self.splitter)
        self.assertEqual(self.splitter.chunk_size, 100)
    
    # TODO: Add more tests for split_pdf method

if __name__ == '__main__':
    unittest.main()