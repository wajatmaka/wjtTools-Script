#SEND SMS 

Send sms for gsm serial utils  wavecom/modempool device 
version : python2.7

###How To Use?
Install depends
> pip install -r requirements.txt

Usage 
Sending SMS
> python2.7 send.wjt /dev/ttyUSB0 081375799611 "kirim pesan"


USSD Request
> python2.7 ussd.wjt /dev/ttyUSB0 '*888#'
