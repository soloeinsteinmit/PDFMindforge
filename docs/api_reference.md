# API Reference 📚

## Core Classes

### PDFProcessor

Main class for processing PDF documents into machine-learning friendly formats.

#### Constructor

```python
PDFProcessor(
    chunk_size: int = 100,
    batch_multiplier: int = 2,
    langs: str = "English",
    clear_cuda_cache: bool = True,
    min_pages_for_split: int = 200
)
```

Parameters:
- `chunk_size`: Number of pages per chunk when splitting PDFs
- `batch_multiplier`: Multiplier for batch processing
- `langs`: Language specification for processing
- `clear_cuda_cache`: Whether to clear CUDA cache on initialization
- `min_pages_for_split`: Minimum number of pages before splitting a PDF

#### Methods

##### process_pdf_to_md
```python
def process_pdf_to_md(
    input_path: str,
    output_path: str,
    split_if_large: bool = True
) -> str
```

Parameters:
- `input_path`: Path to input PDF file
- `output_path`: Path for output markdown files
- `split_if_large`: Whether to split large PDFs into chunks

Returns:
- Path to the output directory containing markdown files

##### batch_process_directory
```python
def batch_process_directory(
    input_dir: str,
    output_dir: str,
    create_zip: bool = True
) -> Optional[str]
```

Parameters:
- `input_dir`: Input directory containing PDF files
- `output_dir`: Output directory for markdown files
- `create_zip`: Whether to create a ZIP of output files

Returns:
- Path to ZIP file if create_zip is True, None otherwise

### PDFSplitter

Handles splitting of large PDF documents into smaller chunks.

#### Constructor
```python
PDFSplitter(
    chunk_size: int = 100,
    min_pages_for_split: int = 200
)
```

Parameters:
- `chunk_size`: Number of pages per chunk
- `min_pages_for_split`: Minimum pages before splitting

#### Methods

##### split_pdf
```python
def split_pdf(
    file_path: str,
    output_folder: str
) -> List[str]
```

Parameters:
- `file_path`: Path to the input PDF file
- `output_folder`: Directory to store split PDF files

Returns:
- List of paths to split PDF files

## Utility Classes

### GPUManager

Manages GPU resources and CUDA operations.

#### Methods

##### is_cuda_available
```python
@staticmethod
def is_cuda_available() -> bool
```
Returns whether CUDA is available.

##### clear_cuda_cache
```python
@staticmethod
def clear_cuda_cache()
```
Clears CUDA cache if GPU is available.

##### get_device
```python
@staticmethod
def get_device() -> str
```
Returns the current device ("cuda" or "cpu").

##### get_gpu_memory_info
```python
@staticmethod
def get_gpu_memory_info() -> dict
```
Returns GPU memory usage information.

### FileManager

Handles file operations for PDFMindforge.

#### Methods

##### create_directory
```python
@staticmethod
def create_directory(directory: str) -> None
```
Creates directory if it doesn't exist.

##### get_pdf_files
```python
@staticmethod
def get_pdf_files(
    directory: str,
    recursive: bool = True
) -> List[str]
```
Returns list of PDF files in directory.

##### create_zip
```python
@staticmethod
def create_zip(
    source_dirs: List[str],
    output_path: str
) -> str
```
Creates ZIP archive from directories.