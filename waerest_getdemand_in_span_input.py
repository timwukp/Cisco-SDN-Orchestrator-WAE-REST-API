import urllib
import urllib2
import json
import string
import time
from pprint import pprint

periodStart = raw_input('Enter periodStart time in format DD.MM.YYYY HH:MM:SS: ')
pattern = '%d.%m.%Y %H:%M:%S'
epoch1 = int(time.mktime(time.strptime(periodStart, pattern)))
print (epoch1)

periodEnd = raw_input('Enter periodEnd time in format DD.MM.YYYY HH:MM:SS: ')
epoch2 = int(time.mktime(time.strptime(periodEnd, pattern)))
print (epoch2)

source = raw_input('Enter source name: ')

destination = raw_input('Enter destination name: ')


BaseURL = 'http://10.75.158.171:7777/wae'

#### A POST API call to query a demand between 2 nodes ###
OnDemandQueryURL = BaseURL+'/demand/calendared/get-demands/in-span/node-to-node'

#### JSON format  ###
####Gets list of persistent admitted demands between srcNode and dstNode in specified period of time. If only start of the period is specified, it will return demands that span only single timestamp#########
Getjoblist = {
  "periodStart" : epoch1,
  "source" : source,
  "periodEnd" : epoch2,
  "destination" : destination
}
## main ##

#### Create REST API request with input in JSON format  ###
req = urllib2.Request(OnDemandQueryURL, json.dumps(Getjoblist), {'Content-Type': 'application/json'})

#### Make REST Request  ###
u = urllib2.urlopen(req)

#### Parse the Response sent in JSON format  ###
resp = json.loads(u.read().decode('utf-8'))


#### Render the Response  ###
pprint(resp)
