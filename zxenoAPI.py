import sys
import re
import json
import urllib
file = urllib.urlopen("http://xenotium.pl/workshop/index.php/api/trm/stations/format/json")
f = file.read()
data = json.loads(f)
print data['1']
#print data[1]
for i in range(1,len(data)):
	print data[str(i)]
