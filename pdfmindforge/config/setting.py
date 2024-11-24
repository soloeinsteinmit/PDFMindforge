"""
Configuration settings for PDFMindforge.
"""

from dataclasses import dataclass
from typing import Optional
import os
import json

@dataclass
class PDFSettings:
    """Settings for PDF processing."""
    chunk_size: int = 100
    batch_multiplier: int = 2
    langs: str = "English"
    min_pages_for_split: int = 200
    clear_cuda_cache: bool = True

@dataclass
class GPUSettings:
    """Settings for GPU operations."""
    use_gpu: bool = True
    memory_limit: Optional[int] = None
    optimize_for_speed: bool = True

@dataclass
class ProcessingSettings:
    """Settings for document processing."""
    output_format: str = "markdown"
    create_zip: bool = True
    recursive_search: bool = True
    preserve_images: bool = True

class Settings:
    """Global settings manager for PDFMindforge."""
    
    def __init__(self):
        self.pdf = PDFSettings()
        self.gpu = GPUSettings()
        self.processing = ProcessingSettings()
        
        # Load custom settings if available
        self.load_from_file()
    
    def load_from_file(self, config_path: str = None) -> None:
        """
        Load settings from a JSON configuration file.
        
        Args:
            config_path: Path to config file. If None, checks default locations.
        """
        if config_path is None:
            config_path = self._get_default_config_path()
        
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
                
                # Update PDF settings
                if 'pdf' in config:
                    for key, value in config['pdf'].items():
                        setattr(self.pdf, key, value)
                
                # Update GPU settings
                if 'gpu' in config:
                    for key, value in config['gpu'].items():
                        setattr(self.gpu, key, value)
                
                # Update processing settings
                if 'processing' in config:
                    for key, value in config['processing'].items():
                        setattr(self.processing, key, value)
    
    def save_to_file(self, config_path: str = None) -> None:
        """
        Save current settings to a JSON configuration file.
        
        Args:
            config_path: Path to save config file. If None, uses default location.
        """
        if config_path is None:
            config_path = self._get_default_config_path()
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
        
        config = {
            'pdf': {
                'chunk_size': self.pdf.chunk_size,
                'batch_multiplier': self.pdf.batch_multiplier,
                'langs': self.pdf.langs,
                'min_pages_for_split': self.pdf.min_pages_for_split,
                'clear_cuda_cache': self.pdf.clear_cuda_cache
            },
            'gpu': {
                'use_gpu': self.gpu.use_gpu,
                'memory_limit': self.gpu.memory_limit,
                'optimize_for_speed': self.gpu.optimize_for_speed
            },
            'processing': {
                'output_format': self.processing.output_format,
                'create_zip': self.processing.create_zip,
                'recursive_search': self.processing.recursive_search,
                'preserve_images': self.processing.preserve_images
            }
        }
        
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=4)
    
    def _get_default_config_path(self) -> str:
        """Get the default configuration file path."""
        return os.path.join(
            os.path.expanduser("~"),
            ".pdfmindforge",
            "config.json"
        )
    
    @classmethod
    def from_file(cls, config_path: str) -> 'Settings':
        """
        Create Settings instance from a configuration file.
        
        Args:
            config_path: Path to the configuration file
            
        Returns:
            Settings instance with loaded configuration
        """
        settings = cls()
        settings.load_from_file(config_path)
        return settings