# Configuration

This folder contains configuration files used across the project.

## Key File

- `config.py` – Defines:
  - Dataset paths
  - Checkpoint paths
  - Output directories
  - Training parameters

## Important

Paths are environment-specific (HPC setup).

Before running any script, update:

```python
DATA_PATH = "/your/path"
CHECKPOINT_PATH = "/your/path"
RESULTS_PATH = "/your/path"