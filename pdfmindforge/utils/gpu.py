"""
GPU-related utilities for PDFMindforge.
"""

import torch

class GPUManager:
    """Manages GPU resources and CUDA operations."""
    
    @staticmethod
    def is_cuda_available() -> bool:
        """Check if CUDA is available."""
        return torch.cuda.is_available()
    
    @staticmethod
    def clear_cuda_cache():
        """Clear CUDA cache if GPU is available."""
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    
    @staticmethod
    def get_device() -> str:
        """Get the current device (cuda or cpu)."""
        return "cuda" if torch.cuda.is_available() else "cpu"
    
    @staticmethod
    def get_gpu_memory_info() -> dict:
        """Get GPU memory usage information."""
        if not torch.cuda.is_available():
            return {"error": "CUDA not available"}
            
        device = torch.cuda.current_device()
        return {
            "total": torch.cuda.get_device_properties(device).total_memory,
            "allocated": torch.cuda.memory_allocated(device),
            "cached": torch.cuda.memory_reserved(device)
        }