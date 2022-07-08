import subprocess
import os
from termcolor import colored

# Clearing Screen.
os.system('cls')

print(colored("""[\tScript Author: Akash Pandey\n\tGithub: https://github.com/1337-L3V1ATH0N/\t]""","white"))
with open('Audit.txt','w') as file:
    file.write("\tScript Author: Akash Pandey\n")
    file.write("\tGithub: https://github.com/1337-L3V1ATH0N/\n\n")
    file.close()
    
# Finding hostname.
print(colored("\n\n== HOSTNAME ==\n","yellow"))
hostname=subprocess.check_output(['hostname'],shell=True,text=True).split('\n')
print(hostname[0])
with open('Audit.txt','a') as file:
    file.write(str("\n== HOSTNAME ==\n\n"+ hostname[0]+"\n"))
    file.close()
    
# Checking Server Type.
print(colored("\n== Server Version ==\n","yellow"))
OS=subprocess.check_output(['cmd.exe','/c','systeminfo'],shell=True,text=True).split('\n')
with open('Audit.txt','a') as file:
        file.write("\n== Server Version ==\n\n")
        file.close()
for osname in OS[2:4]:
    print(osname)
    with open('Audit.txt','a') as file:
        file.write(osname+'\n')
        file.close()
        
# Checking for IP Address.
print(colored("\n== IPv4 Addresses ==\n","yellow"))
ipconfig=subprocess.check_output(['cmd.exe','/c','ipconfig','|','findstr','/i','IPv4'],shell=True,text=True).split('\n')
with open('Audit.txt','a') as file:
    file.write("\n== IPv4 Addresses ==\n\n")
    file.close()
for ip in ipconfig:
    print(ip)
    with open('Audit.txt','a') as file:
        file.write(ip+"\n")
        
# Checking if Server is in Domain or Workgroup.
print(colored("\n== Checking for Domain Name ==\n","yellow"))
with open('Audit.txt','a') as file:
    file.write("\n== Checking for Domain Name ==\n\n")
    file.close()
for domain in OS:
    if "Domain:" in domain:
        print(colored(domain,"white"))
        with open('Audit.txt','a') as file:
            file.write(domain+"\n")
            file.close()
    else:
        pass
    
# Checking if Server is Physical or Virtual.
print(colored("\n== Checking if Server is Physical or Virtual ==\n","yellow"))
with open('Audit.txt','a') as file:
    file.write("\n== Checking if Server is Physical or Virtual ==\n\n")
    file.close()
for srvtype in OS:
    if "System Manufacturer:" in srvtype:
        with open('Audit.txt','a') as file:
            file.write(srvtype+"\n")
            file.close
    elif "System Model:" in srvtype:
        with open('Audit.txt','a') as file:
            file.write(srvtype+"\n")
            file.close()
    else:
        pass
    
# Checking if PowerShell is blocked.
print(colored("\n== Checking for PowerShell ==\n","yellow"))
with open('Audit.txt','a') as file:
    file.write("\n== Checking for PowerShell ==\n\n")
    file.close()
#print(colored("[Note] While checking for powershell if cmd gets stucked then PowerShell isn't blocked.","white"))
try:
    subprocess.check_output('powershell.exe -c exit',shell=True)
    print(colored("[!] PowerShell is not blocked.","red"))
    with open('Audit.txt','a') as file:
        file.write("[!] PowerShell is not blocked.\n")
        file.close()
    pass
except subprocess.CalledProcessError as err:
    print(colored("[+] PowerShell is blocked.","green"))
    with open('Audit.txt','a') as file:
        file.write("[+] PowerShell is blocked.\n")
        file.close()
    pass

# Checking for Drives & NTFS filesystem.
print(colored("\n== Checking for Drives & FileSystem==\n","yellow"))
with open('Audit.txt','a') as file:
    file.write("\n== Checking for Drives & NTFS Filesystem ==\n\n")
    file.close()
filesystem=subprocess.check_output(['wmic','logicaldisk','get','caption,','filesystem'],shell=True,text=True).split('\n')
for drives in filesystem:
    with open('Audit.txt','a') as file:
        file.write(drives+"\n")
        file.close()
        
# Checking for Users with Admin rights.
print(colored("\n== Checking for Users with Admin rights ==\n","yellow"))
print("\n[Note] : On System level\n")
with open('Audit.txt','a') as file:
    file.write("\n== Checking for Admin rights ==\n[Note]: On System level\n\n")
    file.close()
admin=subprocess.check_output(['net','localgroup','Administrators'],shell=True,text=True).split('\n')
for user in admin[7:]:
    if user==' ' or user=='' or user=='The command completed successfully.':
        pass
    else:
        print(user)
        with open('Audit.txt','a') as file:
            file.write(user+"\n")
            file.close()

# Checking for System Patches.
print(colored("\n== Checking for Security Patches ==\n","yellow"))
with open('Audit.txt','a') as file:
    file.write("\n== Checking for System Patches ==\n\n")
    file.close()
patches=subprocess.check_output(['wmic','qfe','get','Description,','HotFixID,','InstalledOn,','InstalledBy'],shell=True,text=True).split("\n")
for patch in patches:
    print(patch)
    with open('Audit.txt','a') as file:
        file.write(patch+"\n")
        file.close()

# Checking for Password Policy
print(colored("\n== Checking Password Policy for Current User on Domain level ==\n","yellow"))
with open('Audit.txt','a') as file:
    file.write("\n== Checking Password Policy for Current User on Domain level ==\n\n")
    file.close()
try:
    passw=subprocess.check_output(['net','user','%username%','/domain'],shell=True,text=True).split('/n')
    for data in passw:
        print(colored(data,"green"))
        with open('Audit.txt','a') as file:
            file.write(data)
            file.close()
except subprocess.CalledProcessError:
    print(colored("[!] System is not connected to a Domain","red"))
    with open('Audit.txt','a') as file:
        file.write("[!] System is not connected to a Domain.")
        file.close()
        
# Checking if User arcsight is created or if server is configured with SIEM.
print(colored("\n== Checking for SIEM LogShipping through user ARCSIGHT ==\n","yellow"))
with open('Audit.txt','a') as file:
    file.write("\n== Checking for SIEM LogShipping through user ARCSIGHT ==\n\n")
    file.close()
users=subprocess.check_output(["net","localgroup","administrators"],shell=True,text=True).split('\n')
for user in users:
    if "arcsight" in user:
        print(colored("[+] System is configured for SIEM LogShipping.","red"))
        with open('Audit.txt','a') as file:
            file.write("\n[+] System is configured for SIEM LogShipping.\n\n")
            file.close()
        break
    else:
        print(colored("[!] System is not configured for SIEM LogShipping.","green"))
        with open('Audit.txt','a') as file:
            file.write("[!] System is not configured for SIEM LogShipping.\n")
            file.close()
        break
            
# Checking for System End-Of-Life.
print(colored("\n== Checking for System End-Of-Life ==\n","yellow"))
with open('Audit.txt','a') as file:
    file.write("\n== Checking for System End-Of-Life ==\n\n")
    file.close()
for osname in OS[2:4]:
    if "Microsoft Windows 2008" in osname:
        print(colored("[!] Server is Unsupported.","red"))
        with open('Audit.txt','a') as file:
            file.write("[!] Server is Unsupported.\n")
            file.close()
        break
    else:
        print(colored("[+] Server Seems to be Up-To-Date.","green"))
        with open('Audit.txt','a') as file:
            file.write("[!] Server Seems to be Up-To-Date.\n")
            file.close()
        break

# Checking for Windows License Key.

print(colored("\n== Checking for License Key ==\n","yellow"))
with open('Audit.txt','a') as file:
    file.write("\n== Checking for License Key ==\n\n")
    file.close()
key=subprocess.check_output(['wmic','path','softwarelicensingservice','get','oa3xoriginalproductkey'],shell=True,text=True).split(" ")
print(colored("[Note] If nothing returns then Windows is not Activated.","white"))
for lic in key[9:10]:
    print(lic)
    with open('Audit.txt','a') as file:
        file.write(lic)
        file.close()
