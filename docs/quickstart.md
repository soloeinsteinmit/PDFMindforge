# Quick Start Guide 🚀

Get started with PDFMindforge in minutes! This guide will show you the basic usage patterns.

## Basic Usage

### 1. Single PDF Processing

```python
from pdfmindforge import PDFProcessor

# Initialize processor with default settings
processor = PDFProcessor()

# Process a single PDF
processor.process_pdf_to_md(
    input_path="path/to/your.pdf",
    output_path="path/to/output"
)
```

### 2. Batch Processing
```python
# Process all PDFs in a directory
processor.batch_process_directory(
    input_dir="path/to/pdfs",
    output_dir="path/to/output",
    create_zip=True  # Automatically create a ZIP archive
)
```

## Configuration Options

Initialize PDFProcessor with these options to customize behavior:

```python
processor = PDFProcessor(
    chunk_size=100,          # Pages per chunk when splitting
    batch_multiplier=2,      # Batch size multiplier
    langs="English",         # Language specification
    clear_cuda_cache=True,   # Clear GPU memory before processing
    min_pages_for_split=200  # Minimum pages before splitting
)
```

## Common Patterns

### 1. Processing Large PDFs
```python
# Automatically splits large PDFs into manageable chunks
processor.process_pdf_to_md(
    input_path="large_document.pdf",
    output_path="output_dir",
    split_if_large=True  # Enable automatic splitting
)
```

### 2. Creating ZIP Archives
```python
# Process and create ZIP in one go
zip_path = processor.batch_process_directory(
    input_dir="pdf_folder",
    output_dir="output_folder",
    create_zip=True
)
print(f"Archive created at: {zip_path}")
```

### 3. GPU Optimization
```python
from pdfmindforge.utils import GPUManager

# Check GPU availability
if GPUManager.is_cuda_available():
    processor = PDFProcessor(
        batch_multiplier=4,  # Increase for better GPU utilization
        clear_cuda_cache=True
    )
```

## Next Steps

- Check out Advanced Usage for more features
- Read the API Reference for detailed documentation
- Visit our GitHub repository for updates