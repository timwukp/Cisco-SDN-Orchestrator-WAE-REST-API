import urllib
import urllib2
import json
from pprint import pprint

BaseURL = 'http://10.75.158.171:7777/wae'

#### A POST API call to query a demand between 2 nodes ###
OnDemandQueryURL = BaseURL+'/demand/calendared/admit/node-to-node'

#### admit tunnel element in JSON format  ###
AdmitTunnelPath = { 
  "requests" : [ { 
    "timeInterval" : { 
      "fromTime" : 1410796800, 
      "tillTime" : 1410804000 
    }, 
    "endpoints" : { 
      "source" : { 
        "name" : "PE1" 
      }, 
      "destination" : { 
        "name" : "PE2" 
      } 
    }, 
    "bandwidth" : 10, 
    "priority" : 1 
  } ], 
  "admissionPlan" : "COMPOUND" 
}
## main ##

#### Create REST API request with input in JSON format  ###
req = urllib2.Request(OnDemandQueryURL, json.dumps(AdmitTunnelPath), {'Content-Type': 'application/json'})

##### PUT method####
req.get_method = lambda: 'PUT'

#### Make REST Request  ###
u = urllib2.urlopen(req)

#### Parse the Response sent in JSON format  ###
resp = json.loads(u.read().decode('utf-8'))


#### Render the Response  ###
pprint(resp)
