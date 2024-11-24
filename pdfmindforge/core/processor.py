"""
Main processor class for PDFMindforge.
"""

import os
import subprocess
from typing import List, Optional

from ..utils.gpu import GPUManager
from ..utils.io import FileManager
from .splitter import PDFSplitter

class PDFProcessor:
    """
    A comprehensive class for processing PDF files and converting them to markdown format.
    
    This class handles:
    - PDF splitting for large documents
    - Single and batch PDF processing
    - Conversion to markdown using marker_single
    - ZIP file creation for processed files
    - CUDA memory management for GPU resources
    """
    
    def __init__(
        self,
        chunk_size: int = 100,
        batch_multiplier: int = 2,
        langs: str = "English",
        clear_cuda_cache: bool = True,
        min_pages_for_split: int = 200
    ):
        """
        Initialize the PDF processor with specified parameters.
        
        Args:
            chunk_size: Number of pages per chunk when splitting large PDFs
            batch_multiplier: Multiplier for batch processing
            langs: Language specification for processing
            clear_cuda_cache: Whether to clear CUDA cache on initialization
            min_pages_for_split: Minimum number of pages before splitting a PDF
        """
        self.batch_multiplier = batch_multiplier
        self.langs = langs
        
        # Initialize components
        self.splitter = PDFSplitter(chunk_size, min_pages_for_split)
        self.gpu_manager = GPUManager()
        self.file_manager = FileManager()
        
        if clear_cuda_cache:
            self.gpu_manager.clear_cuda_cache()
    
    def process_pdf_to_md(
        self,
        input_path: str,
        output_path: str,
        split_if_large: bool = True,
        create_zip: bool = True
    ) -> str:
        """
        Process a single PDF file to markdown format.
        
        Args:
            input_path: Path to input PDF file
            output_path: Path for output markdown files
            split_if_large: Whether to split large PDFs into chunks
            create_zip: Whether to create a ZIP of output files
        
        Returns:
            Path to the output directory containing markdown files
        """
        self.file_manager.create_directory(output_path)
        
        if split_if_large:
            split_folder = f"{output_path}_split"
            split_files = self.splitter.split_pdf(input_path, split_folder)
            
            for split_file in split_files:
                output_name = os.path.join(
                    output_path,
                    os.path.basename(split_file).replace(".pdf", "")
                )
                self._run_marker_single(split_file, output_name)
        else:
            self._run_marker_single(input_path, output_path)
        
        if create_zip:
            zip_path = self.file_manager.create_zip([output_path], output_path)
            return zip_path
        else:
            return output_path
    
    def _run_marker_single(self, pdf_path: str, output_path: str) -> None:
        """Execute marker_single command for PDF to markdown conversion."""
        command = [
            "marker_single",
            pdf_path,
            output_path,
            "--batch_multiplier",
            str(self.batch_multiplier),
            "--langs",
            self.langs
        ]
        subprocess.run(command, check=True)
    
    def batch_process_directory(
        self,
        input_dir: str,
        output_dir: str,
        create_zip: bool = True
    ) -> Optional[str]:
        """
        Process all PDF files in a directory.
        
        Args:
            input_dir: Input directory containing PDF files
            output_dir: Output directory for markdown files
            create_zip: Whether to create a ZIP of output files
        
        Returns:
            Path to ZIP file if create_zip is True, None otherwise
        """
        self.file_manager.create_directory(output_dir)
        pdf_files = self.file_manager.get_pdf_files(input_dir)
        processed_dirs = []
        
        for pdf_file in pdf_files:
            relative_path = self.file_manager.get_relative_path(pdf_file, input_dir)
            output_path = os.path.join(
                output_dir,
                os.path.splitext(relative_path)[0]
            )
            processed_dir = self.process_pdf_to_md(pdf_file, output_path)
            processed_dirs.append(processed_dir)
        
        if create_zip:
            return self.file_manager.create_zip(processed_dirs, output_dir)
        return None
    
    def create_zip(self, source_dir: str, output_path: str) -> str:
        """
        Create a ZIP file from a single directory.
        
        Args:
            source_dir: Directory containing files to zip
            output_path: Path for output ZIP file
        
        Returns:
            Path to the created ZIP file
        """
        return self.file_manager.create_zip([source_dir], os.path.splitext(output_path)[0])