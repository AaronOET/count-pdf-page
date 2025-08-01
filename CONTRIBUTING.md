# Contributing to PDF Page Counter

Thank you for your interest in contributing to PDF Page Counter! This document provides guidelines for contributing to the project.

## Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AaronOET/count-pdf-page.git
   cd count-pdf-page
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install development dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

## Development Workflow

### Running Tests

Run the test suite:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=pdf_page_counter --cov-report=html
```

### Code Formatting

Format code with Black:
```bash
black src tests
```

Check formatting:
```bash
black --check src tests
```

### Linting

Run flake8:
```bash
flake8 src tests
```

### Type Checking

Run mypy:
```bash
mypy src
```

### Building the Package

Build the package:
```bash
python -m build
```

## Code Style

- Follow PEP 8 style guidelines
- Use Black for code formatting (line length: 88)
- Add type hints for all functions
- Write docstrings for all public functions and classes
- Keep functions focused and small

## Testing

- Write tests for all new functionality
- Maintain or improve test coverage
- Use descriptive test names
- Mock external dependencies appropriately

## Submitting Changes

1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Add tests for new functionality**
5. **Run the test suite and ensure all tests pass**
6. **Format your code with Black**
7. **Run linting and type checking**
8. **Commit your changes:**
   ```bash
   git commit -m "Add: description of your changes"
   ```
9. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```
10. **Create a Pull Request**

## Commit Message Guidelines

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

## Release Process

1. Update version number in `src/pdf_page_counter/__init__.py`
2. Update CHANGELOG.md
3. Create a new tag: `git tag v0.1.1`
4. Push the tag: `git push origin v0.1.1`
5. Create a GitHub release

## Questions?

If you have questions about contributing, please open an issue on GitHub.
