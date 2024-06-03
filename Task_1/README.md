### USER GUIDE
#### Launch
    python3 main.py [-h] [--human | --inode]

#### Argument Description
- --human - Execute and parse linux system command "df -h";
- --inode - Execute and parse linux system command "df -i";
- In case of no options execute "df".

#### Output
Output JSON dict to stdout with the following keys:
- "status": "success" | "failure"
- "error": "<error message>" | "None"
- "result": "None" or dictionary with the following keys: 
    - In case of "df -h": [Filesystem, Size, Used, Avail, Use%, Mounted on]
    - In case of "df -i": [Filesystem, Inodes, IUsed, IFree, IUse%, Mounted on]
    - In case of "df": [Filesystem, 1K-blocks, Used, Available, Use%, Mounted on]

#### Requirements
Utility use ***python 3.6.x***, ***json***, ***subprocess.Popen***, ***argrapse***;
Utility is written according to OOP principles:
- Separate class for executors with base class;
- Separate class for parsers with base class;
- Executor classes encapsulate parser classes;

All code is covered by unittests (using framework ***unittest***).

