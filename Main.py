from cgitb import html
from sre_compile import MAXCODE
import sys
import subprocess
import os
import requests

savePath = ""


with open(r"C:\Users\Zohaib\Desktop\Log.txt", "w") as f:
    f.write("Debug Statements \n\n")
    

with open(r"C:\Users\Zohaib\Desktop\Pics.txt", "r") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    savePath = lines[0]
    lines.pop(0)    
    
       
nameNum = 1
from os import listdir
from os.path import isfile, join
files = [f for f in listdir(savePath) if isfile(join(savePath, f))]
for fileName in files:
    if int(fileName[:-4]) >= nameNum:
        nameNum =  int(fileName[:-4])+1



with open(r"C:\Users\Zohaib\Desktop\Log.txt", "a") as file:
    counter =0
    for x in lines:
        file.write(x + "\n")
        tempRet = "https://i.pinimg.com/564x/2b/a3/ea/2ba3eaf1401ceec39b2fd98f8a39f278.jpg"
        maxcount = 0
        while tempRet == "https://i.pinimg.com/564x/2b/a3/ea/2ba3eaf1401ceec39b2fd98f8a39f278.jpg":
            htmlCode = requests.get(url = x).text
            print(htmlCode.find("https://i.pinimg.com/564x"))
            halfCode = htmlCode[htmlCode.find("https://i.pinimg.com/564x"):]   
            imageURL = halfCode[:halfCode.find(".jpg")+4]
            tempRet = imageURL
            maxcount = maxcount +1
            if maxcount > 30:
                file.write("Pinterest displays wrong image when scraping URL beyond 30 trycount. Please")
                break
            
        saveName = str(nameNum) +".png"
        saveName = savePath+saveName
        img_data = requests.get(imageURL).content
        with open(saveName, 'wb') as handler:
            handler.write(img_data)
        nameNum = nameNum+1
        

with open(r"C:\Users\Zohaib\Desktop\Pics.txt", "w") as f:
    f.write(savePath)
        
