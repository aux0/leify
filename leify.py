def leify(s):
	return 'le ' + ' le '.join(s.split())

def main():
	s = raw_input('Leify what? ')
	print '%s\n' % leify(s)

if (__name__ == '__main__'):
	main()