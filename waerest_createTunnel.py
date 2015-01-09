import urllib
import urllib2
import json
from pprint import pprint

BaseURL = 'http://10.75.158.171:7777/wae'

#### A POST API call to query a demand between 2 nodes ###
OnDemandQueryURL = BaseURL+'/network/modeled/entities/tunnel/pcep/new/create-basic'

#### Create Tunnel in JSON format  ###
CreateTunnel = {
  "teTunnel" : {
    "name" : "te_176",
    "source" : "PE1",
    "destination" : "PE2",
    "pcep" : "true",
    "type" : "RSVP"
  }
  
}

## main ##

#### Create REST API request with input in JSON format  ###
req = urllib2.Request(OnDemandQueryURL, json.dumps(CreateTunnel), {'Content-Type': 'application/json'})

#### Make REST Request  ###
u = urllib2.urlopen(req)

#### Parse the Response sent in JSON format  ###
resp = json.loads(u.read().decode('utf-8'))


#### Render the Response  ###
pprint(resp)
