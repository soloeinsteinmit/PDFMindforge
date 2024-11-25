# Advanced Usage Guide 🚀

This guide covers advanced features and optimization techniques for PDFMindforge.

## GPU Acceleration 🎮

PDFMindforge leverages CUDA for GPU acceleration. Install with CUDA support:

```bash
pip install pdfmindforge[cuda]
```

### Optimizing GPU Usage

```python
processor = PDFProcessor(
    batch_multiplier=2,      # Controls VRAM usage (2 = ~6GB)
    clear_cuda_cache=True,   # Manage GPU memory
    workers=4               # Parallel processing
)
```

### Memory Management Tips

- Each worker uses ~5GB VRAM at peak
- Adjust `batch_multiplier` based on available GPU memory
- Use `clear_cuda_cache=True` for long-running processes
- Monitor GPU memory with `GPUManager.get_gpu_memory_info()`

## Batch Processing 📚

Process large datasets efficiently using batch mode:

```python
processor.batch_process_directory(
    input_dir="documents",
    output_dir="processed",
    recursive=True,          # Include subdirectories
    max_files=1000,         # Limit number of files
    use_marker_batch=True,  # Enable fast batch mode
    create_zip=True         # Save all outputs in ZIP
)
```

### Batch Processing Tips

1. Enable `use_marker_batch` for faster processing
2. Use `recursive=True` to process nested directories
3. Set `max_files` to prevent memory issues
4. Enable `create_zip` when working with online notebooks

## Large Document Processing 📄

Handle large PDFs efficiently:

```python
processor = PDFProcessor(
    chunk_size=50,           # Smaller chunks for memory
    min_pages_for_split=100, # Split threshold
    batch_multiplier=1       # Conservative VRAM usage
)

# Process with splitting
processor.process_pdf_to_md(
    input_path="large.pdf",
    output_path="output",
    split_if_large=True,    # Enable splitting
    create_zip=True         # Combine outputs
)
```

### Large Document Tips

1. Reduce `chunk_size` for memory efficiency
2. Lower `min_pages_for_split` for complex documents
3. Use conservative `batch_multiplier` settings
4. Enable `create_zip` to manage multiple outputs

## Multi-Language Support 🌐

Process documents in multiple languages:

```python
processor = PDFProcessor(
    langs="English,French,German",  # Multiple languages
    min_length=1000               # Skip short texts
)
```

### Language Processing Tips

1. Specify multiple languages for mixed documents
2. Use `min_length` to filter non-text PDFs
3. Consider memory usage with multiple languages

## Performance Optimization 🔧

### Memory Usage

```python
# Memory-efficient settings
processor = PDFProcessor(
    chunk_size=50,          # Smaller chunks
    batch_multiplier=1,     # Minimal VRAM
    min_length=500,        # Skip small texts
    clear_cuda_cache=True  # Clean memory
)
```

### Processing Speed

```python
# Speed-optimized settings
processor = PDFProcessor(
    batch_multiplier=3,     # More VRAM for speed
    workers=6,             # More parallel workers
    chunk_size=150        # Larger chunks
)
```

## Advanced Code Examples 💻

### Research Paper Processing

Process a directory of academic papers with custom settings:

```python
from pdfmindforge import PDFProcessor
from pathlib import Path
import logging

def process_research_papers(papers_dir: str, output_base: str):
    """Process research papers with specialized settings."""
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("paper_processor")
    
    # Initialize with research-paper optimized settings
    processor = PDFProcessor(
        # OCR settings for academic content
        langs="English",
        min_length=2000,        # Skip abstracts/cover pages
        
        # Performance settings for dense text
        chunk_size=100,
        batch_multiplier=2,
        workers=4,
        
        # Memory management
        clear_cuda_cache=True
    )
    
    try:
        # Process papers by category
        for category in Path(papers_dir).iterdir():
            if category.is_dir():
                logger.info(f"Processing category: {category.name}")
                
                # Create category-specific output
                output_dir = Path(output_base) / category.name
                
                # Process with category tracking
                zip_path = processor.batch_process_directory(
                    input_dir=str(category),
                    output_dir=str(output_dir),
                    recursive=True,
                    use_marker_batch=True,
                    create_zip=True
                )
                
                logger.info(f"Category {category.name} processed: {zip_path}")
                
    except Exception as e:
        logger.error(f"Error processing papers: {str(e)}")
        raise
    
    logger.info("All papers processed successfully")
```

### Large Dataset Pipeline

Process a large dataset with progress tracking and error handling:

```python
from pdfmindforge import PDFProcessor
from pdfmindforge.utils import GPUManager
from typing import List, Dict
import json
import time

class DatasetProcessor:
    def __init__(self, batch_size: int = 1000):
        self.batch_size = batch_size
        self.processor = PDFProcessor(
            batch_multiplier=2,
            workers=6,
            clear_cuda_cache=True
        )
        self.stats: Dict[str, int] = {
            "processed": 0,
            "failed": 0,
            "total_time": 0
        }
    
    def process_batch(self, files: List[str], output_dir: str) -> None:
        """Process a batch of files with stats tracking."""
        start_time = time.time()
        
        try:
            # Process batch
            self.processor.batch_process_directory(
                input_dir=files[0].parent,
                output_dir=output_dir,
                max_files=len(files),
                use_marker_batch=True
            )
            
            # Update stats
            self.stats["processed"] += len(files)
            
        except Exception as e:
            self.stats["failed"] += len(files)
            print(f"Batch failed: {str(e)}")
            
        finally:
            # Clean up GPU memory
            GPUManager.clear_cuda_cache()
            
        # Update timing
        batch_time = time.time() - start_time
        self.stats["total_time"] += batch_time
    
    def process_dataset(self, dataset_dir: str, output_dir: str) -> Dict:
        """Process entire dataset in batches."""
        # Get all PDF files
        pdf_files = list(Path(dataset_dir).rglob("*.pdf"))
        total_files = len(pdf_files)
        
        # Process in batches
        for i in range(0, total_files, self.batch_size):
            batch = pdf_files[i:i + self.batch_size]
            print(f"Processing batch {i//self.batch_size + 1}")
            self.process_batch(batch, output_dir)
            
            # Save progress
            self._save_progress()
        
        return self.stats
    
    def _save_progress(self) -> None:
        """Save processing statistics."""
        with open("processing_stats.json", "w") as f:
            json.dump(self.stats, f, indent=2)

# Usage example
processor = DatasetProcessor(batch_size=500)
stats = processor.process_dataset("large_dataset", "processed_data")
print(f"Processing complete. Stats: {stats}")
```

### Custom Processing Pipeline

Create a specialized processing pipeline with custom handling:

```python
from pdfmindforge import PDFProcessor
from pathlib import Path
from typing import Optional
import shutil
import logging

class CustomProcessor:
    def __init__(self):
        self.processor = PDFProcessor(
            batch_multiplier=2,
            workers=4,
            clear_cuda_cache=True
        )
        self.logger = self._setup_logging()
    
    @staticmethod
    def _setup_logging() -> logging.Logger:
        """Configure logging for the processor."""
        logger = logging.getLogger("custom_processor")
        handler = logging.FileHandler("processing.log")
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
    
    def _preprocess_pdf(self, pdf_path: Path) -> Optional[Path]:
        """Preprocess PDF before main processing."""
        try:
            # Create preprocessing directory
            prep_dir = Path("preprocessing")
            prep_dir.mkdir(exist_ok=True)
            
            # Copy to preprocessing area
            prep_path = prep_dir / pdf_path.name
            shutil.copy2(pdf_path, prep_path)
            
            return prep_path
            
        except Exception as e:
            self.logger.error(f"Preprocessing failed for {pdf_path}: {e}")
            return None
    
    def _postprocess_results(self, output_path: Path) -> None:
        """Post-process the results."""
        try:
            # Create archive of results
            if output_path.is_dir():
                shutil.make_archive(
                    str(output_path),
                    'zip',
                    str(output_path)
                )
                self.logger.info(f"Created archive: {output_path}.zip")
                
        except Exception as e:
            self.logger.error(f"Postprocessing failed: {e}")
    
    def process_document(self, input_path: str, output_path: str) -> bool:
        """Process a document with custom pre/post processing."""
        input_path = Path(input_path)
        output_path = Path(output_path)
        
        try:
            # Preprocess
            self.logger.info(f"Preprocessing: {input_path}")
            prep_path = self._preprocess_pdf(input_path)
            if not prep_path:
                return False
            
            # Main processing
            self.logger.info("Starting main processing")
            self.processor.process_pdf_to_md(
                input_path=str(prep_path),
                output_path=str(output_path),
                split_if_large=True
            )
            
            # Postprocess
            self.logger.info("Post-processing results")
            self._postprocess_results(output_path)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Processing failed: {e}")
            return False
        
        finally:
            # Cleanup
            if prep_path and prep_path.exists():
                prep_path.unlink()

# Usage example
processor = CustomProcessor()
success = processor.process_document(
    "important_document.pdf",
    "processed_output"
)
```

These examples demonstrate advanced usage patterns including:
- Custom logging and error handling
- Progress tracking and statistics
- Pre/post processing steps
- Batch processing with GPU memory management
- Dataset organization and management
- Robust error recovery

## Advanced Configuration Examples 🛠️

### Online Notebook Setup

```python
processor = PDFProcessor(
    batch_multiplier=2,
    clear_cuda_cache=True
)

# Process and download results
zip_path = processor.batch_process_directory(
    input_dir="data",
    output_dir="results",
    create_zip=True  # For easy download
)
```

### High-Performance Setup

```python
processor = PDFProcessor(
    batch_multiplier=3,     # High VRAM usage
    workers=8,             # Many workers
    chunk_size=200,       # Large chunks
    min_length=1000      # Skip small files
)
```

### Memory-Constrained Setup

```python
processor = PDFProcessor(
    batch_multiplier=1,     # Minimal VRAM
    workers=2,             # Few workers
    chunk_size=50,        # Small chunks
    clear_cuda_cache=True # Aggressive memory management
)
```

## Best Practices Summary 💡

1. **GPU Usage**
   - Match `batch_multiplier` to GPU memory
   - Enable `clear_cuda_cache` for stability
   - Monitor GPU memory usage

2. **Batch Processing**
   - Use `marker_batch` for speed
   - Enable `create_zip` for notebooks
   - Set appropriate `max_files`

3. **Memory Management**
   - Adjust `chunk_size` based on RAM
   - Use conservative settings for large files
   - Enable memory cleaning features

4. **Performance**
   - Balance workers and GPU memory
   - Optimize chunk size for your case
   - Use appropriate language settings

## Troubleshooting 🔍

### Common Issues

1. **Out of Memory**
   - Reduce `batch_multiplier`
   - Lower `chunk_size`
   - Decrease worker count
   - Enable `clear_cuda_cache`

2. **Slow Processing**
   - Enable `use_marker_batch`
   - Increase `batch_multiplier`
   - Adjust `chunk_size`
   - Add more workers

3. **Poor OCR Quality**
   - Check language settings
   - Adjust `min_length`
   - Consider document complexity