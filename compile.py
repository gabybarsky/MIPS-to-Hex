def toHex(string):
	binary = [string[i:i+4] for i in range(0, len(string), 4)]
	binary = ''.join(binary)
	return hex(int(binary, 2))

def argsToBinary(args):
	for i in range(0, len(args)):
		args[i] = int(args[i][1:])
		args[i] = '{:05b}'.format(args[i])

	return args

def singleToBinary(arg):
	arg = int(arg[1:])
	arg = '{:05b}'.format(arg)
	return arg


def compile(string):
	args = string.split(' ')
	command = args.pop(0)
	retVal = ""

	if(len(args) > 3):
		return "Too many args"

	if (command == ".word"):
		return "0x" + hex(int(args[0]))[2:].zfill(8)
	elif (command == "add"):
		#add $d, $s, $t | 0000 00ss ssst tttt dddd d000 0010 0000
		#$d = $s + $t
		args = argsToBinary(args)
		retVal = "000000" + args[1] + args[2] + args[0] + "00000100000"
	elif (command == "sub"):
		args = argsToBinary(args)
		retVal = "000000" + args[1] + args[2] + args[0] + "00000100010"
	elif (command == "mult"):
		args = argsToBinary(args)
		retVal = "000000" + args[0] + args[1] + "0000000000011000"
	elif (command == "multu"):
		args = argsToBinary(args)
		retVal = "000000" + args[0] + args[1] + "0000000000011001"
	elif (command == "div"):
		args = argsToBinary(args)
		retVal = "000000" + args[0] + args[1] + "0000000000011010"
	elif (command == "divu"):
		args = argsToBinary(args)
		retVal = "000000" + args[0] + args[1] + "0000000000011011"
	elif (command == "mfhi"):
		args = argsToBinary(args)
		retVal = "0000000000000000" + args[0] + "00000010000"
	elif (command == "mflo"):
		args = argsToBinary(args)
		retVal = "0000000000000000" + args[0] + "00000010010"
	elif (command == "lis"):
		args = argsToBinary(args)
		retVal = "0000000000000000" + args[0] + "00000010100"
	elif (command == "lw"):
		args[0] = singleToBinary(args[0])
		address = args[1].split('(')
		address[1] = address[1].split(')')[0]

		retVal = "100011" + singleToBinary(address[1]) + args[0]
		return ".word " + toHex(retVal) + hex(int(address[0]))[2:].zfill(4)
	elif (command == "sw"):
		args[0] = singleToBinary(args[0])
		address = args[1].split('(')
		address[1] = address[1].split(')')[0]

		retVal = "101011" + singleToBinary(address[1]) + args[0]
		return ".word " + toHex(retVal) + hex(int(address[0]))[2:].zfill(4)
	elif (command == "slt"):
		args = argsToBinary(args)
		retVal = "000000" + args[1] + args[2] + args[0] + "00000101010"
	elif (command == "sltu"):
		args = argsToBinary(args)
		retVal = "000000" + args[1] + args[2] + args[0] + "00000101011"
	elif (command == "beq"):
		args[0] = singleToBinary(args[0])
		args[1] = singleToBinary(args[1])
		retVal = "000100" + args[0] + args[1]
		return ".word " + toHex(retVal) + hex(int(args[2]))[2:].zfill(4)
	elif (command == "bne"):
		args[0] = singleToBinary(args[0])
		args[1] = singleToBinary(args[1])
		retVal = "000101" + args[0] + args[1]
		return ".word " + toHex(retVal) + hex(int(args[2]))[2:].zfill(4)
	elif (command == "jr"):
		args = argsToBinary(args)
		retVal = "000000" + args[0] + "000000000000000001000"
	elif (command== "jalr"):
		args = argsToBinary(args)
		retVal = "000000" + args[0] + "000000000000000001001"
	else:
		return "Invalid format. Please use [command] $i $j $k"

	return ".word 0x" + toHex(retVal)[2:].zfill(8)

while True:
	instruction = raw_input("Please enter a command (no commas): ")
	print compile(instruction)
