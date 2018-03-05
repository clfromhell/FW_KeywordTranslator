import os
import ConfigParser
import sys
from datetime import datetime
from shutil import copyfile

cp = ConfigParser.SafeConfigParser()

loc_dir = os.path.dirname(os.path.realpath(__file__))
cfg = loc_dir + "\\Settings.cfg"
Dictionary = loc_dir + "\\Stichw.csv"

cp.read(cfg)
#print "Using Configfile: " + cfg

ts = datetime.strftime(datetime.today(),"%d-%m-%Y--%H-%M-%S")

try:	
	for root, dirs, files in os.walk(loc_dir + "\\Temp"):
		for file in files:
			f = file

	fax = open(loc_dir + "\\Temp\\" + str(f), 'r')

	t = fax.read()

	with open(Dictionary, 'r') as d:
		next(d)
		for line in d:
			arrline = line.split(";")
			if arrline[0] in t:
				ov = arrline[0]
				nv = arrline[2]
				#print ov + " -> " + nv
				t = t.replace(ov, nv)
				
			del arrline[:]

	nf = open(str(cp.get("Allgemein", "Ziel")) + "\\" + ts + ".txt", 'w')
	nf.write(t)
	nf.close()
	
	fax.close()
	
except:
	try:
		copyfile(t, str(cp.get("Allgemein", "Ziel")) + "\\" + ts + ".txt")
	except:
		pass
	
	pass

try:
	os.remove(root + "\\" + f)
except:
	pass
	
sys.exit(0)

