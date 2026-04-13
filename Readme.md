![Python](https://img.shields.io/badge/python-3.10-blue)
![PyTorch](https://img.shields.io/badge/framework-PyTorch-red)

# Motion Artifact Reduction in CT using Super-Large Kernel CNNs (MR-LKV)

## Overview

Motion artifacts in Computed Tomography (CT) scans significantly degrade image quality and affect clinical diagnosis. These artifacts arise due to inconsistencies in projection data caused by patient motion and often exhibit global spatial patterns.

This project proposes a deep learning framework based on **super-large kernel convolutional networks (MR-LKV)** to effectively model and reduce motion artifacts. The approach is implemented and evaluated in both the **projection domain (sinogram space)** and the **image domain (reconstructed CT images)**.

## Objectives

- Develop a deep learning pipeline for motion artifact reduction
- Compare multiple models: MR-LKV (proposed), U-Net, RepLKNet, SwinIR, and Restormer
- Evaluate performance in projection and image domains
- Analyze trade-offs between accuracy (PSNR, SSIM), computational complexity, and inference time

## Repository Structure

```
.
├── src/
│   ├── config/                    # Configuration (paths, hyperparameters)
│   ├── models/                    # MR-LKV, U-Net, RepLKNet
│   ├── image_domain/              # Image-domain training & inference
│   ├── projection_domain/         # Projection-domain pipeline
│   └── ExternalRepo/
│       ├── Restormer/             # Submodule
│       ├── SwinIR/                # Submodule
│       └── diffct/                # Locally modified version
├── checkpoints/                   # Model weights (.pth)
├── results/                       # Plots, logs, reconstructions
├── job.sh                         # HPC job script
├── setup.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/DEBANJANAB991/Effectiveness-of-Super-Large-Kernel-CNN-for-Motion-Artifact-Reduction.git

```

### 2. Create environment

```bash
conda create -n thesis-gpu python=3.10
conda activate thesis-gpu
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or install in editable mode:

```bash
pip install -e .
```

## Dataset

- **Dataset:** [CQ500 CT dataset](http://headctstudy.qure.ai/dataset)
- **Preprocessing includes:** DICOM loading, conversion to sinograms, and synthetic motion artifact generation

> **Note:** The dataset is not included in this repository due to size and privacy constraints.

## Pipeline Overview

### 1. Preprocessing

- Convert DICOM to sinogram
- Add synthetic motion artifacts

### 2. Projection Domain

- Train model on sinograms
- Reconstruct using FDK
- Convert 2D to 3D

### 3. Image Domain

- Train model on reconstructed images
- Perform artifact correction

### 4. Evaluation

- Metrics: PSNR, SSIM
- Visual comparison
- ROI-based analysis

## Models

### Proposed Model

- **MR-LKV** — Motion Restoration using Large Kernel conVolution

### Baselines

- U-Net
- RepLKNet
- SwinIR
- Restormer

### External Models

- [Restormer](https://github.com/swz30/Restormer)
- [SwinIR](https://github.com/JingyunLiang/SwinIR)

### DiffCT (Modified)

This project includes a locally modified version of [DiffCT](https://github.com/sypsyp97/diffct), adapted for pipeline integration, custom preprocessing, and projection handling.

## Usage

### Image Domain Training

```bash
python3 src/image_domain/training/train.py
```

### Projection Domain Training

```bash
python3 src/projection_domain/training/train.py
```

### Image Domain Inference

```bash
python3 src/image_domain/inference/run_inference.py
```
### Projection Domain Inference

```bash
python3 src/projection_domain/inference/run_inference.py
```

## Results

Results are stored in the `results/` directory and include training curves, quantitative evaluation tables, visual comparisons, and ROI analysis.

## Pretrained Models

Pretrained model weights are available here.

### Image Domain

https://drive.google.com/drive/folders/1s54Kxz7kzvkK6pQEev2daEGw6yAZX7_X?usp=sharing

### Projection Domain

https://drive.google.com/drive/folders/1un4rHg42g8VVwGFvoAxTtyeK8QIHMHTD?usp=sharing



### Usage

Download the files and place them in checkpoints/ folder.


Then update paths in src/config/config.py

## HPC Usage

Submit the job script on your cluster:

```bash
sbatch job.sh
```

## Reproducibility Note

This project was developed and executed on an HPC environment. As a result, file paths in `config.py` are specific to the HPC system, datasets are not included, and some scripts expect preprocessed data and directory structures to already be in place.

**To run this project, users need to:**

1. Update paths in `src/config/config.py` to match your local or cluster environment.
2. Provide the CT dataset (e.g., CQ500) and preprocessed sinograms, or regenerate them using the provided preprocessing scripts.
3. Adjust checkpoint paths and output directories as needed.

The codebase is structured for clarity and research reproducibility, but requires environment-specific adaptation to run end-to-end.

## Key Contributions

- Introduced MR-LKV for global artifact modeling using super-large kernel convolutions
- Demonstrated effectiveness of large-kernel CNNs for CT artifact reduction
- Compared projection-domain vs. image-domain learning strategies
- Built a reproducible end-to-end CT artifact reduction pipeline

## Citation

```bibtex
@mastersthesis{bhattacharjya2026,
  title   = {Motion Artifact Reduction in CT using Super-Large Kernel CNNs},
  author  = {Debanjona Bhattacharjya},
  year    = {2026}
}
```

## Author

**Debanjona Bhattacharjya**
Master's Thesis — Germany

## Contact

> debanjona.b.bhattacharjya@fau.de
