# Frequently Asked Questions ❓

## General Questions 🤔

### What is PDFMindforge?
PDFMindforge is a Python library for processing PDF documents into machine-learning friendly formats. It leverages [marker](https://github.com/VikParuchuri/marker), a powerful OCR and document understanding tool, for high-quality text extraction and processing.

### What makes PDFMindforge different from other PDF processors?
PDFMindforge combines the power of marker's advanced OCR capabilities with efficient batch processing and GPU acceleration. It's specifically designed for handling large document collections and academic papers with superior text extraction quality.

## Installation Questions 🔧

### Why do I need CUDA support?
CUDA support enables GPU acceleration, which can significantly speed up processing, especially for large documents. marker's OCR engine benefits greatly from GPU acceleration.

### What if I don't have a GPU?
PDFMindforge works without a GPU, but processing will be slower. The CPU version is suitable for small documents or when processing speed isn't critical.

### Why am I getting CUDA out of memory errors?
This usually happens when processing large documents. Try:
1. Reducing `batch_multiplier`
2. Enabling `clear_cuda_cache`
3. Processing fewer documents simultaneously
4. Reducing `chunk_size`

## Usage Questions 📚

### How does marker integration work?
PDFMindforge uses marker's CLI tool (`marker_single`) for text extraction and OCR. marker provides:
- High-quality OCR capabilities
- Layout-aware text extraction
- Support for multiple languages
- Efficient batch processing

For more details, visit [marker's GitHub repository](https://github.com/VikParuchuri/marker).

### What's the recommended way to process large document collections?
```python
processor = PDFProcessor(
    batch_multiplier=2,      # Adjust based on GPU memory
    workers=4,               # Parallel processing
    use_marker_batch=True,   # Enable marker's batch mode
    clear_cuda_cache=True    # Manage memory
)
```

### How can I optimize processing speed?
1. Enable GPU acceleration with CUDA
2. Use marker's batch mode (`use_marker_batch=True`)
3. Adjust `batch_multiplier` based on GPU memory
4. Increase `workers` for parallel processing
5. Use appropriate `chunk_size` for your documents

### What languages are supported?
PDFMindforge supports all languages supported by marker. Specify languages in the `langs` parameter:
```python
processor = PDFProcessor(langs="English,French,German")
```

## Performance Questions ⚡

### What's the optimal batch_multiplier value?
- 2-3 for 8GB VRAM
- 3-4 for 12GB VRAM
- 4-6 for 16GB+ VRAM

### How much RAM do I need?
- Minimum: 8GB RAM
- Recommended: 16GB RAM
- For large batches: 32GB+ RAM

### How can I reduce memory usage?
1. Lower `batch_multiplier`
2. Reduce `chunk_size`
3. Process fewer documents simultaneously
4. Enable `clear_cuda_cache`
5. Use `min_length` to skip small documents

## Troubleshooting 🔍

### Why are some PDFs skipped during processing?
PDFs might be skipped if:
- They're too small (adjust `min_length`)
- They're corrupted or password-protected
- They contain mainly images (marker handles this automatically)

### Why is text quality poor for some documents?
Check if:
1. The correct language is specified
2. The PDF has proper text encoding
3. The document isn't heavily image-based
4. marker's OCR settings are appropriate

### How do I handle memory errors?
1. Reduce batch size:
```python
processor = PDFProcessor(
    batch_multiplier=1,
    chunk_size=50,
    clear_cuda_cache=True
)
```

2. Process in smaller chunks:
```python
processor.batch_process_directory(
    input_dir="docs",
    max_files=100,
    use_marker_batch=True
)
```

## Integration Questions 🔌

### Can I use PDFMindforge with other ML libraries?
Yes! PDFMindforge's output is compatible with most ML libraries. The extracted text is provided in clean, structured formats.

### How do I integrate with marker directly?
While PDFMindforge handles marker integration automatically, you can also use marker's CLI directly:
```bash
marker_single input.pdf output.md
```

### Can I customize marker's settings?
PDFMindforge uses optimized marker settings, but you can adjust parameters like:
- Language settings
- Batch processing mode
- OCR quality settings

## Updates and Support 🆙

### How often is PDFMindforge updated?
We regularly update to maintain compatibility with marker and add new features. Check our GitHub repository for the latest updates.

### Where can I get help?
1. Check this FAQ
2. Visit our GitHub Issues
3. Read marker's documentation
4. Join our Discord community (Coming Soon!)

### How can I contribute?
We welcome contributions! Check our GitHub repository for:
- Issue reporting
- Feature requests
- Pull requests
- Documentation improvements
