class StringWork():
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input()

    def print_String(self):
        print(self.s.upper())

str = StringWork()
str.get_String()
str.print_String()