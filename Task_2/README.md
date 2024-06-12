## USER GUIDE
### Usage
---
    main.py [-h] (--s_p SERVER_PASSWORD | --s_f SERVER_PASS_FILE_NAME) (--c_p CLIENT_PASSWORD | --c_f CLIENT_PASS_FILE_NAME) --s_u SERVER_USER --c_u CLIENT_USER
               --s_i SERVER_IP --c_i CLIENT_IP

**options:**    
-    -h, --help                     show this help message and exit
-    --s_p SERVER_PASSWORD          server password
-    --s_f SERVER_PASS_FILE_NAME    server file name with password
-    --c_p CLIENT_PASSWORD          client password
-    --c_f CLIENT_PASS_FILE_NAME    client file name with password
-    --s_u SERVER_USER              user name
-    --c_u CLIENT_USER              user name
-    --s_i SERVER_IP                server ip address
-    --c_i CLIENT_IP                client ip address

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
- ***pgrep***;
- ***pkill***

At the end of the utility execution, the server shutdown is monitored ***iperf3*** after finishing measurements.

Also, for all modules of the application ***Unit tests*** is written.
