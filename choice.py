import os
print (
"""
----------------------------------------------------
Linux Menu based projects - Run any command of linux
----------------------------------------------------
1.Date command
2.Cal Command
3.Ifconfig
4.ls
"""
)
choice = input("Enter your choice:")
if choice == "1" :
    user = input ("Enter username:")
    ip = input ("Enter your remote:")
    os.system (f" ssh {user}@{ip} date")
elif choice == "2" :
    user = input ("Enter username:")
    ip = input ("Enter your remote:")
    os.system (f" ssh {user}@{ip} cal")
elif choice == "3" :
    user = input ("Enter username:")
    ip = input ("Enter your remote:")
    os.system (f" ssh {user}@{ip} ifconfig")
elif choice == "4" :
    user = input ("Enter username:")
    ip = input ("Enter your remote:")
    os.system (f" ssh {user}@{ip} ls")