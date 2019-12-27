import csv
import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import datetime
import wiringpi as pi
import time
import mcp_adc

SPI_CE = 0
SPI_SPEED = 1000000
READ_CH = 0
VREF = 3.3
adc = mcp_adc.mcp3208( SPI_CE, SPI_SPEED, VREF )
value = adc.get_value( READ_CH )

now = datetime.datetime.now()
Name = value
City = 'citycity'


fmt_name = "python-data/test_{0:%Y%m%d-%H%M%S}.csv".format(now)

with open(fmt_name,'w') as f:
    for i in range(0,50):
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([i,Name,City])
        time.sleep( 0.1 )
f.close()

print(now.date())
print(fmt_name)


gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)


f = drive.CreateFile({'title': "/{0:%Y%m%d-%H%M%S}.csv".format(now), 'mimeType': 'text/comma-separated-values'})
f.SetContentFile('%s' % fmt_name)
print('uploading files... ...')
f.Upload()

print('completed uploading files')
