# Quick Start Guide 🚀

Get started with PDFMindforge in minutes! This guide covers basic installation and usage.

## Installation 

Install PDFMindforge using pip:

```bash
# Basic installation
pip install pdfmindforge

# With GPU support (recommended)
pip install pdfmindforge[cuda]
```

## Basic Usage 

Here's a simple example to get you started:

```python
from pdfmindforge import PDFProcessor

# Initialize processor
processor = PDFProcessor()

# Process a single PDF
processor.process_pdf_to_md(
    input_path="document.pdf",
    output_path="output"
)
```

## Batch Processing 

Process multiple PDFs efficiently:

```python
# Initialize with GPU optimization
processor = PDFProcessor(
    batch_multiplier=2,    # Use more VRAM for speed
    workers=4             # Process 4 files in parallel
)

# Process directory of PDFs
processor.batch_process_directory(
    input_dir="pdfs",
    output_dir="output",
    use_marker_batch=True,  # Enable fast batch processing
    recursive=True,         # Include subdirectories
    create_zip=True         # Create ZIP of outputs
)
```

## Common Options 

### Performance Settings

- `batch_multiplier`: Control VRAM usage (default=2)
- `workers`: Number of parallel workers
- `chunk_size`: Pages per chunk when splitting
- `clear_cuda_cache`: Manage GPU memory

### Processing Options

- `langs`: OCR language(s) (e.g., "English,French")
- `min_length`: Skip PDFs with little text
- `min_pages_for_split`: When to split large PDFs
- `max_pages`: Limit pages to process
- `start_page`: Starting page number

## Tips for Best Results 

1. **GPU Acceleration**
   - Install with `[gpu]` extra for faster processing
   - Use `batch_multiplier=2` for optimal speed/memory balance
   - Enable `clear_cuda_cache=True` for long runs

2. **Large Documents**
   - Set appropriate `min_pages_for_split`
   - Use smaller `chunk_size` for memory efficiency
   - Enable `split_if_large=True` when processing

3. **Batch Processing**
   - Use `use_marker_batch=True` for better performance
   - Set `workers` based on available resources
   - Enable `recursive=True` to process subdirectories

4. **Memory Management**
   - Each worker uses ~5GB VRAM peak
   - Adjust `batch_multiplier` based on available RAM
   - Use `min_length` to skip image-heavy PDFs

## Next Steps 

- Check out [Advanced Usage](advanced_usage.md) for more features
- See [API Reference](api_reference.md) for detailed documentation
- Visit our [GitHub](https://github.com/soloeinsteinmit/pdfmindforge) for updates