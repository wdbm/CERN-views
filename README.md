# CERN-views

utilities for viewing CERN information

![](images/2015-08-27T1019Z_1.png)
![](images/2015-08-27T1019Z_2.png)

# quick start

```Bash
sudo pip install selenium
sudo pip install moviepy
git clone https://github.com/wdbm/CERN-views.git
cd CERN-views
wget https://raw.githubusercontent.com/wdbm/smuggle/master/smuggle.py
wget https://raw.githubusercontent.com/wdbm/shijian/master/shijian.py
```

# ACR, OPV recording

## checklist

A possible checklist before recording is as follows:

- Set the username and the passcode appropriately.
- Set the time duration of the recording. The default recording time is 1 week.

|**time**|**time in seconds**|
|---|---|
|8 hours|28800|
|10 hours|36000|
|1 day|86400|
|2 days|172800|
|3 days|259200|
|4 days|345600|
|1 week|604800|
|1 month|2629740|
|1 year|31556900|

## procedure

```Bash
./record_ACR_OPV_auto-SSO.py
./process_raw_to_tiles_ACR_OPV.py # or process_raw_to_tiles_ACR_OPV_2.py
./process_tiles_to_video_ACR_OPV_2.py
```

# OPVV-1

- OP Vistars multiplex view: <http://htmlpreview.github.io/?https://raw.githubusercontent.com/wdbm/CERN-views/master/OPVV-1.html>

# ATLAS-1

- LHC status, ATLAS status, ATLAS event display multiplex view: <http://htmlpreview.github.io/?https://raw.githubusercontent.com/wdbm/CERN-views/master/ATLAS-1.html>
