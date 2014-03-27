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

The script has two options:

- Verbose output
- Ability to specify the username to use to login

To run with verbose output:

```
python checkcsil.py -v
```

To run with a specific username:

```
python checkcsil.py USERNAME
```

To run with both options:

```
python checkcsil.py -v USERNAME
```

To show a help menu:

```
python checkcsil.py -h
```
