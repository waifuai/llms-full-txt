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

## Usage Examples

### Generate `llms-full.txt`
```bash
python src/generate_llms.py
```

### Generate a Table of Contents
```bash
python src/generate_toc.py
```

### Count Lines of Code
```bash
python src/count_lines_of_code.py
```

### Count Characters in Code
```bash
python src/count_chars_of_code.py
```

## License

This repository is licensed under the MIT-0 License.