CheckCSIL
---------

A tiny Python script to check the UCSB CSIL for available workstations.

### Features

- Connects via SSH to each CSIL workstation and runs `who` to find out if there are users logged in
- Outputs the first server which is available

### Requirements

- [Python 3](http://www.python.org)
- [Paramiko](https://github.com/paramiko/paramiko)

### Instructions

- To run: `python checkcsil.py`