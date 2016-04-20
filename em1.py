import imaplib
import numpy
import email
from sys import argv
cl4 = open('mess_clean4.txt','a')
#target =open('mess_clean1.txt','a')
cl2 = open('mess_clean2.txt','a')
cl3 = open('mess_clean3.txt','a')
M = imaplib.IMAP4_SSL('imap.gmail.com',993)
M.login('abgtm2122@gmail.com','gtmab2122')
M.select()
typ,data = M.uid('search',None,'ALL')
for num in data[0].split():
	idx_clean0A=[]
	idx_clean_http=[]
	t,d = M.fetch(num,'(RFC822)')
	if(d[0] == None):
		pass
	else:
		mess = email.message_from_string(d[0][1])
		if mess['From'] == '"spotcrime.com" <system@spotcrime.com>' :
			print num
			#print str(mess['Link'])
			p = str(mess)
			#print len(str(mess))
			idx_copy = p.find("Address: Columbia University,=")
			#print idx_copy
			idx_stop = p.find("unsubscribe")
			print idx_stop
			idx=0	
			p = p[idx_copy+30+25+51+74+73+1:idx_stop-130]
			while idx < len(p):
				idx_clean0A.append(p.find("=0A",idx))
				idx+=4		
					
			
			idx_clean0A = numpy.unique(idx_clean0A)
			print len(idx_clean0A)
			idx=0

			while idx<len(p):
				idx_clean_http.append(p.find("http",idx))
				idx+=5
			idx_clean_http = numpy.unique(idx_clean_http)
			print len(idx_clean_http)
			for i in range(1,len(idx_clean0A)):
				
				x=(p[idx_clean0A[i]+3:idx_clean_http[i]-1])#+"\n")
				xx = list(x)
				for i in range(len(xx)):
					if xx[i] == '=' or xx[i] =='\r' or xx[i] == '\n':
						xx[i] = ''				
					
				count = 0
				i=0
				while(1):
					if i >= len(xx):break
					if xx[i] == ' ' :
						count=count+1
					
					else : 
						count = 0
					if count>1:
						xx[i]=''
					if count>19:
						xx[i] = '\n'
					
					
					i+=1	
				i=0
				while(1):
					if i+5 >=len(xx):break
					if xx[i].isupper() and xx[i+1] == ' ' and xx[i+2] ==' ' and xx[i+3].isupper() and not(xx[i+4].isupper()) and not(xx[i+5].isupper()) :
						xx[i+2]='\n'
					if xx[i].isupper() and xx[i+1] == ' ' and xx[i+2].isupper() and not(xx[i+3].isupper()) and not(xx[i+3].isupper()) :
                                                xx[i+1]='\n'
		 	
					cl4.write(xx[i])
					i+=1
				'''
				while(1):
                                        if i+5 >=len(xx):break
                                        if xx[i].isupper() and xx[i+1] == ' ' and xx[i+2] ==' ' and xx[i+3].isupper() and not(xx[i+4].isupper()) and not(xx[i+5].isupper()):
                                                xx[i+2]='\n'
                                        if xx[i].isupper() and xx[i+1] == ' ' and xx[i+2].isupper() and not(xx[i+3].isupper()) and not(xx[i+3].isupper()):
                                                xx[i+1]='\n'

                                        cl4.write(xx[i])
                                        i+=1
 				'''	
				#while(1):
				#	if i>=len(xx):break
				#	if(xx[i]==' '):xx[i]=','
					
							
				#print xx
			#	print x.count('\n')
			#	print idx_clean0A
			#	print idx_clean_http
				#for j in len(x):
				#	if x[j] == ' ': x[j]=''
				
			cl4.close()
			cl2.close()
			cl3.close()			
			
						
	
#print data[0].split()
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
