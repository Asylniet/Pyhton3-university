import re
def text_match(text):
        patterns = '^ab{2,3}'
        if re.search(patterns,  text):
                return 'Mathces!'
        else:
                return('Does not match')

print(text_match(input()))