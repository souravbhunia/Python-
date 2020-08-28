''''
first="Sourav"
last="Bhunia"
msg=f'{first} {last} is a coder'
print(msg)


course='python for beginners'
msg=f'{course} '
print(len(course))
print(msg)

'''''
def my_fun():
    global a 
    a=10
    b=20
    c=a+b 
    print(c)

my_fun()

def fun():
    print(a)

fun()