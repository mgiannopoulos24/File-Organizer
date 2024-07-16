# File Organizer CLI Tool
This command-line interface (CLI) tool organizes files in a specified directory based on their types. It uses the `magic` library to identify file types by content, allowing for accurate categorization even when file extensions are unreliable.

## Features
- **Automatic File Categorization:** Files are categorized into directories such as Images, Videos, Documents, Music, Archives, and Others based on their MIME types.
- **Flexible and Customizable:** Easily customizable to add more categories or modify existing ones in the organizer.py script.
- **Command-Line Interface:** Simple to use directly from the command line with Python.
## Requirements
- Python 3.x
- `python-magic` library 

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

## Example
Suppose you have a directory `~/Downloads` with various files:

```console
User@Github:~$ ll ~/Downloads/
total 5316
drwxr-xr-x  2 dwish dwish    4096 Jul 17 01:16  ./
drwxr-x--- 21 dwish dwish    4096 Jul 17 01:11  ../
-rw-r--r--  1 dwish dwish   20480 Jul 16 02:53  archive.zip
-rw-r--r--  1 dwish dwish 2689704 Jul 17 01:14  audio.mp3
-rw-r--r--  1 dwish dwish    1965 Jul 17 01:11  document.pdf
-rw-r--r--  1 dwish dwish    1781 Nov 30  2023  photo.jpg
-rw-r--r--  1 dwish dwish      74 Jul 17 01:14  script.sh
-rw-r--r--  1 dwish dwish 2689704 Jul 17 01:14  video.mp4
```

Running the organizer tool:

```console
python3 organizer.py ~/Downloads
```

After running, your directory structure will look like this:

```console
User@Github:~$ ll ~/Downloads/
total 32
drwxr-xr-x  8 dwish dwish 4096 Jul 17 01:18 ./
drwxr-x--- 21 dwish dwish 4096 Jul 17 01:17 ../
drwxr-xr-x  2 dwish dwish 4096 Jul 17 01:18 Archives/
drwxr-xr-x  2 dwish dwish 4096 Jul 17 01:18 Documents/
drwxr-xr-x  2 dwish dwish 4096 Jul 17 01:18 Images/
drwxr-xr-x  2 dwish dwish 4096 Jul 17 01:18 Music/
drwxr-xr-x  2 dwish dwish 4096 Jul 17 01:18 Others/
drwxr-xr-x  2 dwish dwish 4096 Jul 17 01:18 Videos/
```

## Contributing
Contributions are welcome! Feel free to fork the repository, create pull requests, and suggest improvements.

## Acknowledgments
- Inspired by the need to organize files efficiently.
- Special thanks to the creators of the `python-magic` library for MIME type identification.