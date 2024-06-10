## USER GUIDE
### Usage
---
    main.py [-h] (--pass PASSWORD | --file FILE_NAME) --user USER --host HOST

**options:**
-  -h, --help        show this help message and exit
-  --pass PASSWORD   password
-  --file FILE_NAME  file name with password
-  --user USER       user name
-  --host HOST       host (ip address)

### Output
---
The result of the command is the following structure:

```
{
    'error': str('Description of error if exists'),
    'result': 'json with hostnames, IPs, Interval, Transfer, Bandwidth',
    'status': int('0 in case of success and ANY in all other cases')
}
```

### Requirements
---
Utility use:
- ***python 3.6.8***;
- ***json***;
- ***subprocess.Popen***;
- ***argrapse***;
- ***iperf3***;
- ***pgrep***

At the end of the utility execution, the server shutdown is monitored ***iperf3*** after finishing measurements.

Also, for all modules of the application ***Unit tests*** is written.
