import urllib
import urllib2
import json
from pprint import pprint

while True:

    BaseURL = 'http://10.75.158.171:7777/wae'

    #### A POST API call to query all node details ###
    OnDemandQueryURL = BaseURL+'/network/modeled/entities/node/get-all-nodes'

    #### Make REST Request  ###
    u = urllib2.urlopen(OnDemandQueryURL)

    #### Parse the Response sent in JSON format  ###
    resp = json.loads(u.read().decode('utf-8'))



    #### Render the Response  ###
    pprint(resp)

    YesOrNo=raw_input('Do you want to search again?(Y/N): ')
    if YesOrNo=='N':
     print('Bye-bye')
     break
    
