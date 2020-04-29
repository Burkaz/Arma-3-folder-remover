import os
import getpass
import time
import shutil

username = getpass.getuser()
print ("Hello " + (username))
print ("Starting the proccess of removing files!")

filepath = os.path.expanduser(os.getenv('USERPROFILE'))+'\\Documents\\Arma 3'
shutil.rmtree(filepath)
print("Removed " + filepath)
time.sleep(2)
filepath = os.path.expanduser(os.getenv('USERPROFILE'))+'\\Documents\\Arma 3 - Other Profiles'
shutil.rmtree(filepath)
print("Removed " + filepath)
time.sleep(2)
filepath = os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Arma 3'
shutil.rmtree(filepath)
print("Removed " + filepath)
time.sleep(2)
filepath = os.path.expanduser(os.getenv('USERPROFILE'))+'\\AppData\\Local\\Arma 3 Launcher'
shutil.rmtree(filepath)
print("Removed " + filepath)
time.sleep(2)
print("All done! Don't forget to change your IP or get a VPN to join the server you were banned on!")