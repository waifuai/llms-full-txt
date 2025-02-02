import os
import shutil
import tempfile
import unittest

# Add the src directory to the Python path so we can import modules.
import sys
SRC_DIR = os.path.join(os.path.dirname(__file__), "..", "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from count_chars_of_code import count_characters
from count_lines_of_code import count_lines_of_code
from generate_llms import generate_llms_full
from generate_toc import generate_toc
from utils import safe_read, CODE_EXTENSIONS

class TestCountFunctions(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for test files.
        self.test_dir = tempfile.mkdtemp()
        
        # Create a test Python file.
        self.test_file_path = os.path.join(self.test_dir, "test.py")
        self.test_content = "print('hello world')\nprint('test')\n"
        with open(self.test_file_path, "w", encoding="utf-8") as f:
            f.write(self.test_content)

    def tearDown(self):
        # Remove the temporary directory after tests.
        shutil.rmtree(self.test_dir)

    def test_count_characters(self):
        # Test the count_characters function.
        result = count_characters(self.test_dir)
        self.assertIsNotNone(result)
        total_chars, file_counts = result
        expected_chars = len(self.test_content)
        self.assertEqual(total_chars, expected_chars)
        self.assertIn(self.test_file_path, file_counts)
        self.assertEqual(file_counts[self.test_file_path], expected_chars)

    def test_count_lines_of_code(self):
        # Test the count_lines_of_code function.
        result = count_lines_of_code(self.test_dir)
        self.assertIsNotNone(result)
        total_lines, file_counts = result
        expected_lines = len(self.test_content.splitlines())
        self.assertEqual(total_lines, expected_lines)
        self.assertIn(self.test_file_path, file_counts)
        self.assertEqual(file_counts[self.test_file_path], expected_lines)

class TestGenerateLLMSFull(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to simulate a project structure.
        self.test_dir = tempfile.mkdtemp()

        # Create a Markdown file with a title and a summary.
        self.md_filename = os.path.join(self.test_dir, "doc.md")
        self.md_content = "# Test Documentation\n> This is a summary.\n\nDetailed content here."
        with open(self.md_filename, "w", encoding="utf-8") as f:
            f.write(self.md_content)

        # Create a code/text file.
        self.code_filename = os.path.join(self.test_dir, "example.py")
        self.code_content = "print('example code')"
        with open(self.code_filename, "w", encoding="utf-8") as f:
            f.write(self.code_content)

        # Output file for llms-full.txt will be created in the temporary directory.
        self.output_file = os.path.join(self.test_dir, "llms-full.txt")

    def tearDown(self):
        # Clean up the temporary directory.
        shutil.rmtree(self.test_dir)

    def test_generate_llms_full(self):
        # Run the generate_llms_full function.
        generate_llms_full(self.test_dir, output_file=self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

        # Read the output file and perform basic checks.
        with open(self.output_file, "r", encoding="utf-8") as f:
            output_content = f.read()

        # Check that the Markdown documentation section was added.
        self.assertIn("# Project Documentation (Markdown Files)", output_content)
        self.assertIn("## Test Documentation", output_content)
        self.assertIn("> This is a summary.", output_content)
        self.assertIn("Detailed content here.", output_content)

        # Check that the code file section was added.
        self.assertIn("# Code and Other Files", output_content)
        self.assertIn("## example.py", output_content)
        self.assertIn("print('example code')", output_content)

class TestGenerateTOC(unittest.TestCase):
    def test_generate_toc(self):
        # Create a sample markdown string with various heading levels.
        markdown_text = (
            "# Title\n"
            "Some introduction text.\n"
            "## Section One\n"
            "Content of section one.\n"
            "### Subsection A\n"
            "Content of subsection A.\n"
            "## Section Two\n"
            "Content of section two.\n"
        )
        toc = generate_toc(markdown_text)
        # The TOC should have entries corresponding to each heading.
        self.assertIn("* [Title](#title)", toc)
        self.assertIn("  * [Section One](#section-one)", toc)
        self.assertIn("    * [Subsection A](#subsection-a)", toc)
        self.assertIn("  * [Section Two](#section-two)", toc)

class TestSafeRead(unittest.TestCase):
    def setUp(self):
        # Create a temporary file to test safe_read.
        self.test_dir = tempfile.mkdtemp()
        self.file_path = os.path.join(self.test_dir, "test.txt")
        self.content = "Sample content for safe read."
        with open(self.file_path, "w", encoding="utf-8") as f:
            f.write(self.content)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_safe_read_success(self):
        # Verify safe_read correctly returns the content.
        result = safe_read(self.file_path)
        self.assertEqual(result, self.content)

    def test_safe_read_nonexistent(self):
        # Verify safe_read returns None for a non-existent file.
        non_existent = os.path.join(self.test_dir, "nofile.txt")
        result = safe_read(non_existent)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
