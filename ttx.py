import os

##os.mkdir('checkversion')
try:
     os.mkdir("checkversion")
except  FileExistsError:
      pass
print ('omar'*100)

os.system("cd checkversion && wget https://github.com/omarv7y/fees/blob/main/omar.txt")
s=open("checkversion/omar.txt","r")
version=s.read()
current_version=open("omar.txt","r").read()
if version!=current_version:
      os.system("rm ttx.py omar.txt && git clone https://github.com/omarv7y/fees.git")
      print("updated")
else:
      print ("No Updates")

