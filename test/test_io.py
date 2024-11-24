import unittest
import os
from pdfmindforge.utils import FileManager

class TestFileManager(unittest.TestCase):
    def test_create_directory(self):
        test_dir = "test_directory"
        FileManager.create_directory(test_dir)
        self.assertTrue(os.path.exists(test_dir))
        os.rmdir(test_dir)
    
    # TODO: Add more tests for get_pdf_files, create_zip, etc.

if __name__ == '__main__':
    unittest.main()