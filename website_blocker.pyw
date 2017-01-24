#For anyone wants to use this script, pls check where your hosts file locates, the host_path I used is the usual location where the hosts file should be located
#Besides, for any websites you would like to block for any reason, pls modify the website_list
#the time that you want to block those websites, pls set them in the very first if-statement as the one below is saying
#"block those website from 8 am to 1 pm"
#Lastly, This script is made for practice purpose, and it is not completely finished since it lacks of a functionality that
#once exit the script in task manager, the hosts file should be rewritten to be the original one which does not contain any
#websites to block
import time
from datetime import datetime as dt
host_path="C:\Windows\System32\drivers\etc\hosts"
host_temp="hosts"
redirect="127.0.0.1"
website_list=["www.google.com","facebook.com","www.twitter.com","twitter.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,13):
        print("Work hours!")
        with open(host_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()  #each line in the file will be stored in a list
            file.seek(0) #place the pointer to the first character of the file content
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()

        print("Happy hours!")
    time.sleep(3)

#Remove all lines that contained websites_list objects in the host file in order to
#recover the host file back to the unmodified one
