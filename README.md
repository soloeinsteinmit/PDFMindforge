# PDFMindforge 🔄📚

[![PyPI version](https://badge.fury.io/py/pdfmindforge.svg)](https://badge.fury.io/py/pdfmindforge)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)

Transform your PDF documents into machine-learning ready formats with intelligence and ease! 🚀

## ✨ Features

- 📊 Smart PDF splitting based on content size and complexity
- 🔄 Batch processing with multi-document support
- 🎯 Markdown conversion with formatting preservation
- 💨 GPU acceleration support for faster processing
- 📦 Automatic ZIP archiving of processed documents
- 🔍 Intelligent page threshold detection
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

# Initialize processor
processor = PDFProcessor(
    chunk_size=100,
    batch_multiplier=2,
    langs="English"
)

# Process a single PDF
processor.process_pdf_to_md(
    input_path="path/to/your.pdf",
    output_path="path/to/output"
)

# Batch process an entire directory
processor.batch_process_directory(
    input_dir="path/to/pdfs",
    output_dir="path/to/output",
    create_zip=True
)
```

## 📋 Requirements

- Python 3.9+
- PyTorch (for GPU acceleration)
- PyPDF2
- marker_single

## 🛠️ Advanced Configuration

### GPU Acceleration

PDFMindforge automatically detects and utilizes available GPU resources:

```python
processor = PDFProcessor(
    clear_cuda_cache=True,  # Clear GPU memory before processing
    batch_multiplier=4      # Increase for better GPU utilization
)
```

### Custom Splitting Rules

Configure how documents are split:

```python
processor = PDFProcessor(
    min_pages_for_split=200,  # Minimum pages before splitting
    chunk_size=50            # Pages per chunk
)
```

## 🔍 API Reference

### PDFProcessor

#### Main Methods

- `process_pdf_to_md(input_path, output_path, split_if_large=True)`
- `batch_process_directory(input_dir, output_dir, create_zip=True)`
- `split_pdf(file_path, output_folder)`
- `create_zip(source_dir, output_path)`

#### Configuration Options

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| chunk_size | int | 100 | Number of pages per chunk |
| batch_multiplier | int | 2 | Batch size multiplier |
| langs | str | "English" | Document language |
| min_pages_for_split | int | 200 | Minimum pages before splitting |
| clear_cuda_cache | bool | True | Clear GPU cache on init |

## 📊 Performance Tips

1. 🚀 Adjust `batch_multiplier` based on available RAM
2. 💻 Use GPU acceleration for large documents
3. 📈 Optimize `chunk_size` for your specific use case
4. 🔧 Configure `min_pages_for_split` based on document complexity

## 🤝 Contributing

We welcome contributions! Please the [Contributing Guide](CONTRIBUTING.md) for details.

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

## 🔜 Roadmap

- [ ] Multi-language support enhancement
- [ ] Advanced OCR integration
- [ ] Custom markdown template support
- [ ] Progress tracking UI
- [ ] Parallel processing optimization
- [ ] Cloud storage integration
- [ ] Read pdf from URL(from web)
- [ ] Support for non-English languages
- [ ] Split by file size option

---

Made with ❤️ by the Solomon Eshun
