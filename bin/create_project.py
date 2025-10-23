#!/usr/bin/env python3
"""
Script to create a standardized project structure for research projects.
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import datetime


def create_project(project_name, base_path=".", dry_run=False):
    """
    Create a standardized project structure for research projects.
    
    Args:
        project_name (str): Name of the project
        base_path (str): Base directory where project will be created
        dry_run (bool): Preview without creating files
    """
    # Define the project root
    project_root = Path(base_path) / project_name
    
    # Error if the target project directory already exists.
    # If the exact path exists and is a directory, refuse to overwrite.
    # If the path exists but is not a directory (e.g. a file with the same name),
    # bail early because subsequent mkdir(parents=True) will raise NotADirectoryError.
    if project_root.exists():
        if project_root.is_dir():
            print(f"Error: Directory '{project_root}' already exists.")
            sys.exit(1)
        else:
            print(f"Error: Path '{project_root}' exists and is not a directory.")
            sys.exit(1)
    
    # Define directory structure
    directories = [
        "metadata",
        "docs",
        "data/raw/sequencing",
        "data/raw/imaging",
        "data/references",
        "data/processed",
        "src/preprocessing",
        "src/training",
        "src/evaluation",
        "src/analysis",
        "src/visualization",
        "src/utils",
        "models/checkpoints",
        "models/final_models",
        "results/figures",
        "results/tables",
        "results/reports",
        "notebooks",
        "configs",
        "environment",
        "temp",
        "archive",
    ]
    
    # If dry-run, print the planned project tree and exit (no file operations)
    if dry_run:
        tree = f"{project_name}/\n"
        tree += "├── README.md\n"
        tree += "├── LICENSE\n"
        tree += "├── metadata/\n"
        tree += "│   ├── project_metadata.txt\n"
        tree += "│   ├── sample_metadata.csv\n"
        tree += "│   └── experiment_metadata.xlsx\n"
        tree += "├── docs/\n"
        tree += "├── data/\n"
        tree += "│   ├── raw/\n"
        tree += "│   │   ├── sequencing/\n"
        tree += "│   │   └── imaging/\n"
        tree += "│   ├── references/\n"
        tree += "│   └── processed/\n"
        tree += "├── src/\n"
        tree += "│   ├── preprocessing/\n"
        tree += "│   ├── training/\n"
        tree += "│   ├── evaluation/\n"
        tree += "│   ├── analysis/\n"
        tree += "│   ├── visualization/\n"
        tree += "│   └── utils/\n"
        tree += "├── models/\n"
        tree += "│   ├── checkpoints/\n"
        tree += "│   └── final_models/\n"
        tree += "├── results/\n"
        tree += "│   ├── figures/\n"
        tree += "│   ├── tables/\n"
        tree += "│   └── reports/\n"
        tree += "├── notebooks/\n"
        tree += "├── configs/\n"
        tree += "├── environment/\n"
        tree += "│   ├── environment.yml\n"
        tree += "│   └── requirements.txt\n"
        tree += "├── temp/\n"
        tree += "└── archive/\n"
        print(tree)
        return

    # Create directories (silent). Wrap mkdir in try/except to report clearer errors
    # when a path component is an existing file (NotADirectoryError) or other OS
    # errors occur (permissions, etc.).
    for directory in directories:
        dir_path = project_root / directory
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
        except NotADirectoryError:
            print(f"Error: Cannot create directory '{dir_path}': a path component is not a directory.")
            sys.exit(1)
        except OSError as e:
            print(f"Error: Failed to create directory '{dir_path}': {e}")
            sys.exit(1)

    # Create an empty README.md at project root (single file)
    with open(project_root / "README.md", "w") as f:
        f.write("")
    
    # Create empty LICENSE
    with open(project_root / "LICENSE", "w") as f:
        f.write("")
    
    # Create empty metadata files
    meta_files = [
        (project_root / "metadata/project_metadata.txt"),
        (project_root / "metadata/sample_metadata.csv"),
        (project_root / "metadata/experiment_metadata.xlsx"),
    ]
    for p in meta_files:
        with open(p, "w") as f:
            f.write("")
    
    # Create empty environment files
    env_files = [
        (project_root / "environment/requirements.txt"),
        (project_root / "environment/environment.yml"),
    ]
    for p in env_files:
        with open(p, "w") as f:
            f.write("")
    
    # Keep configs/ empty (no default config file created)
    
    print(f"\n✓ Project structure created successfully at: {project_root.resolve()}")
    print(f"\nNext steps:")
    # Show the full (absolute) path when suggesting the `cd` command
    print(f"1. cd {project_root.resolve()}")
    print(f"2. Update README.md and other files with your project information")
    print(f"3. Modify the project structure as needed for your specific requirements.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a standardized project structure.")
    parser.add_argument("project_name", help="Name of the project to create")
    parser.add_argument("base_path", nargs="?", default=".", help="Base directory where project will be created")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be created without writing files")

    args = parser.parse_args()

    create_project(args.project_name, args.base_path, dry_run=args.dry_run)

