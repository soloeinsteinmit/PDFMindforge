from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pdfmindforge",
    version="0.1.0",
    author="Solomon Eshun",
    author_email="solomoneshun373@gmail.com",
    description="Transform PDF documents into machine-learning friendly formats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soloeinsteinmit/PDFMindforge",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.4.1",
        "transformers>=4.46.1",
        "accelerate>=0.24.1",
        "huggingface_hub>=0.19.4",
        "safetensors",
        "tokenizers",
        "Pillow",
        "numpy",
        "tqdm",
        "marker-pdf",
        "PyPDF2",
        "zip-files"
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=22.0",
            "isort>=5.0",
            "flake8>=3.9",
        ],
        "cuda": [
            "torch>=2.4.1+cu118",  # CUDA 11.8 version
            "torchvision>=0.15.0+cu118",
            "torchaudio>=2.0.0+cu118"
        ]
    }
)