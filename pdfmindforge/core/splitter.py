"""
PDF splitting functionality for handling large PDF documents.
"""

import os
from typing import List
from PyPDF2 import PdfReader, PdfWriter

class PDFSplitter:
    """Handles splitting of large PDF documents into smaller chunks."""
    
    def __init__(self, chunk_size: int = 100, min_pages_for_split: int = 200):
        """
        Initialize the PDF splitter.
        
        Args:
            chunk_size: Number of pages per chunk when splitting large PDFs
            min_pages_for_split: Minimum number of pages before splitting a PDF
        """
        self.chunk_size = chunk_size
        self.min_pages_for_split = min_pages_for_split
    
    def split_pdf(self, file_path: str, output_folder: str) -> List[str]:
        """
        Split a large PDF file into smaller chunks.
        
        Args:
            file_path: Path to the input PDF file
            output_folder: Directory to store split PDF files
        
        Returns:
            List of paths to split PDF files
        """
        
        os.makedirs(output_folder, exist_ok=True)
        split_files = []
        
        pdf = PdfReader(file_path)
        num_pages = len(pdf.pages)
        
        # Only split if pages exceed minimum threshold
        if num_pages <= self.min_pages_for_split:
            return [file_path]
            
        num_parts = (num_pages + self.chunk_size - 1) // self.chunk_size
        print(f"Splitting {file_path} into {num_parts} parts...")
        
        for part in range(num_parts):
            pdf_writer = PdfWriter()
            start_page = part * self.chunk_size
            end_page = min(start_page + self.chunk_size, num_pages)
            
            for page in range(start_page, end_page):
                pdf_writer.add_page(pdf.pages[page])
                
            output_filename = os.path.join(output_folder, f'part_{part + 1}.pdf')
            with open(output_filename, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
            split_files.append(output_filename)
            
        return split_files