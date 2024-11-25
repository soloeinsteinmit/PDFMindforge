"""
Sample usage examples for PDFMindforge.
"""

from pdfmindforge import PDFProcessor

def basic_usage():
    """Basic usage example."""
    # Initialize processor with default settings
    processor = PDFProcessor()
    
    # Process a single PDF
    processor.process_pdf_to_md(
        input_path="sample.pdf",
        output_path="output"
    )

def gpu_optimized():
    """Example with GPU optimization."""
    # Initialize with GPU-optimized settings
    processor = PDFProcessor(
        batch_multiplier=2,      # Use more VRAM for speed
        workers=4,               # Process 4 files in parallel
        clear_cuda_cache=True    # Manage GPU memory
    )
    
    # Process directory of PDFs using batch mode
    processor.batch_process_directory(
        input_dir="pdfs",
        output_dir="output",
        use_marker_batch=True,   # Enable fast batch processing
        create_zip=True          # Create ZIP of outputs
    )

def advanced_usage():
    """Advanced usage with custom settings."""
    # Initialize with advanced settings
    processor = PDFProcessor(
        # Performance settings
        chunk_size=150,          # Larger chunks for faster processing
        batch_multiplier=3,      # More VRAM usage (needs ~9GB)
        workers=6,               # Process 6 files in parallel
        
        # Processing settings
        langs="English,French",  # Multi-language support
        min_length=1000,        # Skip PDFs with little text
        min_pages_for_split=300 # Split very large PDFs
    )
    
    # Process with advanced options
    processor.batch_process_directory(
        input_dir="documents",
        output_dir="processed",
        recursive=True,          # Include subdirectories
        max_files=100,          # Limit number of files
        use_marker_batch=True    # Use fast batch mode
    )

def large_document():
    """Example for processing large documents."""
    # Initialize with settings for large documents
    processor = PDFProcessor(
        chunk_size=50,           # Smaller chunks for memory efficiency
        batch_multiplier=1,      # Conservative VRAM usage
        min_pages_for_split=100  # Split into smaller parts
    )
    
    # Process large PDF with splitting
    processor.process_pdf_to_md(
        input_path="large_document.pdf",
        output_path="large_output",
        split_if_large=True      # Enable automatic splitting
    )

if __name__ == "__main__":
    # Run examples
    print("Running basic usage example...")
    basic_usage()
    
    print("\nRunning GPU-optimized example...")
    gpu_optimized()
    
    print("\nRunning advanced usage example...")
    advanced_usage()
    
    print("\nProcessing large document...")
    large_document()