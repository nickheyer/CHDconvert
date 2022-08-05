# CHDconvert
Converts directories containing ".7z" files into ".chd" files, usually for purposes of console emulation.

# Requirements
[`Python`](https://www.python.org/downloads/)

# Installation

Clone CHDconvert
```
git clone https://github.com/nickheyer/CHDconvert
```
Change Directory to where you cloned repo (in previous step)
```
cd C:\Where\you\cloned\this\repo
```
Install Requirements
```
pip install -r requirements.txt
```

# Usage
Examples:

- Simply run it, and provide the folder path when it asks for it.
  ```
  python.exe .\chdconvert.py
  ```
  Converts every .7z file in given path to chd. Extracts first, outputs to folder name + "_tmp", then converts and output to folder     name + "_out"
  
- Provide a folder path as an arg
  ```
  python.exe .\chdconvert.py C:\Where\the\7zip\files\live
  ```
  Does the same as the above

- Provide the delete arg
  ```
  python.exe .\chdconvert.py C:\Where\the\7zip\files\live --delete
  ```
  Same as above, except it deletes the intermediary "folder_tmp" directory

# Shoutouts
Thanks CHDMAN! 
