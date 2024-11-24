"""
Input/Output utilities for PDFMindforge.
"""

import os
import glob
import zipfile
from typing import List, Optional

class FileManager:
    """Handles file operations for PDFMindforge."""
    
    @staticmethod
    def create_directory(directory: str) -> None:
        """Create directory if it doesn't exist."""
        os.makedirs(directory, exist_ok=True)
    
    @staticmethod
    def get_pdf_files(directory: str, recursive: bool = True) -> List[str]:
        """
        Get all PDF files in a directory.
        
        Args:
            directory: Directory to search for PDF files
            recursive: Whether to search recursively in subdirectories
        
        Returns:
            List of paths to PDF files
        """
        pattern = os.path.join(directory, "**/*.pdf" if recursive else "*.pdf")
        return glob.glob(pattern, recursive=recursive)
    
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