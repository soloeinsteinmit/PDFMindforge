"""
Input/Output utilities for PDFMindforge.
"""

import os
import glob
import zipfile
from typing import List, Optional
from PyPDF2 import PdfReader

class FileManager:
    """Handles file operations for PDFMindforge."""
    
    @staticmethod
    def create_directory(directory: str) -> None:
        """Create directory if it doesn't exist."""
        os.makedirs(directory, exist_ok=True)
    
    
    @staticmethod
    def get_pdf_files(
            directory: str, 
            recursive: bool = True, 
            max_files: Optional[int] = None,
            min_length: Optional[int] = None
        ) -> List[str]:
        """
        Get all PDF files in a directory.
        
        Args:
            directory: Directory to search for PDF files
            recursive: Whether to search recursively in subdirectories
            max_files: Maximum number of files to return
            min_length: Minimum number of characters required in PDF
        
        Returns:
            List of paths to PDF files meeting the criteria
        """
        pattern = os.path.join(directory, "**/*.pdf" if recursive else "*.pdf")
        pdf_files = glob.glob(pattern, recursive=recursive)
        
        if min_length is not None:
            filtered_files = []
            for pdf_file in pdf_files:
                try:
                    with open(pdf_file, 'rb') as f:
                        pdf = PdfReader(f)
                        text_length = sum(len(page.extract_text()) for page in pdf.pages)
                        if text_length >= min_length:
                            filtered_files.append(pdf_file)
                except Exception:
                    continue  # Skip files that can't be read
            pdf_files = filtered_files
        
        if max_files is not None:
            pdf_files = pdf_files[:max_files]
        
        return pdf_files
    
    
    @staticmethod
    def create_zip(source_dirs: List[str], output_path: str) -> str:
        """
        Create a ZIP file from multiple directories.
        
        Args:
            source_dirs: List of directories containing files to zip
            output_path: Path for output ZIP file
        
        Returns:
            Path to the created ZIP file
        """
        zip_path = f"{output_path}.zip"
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for source_dir in source_dirs:
                if not os.path.exists(source_dir):
                    continue
                    
                root_dir = os.path.dirname(source_dir)
                
                for root, _, files in os.walk(source_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, root_dir)
                        zipf.write(file_path, arcname)
        
        return zip_path
    
    @staticmethod
    def get_relative_path(file_path: str, base_dir: str) -> str:
        """Get relative path from base directory."""
        return os.path.relpath(file_path, base_dir)
    
    @staticmethod
    def get_pdf_info(pdf_path: str) -> dict:
        """
        Get information about a PDF file.
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            Dictionary containing PDF information
        """
        try:
            with open(pdf_path, 'rb') as f:
                pdf = PdfReader(f)
                return {
                    'num_pages': len(pdf.pages),
                    'text_length': sum(len(page.extract_text()) for page in pdf.pages)
                }
        except Exception as e:
            return {'error': str(e)}