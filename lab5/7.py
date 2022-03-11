def snake_to_camel(word):
        return ''.join(x.capitalize() for x in word.split('_'))

print(snake_to_camel(input()))