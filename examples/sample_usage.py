"""
PDFMindforge Usage Examples

This script demonstrates various ways to use the PDFMindforge package
for processing PDF documents into machine-learning friendly formats.
"""

from pdfmindforge import PDFProcessor

def single_pdf_example():
    """Example of processing a single PDF file"""
    # Initialize the processor with custom settings
    processor = PDFProcessor(
        chunk_size=100,
        batch_multiplier=2,
        langs="English",
        min_pages_for_split=1000  # Only split PDFs with more than 1000 pages
    )

    # Process a single PDF file
    input_pdf = "path/to/your/document.pdf"
    output_dir = "path/to/output/directory"
    
    # Convert PDF to markdown
    processor.process_pdf_to_md(input_pdf, output_dir, create_zip=False)

def batch_processing_example():
    """Example of processing multiple PDF files in a directory"""
    # Initialize the processor
    processor = PDFProcessor(
        chunk_size=100,
        batch_multiplier=2,
        langs="English"
    )

    # Process an entire directory and automatically create ZIP
    input_dir = "path/to/input/directory"
    output_dir = "path/to/output/directory"
    
    zip_path = processor.batch_process_directory(
        input_dir,
        output_dir,
        create_zip=True
    )
    print(f"Processed files have been saved to: {zip_path}")

if __name__ == "__main__":
    print("Running single PDF processing example...")
    single_pdf_example()
    
    print("\nRunning batch processing example...")
    batch_processing_example()