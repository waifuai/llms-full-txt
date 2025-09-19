"""
Utility Functions and Constants

This module provides common utility functions and constants used throughout the LLMs-Full.txt
Generator project. It includes file handling utilities, configuration management, and shared
constants for file type detection.

Key Components:
- safe_read(): Robust file reading with encoding fallback
- load_config(): YAML configuration file loading with error handling
- CODE_EXTENSIONS: Comprehensive tuple of supported file extensions for code analysis
- Logging configuration for consistent error reporting and debugging

Usage:
    from utils import safe_read, CODE_EXTENSIONS, load_config

The module automatically loads configuration from config.yaml on import and sets up logging
for consistent error reporting across the project.
"""

import os
import logging
import yaml

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load configuration
def load_config(config_path='config.yaml'):
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logging.warning(f"Config file {config_path} not found, using defaults")
        return {}
    except Exception as e:
        logging.error(f"Error loading config: {e}")
        return {}

config = load_config()

# Common file extensions for code and text files.
CODE_EXTENSIONS = (
    '.py', '.txt', '.java', '.c', '.cpp', '.h', '.hpp', '.js', '.jsx', '.ts', '.tsx',
    '.html', '.htm', '.css', '.scss', '.less', '.sh', '.bash', '.go', '.rb', '.php',
    '.sql', '.xml', '.json', '.yaml', '.yml', '.ini', '.toml', '.md', '.markdown',
    '.swift', '.kt', '.dart', '.scala', '.groovy', '.perl', '.lua', '.r', '.m',
    '.asm', '.s', '.f', '.for', '.f90', '.f95', '.f03', '.pas', '.ada', '.v',
    '.vhdl', '.csproj', '.sln', '.vb', '.vbs', '.pl', '.tcl', '.coffee', '.hs', '.erl',
    '.rs', '.jl', '.clj', '.lisp', '.scm', '.edn', '.mat', '.m', '.cmake', '.gradle',
    '.dockerfile', '.gitignore', '.env', '.config', '.tf', '.tfvars', '.proto',
    '.ps1', '.bat',
)

def safe_read(filepath):
    """
    Safely read the content of a file by trying UTF-8 and falling back to Latin-1 encoding.

    Args:
        filepath (str): The path to the file.

    Returns:
        str or None: The file content if successful; otherwise, None.
    """
    for encoding in ('utf-8', 'latin-1'):
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"Error reading file {filepath}: {e}")
            return None
    print(f"Skipping file due to encoding issues: {filepath}")
    return None