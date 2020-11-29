print("Coded by mr4fx")
print("Split Mail list Master is now for your assist :D")
print("include your txt Mail list Inside Folder of Script and Lets Roll... !!!")
import sys
import time
import os
import re
import random
name = input("Type your Mail list Name .txt: ")
num_lines = sum(1 for line in open(name))
time.sleep(4)
print("Lets start work...........")
x = open(name, "r")

print(x)
all_of_it = x.read()
print(all_of_it)
time.sleep(11)
print("Mail list Success!!")
time.sleep(2)
print("Get domains :D Wait.....")
with open(name, "r") as f:
    trmat = re.findall(r'@.*', all_of_it)
    time.sleep(4)
    print(trmat)
time.sleep(20)
wow = random.choice(trmat)
file = open(name, "r")
for i in range(1,50):
        wow = random.choice(trmat)
        tbonz = ".*" + wow
        nam = wow + ".txt"
        print(tbonz)
        time.sleep(2)
        print("Please waitng ....")
        tbonzz = re.findall(tbonz, all_of_it)
        print(tbonzz)
        time.sleep(3)
        zab = tbonz + ".txt"
        f = open(nam,'w')
        f.write(str(tbonzz))
        f.close()
        time.sleep(6)
