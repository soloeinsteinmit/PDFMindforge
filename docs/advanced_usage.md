# Advanced Usage Guide 🔧

This guide covers advanced features and optimization techniques for PDFMindforge.

## GPU Optimization

### Memory Management

Monitor and optimize GPU memory usage:

```python
from pdfmindforge import PDFProcessor
from pdfmindforge.utils import GPUManager

# Check GPU status
memory_info = GPUManager.get_gpu_memory_info()
print(f"GPU Memory Usage: {memory_info}")

# Initialize with GPU optimization
processor = PDFProcessor(
    clear_cuda_cache=True,    # Clear GPU memory before starting
    batch_multiplier=4        # Increase for better GPU utilization
)
```

### Performance Tuning

Optimize processing speed based on your hardware:

```python
# For high-end GPUs
processor = PDFProcessor(
    batch_multiplier=8,       # Larger batches for more powerful GPUs
    chunk_size=200           # Larger chunks if memory allows
)

# For systems with limited memory
processor = PDFProcessor(
    batch_multiplier=1,      # Smaller batches
    chunk_size=50,          # Smaller chunks
    clear_cuda_cache=True   # Aggressive memory clearing
)
```

## Large Document Processing

### Customizing Split Behavior

Fine-tune document splitting for your needs:

```python
# For very large documents
processor = PDFProcessor(
    chunk_size=50,            # Smaller chunks for better management
    min_pages_for_split=500   # Split threshold
)

# Process with custom splitting
output_dir = processor.process_pdf_to_md(
    input_path="large_document.pdf",
    output_path="output_dir",
    split_if_large=True
)
```

### Batch Processing Strategies

Efficient processing of multiple documents:

```python
# Process and organize by subdirectories
def process_with_structure(base_dir: str):
    processor = PDFProcessor()
    
    # Process each category
    categories = ["reports", "papers", "books"]
    for category in categories:
        input_dir = f"{base_dir}/{category}"
        output_dir = f"processed/{category}"
        
        # Process with category-specific settings
        processor.batch_process_directory(
            input_dir=input_dir,
            output_dir=output_dir,
            create_zip=True
        )
```

## Custom File Management

### Advanced ZIP Creation

Create custom ZIP archives with specific structures:

```python
from pdfmindforge.utils import FileManager

def create_structured_archive(processed_dirs: List[str], output_path: str):
    # Create ZIP with custom organization
    zip_path = FileManager.create_zip(
        source_dirs=processed_dirs,
        output_path=output_path
    )
    return zip_path
```

### File Organization

Implement custom file organization strategies:

```python
import os
from pdfmindforge.utils import FileManager

def organize_by_size(input_dir: str):
    # Get all PDFs
    pdf_files = FileManager.get_pdf_files(input_dir)
    
    # Organize into size categories
    for pdf_file in pdf_files:
        size = os.path.getsize(pdf_file)
        if size > 10_000_000:  # 10MB
            category = "large"
        elif size > 1_000_000:  # 1MB
            category = "medium"
        else:
            category = "small"
            
        # Move to appropriate directory
        target_dir = f"organized/{category}"
        FileManager.create_directory(target_dir)
        # Move file...
```

## Error Handling

### Implementing Robust Processing

Handle errors gracefully in production environments:

```python
from typing import Optional
import logging

def robust_processing(input_path: str) -> Optional[str]:
    try:
        processor = PDFProcessor(clear_cuda_cache=True)
        output_dir = processor.process_pdf_to_md(
            input_path=input_path,
            output_path="output"
        )
        return output_dir
    except Exception as e:
        logging.error(f"Error processing {input_path}: {str(e)}")
        GPUManager.clear_cuda_cache()  # Clean up
        return None
```

## Best Practices

### Memory Management
- Clear GPU cache regularly
- Monitor memory usage
- Adjust batch sizes based on available memory

### Performance Optimization
- Use appropriate chunk sizes
- Enable GPU acceleration when available
- Implement parallel processing for large batches

### Error Handling
- Implement proper logging
- Clean up resources after errors
- Use try-except blocks for production code

### File Organization
- Maintain clear directory structures
- Implement cleanup procedures
- Use meaningful file naming conventions