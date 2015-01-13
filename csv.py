import os, sys, time
csv = open(sys.argv[1])
apikey = sys.argv[2]
csvvals = csv.readlines()
for line in csvvals[72:]: #skip header
	os.system("./part.sh " + line.split(',')[0] + " " + apikey)
	value = open('value')
	try:
		data = value.readlines()[0]
	except IndexError:
		data = '"value":" "'
		
	value.close()
 	print line.strip('\n') + "," + str(data).split(':', 1)[1][1:].strip('\n')
	time.sleep(0.5)
