import requests
import re
import time

def decodeQR(extension):
    r = requests.get('https://zxing.org/w/decode?u=http%3A%2F%2Ftunnel.web.easyctf.com%2Fimages%2F'+extension+'.png')
    regex = re.compile("Raw text</td><td><pre>([a-zA-z0-9\{_\}]+)", re.IGNORECASE)
    return regex.findall(r.text)

#There are several breaks, use https://online-barcode-reader.inliteresearch.com/
# to handle those
curLink = 'DaicO7460493nYSuvLPW'

for i in range(1000):
    curLink = decodeQR(curLink)[0]
    print(curLink)
    time.sleep(.3)
