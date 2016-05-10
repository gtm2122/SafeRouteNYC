import numpy as np
import time

#file = open('./NYPD_7_Major_Felony_Incidents.csv','r')
file = open('./crime_gps.txt','r')
t = time.time()
cl = open("./coord.txt",'a')



'''
for idx,line in enumerate(file):
	
	print line
	if idx >= 100000:
		idx = line.find('"(')
		idx2=line.find(')"')
		#print idx
		#print idx2
		#print line[idx+2:idx2]
		#cl.write(line[idx+2:idx2]+"\n") ##Initial loading of fixed data from NYC crime dataset
		
		#break
	
	idx1 = line.find("               ")
	idx2=line.find("\n")
	#print line[idx+15:idx2]
	cl.write(line[idx+15:idx2])
	#break
'''
for idx,line in enumerate(file):
	idx	
print (idx+1)



file1=open("./nlines.txt",'r')
t= int(file1.readlines()[0])
file1.close()
#file1=open("./nlines.txt",'a')
#cl1=open("./coord.txt",'a')
for ind,line in enumerate(file):
	if ind<idx+1 and ind>t :
		
		#file1.write(line)		
		a = line.find("               ")
	        b=line.find("\n")
		cl.write(line[a+15:b])

#file.close()
cl.close()
file1=open("./nlines.txt",'w')
file1.write(str(idx+1))
file1.close()

#print time.time()-t



#print L.shape()
