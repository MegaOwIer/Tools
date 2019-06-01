from os import system as cmd

def move_file(_from, _to):
	command = F'cp {_from} {_to}'
	print('> ' + command + ' .....')
	cmd(command)

if __name__ == '__main__':
	move_file('c_cpp_properties.json', '../c_cpp_properties.json')
	move_file('compile.py', '../scripts/compile.py')
	print('------- Installed -------')