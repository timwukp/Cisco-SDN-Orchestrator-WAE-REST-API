import urllib
import urllib2
import json
from pprint import pprint

BaseURL = 'http://10.75.158.171:7777/wae'

#### A POST API call to query all node name ###
OnDemandQueryURL = BaseURL+'/network/modeled/entities/node/get-keys'

#### Make REST Request  ###
u = urllib2.urlopen(OnDemandQueryURL)

#### Parse the Response sent in JSON format  ###
resp = json.loads(u.read().decode('utf-8'))


#### Render the Response  ###
pprint(resp)
