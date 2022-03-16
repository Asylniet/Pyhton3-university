from time import sleep
import math

num = int(input("Number: "))
timing = int(input("Delay time: "))

def root(num):
    sleep(timing / 1000)
    return math.sqrt(num)

print(f"Square root of {num} after {timing} miliseconds is {root(num)}")