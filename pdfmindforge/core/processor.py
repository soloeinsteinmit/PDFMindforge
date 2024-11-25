"""
Main processor class for PDFMindforge.
"""

import os
import subprocess
import multiprocessing
from typing import List, Optional, Dict

from ..utils.gpu import GPUManager
from ..utils.io import FileManager
from .splitter import PDFSplitter

class PDFProcessor:
    """
    A comprehensive class for processing PDF files and converting them to markdown format.
    
    This class handles:
    - PDF splitting for large documents
    - Single and batch PDF processing with parallel workers
    - Conversion to markdown using marker_single or marker batch
    - ZIP file creation for processed files
    - CUDA memory management for GPU resources
    
    Attributes:
        chunk_size: Number of pages per chunk when splitting large PDFs
        batch_multiplier: Multiplier for batch processing. Higher numbers will take more VRAM, but process faster.
                        Default value of 2 will use ~6GB of VRAM (2x the base 3GB requirement)
        langs: Optional comma-separated list of languages for OCR. Required only if using tesseract
        clear_cuda_cache: Whether to clear CUDA cache on initialization
        min_pages_for_split: Minimum number of pages before splitting a PDF
        max_pages: Maximum number of pages to process. None means process entire document
        start_page: Page number to start processing from. None means start from first page
        workers: Number of PDFs to process in parallel. Each worker uses ~5GB VRAM peak, 3.5GB average
        min_length: Minimum number of characters required in PDF for processing. If you're processing a lot of pdfs, *marker* recommends setting this to avoid OCRing pdfs that are mostly images. (slows everything down)
    """
    
    def __init__(
        self,
        chunk_size: int = 100,
        batch_multiplier: int = 2,
        langs: Optional[str] = "English",
        clear_cuda_cache: bool = True,
        min_pages_for_split: int = 200,
        max_pages: Optional[int] = None,
        start_page: Optional[int] = None,
        workers: Optional[int] = None,
        min_length: Optional[int] = None
    ):
        """Initialize the PDF processor with specified parameters."""
        self.batch_multiplier = batch_multiplier
        self.langs = langs
        self.max_pages = max_pages
        self.start_page = start_page
        self.min_length = min_length
        
        # Initialize components
        self.splitter = PDFSplitter(chunk_size, min_pages_for_split)
        self.gpu_manager = GPUManager()
        self.file_manager = FileManager()
        
        # Set optimal worker count based on GPU/CPU capabilities
        max_gpu_workers = self.gpu_manager.get_max_workers() if self.gpu_manager.is_cuda_available() else 1
        max_cpu_workers = multiprocessing.cpu_count()
        self.workers = min(workers or max_gpu_workers, max_cpu_workers)
        
        if clear_cuda_cache and self.gpu_manager.is_cuda_available():
            self.gpu_manager.clear_cuda_cache()
    
    def _run_marker_single(self, pdf_path: str, output_path: str) -> None:
        """Execute marker_single command for PDF to markdown conversion."""
        # Validate input file
        pdf_info = self.file_manager.get_pdf_info(pdf_path)
        if pdf_info.get("error"):
            raise ValueError(f"Error reading PDF: {pdf_info['error']}")
            
        command = [
            "marker_single",
            pdf_path,
            output_path,
            "--batch_multiplier",
            str(self.batch_multiplier)
        ]
        
        # Add optional parameters
        if self.langs:
            command.extend(["--langs", self.langs])
        if self.max_pages:
            command.extend(["--max_pages", str(self.max_pages)])
        if self.start_page:
            command.extend(["--start_page", str(self.start_page)])
        if self.min_length:
            command.extend(["--min_length", str(self.min_length)])
            
        subprocess.run(command, check=True)
    
    
    def _run_marker_batch(self, input_dir: str, output_dir: str, max_files: Optional[int] = None) -> None:
        """Execute marker command for batch PDF processing."""
        command = [
            "marker",
            input_dir,
            output_dir,
            "--workers",
            str(self.workers)
        ]
        
        # Add optional parameters
        if max_files:
            command.extend(["--max", str(max_files)])
        if self.min_length:
            command.extend(["--min_length", str(self.min_length)])
        if self.langs:
            command.extend(["--langs", self.langs])
            
        subprocess.run(command, check=True)
    
    
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
            create_zip: Whether to create a ZIP of output files. Useful when working on online notebooks and want to save all processed files at once.
            
        Returns:
            Path to output file or ZIP file if create_zip is True
        """
        self.file_manager.create_directory(output_path)
        
        if split_if_large and self.splitter.should_split(input_path):
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
            return self.file_manager.create_zip([output_path], output_path)
        return output_path
    
    def batch_process_directory(
        self,
        input_dir: str,
        output_dir: str,
        recursive: bool = True,
        create_zip: bool = True,
        max_files: Optional[int] = None,
        use_marker_batch: bool = True
    ) -> str:
        """
        Process all PDF files in a directory.
        
        Args:
            input_dir: Directory containing PDF files
            output_dir: Directory for output files
            recursive: Whether to search subdirectories
            create_zip: Whether to create a ZIP of all outputs. Useful when working on online notebooks with large datasets and want to save all processed files at once
            max_files: Maximum number of PDFs to process
            use_marker_batch: Whether to use marker batch processing (faster) or process files individually
            
        Returns:
            Path to output directory or ZIP file if create_zip is True
        """
        self.file_manager.create_directory(output_dir)
        
        if use_marker_batch:
            self._run_marker_batch(input_dir, output_dir, max_files)
            if create_zip:
                return self.file_manager.create_zip([output_dir], output_dir)
            return output_dir
            
        # Individual processing fallback
        pdf_files = self.file_manager.get_pdf_files(
            input_dir,
            recursive=recursive,
            max_files=max_files,
            min_length=self.min_length
        )
        
        if not pdf_files:
            raise ValueError(f"No valid PDF files found in {input_dir}")
        
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
        return output_dir