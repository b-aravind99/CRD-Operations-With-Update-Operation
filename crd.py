import time
import json
import threading
from threading import *

with open('E:/data.json') as f:
	file = json.load(f)
	f.close()


def newKeyValue(key,value,ttl=0):
	if key in file:
		print("Error:Please Check, key already exists !!!")
	else:
		if(key.isalpha()):
			if len(file)<(1024*1024*1024) and value<=(16*1024):
				if(ttl==0):
					temp = [value,ttl]
				else:
					temp = [value,ttl+time.time()]
				if len(key)<=32:
					file[key] = temp
					print("Successfully added the key:"+key)
			else:
				print("Error:Either the file size exceeded or value size is more than the allowed size !!!")
		else:
			print("Error:Check the 'key' name,its invalid and should contain only alphabets !!!")


def readKey(key):
	if key not in file:
		print("Error:Invalid key, key not present in the file !!!")
	else:
		temp = file[key]
		if temp[1] == 0:
			obj = str(key)+":"+str(temp[0])
			return obj
		else:
			if time.time() < temp[1]:
				obj = str(key)+":"+str(temp[0])
				return obj
			else:
				print("Error:The time to live of the key has expired !!!")


def deleteKey(key):
	if key not in file:
		print("Error:Invalid key, key not present in the file !!!")
	else:
		temp = file[key]
		if temp[1] != 0:
			if time.time() < temp[1]:
				del file[key]
				print(key," deleted successfully !!!")
			else:
				print("Error:The time to live of the key -",key," has expired !!!")
		else:
			del file[key]
			print(key," deleted successfully !!!")


def updateValue(key,value):
	temp = file[key]
	if(temp[1]!=0):
		if time.time() < temp[1]:
			if key not in file:
				print("Error:Invalid key, key not present in the file !!!")
			else:
				newTemp = []
				newTemp.append(value)
				newTemp.append(temp[1])
				file[key] = newTemp
		else:
			print("Error:The time to live of the key -",key," has expired !!!")
	else:
		if key not in file:
			print("Error:Invalid key, key not present in the file !!!")
		else:
			newTemp = []
			newTemp.append(value)
			newTemp.append(0)
			file[key] = newTemp


with open('E:/data.json','w') as f:
     json.dump(file,f)  
     f.close()	