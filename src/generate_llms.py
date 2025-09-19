import os
import re
import argparse
from utils import safe_read

def generate_llms_full(directory, output_file="llms-full.txt"):
    """
    Generates a llms-full.txt file from a directory structure, including Markdown files and other text files.

    Args:
        directory (str): The root directory to process.
        output_file (str): The output file name (default: "llms-full.txt").
    """
    markdown_files = []
    other_text_files = []

    # Categorize files
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if filename.endswith(".md"):
                markdown_files.append(filepath)
            elif filename.endswith((".txt", ".py", ".js", ".html", ".sh", ".rs", ".toml")):
                other_text_files.append(filepath)

    # Sort files for consistent output
    markdown_files.sort()
    other_text_files.sort()

    with open(output_file, "w", encoding="utf-8") as outfile:
        # Process Markdown Files
        outfile.write("# Project Documentation (Markdown Files)\n")
        outfile.write("> Comprehensive documentation of the project in Markdown format.\n\n")
        for filepath in markdown_files:
            content = safe_read(filepath)
            if content is None:
                continue

            # Extract title or derive from filename
            title_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else os.path.basename(filepath).replace(".md", "").replace("_", " ").title()
            outfile.write(f"## {title}\n")

            # Extract summary if available
            summary_match = re.search(r"^>\s+(.+)", content, re.MULTILINE)
            if summary_match:
                summary = summary_match.group(1).strip()
                outfile.write(f"> {summary}\n\n")
            else:
                outfile.write(f"> Content from: {filepath}\n\n")

            # Remove title and summary if already written
            content_to_write = content
            if title_match:
                content_to_write = content_to_write.replace(title_match.group(0), "", 1)
            if summary_match:
                content_to_write = content_to_write.replace(summary_match.group(0), "", 1)
            outfile.write(content_to_write.strip() + "\n\n")

        # Process Other Text Files
        outfile.write("# Code and Other Files\n")
        outfile.write("> Code snippets, scripts, and other relevant text files.\n\n")
        for filepath in other_text_files:
            content = safe_read(filepath)
            if content is None:
                continue

            title = os.path.basename(filepath)
            outfile.write(f"## {title}\n")
            outfile.write(f"> File: {filepath}\n\n")
            outfile.write("```\n")
            outfile.write(content.strip() + "\n")
            outfile.write("```\n\n")

    print(f"Successfully generated {output_file} from {directory}")

def main():
    root_directory = input("Enter the root directory to process: ")
    generate_llms_full(root_directory)

if __name__ == "__main__":
    main()