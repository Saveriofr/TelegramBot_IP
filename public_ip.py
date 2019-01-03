import requests
 
r = requests.get(r'http://jsonip.com')
ip= r.json()['ip']
print 'Your IP is', ip
