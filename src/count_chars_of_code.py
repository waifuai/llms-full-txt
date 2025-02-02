import os
from utils import CODE_EXTENSIONS, safe_read

def count_characters(directory):
    """
    Counts the characters in all text-based files within a directory (and its subdirectories).

    Args:
        directory (str): The path to the directory to analyze.

    Returns:
        tuple: (total_chars, file_counts)
    """
    directory = os.path.abspath(directory)
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        return None

    total_chars = 0
    file_counts = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(CODE_EXTENSIONS):
                filepath = os.path.join(root, file)
                content = safe_read(filepath)
                if content is not None:
                    char_count = len(content)
                    total_chars += char_count
                    file_counts[filepath] = char_count

    return total_chars, file_counts

def main():
    target_directory = input("Enter the directory path: ")
    result = count_characters(target_directory)
    if result:
        total_chars, _ = result
        print(f"\n--- Character Counts for '{target_directory}' ---")
        print(f"Total Characters: {total_chars}")

if __name__ == "__main__":
    main()