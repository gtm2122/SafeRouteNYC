import re
import numpy
crime = ["haha","bahaha","crimson"]
st = "I am inside of your bahahaha and also bahahaha crimson"
idx=[]
for j in crime:
	for i in re.finditer(j , st):
		idx.append(i.start())
idx = numpy.sort(idx)
print idx		
	#i+=st.find(i)
#if crime in st:print "ok"
