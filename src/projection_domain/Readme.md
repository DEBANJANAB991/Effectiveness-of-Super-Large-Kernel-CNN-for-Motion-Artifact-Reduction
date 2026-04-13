# Projection Domain Pipeline

This module performs motion artifact reduction in sinogram (projection) space.

## Components

- `preprocessing/`
  - DICOM to sinogram conversion
  - Motion artifact generation

- `training/`
  - Model training on sinograms

- `inference/`
  - Prediction and reconstruction

- `Visualisation and Plots`
 - Visualisation of Predicted Volume Slices


## Workflow

1. Convert CT data to sinograms
2. Add motion artifacts
3. Train model to correct sinograms
4. Reconstruct corrected images (FDK)

## Notes

- Reconstruction step uses FDK algorithm
- Requires DiffCT integration