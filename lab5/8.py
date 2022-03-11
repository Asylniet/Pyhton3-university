import re
def text_match(text):
        patterns = '[A-Z][^A-Z]*'
        x = re.findall(patterns, text)
        return x

print(text_match(input()))