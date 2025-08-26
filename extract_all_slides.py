#!/usr/bin/env python3

import os
import sys
from pdf2image import convert_from_path
from pathlib import Path

def extract_slides_to_images():
    slides_dir = Path("Slides")
    output_dir = Path("extracted_slides")
    
    if not slides_dir.exists():
        print(f"Error: {slides_dir} directory not found")
        return False
    
    output_dir.mkdir(exist_ok=True)
    
    pdf_files = sorted(slides_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found in Slides directory")
        return False
    
    print(f"Found {len(pdf_files)} PDF files")
    
    total_pages = 0
    
    for pdf_file in pdf_files:
        print(f"\nProcessing: {pdf_file.name}")
        
        pdf_base = pdf_file.stem
        pdf_output_dir = output_dir / pdf_base
        pdf_output_dir.mkdir(exist_ok=True)
        
        try:
            images = convert_from_path(pdf_file, dpi=150)
            
            for i, image in enumerate(images, 1):
                image_filename = pdf_output_dir / f"{pdf_base}_page_{i:03d}.png"
                image.save(image_filename, "PNG")
                print(f"  Saved: {image_filename.name}")
                total_pages += 1
                
        except Exception as e:
            print(f"  Error processing {pdf_file.name}: {e}")
            continue
    
    print(f"\nExtraction complete! Total pages extracted: {total_pages}")
    return True

if __name__ == "__main__":
    success = extract_slides_to_images()
    sys.exit(0 if success else 1)