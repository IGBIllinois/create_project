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
    
    # Canonical structure block (used for dry-run output and README templates)
    structure_block = f"""{project_name}/
├── README.md                    # Project-level README
├── LICENSE                      # Empty placeholder license file
├── metadata/
│   ├── project_metadata.txt     # Project-level information (title, PI, funding)
│   ├── sample_metadata.csv      # Sample information (IDs, species, conditions)
│   └── experiment_metadata.xlsx # Experimental details (protocols, reagents, dates)
├── data/
│   ├── raw/
│   │   ├── sequencing/          # Raw sequencing data
│   │   └── imaging/             # Raw imaging data
│   ├── references/              # Reference datasets or external resources
│   └── processed/               # Cleaned or feature-extracted data
├── src/
│   ├── preprocessing/           # Scripts to prepare and clean raw data
│   ├── training/                # Model training scripts
│   ├── evaluation/              # Evaluation scripts
│   ├── analysis/                # Analysis scripts
│   ├── visualization/           # Visualization scripts
│   └── utils/                   # Utility functions
├── results/
│   ├── figures/                 # Plots and visualizations
│   ├── tables/                  # Metrics and summary tables
│   └── reports/                 # Reports or summaries of analysis
├── docs/                        # Supporting documentation and protocols
├── notebooks/                   # Jupyter or R notebooks
├── configs/                     # Hyperparameters, training configs, experiment settings
├── models/
│   ├── checkpoints/             # Intermediate saved model states
│   └── final_models/            # Final trained models
├── environment/
│   ├── environment.yml          # Environment file (empty placeholder)
│   └── requirements.txt         # Requirements file (empty placeholder)
├── temp/                        # Temporary files and cache
└── archive/                     # Backup of old scripts, data, or model versions
"""
    
    # If dry-run, print the planned project tree and exit (no file operations)
    if dry_run:
        print(structure_block)
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

    # Look for a repo-level templates/README.md next to the project root of
    # this script. If present, format it with the project name and structure.
    repo_root = Path(__file__).resolve().parent.parent
    template_path = repo_root / "templates" / "README.md"
    if template_path.exists():
        try:
            tpl = template_path.read_text()
            readme_text = tpl.format(project_name=project_name, structure=structure_block)
        except Exception:
            # If templating fails for any reason, fall back to the default text.
            readme_text = f"# {project_name}\n\nA standardized project layout created by create_project.py.\n\n{structure_block}\n"
    else:
        readme_text = f"# {project_name}\n\nA standardized project layout created by create_project.py.\n\n{structure_block}\n"

    (project_root / "README.md").write_text(readme_text)
    
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
    
    print(f"\n✓ Project structure created successfully at: {project_root.resolve()}")
    print(f"\nSee the README.md for an overview of the structure.")
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

