# Contributing to PDFMindforge 🤝

First off, thank you for considering contributing to PDFMindforge! It's people like you that make PDFMindforge such a great tool. 🌟

## Getting Started 🚀

### Fork the Repository

1. Fork the repository on GitHub
2. Clone your fork locally:
```bash
git clone git@github.com:soloeinsteinmit/pdfmindforge.git
cd pdfmindforge
```

3. Create a branch for your work:
```bash
git checkout -b feature/amazing-feature
```

### Set Up Development Environment

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

## Development Process 💻

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add type hints where possible
- Include docstrings for functions and classes

### Commit Messages

Structure your commit messages like this:
```
feat: add batch processing capability

- Added new BatchProcessor class
- Implemented progress tracking
- Added tests for batch processing
```

Common prefixes:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding/modifying tests
- `chore`: Maintenance tasks

### Testing

Please add tests for any new functionality. Run tests locally before submitting:

```bash
pytest tests/
```

## Submitting Changes 📮

1. Push to your fork
2. Submit a Pull Request (PR)
3. In your PR description, please include:
   - What changes you've made
   - Why you've made them
   - Any notes on testing
   - Screenshots (if relevant)

## Bug Reports 🐛

When filing a bug report, please include:

- Your Python version
- PDFMindforge version
- Minimal code to reproduce the issue
- Expected vs actual behavior
- Any error messages

## Feature Requests 💡

I love hearing new ideas! When suggesting features, please:

- Explain the problem you're trying to solve
- Describe how you envision it working
- Note if you're willing to help implement it

## Questions and Discussion 💭

- For quick questions, create an issue with the "question" label
- For longer discussions about direction or design, create an issue with the "discussion" label

## License 📄

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing! 🙏
