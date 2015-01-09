import urllib
import urllib2
import json
from pprint import pprint

BaseURL = 'http://10.75.158.171:7777/wae'

#### A POST API call to query a demand between 2 nodes ###
OnDemandQueryURL = BaseURL+'/demand/calendared/get-demands/in-span/node-to-node'

#### JSON format  ###
####Gets list of persistent admitted demands between srcNode and dstNode in specified period of time. If only start of the period is specified, it will return demands that span only single timestamp#########
Getjoblist = {
  "periodStart" : 1410796800,
  "source" : "PE1",
  "periodEnd" : 1410804000,
  "destination" : "PE2"
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
