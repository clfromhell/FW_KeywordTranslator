import os
import ConfigParser
import sys
from datetime import datetime
from shutil import copyfile
import platform

# Workaround for compatibility issues with different operating systems
if platform.system() == 'Linux':
	dirvar = "/"
elif platform.system() == 'Windows':
	dirvar = "\\"

cp = ConfigParser.SafeConfigParser()

# Get current directory and set file paths
loc_dir = os.path.dirname(os.path.realpath(__file__))
cfg = loc_dir + dirvar + "Settings.cfg"
Dictionary = loc_dir + dirvar + "Stichw.csv"

# Read Settings.cfg
cp.read(cfg)

# Set timestamp for outfile
ts = datetime.strftime(datetime.today(),"%d-%m-%Y--%H-%M-%S")

# Check if Temp-Folder exists and if not, create the folder and exit (If there's no folder, there's also no file to be checked :-) )
if not os.path.isdir(loc_dir + dirvar + "Temp"):
	os.makedirs(loc_dir + dirvar + "Temp")
	sys.exit(0)

try:	
	
	# Walk through the Temp-Folder and get the filename
	for root, dirs, files in os.walk(loc_dir + dirvar + "Temp"):
		for file in files:
			f = file
	
	# Open the file and read it
	fax = open(loc_dir + dirvar + "Temp" + dirvar + str(f), 'r')
	t = fax.read()
	
	# Loop through the Keyword Dictionary and replace Values
	with open(Dictionary, 'r') as d:
		next(d)
		for line in d:
			arrline = line.split(";")
			if arrline[0] in t:
				ov = arrline[0]
				nv = arrline[2]
				t = t.replace(ov, nv)
				
			del arrline[:]
	
	# Create the Destination-File in the Folder specified in Settings.cfg
	nf = open(str(cp.get("Allgemein", "Ziel")) + divar + ts + ".txt", 'w')
	nf.write(t)
	nf.close()
	
	fax.close()
	
except:
	
	# If something's wrong, just copy the original File to the Destination Folder
	try:
		copyfile(t, str(cp.get("Allgemein", "Ziel")) + dirvar + ts + ".txt")
	except:
		pass
	
	pass

try:
	
	# Delete the original File if possible
	os.remove(root + dirvar + f)
except:
	pass
	
#sys.exit(0)

