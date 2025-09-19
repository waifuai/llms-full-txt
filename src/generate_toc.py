"""
Table of Contents Generator

This script generates a table of contents (TOC) from Markdown text by parsing headers and creating
anchor links. It supports multiple header levels and produces a clean, navigable TOC in Markdown format.

Key Features:
- Parses Markdown headers (# ## ###) of all levels
- Generates anchor links from header text automatically
- Handles special characters by escaping and URL-encoding
- Creates hierarchical indentation for nested sections
- Produces clean, readable Markdown output

Usage:
    python -m src.generate_toc [markdown_file]

Output:
    Creates a toc.md file with the generated table of contents

Example:
    python -m src.generate_toc README.md
"""

import re
import html
import argparse

def generate_toc(markdown_text):
    """
    Generates a table of contents (TOC) from Markdown text.

    Args:
        markdown_text (str): The Markdown content.

    Returns:
        str: The generated TOC in Markdown format.
    """
    toc = []
    lines = markdown_text.split('\n')
    for line in lines:
        if line.startswith('#'):
            level = line.count('#')
            title = line.strip('# ').strip()
            # Escape special characters and generate an anchor link
            title = html.escape(title)
            anchor = re.sub(r"[^\w\s-]", "", title).lower()
            anchor = re.sub(r"\s+", "-", anchor)
            anchor = re.sub(r"-+", "-", anchor)
            indent = '  ' * (level - 1)
            toc.append(f"{indent}* [{title}](#{anchor})")
    return "\n".join(toc)

def main():
    input_file = input("Enter the path to the Markdown file: ")
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            markdown_text = f.read()
    except Exception as e:
        print(f"Error reading file {input_file}: {e}")
        return

    toc = generate_toc(markdown_text)
    output_file = "toc.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(toc)
    print(f"Table of contents written to {output_file}")

if __name__ == "__main__":
    main()