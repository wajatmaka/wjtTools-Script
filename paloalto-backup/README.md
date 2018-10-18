# Automatic Paloalto Backup Configuration #

As such a title, this tools for automatic backup paloalto configuration.

## License ##
```bash
 ---------------------------------------------------------------------------------
 "THE BEER-WARE LICENSE" (Revision 42):
 <phk@FreeBSD.ORG> wrote this file.  As long as you retain this notice you
 can do whatever you want with this stuff. If we meet some day, and you think
 this stuff is worth it, you can buy me a beer or coffee in return. Dwiyan Galuh W
 ---------------------------------------------------------------------------------
 
 Created : Dwiyan Galuh W
 https://blog.wajatmaka.com
 https://github.com/wajatmaka
```
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

## Results ##
Check in your home directory
