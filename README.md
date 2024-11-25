# PDFMindforge 🔄📚

[![PyPI version](https://badge.fury.io/py/pdfmindforge.svg)](https://badge.fury.io/py/pdfmindforge)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/)

Transform your PDF documents into machine-learning ready formats with intelligence and ease! 🚀

## ✨ Features

- 📊 Smart PDF splitting based on content size and complexity
- 🔄 Batch processing with parallel workers (GPU-optimized)
- 🎯 Markdown conversion with formatting preservation
- 💨 GPU acceleration support for faster processing
- 📦 Automatic ZIP archiving of processed documents
- 🖼️ Automatic image extraction and linking
- 🎛️ Configurable processing parameters
- 📈 Progress tracking and logging
- 🛡️ Error handling and recovery
- 🔧 Easy-to-use API

## 🎯 Purpose

PDFMindforge is designed to streamline the process of converting PDF documents into machine-learning friendly formats. Whether you're building a training dataset, analyzing document structures, or need to process large volumes of PDFs, PDFMindforge provides the tools you need.

## 🚀 Quick Start

### Installation

```bash
# Basic installation
pip install pdfmindforge

# Install with CUDA support (recommended for GPU acceleration)
pip install pdfmindforge[cuda]
```

### Basic Usage

```python
from pdfmindforge import PDFProcessor

# Initialize processor with optimal settings
processor = PDFProcessor()

# Process a single PDF
processor.process_pdf_to_md(
    input_path="input.pdf",
    output_path="output_folder"
)

# Process multiple PDFs in parallel
processor.batch_process_directory(
    input_dir="input_folder",
    output_dir="output_folder",
    workers=4  # Number of parallel workers
)
```

## 📋 Requirements

- Python 3.9+
- PyTorch (for GPU acceleration)
- PyPDF2
- marker_single

## 📚 API Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| chunk_size | int | 100 | Pages per chunk when splitting PDFs |
| batch_multiplier | int | 2 | VRAM multiplier (2 = ~6GB VRAM) |
| langs | str | "English" | OCR language(s) |
| clear_cuda_cache | bool | True | Clear GPU memory on init |
| min_pages_for_split | int | 200 | When to split large PDFs |
| max_pages | int | None | Max pages to process |
| start_page | int | None | Starting page number |
| workers | int | None | Parallel processing workers |
| min_length | int | None | Min text length to process |

## 🛠️ Advanced Configuration

### GPU Acceleration

PDFMindforge automatically detects and utilizes available GPU resources. The number of workers is optimized based on:
- Available VRAM (each worker uses ~5GB peak)
- CPU cores
- Document complexity

### Processing Options

```python
processor = PDFProcessor(
    # Basic settings
    chunk_size=100,              # Pages per chunk when splitting
    batch_multiplier=2,          # VRAM multiplier (2 = ~6GB VRAM)
    min_pages_for_split=200,     # When to split large PDFs
    
    # Processing control
    max_pages=None,              # Max pages to process per PDF
    start_page=None,             # Starting page number
    workers=4,                   # Parallel processing workers
    
    # OCR settings
    langs="English",             # OCR language(s)
    min_length=None,            # Min text length to process
    
    # Resource management
    clear_cuda_cache=True       # Clear GPU memory on init
)

# Batch processing with options
processor.batch_process_directory(
    input_dir="pdfs",
    output_dir="output",
    recursive=True,         # Search subdirectories
    create_zip=True,        # Create ZIP archive
    max_files=None,         # Max files to process
    use_marker_batch=True   # Use fast batch processing
)
```

## 📊 Performance Tips

1. 🚀 Adjust `batch_multiplier` based on available RAM
2. 💻 Use GPU acceleration for large documents
3. 📈 Enable `use_marker_batch` for processing many files
4. 🔧 Set `min_length` to skip image-heavy PDFs
5. 📈 Optimize `chunk_size` for your specific use case
6. 🔧 Configure `min_pages_for_split` based on document complexity

## Troubleshooting

### Common Issues

1. **Out of Memory Errors**
   - Reduce `batch_multiplier`
   - Lower number of `workers`
   - Enable `clear_cuda_cache`

2. **Slow Processing**
   - Enable GPU acceleration
   - Use `use_marker_batch=True` for multiple files
   - Set appropriate `min_length` to skip image-heavy PDFs

## Documentation

For detailed documentation, visit our [Documentation Site](https://docs.pdfmindforge.com). Coming soon!

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
git clone https://github.com/soloeinsteinmit/pdfmindforge.git
cd pdfmindforge
pip install -e ".[dev]"
```

## 📝 License

MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- PyPDF2 team for the excellent PDF processing library
- Marker Single project for markdown conversion capabilities
- PyTorch team for GPU acceleration support

## 📮 Contact & Support

- 📧 Create an issue for bug reports
- 🌟 Star the repo if you find it useful
- 🔄 Fork for your own modifications
- 📞 Contact: [Solomon Eshun](mailto:solomoneshun373@gmail.com)

## 🔜 Roadmap

- [ ] Multi-language support enhancement
- [ ] Advanced OCR integration
- [ ] Progress tracking UI
- [ ] Parallel processing optimization
- [ ] Cloud storage integration
- [ ] Read pdf from URL(from web)
- [ ] Split by file size option
- And much more!

---

Made with ❤️ by Solomon Eshun
