![version](https://img.shields.io/badge/version-1.2.0-success)
# mydea
A basic thought-catching program

# Idea storage
Ideas are stored in a .txt file in the working directory. There is no fixed location.

## Add bash command (mydea example)
This assumes py_idea.py has been placed in /usr/bin.
Run `alias mydea="/usr/bin/py_idea.py"`

### If you don't use Linux
If you have python, you can just run the python script in the command line by using `python3 py_idea.py` or `python py_idea.py`

# 1.2.0 Release Notes
- One file can be used by running the script from anywhere without creating a new file per working directory.
- A simple '.imi' configuration file is used to store the path of the file used for ideas and the value of the silent mode setting.
- The file that is used for ideas can be set to any path from the script (type p).
- Code cleaned up.
