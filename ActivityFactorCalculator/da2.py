import os
import re
import sys
'''
To run the file in Ubuntu type python3 da2.py filename.v
The activity factor of the outputs are calculated and written in filename.txt
'''
vinput=sys.argv[1]
vfilename = vinput
tbfilename=vfilename[:-2] + ".txt"
print(tbfilename)
output_acts={}
universal_dict={}
#Dictionary to store the gate names and their probablities
vfile = open(vfilename, "r")
tbfile = open(tbfilename, "w+")
#All the inputs,outputs and wires are found and stored in invar,outvar,and wire
for x in vfile:
	#Input finding
	if re.findall('^\s*input',x):
		line=x
		if not x[len(x)-2]==';':
			while 1:
				l=vfile.readline()
				line=line+l
				if line[len(line)-2]==';':
					break
		invar=[]
		line=line.replace('\n','')
		line=line.replace('	','')
		line=line.replace('     ','')
		if re.findall('^\s*input \[(.*)\]',line):
			yin= re.findall('^\s*input \[(.*)\]',line)
			zin= re.findall('^\s*input \[.*\] (.*);',line)
			inbit = yin[0].split(':')
			size = int(inbit[0])-int(inbit[1]) +1
			invar = zin[0].split(',')

		if re.findall('^\s*input ([^\[])',line):
			pin= re.findall('^\s*input (.*);*',line)
			pin=pin[0].replace(';','')
			pin=pin.replace(' ','')
			pin=pin.split(",")
			invar=pin
			print(invar)
		input_acts={}
		for x in invar:
			print(x)
			input_acts.update({x:0.5})
			universal_dict.update({x:0.5})
	#Output calculation
	if re.findall('^\s*output',x):
		line=x
		if not x[len(x)-2]==';':
			while 1:
				l=vfile.readline()
				line=line+l
				if line[len(line)-2]==';':
					break
		outvar=[]
		line=line.replace('\n','')
		line=line.replace('	','')
		line=line.replace('     ','')
		if re.findall('^\s*output \[(.*)\]',line):
			yin= re.findall('^\s*output \[(.*)\]',line)
			zin= re.findall('^\s*output \[.*\] (.*);',line)
			outbit = yin[0].split(':')
			size = int(outbit[0])-int(outbit[1]) +1
			outvar = zin[0].split(',')

		if re.findall('^\s*output ([^\[])',line):
			pin= re.findall('^\s*output (.*);*',line)
			pin=pin[0].replace(';','')
			pin=pin.replace(' ','')
			pin=pin.split(",")
			outvar=pin
			print(outvar)
			output_acts={}
	#Wire calculations 
	if re.findall('^\s*wire',x):
		line=x
		if not x[len(x)-2]==';':
			while 1:
				l=vfile.readline()
				line=line+l
				if line[len(line)-2]==';':
					break
		wire=[]
		wire_acts={}
		line=line.replace('\n','')
		line=line.replace('	','')
		line=line.replace('     ','')
		if re.findall('^\s*wire \[(.*)\]',line):
			yin= re.findall('^\s*wire \[(.*)\]',line)
			zin= re.findall('^\s*wire \[.*\] (.*);',line)
			wibit = yin[0].split(':')
			size = int(inbit[0])-int(inbit[1]) +1
			wire = zin[0].split(',')

		if re.findall('^\s*wire ([^\[])',line):
			pin= re.findall('^\s*wire (.*);*',line)
			pin=pin[0].replace(';','')
			pin=pin.replace(' ','')
			pin=pin.split(",")
			wire=pin
			print(wire)
	newline=[]
	#print("NAND Gate probablities are found here")
	if re.findall('^\s*nand',x):
		print("nandgates")
		line=x
		line=line.split('(');
		line=line[1].split(')');
		line=line[0]
		line=line.split(',')
		for a in line:
			a=a.replace(" ","")
			newline.append(a)
		print(newline)
		if(len(newline)==4):
			check=universal_dict[newline[1]]*universal_dict[newline[2]]*universal_dict[newline[3]]
			value=1-check
			universal_dict.update({newline[0]:value})
		if(len(newline)==5):
			check=universal_dict[newline[1]]*universal_dict[newline[2]]*universal_dict[newline[3]]*universal_dict[newline[4]]
			value=1-check
			universal_dict.update({newline[0]:value})
		if(len(newline)==6):
			check=universal_dict[newline[1]]*universal_dict[newline[2]]*universal_dict[newline[3]]*universal_dict[newline[4]]*universal_dict[newline[5]]
			value=1-check
			universal_dict.update({newline[0]:value})
		if(len(newline)==7):
			check=universal_dict[newline[1]]*universal_dict[newline[2]]*universal_dict[newline[3]]*universal_dict[newline[4]]*universal_dict[newline[5]]*universal_dict[newline[6]]
			value=1-check
			universal_dict.update({newline[0]:value})
		if(len(newline)==8):
			check=universal_dict[newline[1]]*universal_dict[newline[2]]*universal_dict[newline[3]]*universal_dict[newline[4]]*universal_dict[newline[5]]*universal_dict[newline[6]]*universal_dict[newline[7]]
			value=1-check
			universal_dict.update({newline[0]:value})
		if(len(newline)==9):
			check=universal_dict[newline[1]]*universal_dict[newline[2]]*universal_dict[newline[3]]*universal_dict[newline[4]]*universal_dict[newline[5]]*universal_dict[newline[6]]*universal_dict[newline[7]]*universal_dict[newline[8]]
			value=1-check
			universal_dict.update({newline[0]:value})
		if(len(newline)==10):
			check=universal_dict[newline[1]]*universal_dict[newline[2]]*universal_dict[newline[3]]*universal_dict[newline[4]]*universal_dict[newline[5]]*universal_dict[newline[6]]*universal_dict[newline[7]]*universal_dict[newline[8]]*universal_dict[newline[9]]
			value=1-check
			universal_dict.update({newline[0]:value})
		if(len(newline)==3):
			check=universal_dict[newline[1]]*universal_dict[newline[2]]
			value=1-check
			universal_dict.update({newline[0]:value})					
	#print("NOT Gates probablities are found here")
	if re.findall('^\s*not',x):
		print("notgates")
		line=x
		line=line.split('(');
		line=line[1].split(')');
		line=line[0]
		line=line.split(',')
		for a in line:
			a=a.replace(" ","")
			newline.append(a)
		print(newline)
		check=1-universal_dict[newline[1]]
		universal_dict.update({newline[0]:check})
	if re.findall('^\s*buf',x):
		print("Buffers")
		line=x
		line=line.split('(');
		line=line[1].split(')');
		line=line[0]
		line=line.split(',')
		for a in line:
			a=a.replace(" ","")
			newline.append(a)
		print(newline)
		check=universal_dict[newline[1]]
		universal_dict.update({newline[0]:check})
	#print("AND Gates probablities are found here")
	if re.findall('^\s*and',x):
		print("andgates")
		line=x
		line=line.split('(');
		line=line[1].split(')');
		line=line[0]
		line=line.split(',')
		for a in line:
			a=a.replace(" ","")
			newline.append(a)
		print(newline)
		prod=1
		length=len(newline)
		for i in range(1,length):
			prod=prod*universal_dict[newline[i]]
		print(prod)
		universal_dict.update({newline[0]:prod})
	#print("XOR Gates probablities are found here")
	if re.findall('^\s*xor',x):
		print("xorgates")
		line=x
		line=line.split('(');
		line=line[1].split(')');
		line=line[0]
		line=line.split(',')
		for a in line:
			a=a.replace(" ","")
			newline.append(a)
		print(newline)
		if len(newline)==3:
			check1=1-universal_dict[newline[1]]
			check2=1-universal_dict[newline[2]]
			value=universal_dict[newline[1]]*check2 +universal_dict[newline[2]]*check1
			#print(value)
			universal_dict.update({newline[0]:value})
	#print("NOR Gates probablities are found here")
	if re.findall('^\s*nor',x):
		print("norgates")
		line=x
		line=line.split('(');
		line=line[1].split(')');
		line=line[0]
		line=line.split(',')
		for a in line:
			a=a.replace(" ","")
			newline.append(a)
		print(newline)
		prod=1
		length=len(newline)
		for i in range(1,length):
			i1=1-universal_dict[newline[i]]
			prod=prod*i1
		universal_dict.update({newline[0]:prod})
	#print("OR Gates probablities are found here")
	if re.findall('^\s*or',x):
		print("orgates")
		line=x
		line=line.split('(');
		line=line[1].split(')');
		line=line[0]
		line=line.split(',')
		for a in line:
			a=a.replace(" ","")
			newline.append(a)
		print(newline)
		prod=1
		length=len(newline)
		for i in range(1,length):
			i1=1-universal_dict[newline[i]]
			prod=prod*i1
			value1=1-prod
		universal_dict.update({newline[0]:value1})		

#print(input_acts)
#print(wire_acts)
#print(output_acts)
		
tbfile.write("Outputs-")
for x in outvar:
	tbfile.write(x+" ")
tbfile.write("\n")
tbfile.write("\n")
tbfile.write("Inputs-")
for x in invar:
	tbfile.write(x+" ")
tbfile.write("\n")
tbfile.write("\n")
tbfile.write("Wires-")
for x in wire:
	tbfile.write(x+" ")
tbfile.write("\n")
tbfile.write("\n")
tbfile.write("Input Probablilities\n")
for k,v in universal_dict.items():
	if str(k) in invar:
		tbfile.write(str(k)+'-'+str(v)+'\n')
tbfile.write("\n")
tbfile.write("\n")
tbfile.write("Wire Probablilities\n")
for k,v in universal_dict.items():
	if str(k) in wire:
		tbfile.write(str(k)+'-'+str(v)+'\n')
tbfile.write("\n")
tbfile.write("\n")
tbfile.write("Output Probablilities\n")
for k,v in universal_dict.items():
	if str(k) in outvar:
		tbfile.write(str(k)+'-'+str(v)+'\n')
tbfile.write("\n")
tbfile.write("\n")
tbfile.write("Activity factors of all the outputs go here\n")
for k,v in universal_dict.items():
	if str(k) in outvar:
		check1=1-float(v)
		value=float(v)*check1
		tbfile.write("Activity factor-")
		tbfile.write(str(k)+'-'+str(value)+'\n')
tbfile.write("\n")
tbfile.write("\n")
vfile.close()
tbfile.close()
