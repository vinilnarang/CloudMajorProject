import os,sys

def didItWork():
	temp=raw_input('Y/N : ')
	if temp=='Y' or temp=='y':
		return
	elif temp=='N' or temp=='n':
		sys.exit()
	else:
		didItWork()

#STOPPING ALL SERVICES
didItWork()
print "*****************************STOPPING ALL SERVICES**********************************"
os.system("bash stop1.sh")
os.system("bash stop2.sh")
os.system("sudo service zookeeper-server stop")
os.system("bash stop3.sh")

#STARTING ALL SERVICES
didItWork()
print "*****************************STARTING ALL SERVICES**********************************"
os.system("bash start1.sh")
os.system("bash start2.sh")
os.system("sudo service zookeeper-server start")
os.system("bash start3.sh")
