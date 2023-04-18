import random

name = random.randint(0, 10)
for x in range(10):
    if x != 0:
        print(x)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'The random number is: {name}')  # Press Ctrl+F8 to toggle the breakpoint.




if __name__ == '__main__':
    print_hi(name=name)
