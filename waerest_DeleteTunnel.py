import urllib
import urllib2
import json
from pprint import pprint

BaseURL = 'http://10.75.158.171:7777/wae'

#### A POST API call to query a demand between 2 nodes ###
OnDemandQueryURL = BaseURL+'/network/modeled/entities/tunnel/delete/byName'

#### GetAdmitRecordsRequest element in JSON format  ###
DeleteTunnel = {
  "srcNode" : "PE1",
  "tunnelName" : "te_176",
  "removeEros" : "false"
}

## main ##

#### Create REST API request with input in JSON format  ###
req = urllib2.Request(OnDemandQueryURL, json.dumps(DeleteTunnel), {'Content-Type': 'application/json'})

#### Make REST Request  ###
u = urllib2.urlopen(req)

#### Parse the Response sent in JSON format  ###
resp = json.loads(u.read().decode('utf-8'))


#### Render the Response  ###
pprint(resp)
