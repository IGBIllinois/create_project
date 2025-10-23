[![Build Status](https://github.com/IGBIllinois/create_project/actions/workflows/main.yml/badge.svg)](https://github.com/IGBIllinois/create_project/actions/workflows/main.yml)


# create_project.py

This repository contains `create_project.py`, a small Python CLI that generates a
standardized research project layout. The tool is intentionally minimal: it creates the
directory tree and a few empty placeholder files so teams can start with a consistent
structure.

## Current behavior

- Creates the directory layout silently (no per-directory printouts).
- Writes a single empty `README.md` at the project root.
- Creates empty placeholder files in `metadata/` and `environment/`.
- Aborts early if the target project directory already exists.

## CLI flags / help

The script supports the following options. View full help from the command line:

```bash
python create_project.py --help
```

- `--dry-run`: print the planned project tree to stdout and do not write any files or
	directories (useful for previewing).

## Usage

```bash
python create_project.py <project_name> [base_path] [--dry-run]
```

### Arguments

- `project_name` (required): Name of the project to create
- `base_path` (optional): Base directory where the project will be created. Defaults to current directory (`.`) if not specified.

Examples:

```bash
# Preview the project layout without creating anything
python create_project.py my_project --dry-run

# Create a new project in the current directory
python create_project.py my_project

# Create a project at a specific location
python create_project.py my_project ~/Documents/Projects

# Create a project with an absolute path
python create_project.py my_project /path/to/location

# Combine base_path with other options
python create_project.py my_project ~/Research --dry-run

# Note: If the target directory already exists, the command will abort with an error.
```

## Generated layout

When run, the script creates the following tree (all files are empty placeholders unless
noted otherwise):

```
$PROJECT_NAME/
├── README.md                   	# Project-level README 
├── LICENSE                     	# Empty placeholder license file
├── metadata/
│   ├── project_metadata.txt    	# Project-level information (title, PI, funding)
│   ├── sample_metadata.csv     	# Sample information (IDs, species, conditions)
│   └── experiment_metadata.xlsx	# Experimental details (protocols, reagents, dates)
├── data/
│   ├── raw/
│   │   ├── sequencing/        	 	# Raw sequencing data
│   │   └── imaging/           	 	# Raw imaging data
│   ├── references/             	# Reference datasets or external resources
│   └── processed/             		# Cleaned or feature-extracted data
├── src/
│   ├── preprocessing/          	# Scripts to prepare and clean raw data
│   ├── training/               	# Model training scripts
│   ├── evaluation/             	# Evaluation scripts
│   ├── analysis/               	# Analysis scripts
│   ├── visualization/          	# Visualization scripts
│   └── utils/                  	# Utility functions
├── results/
│   ├── figures/                	# Plots and visualizations
│   ├── tables/                 	# Metrics and summary tables
│   └── reports/                	# Reports or summaries of analysis
├── docs/                       	# Supporting documentation and protocols
├── notebooks/                  	# Jupyter or R notebooks
├── configs/                    	# Hyperparameters, training configs, experiment settings
├── models/
│   ├── checkpoints/            	# Intermediate saved model states
│   └── final_models/           	# Final trained models
├── environment/
│   ├── environment.yml         	# Environment file (empty placeholder)
│   └── requirements.txt        	# Requirements file (empty placeholder)
├── temp/                       	# Temporary files and cache
└── archive/                    	# Backup of old scripts, data, or model versions
```
