# Automatic Paloalto Backup Configuration #

As such a title, this tools for automatic backup paloalto configuration.

## Requierment ##

* python3
* configparser
* pip3

Install Depedency
```bash
pip3 install -r requierment.txt
```


## How to Get Token Paloalto ##

How to get token
```bash
curl https://<firewall-ip>/api/?type=keygen&user=<username>&password=<password>
```

and copy paste in variable TOKEN paloalto.cfg, don't forget fill IP with ipaddress or hostname paloalto.


## How To Use? ##

```bash
python3 paloalto-backup

``` 


