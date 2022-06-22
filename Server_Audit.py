import subprocess
import os
from termcolor import colored

# Clearing Screen.

os.system('cls')

print(colored("""[\tScript Author: Akash Pandey\n\tGithub: https://github.com/1337-L3V1ATH0N/\t]""","white"))

# Finding hostname.
print(colored("\n== HOSTNAME ==\n","yellow"))
os.system('cmd.exe /c hostname')

# Checking Server Type.

print(colored("\n== Server Version ==\n","yellow"))
OS=subprocess.check_output(['cmd.exe','/c','systeminfo'],shell=True,text=True).split('\n')
for osname in OS[2:4]:
    print(osname)

# Checking for IP Address.

print(colored("\n== IPv4 Addresses ==\n","yellow"))
ipconfig=subprocess.check_output(['cmd.exe','/c','ipconfig','|','findstr','/i','IPv4'],shell=True,text=True).split('\n')
for ip in ipconfig:
    print(ip)

# Checking if Server is in Domain or Workgroup.
print(colored("\n== Checking for Domain Name ==\n","yellow"))
for domain in OS:
    if "Domain:" in domain:
        print(colored(domain,"white"))
    else:
        pass
    
# Checking if Server is Physical or Virtual.

print(colored("\n== Checking if Server is Physical or Virtual ==\n","yellow"))
for srvtype in OS:
    if "System Manufacturer:" in srvtype:
        print(srvtype)
    elif "System Model:" in srvtype:
        print(srvtype)
    else:
        pass

# Checking for Drives & NTFS filesystem.
print(colored("\n== Checking for Drives & FileSystem==\n","yellow"))
os.system('wmic logicaldisk get caption, filesystem')

# Checking for Users with Admin rights.
print(colored("\n== Checking for Users with Admin rights ==\n","yellow"))
print("\n[Note] : On System level\n")
admin=subprocess.check_output(['net','localgroup','Administrators'],shell=True,text=True).split('\n')
for user in admin[7:]:
    if user==' ' or user=='' or user=='The command completed successfully.':
        pass
    else:
        print(user)

# Checking for System Patches.
print(colored("\n== Checking for Security Patches ==\n","yellow"))
os.system('wmic qfe get Description, HotFixID, InstalledOn, InstalledBy')

# Checking for Password Policy
print(colored("\n== Checking Password Policy for Current User on Domain level ==\n","yellow"))
try:
    passw=subprocess.check_output(['net','user','%username%','/domain'],shell=True,text=True).split('/n')
    for data in passw:
        print(colored(data,"green"))
except subprocess.CalledProcessError:
    print(colored("[!] System is not connected to a Domain","red"))

# Checking if User arcsight is created or if server is configured with SIEM.
print(colored("\n== Checking for SIEM LogShipping through user ARCSIGHT ==\n","yellow"))
users=subprocess.check_output(["net","users"],shell=True,text=True).split('\n')
for user in users:
    if "arcsight" not in user:
        print(colored("[!] System is not configured for SIEM LogShipping.","red"))
        break
    else:
        print(colored("[+] System is configured for SIEM LogShipping.","green"))
# Checking for System End-Of-Life.
print(colored("\n== Checking for System End-Of-Life ==\n","yellow"))
for osname in OS[2:4]:
    if "Microsoft Windows 2008" in osname:
        print(colored("[!] Server is Unsupported.","red"))
        break
    else:
        print(colored("[+] Server Seems to be Up-To-Date.","green"))
        break

# Checking if PowerShell is blocked.
print(colored("\n== Checking for PowerShell ==\n","yellow"))
print(colored("[Note] While checking for powershell if cmd gets stucked then PowerShell isn't blocked.","white"))
try:
    subprocess.check_output('powershell.exe 2>nul',shell=True)
    print(colored("[!] PowerShell is not blocked.","red"))
    pass
except subprocess.CalledProcessError as err:
    print(colored("[+] PowerShell is blocked.","green"))
    pass
