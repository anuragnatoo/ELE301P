import os
import re
import sys
def decimalToBinary(x, bits, binary):
	for i in range(bits-1,-1,-1):
		k=x>>i
		if k&1:
			binary.append("1")
		else:
			binary.append("0")


vinput=sys.argv[1]
vfilename = vinput
tbfilename=vfilename[:-2] + "_tb.v"
vcdfilename=vfilename[:-2] + ".vcd"

print(tbfilename)

vfile = open(vfilename, "r")
tbfile = open(tbfilename, "w+")

tbfile.write("`include \""+vfilename+"\"\n")
tbfile.write("module top;\n")


variableName = []
variableSize = []


for x in vfile:
	if re.findall('^\s*input',x):
		line=x
		if not x[len(x)-2]==';':
			while 1:
				l=vfile.readline()
				line=line+l
				if line[len(line)-2]==';':
					break
		tbfile.write(line.replace("input", "reg"))
		#print(re.findall('^\s*input \[(.*)\]',line))
		
		print(line)
		print(1)
		invar=[]
		line=line.replace('\n','')
		print(line)
		print(2)
		line=line.replace('	','')
		print(line)
		print(3)
		line=line.replace('     ','')
		print(line)
		print(4)
		if re.findall('^\s*input \[(.*)\]',line):
			yin= re.findall('^\s*input \[(.*)\]',line)
			zin= re.findall('^\s*input \[.*\] (.*);',line)
			print(yin)
			print(zin)
			inbit = yin[0].split(':')
			#print(inbit)
			size = int(inbit[0])-int(inbit[1]) +1
			invar = zin[0].split(',')
			#print("Input variables-",invar)
			for l in range(len(invar)):
				variableName.append(invar[l])
				variableSize.append(size)

		if re.findall('^\s*input ([^\[])',line):
			pin= re.findall('^\s*input (.*);*',line)
			print(pin)
			print(1)
			pin=pin[0].replace(';','')
			pin=pin.replace(' ','')
			pin=pin.split(",")
			print(pin)
			print(2)
			invar=pin
			print(invar)
			for i in range(len(pin)):
				variableName.append(pin[i])
				variableSize.append(1)


	
	if re.findall('^\s*output',x):
		line=x
		print(line)
		if not x[len(x)-2]==';':
			while 1:
				l=vfile.readline()
				line=line+l
				if line[len(line)-2]==';':
					break

		tbfile.write(line.replace("output","wire"))

	if re.findall('^\s*module',x):
		line=x
		if not x[len(x)-2]==';':
			while 1:
				l=vfile.readline()
				line=line+l
				if line[len(line)-2]==';':
					break

		line=line.replace('\n','')
		modname = line.replace("module ", "")
		monitorvar = line.replace("module ","")			#---------->
		if re.findall('^.*\((.*)\);',monitorvar):
			montestvar = re.findall('^.*\((.*)\);',monitorvar)

		m=montestvar[0].split(',')



modname=modname.replace("(", " m0(")
tbfile.write(modname.replace('            ',''))


tbfile.write("\ninitial begin\n")
totalSize=0
for i in range(len(variableSize)):
	totalSize=totalSize+variableSize[i]
# print(totalSize)

maxi = input("Enter maximum number of test cases")

if pow(2,totalSize) < int(maxi):
	maxr= pow(2,totalSize)
else:
	maxr= int(maxi)


for i in range(maxr):
	index=0
	if i==0:
		tbfile.write("\t")
	else:
		tbfile.write("\t#5 ")
	binaryArray=[]
	binaryArray.clear()
	decimalToBinary(i, totalSize, binaryArray)
	#print(binaryArray)
	for j in range(len(variableName)):
		check=variableSize[j]
		tbfile.write(variableName[j]+"="+str(variableSize[j])+"'b")
		while check>0:
			tbfile.write(binaryArray[index])
			index=index+1
			check=check-1
		tbfile.write(" ; ")
	tbfile.write("\n")


tbfile.write("end\n")
tbfile.write("\ninitial begin\n")
tbfile.write("$monitor ($time, \": ")

for i in range(len(m)):
	tbfile.write(m[i]+"=%b ")

tbfile.write("\"")
for i in range(len(m)):
	tbfile.write(","+m[i])
tbfile.write(");\n")

tbfile.write("$dumpfile(\""+vcdfilename+"\");\n$dumpvars;\n")

tbfile.write("end\n")

tbfile.write("\nendmodule")


vfile.close()
tbfile.close()
