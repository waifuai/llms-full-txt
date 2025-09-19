import os
import argparse
from tqdm import tqdm
from utils import CODE_EXTENSIONS, safe_read

def count_lines_of_code(directory):
    """
    Counts the lines of code in all text-based files within a directory (and its subdirectories).

    Args:
        directory (str): The path to the directory to analyze.

    Returns:
        tuple: (total_lines, file_counts)
    """
    directory = os.path.abspath(directory)
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        return None

    total_lines = 0
    file_counts = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(CODE_EXTENSIONS):
                filepath = os.path.join(root, file)
                content = safe_read(filepath)
                if content is not None:
                    lines = content.splitlines()
                    line_count = len(lines)
                    total_lines += line_count
                    file_counts[filepath] = line_count

    return total_lines, file_counts

def main():
    target_directory = input("Enter the directory path: ")
    result = count_lines_of_code(target_directory)
    if result:
        total_lines, _ = result
        print(f"\n--- Line Counts for '{target_directory}' ---")
        print(f"Total Lines of Code: {total_lines}")

if __name__ == "__main__":
    main()