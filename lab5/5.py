import re
def text_match(text):
        patterns = 'a.+b$'
        if re.search(patterns,  text):
                return 'Mathces!'
        else:
                return('Does not match')

print(text_match(input()))