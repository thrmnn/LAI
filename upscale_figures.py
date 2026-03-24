#!/usr/bin/env python3
"""
Upscale and fix DPI metadata for manuscript figures to meet
Springer Nature requirements (minimum 300 DPI).

Originals are backed up to _originals/ subdirectories before any modification.
"""

import os
import shutil
from PIL import Image

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "draft", "figures")


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def backup_original(filepath):
    """Copy the original file into an _originals/ subdirectory."""
    parent = os.path.dirname(filepath)
    backup_dir = os.path.join(parent, "_originals")
    ensure_dir(backup_dir)
    dest = os.path.join(backup_dir, os.path.basename(filepath))
    if not os.path.exists(dest):
        shutil.copy2(filepath, dest)
        print(f"  [backup] {os.path.relpath(filepath, BASE)} -> _originals/")
    else:
        print(f"  [backup] already exists, skipping")


def process_group1():
    """
    Group 1 — matplotlib plots at 150 DPI.
    These have sufficient pixels for print but DPI metadata says 150.
    Resample to 2x pixel dimensions and set DPI to 300.
    """
    print("=" * 70)
    print("GROUP 1: Matplotlib plots (150 DPI -> 2x pixels + 300 DPI metadata)")
    print("=" * 70)

    files = [
        "results/training/overview_multi_panel.png",
        "results/training/model_comparison.png",
        "results/training/feature_importance_plot.png",
        "results/training/lai_vs_height_analysis.png",
        "results/training/ndvi_vs_lai_analysis.png",
    ]

    for rel in files:
        filepath = os.path.join(BASE, rel)
        if not os.path.exists(filepath):
            print(f"  [SKIP] {rel} — file not found")
            continue

        print(f"\n  Processing: {rel}")
        backup_original(filepath)

        img = Image.open(filepath)
        old_size = img.size
        old_dpi = img.info.get("dpi", (None, None))

        # Resample to 2x dimensions
        new_size = (old_size[0] * 2, old_size[1] * 2)
        img_resized = img.resize(new_size, Image.LANCZOS)

        # Save with 300 DPI metadata
        img_resized.save(filepath, dpi=(300, 300))

        # Verify
        verify = Image.open(filepath)
        print(f"    Before: {old_size}, DPI={old_dpi}")
        print(f"    After:  {verify.size}, DPI={verify.info.get('dpi')}")
        print(f"    [OK]")


def process_group2():
    """
    Group 2 — small images (too few pixels for print).
    Upscale to 2x using Lanczos resampling and set DPI to 300.
    JPEG files are converted to PNG to avoid recompression artifacts.
    """
    print("\n" + "=" * 70)
    print("GROUP 2: Small images (upscale 2x + 300 DPI; JPEG -> PNG)")
    print("=" * 70)

    files = [
        ("methods/RGB_zone0.jpeg", "methods/RGB_zone0.png"),
        ("methods/CIR_zone0.jpeg", "methods/CIR_zone0.png"),
        ("methods/tree_viz.png", None),
        ("methods/06_final_combined.png", None),
    ]

    jpeg_to_png = []

    for rel, new_rel in files:
        filepath = os.path.join(BASE, rel)
        if not os.path.exists(filepath):
            print(f"  [SKIP] {rel} — file not found")
            continue

        print(f"\n  Processing: {rel}")
        backup_original(filepath)

        img = Image.open(filepath)
        old_size = img.size
        old_dpi = img.info.get("dpi", (None, None))

        # Resample to 2x dimensions
        new_size = (old_size[0] * 2, old_size[1] * 2)
        img_resized = img.resize(new_size, Image.LANCZOS)

        # Determine output path
        if new_rel is not None:
            # JPEG -> PNG conversion
            out_path = os.path.join(BASE, new_rel)
            jpeg_to_png.append((rel, new_rel))
        else:
            out_path = filepath

        # Ensure RGBA/RGB mode for PNG save
        if img_resized.mode == "CMYK":
            img_resized = img_resized.convert("RGB")

        img_resized.save(out_path, format="PNG", dpi=(300, 300))

        # Verify
        verify = Image.open(out_path)
        out_rel = new_rel if new_rel else rel
        print(f"    Before: {old_size}, DPI={old_dpi}")
        print(f"    After:  {verify.size}, DPI={verify.info.get('dpi')}")
        if new_rel:
            print(f"    Converted: {rel} -> {new_rel}")
        print(f"    [OK]")

    return jpeg_to_png


def process_group3():
    """
    Group 3 — supplementary images (fix DPI metadata only, no resize).
    """
    print("\n" + "=" * 70)
    print("GROUP 3: Supplementary images (DPI metadata fix only)")
    print("=" * 70)

    files = [
        "results/analytics/distributions_by_species.png",
        "methods/hemispherical_fisheye.png",
        "methods/binarized_fisheye.png",
    ]

    for rel in files:
        filepath = os.path.join(BASE, rel)
        if not os.path.exists(filepath):
            print(f"  [SKIP] {rel} — file not found")
            continue

        print(f"\n  Processing: {rel}")
        backup_original(filepath)

        img = Image.open(filepath)
        old_size = img.size
        old_dpi = img.info.get("dpi", (None, None))

        # Re-save with 300 DPI metadata (no resize)
        # Need to preserve all image data — load fully then save
        img.load()

        # For PNG files, we need to handle the pHYs chunk properly
        # Simply re-saving with dpi= parameter sets the metadata
        img.save(filepath, dpi=(300, 300))

        # Verify
        verify = Image.open(filepath)
        print(f"    Before: {old_size}, DPI={old_dpi}")
        print(f"    After:  {verify.size}, DPI={verify.info.get('dpi')}")
        print(f"    [OK]")


def main():
    print("Springer Nature DPI Upgrade Script")
    print(f"Base directory: {BASE}")
    print()

    process_group1()
    jpeg_to_png = process_group2()
    process_group3()

    # Summary of filename changes requiring LaTeX updates
    print("\n" + "=" * 70)
    print("SUMMARY: Filename changes requiring LaTeX updates")
    print("=" * 70)
    if jpeg_to_png:
        for old, new in jpeg_to_png:
            print(f"  {old}  ->  {new}")
        print()
        print("  Update any \\includegraphics references from .jpeg to .png")
        print("  (The original .jpeg files are preserved in _originals/)")
    else:
        print("  No filename changes.")

    print("\nDone.")


if __name__ == "__main__":
    main()
