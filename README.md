# File Organizer CLI Tool
This command-line interface (CLI) tool organizes files in a specified directory based on their types. It uses the `magic` library to identify file types by content, allowing for accurate categorization even when file extensions are unreliable.

## Features
- **Automatic File Categorization:** Files are categorized into directories such as Images, Videos, Documents, Music, Archives, and Others based on their MIME types.
- **Flexible and Customizable:** Easily customizable to add more categories or modify existing ones via a configuration file (`categories.json`).
- **Command-Line Interface:** Simple to use directly from the command line with Python.
- **Parallel Processing:** Uses multiple threads to organize files, making it faster for large directories.
- **Progress Bar:** Provides a visual progress bar using `tqdm` to track the organization process.
- **Safe File Handling:** Handles duplicate files gracefully by renaming them to avoid overwriting.

## Requirements
- Python 3.x
- `python-magic` library
- `tqdm` library

## Installation
1. Clone the repository:
```console
git clone https://github.com/mgiannopoulos24/File-Organizer
```

2. Install dependencies:
```console
pip install -r requirements.txt
```

## Usage
1. Navigate to the directory containing `organizer.py`:
```console
cd path/to/file_organizer
```
2. Run the organizer tool with the path to the directory you want to organize:
```console
python3 organizer.py /path/to/your/source/directory
```
Replace `/path/to/your/source/directory` with the path to the directory containing the files you want to organize.

### Optional Arguments
- `--dry-run`: Lists actions without executing them. This is useful for previewing what changes will be made.

Example:
```console
python3 organizer.py /path/to/your/source/directory --dry-run
```

## Example
Suppose you have a directory `~/Downloads` with various files:

```console
User@Github:~$ ll
total 20364
drwxrwxrwx 1 dwish dwish     4096 Oct  6 14:34 ./
drwxrwxrwx 1 dwish dwish     4096 Oct  6 14:32 ../
-rwxrwxrwx 1 dwish dwish    21173 Oct  6 14:30 archive.zip*
-rwxrwxrwx 1 dwish dwish    54138 Oct  6 14:31 audio.mp3*
-rwxrwxrwx 1 dwish dwish    13939 Sep 11 14:34 document.pdf*
-rwxrwxrwx 1 dwish dwish    72660 Oct  6 14:32 image.jpg*
-rwxrwxrwx 1 dwish dwish     1847 Oct  6 14:34 script.sh*
-rwxrwxrwx 1 dwish dwish 20673054 Oct  6 14:34 video.mp4*
```

Running the organizer tool with `--dry-run`:

```console
python3 organizer.py ~/Downloads --dry-run
```

After running, you will get a list of what the changes will be:

```console
User@Github:~$ python3 organizer.py ~/Downloads/ --dry-run
2024-10-06 14:39:04,653 - WARNING - Config file categories.json not found. Using default categories.
  0%|                                                  | 0/12 [00:00<?, ?it/s]2024-10-06 14:39:04,676 - INFO - Dry run: Would move ~/Downloads/archive.zip to ~/Downloads/Archives/
2024-10-06 14:39:04,680 - INFO - Dry run: Would move ~/Downloads/audio.mp3 to ~/Downloads/Music/
100%|████████████████████████████████████████| 12/12 [00:00<00:00, 834.36it/s]
2024-10-06 14:39:04,684 - INFO - Dry run: Would move ~/Downloads/document.pdf to ~/Downloads/Documents/
2024-10-06 14:39:04,687 - INFO - Dry run: Would move ~/Downloads/image.jpg to ~/Downloads/Images/
2024-10-06 14:39:04,691 - INFO - Dry run: Would move ~/Downloads/script.sh to ~/Downloads/Others/
2024-10-06 14:39:04,695 - INFO - Dry run: Would move ~/Downloads/video.mp4 to ~/Downloads/Videos/
2024-10-06 14:39:04,696 - INFO - Organizing complete.
```

Running the organizer tool normally

```console
python3 organizer.py ~/Downloads
```

After running, your directory structure will look like this:

```console
User@Github:~$ python3 organizer.py ~/Downloads/
2024-10-06 14:42:46,651 - WARNING - Config file categories.json not found. Using default categories.
  0%|                                                  | 0/12 [00:00<?, ?it/s]2024-10-06 14:42:46,684 - INFO - Moved: ~/Downloads/archive.zip -> ~/Downloads/Archives/
100%|████████████████████████████████████████| 12/12 [00:00<00:00, 662.54it/s]
2024-10-06 14:42:46,692 - INFO - Moved: ~/Downloads/audio.mp3 -> ~/Downloads/Music/
2024-10-06 14:42:46,697 - INFO - Moved: ~/Downloads/document.pdf -> ~/Downloads/Documents/
2024-10-06 14:42:46,703 - INFO - Moved: ~/Downloads/image.jpg -> ~/Downloads/Images/
2024-10-06 14:42:46,708 - INFO - Moved: ~/Downloads/script.sh -> ~/Downloads/Others/
2024-10-06 14:42:46,713 - INFO - Moved: ~/Downloads/video.mp4 -> ~/Downloads/Videos/
2024-10-06 14:42:46,714 - INFO - Organizing complete.
User@Github:~$ ll
total 0
drwxrwxrwx 1 dwish dwish 4096 Oct  6 14:42 ./
drwxrwxrwx 1 dwish dwish 4096 Oct  6 14:32 ../
drwxrwxrwx 1 dwish dwish 4096 Oct  6 14:42 Archives/
drwxrwxrwx 1 dwish dwish 4096 Oct  6 14:42 Documents/
drwxrwxrwx 1 dwish dwish 4096 Oct  6 14:42 Images/
drwxrwxrwx 1 dwish dwish 4096 Oct  6 14:42 Music/
drwxrwxrwx 1 dwish dwish 4096 Oct  6 14:42 Others/
drwxrwxrwx 1 dwish dwish 4096 Oct  6 14:42 Videos/
```

## Configuration File Example
You can create a `categories.json` file to customize the file categories. Here is an example of how it might look:

```json
{
    "Images": ["image/jpeg", "image/png", "image/gif", "image/bmp"],
    "Videos": ["video/mp4", "video/x-msvideo", "video/x-matroska"],
    "Documents": ["application/pdf", "application/msword", "application/vnd.ms-excel", "application/vnd.ms-powerpoint", "text/plain"],
    "Music": ["audio/mpeg", "audio/x-wav", "audio/ogg", "audio/flac"],
    "Archives": ["application/zip", "application/x-rar-compressed", "application/x-tar", "application/x-gzip"],
    "Others": []
}
```

## Contributing
Contributions are welcome! Feel free to fork the repository, create pull requests, and suggest improvements.

## Acknowledgments
- Inspired by the need to organize files efficiently.
- Special thanks to the creators of the `python-magic` and `tqdm` libraries for MIME type identification and progress tracking.
