#This is a script owned by Lokesh Balaji. This scirpt holds MIT License.
import subprocess
subprocess.call("./master.sh",shell=True)
subprocess.call("./figlet.sh",shell=True)
option = int(input("Enter the option [0-4] :"))
if(option == 0 ):
	print( " Running Network Mapper ")
	subprocess.call("./nmap.sh",shell=True)
elif(option == 1):
	print(" Running Xerosploit ")
	subprocess.call("./xerosploit.sh",shell=True)
elif(option==2):
	print(" Running RedHawk ")
	subprocess.call("./redhawk.sh",shell=True)
elif(option==3):
	print("Running Reconspider ")
	subprocess.call("./reconspider.sh",shell=True)
elif(option==4):
	print("Running Infoga")
	subprocess.call("./infoga.sh",shell=True)
else:
	print("You have entered a wrong option. Please Reenter the correct option!")
