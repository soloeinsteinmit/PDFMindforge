# Installation Guide 🚀

## Requirements

PDFMindforge requires:
- Python 3.8 or higher
- CUDA-compatible GPU (optional, for GPU acceleration)

## Installation Methods

### Using pip (Recommended)
```bash
pip install pdfmindforge
```

### From Source
```bash
git clone https://github.com/soloeinsteinmit/PDFMindforge.git
cd PDFMindforge
pip install -e .
```

## Dependencies

PDFMindforge will automatically install these dependencies:

- torch>=2.4.1 (with CUDA support)
- transformers>=4.46.1
- accelerate>=0.24.1
- huggingface_hub>=0.19.4
- safetensors
- tokenizers
- Pillow
- numpy
- tqdm
- marker-pdf
- PyPDF2

## GPU Support

PDFMindforge automatically detects and uses available GPU resources. To enable GPU support:

1. Install CUDA toolkit (if not already installed)
2. Verify GPU detection:
```python
from pdfmindforge.utils import GPUManager
print(GPUManager.is_cuda_available())  # Should print True if GPU is available
print(GPUManager.get_device())         # Should print "cuda" if GPU is available
```

## Troubleshooting

### Common Issues

#### GPU Not Detected
- Ensure CUDA toolkit is installed
- Verify PyTorch CUDA installation:
```python
import torch
print(torch.cuda.is_available())
```

#### Memory Issues
Clear GPU memory:
```python
from pdfmindforge.utils import GPUManager
GPUManager.clear_cuda_cache()
```

### Getting Help

If you encounter any issues:

- Check our GitHub Issues
- Read our FAQ