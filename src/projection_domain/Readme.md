# Projection Domain Pipeline

This module performs motion artifact reduction in sinogram (projection) space.

## Components

- `preprocessing/`
  - DICOM to sinogram conversion
  ```bash
   python3 projection_domain/preprocessing/dicom_to_sinogram.py
    ```
  - Motion artifact generation
  ```bash
  python3 projection_domain/preprocessing/add_motion_artifacts.py
  python3 projection_domain/preprocessing/sinogram_to_2D.py
    ```
- `training/`
  - Model training on sinograms
  ```bash
  python3 projection_domain/training/train.py --model mr_lkv --norm batch --max-views-per-patient 100
    ```

- `inference/`
  - Prediction, Reconstruction and Evaluation
  ```bash
  python3 projection_domain/inference/run_inference.py --model mr_lkv
  python3 projection_domain/preprocessing/merge_2D_to_3D.py mr_lkv
  python3 projection_domain/reconstruction/fdk_reconstruction.py mr_lkv
  python3 projection_domain/evaluation/final_evaluation.py --model mr_lkv --clean-folder clean
  ```
- `Visualisation and Plots`
 - Visualisation of Predicted Volume Slices
```bash
python3 projection_domain/visualisation/visualise_ct.py
python3 projection_domain/visualisation/visualise_mrlkv.py
python3 projection_domain/visualisation/metrics_plot.py
python3 projection_domain/visualisation/visualise_sinograms.py

```


## Workflow

1. Convert CT data to sinograms
2. Add motion artifacts
3. Train model to correct sinograms
4. Reconstruct corrected images (FDK)

## Notes

- Reconstruction step uses FDK algorithm
- Requires DiffCT integration