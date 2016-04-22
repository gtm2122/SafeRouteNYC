import imaplib
import numpy
import email
import re
from sys import argv
crimes = ["Robbery","Theft","Assault","Other","Arrest","Vandalism","Shooting","Burglary","Arson"]
cl4 = open('mess_clean4.txt','a')
#target =open('mess_clean1.txt','a')
cl2 = open('mess_clean2.txt','a')
#cl3 = open('mess_clean3.txt','a')
M = imaplib.IMAP4_SSL('imap.gmail.com',993)
M.login('abgtm2122@gmail.com','gtmab2122')
M.select()

typ,data = M.uid('search',None,'ALL')
for num in data[0].split():
	idx_crime=[]
	
	t,d = M.fetch(num,'(RFC822)')
	if(d[0] == None):
		pass
	else:
		mess = email.message_from_string(d[0][1])
		if mess['From'] == '"spotcrime.com" <system@spotcrime.com>' :
			print num
			#print str(mess['Link'])
			p = str(mess)
			cl2.write(p)
			#print len(str(mess))
			idx_copy = p.find("Address: Columbia University,=")
			#print idx_copy
			idx_stop = p.find("unsubscribe")
			print idx_stop
			idx=0	
			p = p[idx_copy+30+25+51+74+73+1:idx_stop-130]
			for j in crimes:
				for i in re.finditer(j,p):
					idx_crime.append(i.start())
			idx_crime=numpy.sort(idx_crime)
			#print idx_crime
			for i in range(len(idx_crime)-1):
				inter_str = (p[idx_crime[i]:idx_crime[i+1]-1])
				#print inter_str
				
			
				inter_str=inter_str.replace('=','')
				inter_str=inter_str.replace('\r','')
				inter_str=inter_str.replace('\n','')
				idx_http = inter_str.find("http") -10
				#print idx_http
				print inter_str[0:idx_http]
				
				cl4.write(inter_str[0:idx_http]+'\r'+'\n')
										
cl4.close()	
								
			
'''
t,d = M.fetch(5,'(RFC822)')
print t
mess=email.message_from_string(d[0][1])
print mess
print mess['From']
#print email.utils.parseaddr(mess['To'])
#print mess.items()
'''
M.close()
M.logout()
