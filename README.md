# mirror, mirror

Uses requests to check for mirrors of a site using a list of TLDs from IANA  

### Dependencies:  
requests, time(not required)

### Usage:  
Execute check.py, it automatically downloads the latest list of TLDs from https://data.iana.org/TLD/tlds-alpha-by-domain.txt  
The auto-download before each run can be removed by commenting/deleting ### lines 6-12  

### Warnings(?):
1. A lot of sites will return 200s but will not be active mirrors of the site you are looking for (used by unrelated parties)  
2. Be careful when visiting unknown sites, but if it takes someone like me to tell you that, I think you deserve to be infected by a botnet malware
