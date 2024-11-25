"""
Configuration module for PDFMindforge.
"""

from .setting import Settings, PDFSettings, GPUSettings, ProcessingSettings

# Create default settings instance
settings = Settings()

__all__ = ['settings', 'Settings', 'PDFSettings', 'GPUSettings', 'ProcessingSettings']