# Image Domain Pipeline

This module performs motion artifact reduction directly on reconstructed CT images.

## Components

- `preprocessing/`
  - DICOM Loading and Sinogram generation
  ```bash
   python3 image_domain/preprocessing/dicom_to_sinogram.py
    ```
  - Motion artifact simulation
  ```bash
  python3 image_domain/preprocessing/add_motion_artifacts.py
  ```
  - Image Reconstruction to 3D volume
  ```bash
  python3 image_domain/preprocessing/train_image_reconstruction.py
  ```

- `training/`
  - Model training on reconstructed images
  ```bash
  python3 image_domain/training/train.py --model mr_lkv --norm batch
  ```

- `inference/`
  - Model testing and evaluation
   ```bash
  python3 image_domain/inference/run_inference.py --model mr_lkv
  python3 image_domain/evaluation/final_evaluation.py --model mr_lkv --clean-folder clean
  ```
- `Visualisation and Plots`
 - Visualisation of Predicted Volume Slices
  ```bash
 python3 image_domain/visualisation/visualise_ct.py
 python3 image_domain/visualisation/visualise_ct_mrlkv.py
 python3 image_domain/visualisation/metrics_plots.py
  ```

## Workflow

1. Load reconstructed CT images
2. Train model on artifact-corrupted images
3. Predict artifact-free reconstructions

## Notes

- Uses configuration from `config/config.py`
- Requires preprocessed data or dataset access