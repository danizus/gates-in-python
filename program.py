
def _or(x,y):
    c=x or y
    return c
def _and(x,y):
    c=x and y
    return c
def _nor(x,y):
    c=not(_or(x,y))
    return c
def _nand(x,y):
    c=not(_and(x,y))
    return c
def _xor(x,y):
    c=_and(_or(x,y),_nand(x,y))
    return c
def _xnor(x,y):
    c=not(_xor(x,y))
    return c
#x and y are the inputs 
x=1 
y=0
#example
#print(_or(_nand(x,y),_xor(x,y)))

for i in [True,False]: 
  for j in [True,False]:
    for z in [True,False]:
     print(i or j)
    