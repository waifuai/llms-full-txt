# LLMs-Full.txt Generator and Utilities

This repository provides a set of Python scripts to generate and work with `llms-full.txt` files—a proposed standard for making website and project documentation more accessible to Large Language Models (LLMs).

## Overview

**llms-full.txt** is a Markdown file that aggregates complete documentation (including code examples) into one file for easy ingestion by LLMs. It complements traditional standards like `sitemap.xml` and `robots.txt` by focusing on content accessibility for AI models.

### Key Features
- **Comprehensive Content:** Combines full documentation and code.
- **AI-Friendly Format:** Uses Markdown to keep the content simple and structured.
- **Efficient Processing:** Consolidates all relevant content to help overcome LLM context limitations.

## Repository Structure

- **README.md:** Project overview and usage instructions.
- **src/**
  - **utils.py:** Shared utility functions and constants.
  - **generate_llms.py:** Generates `llms-full.txt` from a given directory.
  - **generate_toc.py:** Creates a Markdown Table of Contents from a Markdown file.
  - **count_lines_of_code.py:** Counts lines of code in a directory.
  - **count_chars_of_code.py:** Counts characters in code files.

## Installation

1. Install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. (Optional) Create a virtual environment and install project in development mode:
```bash
python -m uv venv .venv
.venv/Scripts/python.exe -m pip install -e .
```

## Configuration

Create a `config.yaml` file in the project root to customize file extensions and settings:

```yaml
file_extensions:
  - '.py'
  - '.js'
  # Add or remove extensions as needed

exclude_patterns:
  - '*.log'
  - '__pycache__'

output:
  default_llms_file: 'llms-full.txt'
```

## Usage Examples

### Generate `llms-full.txt`
```bash
python src/generate_llms.py /path/to/directory
python src/generate_llms.py /path/to/directory -o custom-output.txt
```

### Generate a Table of Contents
```bash
python src/generate_toc.py input.md
python src/generate_toc.py input.md -o custom-toc.md
```

### Count Lines of Code
```bash
python src/count_lines_of_code.py /path/to/directory
```

### Count Characters in Code
```bash
python src/count_chars_of_code.py /path/to/directory
```

All commands now support command-line arguments and show progress indicators for large directories.

## License

This repository is licensed under the MIT-0 License.