# Installation Guide 📥

This guide covers all installation methods and requirements for PDFMindforge.

## System Requirements 💻

- Python 3.9 or higher
- 8GB RAM minimum (16GB recommended)
- CUDA-capable GPU (optional, but recommended)
- Windows, Linux, or macOS

## Dependencies 📦

Core dependencies:
- PyTorch (1.8+)
- PyPDF2 (2.0+)
- marker_single
- multiprocessing

Optional dependencies:
- CUDA Toolkit (11.0+) for GPU acceleration
- cuDNN for improved GPU performance

## Installation Methods

### Using pip (Recommended) 🚀

1. Basic Installation:
```bash
pip install pdfmindforge
```

2. With CUDA Support (Recommended):
```bash
pip install pdfmindforge[cuda]
```

3. Development Version:
```bash
pip install git+https://github.com/soloeinsteinmit/PDFMindforge.git
```

### From Source 🔧

1. Clone the repository:
```bash
git clone https://github.com/soloeinsteinmit/PDFMindforge.git
cd PDFMindforge
```

2. Install dependencies:
```bash
# Basic installation
pip install -r requirements.txt

# With CUDA support
pip install -r requirements-cuda.txt
```

3. Install in development mode:
```bash
pip install -e .
```

## Verify Installation ✅

Test your installation:

```python
from pdfmindforge import PDFProcessor
from pdfmindforge.utils import GPUManager

# Check installation
processor = PDFProcessor()
print("PDFMindforge installed successfully!")

# Check GPU support
if GPUManager.is_cuda_available():
    print("CUDA is available!")
    print(f"GPU Memory: {GPUManager.get_gpu_memory_info()}")
```

## Environment Setup 🌟

### CUDA Setup (Optional)

1. Download and install [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit)
2. Install cuDNN from [NVIDIA Developer](https://developer.nvidia.com/cudnn)
3. Set environment variables:
   ```bash
   # Windows
   set PATH=C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.0\bin;%PATH%
   
   # Linux/macOS
   export PATH=/usr/local/cuda-11.0/bin:$PATH
   ```

### Virtual Environment (Recommended)

Create an isolated environment:

```bash
# Using venv
python -m venv pdfmindforge-env
source pdfmindforge-env/bin/activate  # Linux/macOS
pdfmindforge-env\Scripts\activate     # Windows

# Using conda
conda create -n pdfmindforge python=3.9
conda activate pdfmindforge
```

## Troubleshooting 🔍

### Common Issues

1. **CUDA Not Found**
   ```bash
   # Check CUDA installation
   nvidia-smi
   # Check PyTorch CUDA support
   python -c "import torch; print(torch.cuda.is_available())"
   ```

2. **Memory Issues**
   - Increase available RAM
   - Reduce `batch_multiplier` in PDFProcessor
   - Enable `clear_cuda_cache`

3. **Import Errors**
   - Check Python version compatibility
   - Verify all dependencies are installed
   - Try reinstalling with `pip install --force-reinstall`

### Getting Help

- Check our [GitHub Issues](https://github.com/soloeinsteinmit/PDFMindforge/issues)
- Join our [Discord Community](https://discord.gg/pdfmindforge). Coming Soon!
- Read the [FAQ](faq.md)

## Next Steps 🎯

1. Read the [Quick Start Guide](quickstart.md)
2. Try the [Basic Examples](examples/sample_usage.py)
3. Explore [Advanced Usage](advanced_usage.md)

## Upgrading ⬆️

Keep PDFMindforge up to date:

```bash
# Update to latest stable
pip install --upgrade pdfmindforge

# Update to latest development version
pip install --upgrade git+https://github.com/soloeinsteinmit/PDFMindforge.git