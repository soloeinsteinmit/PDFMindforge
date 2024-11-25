# API Reference 📚

## PDFProcessor

The main class for processing PDF documents.

### Constructor

```python
PDFProcessor(
    chunk_size: int = 100,
    batch_multiplier: int = 2,
    langs: Optional[str] = "English",
    clear_cuda_cache: bool = True,
    min_pages_for_split: int = 200,
    max_pages: Optional[int] = None,
    start_page: Optional[int] = None,
    workers: Optional[int] = None,
    min_length: Optional[int] = None
)
```

#### Parameters

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

### Methods

#### process_pdf_to_md()

Process a single PDF file to markdown format.

```python
process_pdf_to_md(
    input_path: str,
    output_path: str,
    split_if_large: bool = True,
    create_zip: bool = True
) -> str
```

##### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| input_path | str | | Path to input PDF |
| output_path | str | | Path for output files |
| split_if_large | bool | True | Split large PDFs |
| create_zip | bool | True | Create ZIP archive |

##### Returns

- str: Path to output file or ZIP

#### batch_process_directory()

Process all PDF files in a directory.

```python
batch_process_directory(
    input_dir: str,
    output_dir: str,
    recursive: bool = True,
    create_zip: bool = True,
    max_files: Optional[int] = None,
    use_marker_batch: bool = True
) -> str
```

##### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| input_dir | str | | Input directory path |
| output_dir | str | | Output directory path |
| recursive | bool | True | Search subdirectories |
| create_zip | bool | True | Create ZIP archive |
| max_files | int | None | Max files to process |
| use_marker_batch | bool | True | Use fast batch mode |

##### Returns

- str: Path to output directory or ZIP

## Utility Classes 🛠️

### GPUManager

Manages GPU resources and CUDA operations for efficient processing.

#### Methods

##### is_cuda_available()
```python
@staticmethod
def is_cuda_available() -> bool
```
Check if CUDA is available for GPU acceleration.

##### clear_cuda_cache()
```python
@staticmethod
def clear_cuda_cache()
```
Clear CUDA memory cache to free up GPU resources. Useful during long processing sessions.

##### get_device()
```python
@staticmethod
def get_device() -> str
```
Get the current device ("cuda" or "cpu"). Used for torch operations.

##### get_gpu_memory_info()
```python
@staticmethod
def get_gpu_memory_info() -> dict
```
Get detailed GPU memory usage information:
- total: Total VRAM in GB
- allocated: Currently allocated VRAM
- cached: Cached VRAM
- available: Available VRAM

##### get_max_workers()
```python
def get_max_workers(self, safety_margin: float = 0.9) -> int
```
Calculate maximum number of workers based on available VRAM.

Parameters:
- safety_margin: Fraction of total VRAM to consider available (0.0 to 1.0)

##### estimate_vram_usage()
```python
def estimate_vram_usage(self, num_workers: int) -> Dict[str, float]
```
Estimate VRAM usage for a given number of workers.

Parameters:
- num_workers: Number of parallel workers

Returns:
- Dictionary with peak and average VRAM usage estimates in GB

#### Usage Examples

```python
# GPU Memory Management
gpu_manager = GPUManager()

# Check GPU availability
if gpu_manager.is_cuda_available():
    print(f"Using device: {gpu_manager.get_device()}")
    
    # Get memory info
    memory_info = gpu_manager.get_gpu_memory_info()
    print(f"Available VRAM: {memory_info['available']:.2f} GB")
    
    # Calculate optimal workers
    max_workers = gpu_manager.get_max_workers(safety_margin=0.8)
    print(f"Recommended workers: {max_workers}")
    
    # Estimate VRAM usage
    vram_usage = gpu_manager.estimate_vram_usage(max_workers)
    print(f"Peak VRAM usage: {vram_usage['peak_vram']:.2f} GB")
```

### FileManager

Handles file operations and management for PDFs and output files.

#### Methods

##### create_directory()
```python
@staticmethod
def create_directory(directory: str) -> None
```
Create directory if it doesn't exist. Creates parent directories as needed.

##### get_pdf_files()
```python
@staticmethod
def get_pdf_files(
    directory: str,
    recursive: bool = True,
    max_files: Optional[int] = None,
    min_length: Optional[int] = None
) -> List[str]
```
Get all PDF files in a directory meeting specified criteria.

Parameters:
- directory: Directory to search
- recursive: Search in subdirectories
- max_files: Maximum number of files to return
- min_length: Minimum text length required in PDF

##### create_zip()
```python
@staticmethod
def create_zip(source_dirs: List[str], output_path: str) -> str
```
Create a ZIP archive from multiple directories.

Parameters:
- source_dirs: List of directories to zip
- output_path: Output ZIP file path

Returns:
- Path to created ZIP file

##### get_pdf_info()
```python
@staticmethod
def get_pdf_info(pdf_path: str) -> dict
```
Get information about a PDF file.

Returns dictionary with:
- num_pages: Number of pages
- text_length: Total text length
- error: Error message if processing failed

##### get_relative_path()
```python
@staticmethod
def get_relative_path(file_path: str, base_dir: str) -> str
```
Get relative path from base directory. Useful for ZIP archive creation.

#### Usage Examples

```python
# File Operations
file_manager = FileManager()

# Process PDFs in directory
pdf_files = file_manager.get_pdf_files(
    directory="documents",
    recursive=True,
    max_files=100,
    min_length=1000  # Skip small PDFs
)

# Get PDF information
for pdf_file in pdf_files:
    info = file_manager.get_pdf_info(pdf_file)
    print(f"Pages: {info['num_pages']}, Text Length: {info['text_length']}")

# Create ZIP of processed files
output_dirs = ["output/text", "output/images"]
zip_path = file_manager.create_zip(output_dirs, "processed_documents")
print(f"Created archive: {zip_path}")
```

## Error Handling

The library raises standard Python exceptions:

- `ValueError`: Invalid input parameters
- `FileNotFoundError`: Missing files/directories
- `RuntimeError`: Processing errors
- `MemoryError`: Insufficient memory

## Best Practices 💡

### GPU Memory Management

1. **Monitor VRAM Usage**
   ```python
   gpu_manager = GPUManager()
   memory_info = gpu_manager.get_gpu_memory_info()
   if memory_info["available"] < 4:  # Less than 4GB available
       gpu_manager.clear_cuda_cache()
   ```

2. **Optimize Worker Count**
   ```python
   # Conservative worker estimation
   max_workers = gpu_manager.get_max_workers(safety_margin=0.8)
   vram_usage = gpu_manager.estimate_vram_usage(max_workers)
   ```

### File Management

1. **Efficient PDF Processing**
   ```python
   # Process only substantial PDFs
   pdfs = file_manager.get_pdf_files(
       directory="papers",
       min_length=2000,  # Skip small documents
       max_files=500     # Limit batch size
   )
   ```

2. **Organized Output**
   ```python
   # Create structured output
   for category in ["papers", "reports"]:
       file_manager.create_directory(f"output/{category}")
       
   # Create single archive
   zip_path = file_manager.create_zip(
       [f"output/{cat}" for cat in ["papers", "reports"]],
       "processed_documents"
   )
   ```

1. **Memory Management**
   ```python
   processor = PDFProcessor(
       batch_multiplier=1,     # Conservative VRAM
       clear_cuda_cache=True   # Clean memory
   )
   ```

2. **Batch Processing**
   ```python
   processor.batch_process_directory(
       input_dir="pdfs",
       use_marker_batch=True,  # Faster processing
       recursive=True          # Include subdirs
   )
   ```

3. **Large Documents**
   ```python
   processor = PDFProcessor(
       chunk_size=50,          # Smaller chunks
       min_pages_for_split=100 # Split sooner
   )
   ```