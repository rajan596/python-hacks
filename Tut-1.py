# list
d=[2,5]

# for loop
for x in range(1,10):
    d.append(x)

print(d)

# if ...elif....else
if 1<d[2]<5:
    print("Okay")
else:
    print(d.count(2))

if "l"=="le":
    print("first")
elif 5>2:
    print("two")
else:
    print("default")

# function
def print_x(count=5):
    for _ in range(0,count):
        print("Hello " + str(_))

print_x(2)
print_x()

# local global variable
x=6

def example():
    global x
    print(x+6)

example()

# installing modules in unix
# sudo apt-get install python3-matplotlib



