# CEF messages sender

This little python script will send CEF messages to a syslog server.

The script is this small because of the great cefevent module build by Kamus Hadenes. Kudos to him!
https://github.com/kamushadenes
https://endurance.hyadesinc.com/project/cefevent/
I you are cleaver enough you could do without my script, but as my python skills aren't that great I kept this a little more straight forward.
Before you can use the script you should install his module cefevent and pysyslogclient.

```
pip install -Y cefevent,pysyslogclient
```
# Usage
```
python send_syslogs.py --host <IP address> --port <Portnumber> --proto <UDP or TCP> --number <0..9223372036854775807>
```

There is nothing much to add here
