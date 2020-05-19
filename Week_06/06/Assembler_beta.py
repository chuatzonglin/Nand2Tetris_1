def main():
	contents = parser("pong/PongL.asm")
	machineCode = compile(contents)
	
	outF = open("myOutFile.hack", "w")
	for line in machineCode:
	  # write line to output file
	  outF.write(line)
	  outF.write("\n")
	outF.close()

def parser(filepath):
	file = open(filepath,"r")
	inputBuffer = file.readlines()
	file.close()
	
	while("\n" in inputBuffer):
		inputBuffer.remove("\n") 
	
	#print(inputBuffer)
	contents = []
	for line in inputBuffer:
		if not(line.startswith("//")):
			if "//" in line:
				line = line.split("//")[0]
				contents.append(line.strip(" \t\n\r"))
			else:
				contents.append(line.strip(" \t\n\r"))
	#print(contents)
	return contents

def compile(contents):
	machineLanguage = []
	lineNo = 0
	for instruction in contents:
		if instruction[0] == "(" and instruction[-1] == ")":
			symbolTable[instruction[1:-1]] = str("{0:016b}".format(lineNo))
			contents.remove(instruction)
		lineNo += 1
	for i in range(len(contents)):
		if contents[i][0] == "@":
			machineLanguage.append(AInstruction(contents[i][1:]))
		#elif contents[i][0] == "(" and contents[i][-1] == ")":
			#symbolTable[contents[i][1:-1]] = str("{0:016b}".format(len(machineLanguage)+1))
		else :
			machineLanguage.append(CInstruction(contents[i]))

	return machineLanguage

def AInstruction(instruction):
	if instruction.isnumeric():
		instruction = int(instruction)
		return str("{0:016b}".format(instruction))
	else:
		return Symbols(instruction)

def Symbols(instruction):
	global counter, symbolTable
	try:
		return symbolTable[instruction]
	except:
		symbolTable[instruction] = str("{0:016b}".format(counter))
		counter += 1
		return symbolTable[instruction]

def CInstruction(instruction):
	try:
		comp, jump = instruction.split(";")
	except:
		comp = instruction
		jump = "Null"
	try:
		dest, comp = comp.split("=")
	except:
		dest = "Null"

	returnvalue = "111"
	returnvalue += computationCodeLibrary(comp)
	returnvalue += destinationCodeLibrary(dest)
	returnvalue += jumpCodeLibrary(jump)
	
	#print(returnvalue)
	return returnvalue

symbolTable = {}
for i in range(16):
	symbolTable["R{}".format(i)] = str("{0:016b}".format(i))
counter = 16
symbolTable["SP"] = str("{0:016b}".format(0))
symbolTable["LCL"] = str("{0:016b}".format(1))
symbolTable["ARG"] = str("{0:016b}".format(2))
symbolTable["THIS"] = str("{0:016b}".format(3))
symbolTable["THAT"] = str("{0:016b}".format(4))
symbolTable["SCREEN"] = str("{0:016b}".format(16384))
symbolTable["KBD"] = str("{0:016b}".format(24576))

def computationCodeLibrary(instruction):
	if "M" in instruction:
		if instruction == "M":
			return "1110000"
		elif instruction == "!M":
			return "1110001"
		elif instruction == "-M":
			return "1110011"
		elif instruction == "M+1":
			return "1110111"
		elif instruction == "M-1":
			return "1110010"
		elif instruction == "D+M" or instruction == "M+D":
			return "1000010"
		elif instruction == "D-M":
			return "1010011"
		elif instruction == "M-D":
			return "1000111"
		elif instruction == "D&M" or instruction == "M&D":
			return "1000000"
		elif instruction == "D|M" or instruction == "M|D":
			return "1010101"
	else:
		if instruction == "0":
			return "0101010"
		elif instruction == "1":
			return "0111111"
		elif instruction == "D":
			return "0001100"
		elif instruction == "A":
			return "0110000"
		elif instruction == "!D":
			return "0001101"
		elif instruction == "!A":
			return "0110001"
		elif instruction == "-D":
			return "0001111"
		elif instruction == "-A":
			return "0110011"
		elif instruction == "D+1":
			return "0011111"
		elif instruction == "A+1":
			return "0110111"
		elif instruction == "D-1":
			return "0001110"
		elif instruction == "A-1":
			return "0110010"
		elif instruction == "D+A":
			return "0000010"
		elif instruction == "D-A":
			return "0100011"
		elif instruction == "A-D":
			return "0000111"
		elif instruction == "D&A":
			return "0000000"
		elif instruction == "D|A":
			return "0010101"
		elif instruction == "-1":
			return "0111010"

def destinationCodeLibrary(instruction):
	if instruction == "Null":
		return "000"
	elif instruction == "M":
		return "001"
	elif instruction == "D":
		return "010"
	elif instruction == "MD":
		return "011"
	elif instruction == "A":
		return "100"
	elif instruction == "AM":
		return "101"
	elif instruction == "AD":
		return "110"
	elif instruction == "AMD":
		return "111"

def jumpCodeLibrary(instruction):
	if instruction == "Null":
		return "000"
	elif instruction == "JGT":
		return "001"
	elif instruction == "JEQ":
		return "010"
	elif instruction == "JGE":
		return "011"
	elif instruction == "JLT":
		return "100"
	elif instruction == "JNE":
		return "101"
	elif instruction == "JLE":
		return "110"
	elif instruction == "JMP":
		return "111"

if __name__ == '__main__':
	main()