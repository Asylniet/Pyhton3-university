import re
def text_match(text):
        patterns = '[A-Z]+[a-z]+'
        x = re.findall(patterns, text)
        return x

print(text_match(input()))