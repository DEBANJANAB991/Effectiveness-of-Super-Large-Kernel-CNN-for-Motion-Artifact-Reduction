# Source Code

This directory contains the complete implementation of the motion artifact reduction pipeline.

## Structure

- `config/` – Configuration files (paths, parameters)
- `models/` – Deep learning models (MR-LKV, U-Net, RepLKNet)
- `image_domain/` – Image-domain pipeline
- `projection_domain/` – Projection-domain pipeline
- `ExternalRepo/` – External model implementations

## Notes

- All scripts rely on configuration values defined in `config/config.py`
- Paths must be updated before execution