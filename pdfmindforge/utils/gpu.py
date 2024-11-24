"""
GPU-related utilities for PDFMindforge.
"""

import torch
from typing import Dict, Optional

class GPUManager:
    """Manages GPU resources and CUDA operations."""
    
    def __init__(self):
        """Initialize GPU manager."""
        self._vram_per_worker = 5  # GB peak VRAM usage per worker
        self._vram_avg_per_worker = 3.5  # GB average VRAM usage per worker
    
    
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
        total = torch.cuda.get_device_properties(device).total_memory / (1024**3)  # Convert to GB
        allocated = torch.cuda.memory_allocated(device) / (1024**3)
        cached = torch.cuda.memory_reserved(device) / (1024**3)
            
        return {
            "total": total,
            "allocated": allocated,
            "cached": cached,
            "available": total - allocated
        }
        
        
    def get_max_workers(self, safety_margin: float = 0.9) -> int:
        """
        Calculate maximum number of workers based on available VRAM.
        
        Args:
            safety_margin: Fraction of total VRAM to consider available (0.0 to 1.0)
        
        Returns:
            Maximum number of workers that can safely run in parallel
        """
        if not torch.cuda.is_available():
            return 1
            
        memory_info = self.get_gpu_memory_info()
        if "error" in memory_info:
            return 1
            
        available_vram = memory_info["total"] * safety_margin
        return max(1, int(available_vram / self._vram_per_worker))
    
    
    def estimate_vram_usage(self, num_workers: int) -> Dict[str, float]:
        """
        Estimate VRAM usage for a given number of workers.
        
        Args:
            num_workers: Number of parallel workers
            
        Returns:
            Dictionary with peak and average VRAM usage estimates in GB
        """
        return {
            "peak_vram": num_workers * self._vram_per_worker,
            "avg_vram": num_workers * self._vram_avg_per_worker
        }