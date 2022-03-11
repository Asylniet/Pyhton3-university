def change_case(str):
	return ''.join(['_' + i.lower() if i.isupper() else i for i in str]).lstrip('_')
	
str = input()
print(change_case(str))
