""" Code written by Idan Hovav. Inspired by the prompt given by 
programming-challenges.com
Website: http://www.programming-challenges.com/

This is an interpreter for a very basic language.

Syntax for language:
100	means halt
2dn	means set register d to n (between 0 and 9)
3dn	means add n to register d
4dn	means multiply register d by n
5ds	means set register d to the value of register s
6ds	means add the value of register s to register d
7ds	means multiply register d by the value of register s
8da	means set register d to the value in RAM whose 
address is in register a
9sa	means set the value in RAM whose address is in 
register a to the value of register s
0ds	means goto the location in register d unless 
register s contains 0

"""

def read(source):

	lines = []
	for x in source:
		lines.append(x[:len(x)-1]) #gets rid of newline.

	curr = 0
	registers = [000] * 10

	for l in lines:
		#print(l)
		if l == '' or l == "100" or l == '\n':
			break
		hund, ten, one = eval(l[:1]), eval(l[1:2]), eval(l[2:])
		#print(registers)

		if(hund == 2):
			registers[ten] = one
		elif hund == 3:
			a = registers[ten]
			registers[ten] = ((a + one) % 1000)
		elif hund == 4:
			a = registers[ten]
			registers[ten] = ((a * one) % 1000)
		elif hund == 5:
			registers[ten] = registers[one]
		elif hund == 6:
			a = registers[ten]
			registers[ten] = ((a + registers[one]) % 1000)
		elif hund == 7:
			a = registers[ten]
			registers[ten] = ((a * registers[one]) % 1000)
		elif hund == 8:
			index = registers[one]
			registers[ten] = registers[index]
		elif hund == 9:
			index = registers[one]
			registers[index] = registers[ten]
		elif hund == 0:
			if registers[one] != 0:
				curr = registers[ten]
		else:
			print("improper command, gov'na")
	return registers[curr]



if __name__ == "__main__":
	response = input("File Name? ")
	source = open(response, 'r')
	cases = source.readline()
	cases = cases[:len(cases)-1]
	cases = eval(cases) # cases is now the number of cases given.
	while cases:
		source.readline() # get rid of blank line
		val = read(source)
		print(val)
		cases -= 1

