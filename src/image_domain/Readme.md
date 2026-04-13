# Image Domain Pipeline

This module performs motion artifact reduction directly on reconstructed CT images.

## Components

- `preprocessing/`
  - DICOM loading
  - Sinogram generation
  - Motion artifact simulation
  - Image Reconstruction to 3D volume

- `training/`
  - Model training on reconstructed images

- `inference/`
  - Model evaluation and testing

- `Visualisation and Plots`
 - Visualisation of Predicted Volume Slices

## Workflow

1. Load reconstructed CT images
2. Train model on artifact-corrupted images
3. Predict artifact-free reconstructions

## Notes

- Uses configuration from `config/config.py`
- Requires preprocessed data or dataset access