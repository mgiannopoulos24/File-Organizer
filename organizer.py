import os
import sys
import shutil
import magic

# Initialize magic library
mime = magic.Magic(mime=True)

def get_file_type(file_path):
    # Use magic library to determine file type
    return mime.from_file(file_path)

def organize_files(source_dir):
    # Create directories if they don't exist already
    categories = {
        "Images": ["image/jpeg", "image/png", "image/gif", "image/bmp"],
        "Videos": ["video/mp4", "video/x-msvideo", "video/x-matroska"],
        "Documents": ["application/pdf", "application/msword", "application/vnd.ms-excel",
                      "application/vnd.ms-powerpoint", "text/plain"],
        "Music": ["audio/mpeg", "audio/x-wav", "audio/ogg", "audio/flac"],
        "Archives": ["application/zip", "application/x-rar-compressed", "application/x-tar", "application/x-gzip"],
        "Others": []  # Default category for other file types
    }

    for category in categories:
        os.makedirs(os.path.join(source_dir, category), exist_ok=True)

    # Organize files
    for filename in os.listdir(source_dir):
        if filename == "organizer.py" or filename == "README.md":
            continue  # Skip organizing the organizer script and README

        src_path = os.path.join(source_dir, filename)
        if os.path.isfile(src_path):
            file_type = get_file_type(src_path)
            
            moved = False
            for category, mime_types in categories.items():
                if file_type in mime_types:
                    dst_dir = os.path.join(source_dir, category)
                    shutil.move(src_path, dst_dir)
                    print(f"Moved: {filename} -> {category}/")
                    moved = True
                    break

            if not moved:
                dst_dir = os.path.join(source_dir, "Others")
                shutil.move(src_path, dst_dir)
                print(f"Moved: {filename} -> Others/")

    print("Organizing complete.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python organizer.py <source_directory>")
        sys.exit(1)

    source_dir = sys.argv[1]
    if not os.path.isdir(source_dir):
        print(f"Error: {source_dir} is not a valid directory.")
        sys.exit(1)

    organize_files(source_dir)

if __name__ == "__main__":
    main()
