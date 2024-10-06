import os
import sys
import shutil
import magic
import logging
import json
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import argparse
import uuid

# Initialize magic library
mime = magic.Magic(mime=True)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_file_type(file_path):
    try:
        # Use magic library to determine file type
        return mime.from_file(file_path)
    except Exception as e:
        logging.error(f"Error determining file type for {file_path}: {e}")
        return None

def load_categories(config_path="categories.json"):
    if not os.path.exists(config_path):
        logging.warning(f"Config file {config_path} not found. Using default categories.")
        return {
            "Images": ["image/jpeg", "image/png", "image/gif", "image/bmp"],
            "Videos": ["video/mp4", "video/x-msvideo", "video/x-matroska"],
            "Documents": ["application/pdf", "application/msword", "application/vnd.ms-excel",
                          "application/vnd.ms-powerpoint", "text/plain"],
            "Music": ["audio/mpeg", "audio/x-wav", "audio/ogg", "audio/flac"],
            "Archives": ["application/zip", "application/x-rar-compressed", "application/x-tar", "application/x-gzip"],
            "Others": []  # Default category for other file types
        }
    with open(config_path, 'r') as f:
        return json.load(f)

def safe_move(src_path, dst_dir):
    base, ext = os.path.splitext(os.path.basename(src_path))
    dst_path = os.path.join(dst_dir, os.path.basename(src_path))
    while os.path.exists(dst_path):
        dst_path = os.path.join(dst_dir, f"{base}_{uuid.uuid4().hex}{ext}")
    try:
        shutil.move(src_path, dst_path)
        logging.info(f"Moved: {src_path} -> {dst_dir}/")
    except (shutil.Error, OSError) as e:
        logging.error(f"Failed to move {src_path} to {dst_dir}: {e}")

def move_file(source_dir, filename, categories, dry_run):
    src_path = os.path.join(source_dir, filename)
    if os.path.isfile(src_path):
        file_type = get_file_type(src_path)
        if not file_type:
            return

        moved = False
        for category, mime_types in categories.items():
            if file_type in mime_types:
                dst_dir = os.path.join(source_dir, category)
                if dry_run:
                    logging.info(f"Dry run: Would move {src_path} to {dst_dir}/")
                else:
                    safe_move(src_path, dst_dir)
                moved = True
                break

        if not moved:
            dst_dir = os.path.join(source_dir, "Others")
            if dry_run:
                logging.info(f"Dry run: Would move {src_path} to {dst_dir}/")
            else:
                safe_move(src_path, dst_dir)

def organize_files(source_dir, dry_run=False):
    # Load categories from config or use default
    categories = load_categories()

    # Create directories if they don't exist already
    for category in categories:
        os.makedirs(os.path.join(source_dir, category), exist_ok=True)

    # Organize files with progress bar
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(move_file, source_dir, filename, categories, dry_run)
            for filename in tqdm(os.listdir(source_dir))
            if os.path.isfile(os.path.join(source_dir, filename))
        ]
        for future in futures:
            future.result()

    logging.info("Organizing complete.")

def main():
    parser = argparse.ArgumentParser(description="Organize files by type.")
    parser.add_argument('source_directory', help='Directory to organize')
    parser.add_argument('--dry-run', action='store_true', help='List actions without executing them')
    args = parser.parse_args()

    source_dir = args.source_directory
    if not os.path.isdir(source_dir):
        logging.error(f"Error: {source_dir} is not a valid directory.")
        sys.exit(1)

    organize_files(source_dir, dry_run=args.dry_run)

if __name__ == "__main__":
    main()