# CHDconvert
Converts a directory containing ".gz" and ".7z" files into a directory containing ".chd" files, usually for purposes of console emulation.

# Requirements (Included with Linux/Mac)
[`Python`](https://www.python.org/downloads/)\
[`Git`](https://git-scm.com/download/win) 

# Installation
Please select either Method A or Method B to install CHDconvert.

### Method A: Clone CHDconvert
```
git clone https://github.com/nickheyer/CHDconvert
```
Change directory to where you cloned repo (in previous step)
```
cd C:\Where\you\cloned\this\repo
```
Install requirements
```
pip install -r requirements.txt
```

### Method B: Download Release
```
https://github.com/uqKami/CHDconvert/releases/latest
```
Unzip CHDconvert.7z and change directory to where you unzipped
```
cd C:\Where\you\unzipped\the\release
```
Install requirements
```
pip install -r requirements.txt
```

# Linux Additionals
Some Linux distributions can give you chdman via aptitude with the mame-tools package.
Use your distro's package/download manager to get mame-tools (for chdman).
eg. Debian-variants using apt
```
sudo apt install mame-tools
```


# Usage
Examples:

- Simply run it, and provide the folder path when it asks for it.
  ```
  python .\chdconvert.py
  ```
  Converts every .7z file in given path to chd. Extracts first, outputs to folder name + "_tmp", then converts and output to folder     name + "_out"
  
- Provide a folder path as an arg
  ```
  python .\chdconvert.py C:\Where\the\7zip\files\live
  ```
  Does the same as the above

- Provide the delete arg ("-d" or "--delete")
  ```
  python .\chdconvert.py C:\Where\the\7zip\files\live --delete
  ```
  Same as above, except it deletes the intermediary "folder_tmp" directory

- Provide the replace arg ("-r" or "--replace")
  ```
  python .\chdconvert.py C:\Where\the\7zip\files\live --replace
  ```
  Replaces the 7zip file, deleting the original as well as the intermediary files in "folder_tmp"

# Shoutouts
Thanks CHDMAN! 
