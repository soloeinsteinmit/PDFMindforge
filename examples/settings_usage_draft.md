how to use settings

### 1. Using default settings:
```python
from pdfmindforge.config import settings

# Access settings
chunk_size = settings.pdf.chunk_size
use_gpu = settings.gpu.use_gpu

# Modify settings
settings.pdf.chunk_size = 200
settings.gpu.memory_limit = 4096  # MB
```
### 2. Loading custom settings from a file:


```python
from pdfmindforge.config import Settings

# Load from custom config file
custom_settings = Settings.from_file("path/to/config.json")

# Use in PDFProcessor
from pdfmindforge import PDFProcessor

processor = PDFProcessor(
    chunk_size=custom_settings.pdf.chunk_size,
    batch_multiplier=custom_settings.pdf.batch_multiplier,
    langs=custom_settings.pdf.langs
)
```


### 3. Creating and saving custom settings:

``` python
from pdfmindforge.config import Settings, GPUSettings

# Create new settings
settings = Settings()

# Customize GPU settings
settings.gpu = GPUSettings(
    use_gpu=True,
    memory_limit=8192,
    optimize_for_speed=True
)

# Save to file
settings.save_to_file("my_config.json")
```


Example config.json:

```json
{
    "pdf": {
        "chunk_size": 100,
        "batch_multiplier": 2,
        "langs": "English",
        "min_pages_for_split": 200,
        "clear_cuda_cache": true
    },
    "gpu": {
        "use_gpu": true,
        "memory_limit": 4096,
        "optimize_for_speed": true
    },
    "processing": {
        "output_format": "markdown",
        "create_zip": true,
        "recursive_search": true,
        "preserve_images": true
    }
}
```