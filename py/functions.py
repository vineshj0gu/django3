age = 12
name = "jogu"
def hello():
    print ('this is function print')


def hell(txt):
    print ('this is function print  '+ txt)

def hella(txt, age):
    print (f'this is function print  {txt} your age is {age}')

def hella(txt="vines", age=30):
    print (f'this is function print  {txt} your age is {age}')

def hellb(txt="vines", age=34):
    return f'this is function print  {txt} your age is {age}'

g = hellb()
print(g)




#hello()
#hell("boy")
#hella("boy",3)
#hella()
