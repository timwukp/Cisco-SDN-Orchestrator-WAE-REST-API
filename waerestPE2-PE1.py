import urllib
import urllib2
import json
from pprint import pprint

BaseURL = 'http://10.75.158.171:7777/wae'

#### A POST API call to query a demand between 2 nodes ###
OnDemandQueryURL = BaseURL+'/demand/on-demand/query/node-to-node'

#### GetAdmitRecordsRequest element in JSON format  ###
GetAdmitRecordsRequest = {
  "admissionPlan" : "COMPOUND",
  "demands" : [ {
    "endpoints" : {
      "source" : {
        "name" : "PE2"
      },
      "destination" : {
        "name" : "PE1"
      }
    },
    "bandwidth" : 15
  } ]
}

## main ##

#### Create REST API request with input in JSON format  ###
req = urllib2.Request(OnDemandQueryURL, json.dumps(GetAdmitRecordsRequest), {'Content-Type': 'application/json'})

#### Make REST Request  ###
u = urllib2.urlopen(req)

#### Parse the Response sent in JSON format  ###
resp = json.loads(u.read().decode('utf-8'))


#### Render the Response  ###
pprint(resp)
