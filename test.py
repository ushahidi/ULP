import base64, json, urllib2

auth = 'Basic ' + base64.b64encode('user:pass')

def api(url):
	print url
	request = urllib2.Request(url)
	request.add_header('Authorization', auth)
	try:
		return json.load(urllib2.urlopen(request))
	except:
		pass

for project in ['riverid', 'smssync']:
	for resource in api('http://www.transifex.net/api/2/project/%s/resources/' % project):
		for language in api('http://www.transifex.net/api/2/project/%s/resource/%s/?details' % (project, resource['slug']))['available_languages']:
			print api('http://www.transifex.net/api/2/project/%s/resource/%s/stats/%s/' % (project, resource['slug'], language['code']))
