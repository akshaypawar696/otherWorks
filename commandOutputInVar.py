import os
import subprocess
what = ['python3','mongo','pip','pip3','gcc','npm','node','virtualenv','conda','mysql','sqlite3']

havekey = []
havevalue = []
havedict = {}
nothave = []
def checkingVersions(tool):
	try:
		pythonVcheck = os.system("{} --version".format(tool))
	except:
		pass

	if pythonVcheck == 0:
		p = subprocess.Popen("{} --version".format(tool),stdout=subprocess.PIPE, shell=True)		
		(o,e) = p.communicate()
		havekey.append(tool)
		havevalue.append(o)
	else:
		nothave.append(tool)
			
for i in what:
	checkingVersions(i)
havedict = dict(zip(havekey, havevalue))

print("nothave --->",nothave)




for key,value in havedict.items():
	print(key)
	print(value)
	print("**************************************************************")






