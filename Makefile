.PHONY: help install test lint format type-check build clean publish-test publish

help:
	@echo "Available commands:"
	@echo "  install      Install package in development mode"
	@echo "  test         Run tests"
	@echo "  lint         Run linting checks"
	@echo "  format       Format code with Black"
	@echo "  type-check   Run type checking with mypy"
	@echo "  build        Build package"
	@echo "  clean        Clean build artifacts"
	@echo "  publish-test Publish to Test PyPI"
	@echo "  publish      Publish to PyPI"

install:
	pip install -e ".[dev]"

test:
	pytest tests/ --cov=pdf_page_counter --cov-report=html

lint:
	flake8 src tests

format:
	black src tests

type-check:
	mypy src

build:
	python -m build

clean:
	rm -rf build/ dist/ src/*.egg-info/

publish-test:
	twine upload --repository testpypi dist/*

publish:
	twine upload dist/*
