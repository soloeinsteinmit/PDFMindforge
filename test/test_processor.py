import unittest
from pdfmindforge import PDFProcessor

class TestPDFProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = PDFProcessor()
    
    def test_initialization(self):
        self.assertIsNotNone(self.processor)
        self.assertEqual(self.processor.langs, "English")
    
    # TODO: Add more tests for process_pdf_to_md, batch_process_directory, etc.

if __name__ == '__main__':
    unittest.main()