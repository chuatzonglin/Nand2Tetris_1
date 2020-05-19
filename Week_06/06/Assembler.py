import os, sys, errno, fnmatch

temp = r"max/MaxL.asm"
def main():
	filepath = IOfiles(temp)

	filename, filepath, machineCodeDirectory = filepath.getFilePath

	key = 0
	f = {}
	for file in filepath:
		f[key] = (open(file,"r"))
		

		if (f[key].mode == "r"):
			contents = f[key].read()
			print(contents)

		key += 1
	
class IOfiles():
	def __init__(self, filepath):
		self.filepath = filepath
	
	@property
	def getInputName(self):
		"""
		if(len(sys.argv) != 2):
			inputBuffer = input("Input *.asm file or Directory: \n")
		else:
			inputBuffer = sys.argv[1]
		"""
		inputBuffer = temp
		return inputBuffer

	@property
	def getFilePath(self):
		#Getting input
		inputBuffer = self.getInputName
		#Input is Directory
		if ((os.path.isdir(inputBuffer))):
			directory = inputBuffer
			print("Name of Directory: ", directory, "\nChecking for *.asm files...")
			filename, filepath = self.directoryParser(directory)
		#Input is .S*P file
		elif(fnmatch.fnmatch(inputBuffer, "*.asm")):
			filename = [os.path.basename(inputBuffer)]
			filepath = [os.path.abspath(inputBuffer)]
			directory = os.path.dirname(filepath[0])
			print("Name of *.asm: ", filepath[0])
		elif(fnmatch.fnmatch(inputBuffer, '"*.asm"') or fnmatch.fnmatch(inputBuffer, "'*.asm'")):
			inputBuffer = inputBuffer[1:-1]
			filename = [os.path.basename(inputBuffer)]
			filepath = [os.path.abspath(inputBuffer)]
			directory = os.path.dirname(filepath[0])
			print("Name of *.asm: ", filepath[0])
		else:
			print("Input File Error")
			print(inputBuffer)
			quit()

		#Creating Folder to store Machine Code
		machineCodeDirectory = self.createOutputFolder(directory)

		return filename, filepath, machineCodeDirectory

	def directoryParser(self):
		filename = []
		filepath = []
		#Parsing through Directory
		for file in os.listdir(directory):
			if(fnmatch.fnmatch(file, "*.asm")):
				filename.append(file)
				filepath.append(os.path.join(directory,file))
		if (not filename):
			print ("No files in *.asm Format")
			quit()
		return filename,filepath
		

	def createOutputFolder(self,fileDirectory):
		machineCodeDirectory = os.path.join(fileDirectory, "Machine_Code")
		try:
			os.makedirs(machineCodeDirectory)
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise
		return machineCodeDirectory
	
	
if __name__ == '__main__':
	main()