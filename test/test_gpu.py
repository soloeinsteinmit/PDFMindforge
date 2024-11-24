import unittest
from pdfmindforge.utils import GPUManager

class TestGPUManager(unittest.TestCase):
    def test_cuda_availability(self):
        is_available = GPUManager.is_cuda_available()
        self.assertIsInstance(is_available, bool)
    
    def test_get_device(self):
        device = GPUManager.get_device()
        self.assertIn(device, ["cuda", "cpu"])

if __name__ == '__main__':
    unittest.main()