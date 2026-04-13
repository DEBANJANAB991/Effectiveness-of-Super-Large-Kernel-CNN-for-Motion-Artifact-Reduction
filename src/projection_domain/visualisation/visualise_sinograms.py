import os
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
# ================================
# Path
# ================================

from config.config import MERGED_SINOGRAM_3D_TEST_v2
INPUT_DIR = Path(MERGED_SINOGRAM_3D_TEST_v2) /"replknet"

OUTPUT_DIR = "sinogram_visualizations_replknet"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ================================
# Load files
# ================================
files = sorted([f for f in os.listdir(INPUT_DIR) if f.endswith(".npy")])

num_samples = min(10, len(files))

print(f"Found {len(files)} files. Generating {num_samples} samples...")

# ================================
# Visualization function
# ================================
def normalize(img):
    img = img.astype(float)
    img -= img.min()
    if img.max() > 0:
        img /= img.max()
    return img


def visualize_sinogram(sino, save_path, title=""):

    # Ensure shape is [angles, H, W]
    if sino.ndim != 3:
        raise ValueError(f"Unexpected shape: {sino.shape}")

    A, H, W = sino.shape

    # Fix dimension order if needed
    if A < 32:  # heuristic
        sino = np.transpose(sino, (2, 0, 1))
        A, H, W = sino.shape

    # Extract views
    row = sino[:, H//2, :]
    col = sino[:, :, W//2]
    proj = sino[A//2]

    # Normalize
    row = normalize(row)
    col = normalize(col)
    proj = normalize(proj)

    # Plot
    fig, axs = plt.subplots(1, 3, figsize=(12, 4))

    axs[0].imshow(row, cmap='gray')
    axs[0].set_title("Central Row")

    axs[1].imshow(col, cmap='gray')
    axs[1].set_title("Central Column")

    axs[2].imshow(proj, cmap='gray')
    axs[2].set_title("One Projection")

    for ax in axs:
        ax.axis('off')

    plt.suptitle(title)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()


# ================================
# MAIN LOOP
# ================================
for i in range(num_samples):

    file_path = os.path.join(INPUT_DIR, files[i])

    print(f"Processing: {files[i]}")

    sino = np.load(file_path)

    save_path = os.path.join(
        OUTPUT_DIR,
        f"{os.path.basename(INPUT_DIR)}_{i}.png"
    )

    visualize_sinogram(
        sino,
        save_path,
        title=f"{os.path.basename(INPUT_DIR)} - Sample {i}"
    )

print("\n Done! Images saved in:", OUTPUT_DIR)