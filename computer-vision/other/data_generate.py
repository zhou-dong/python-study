import random

def getRandom(x):
    v = random.uniform(0, 1.5)
    if bool(random.getrandbits(1)):
        return x + v
    else:
        if (x-v > 0):
            return x - v
        else:
            return x + v 
        
r = open('./data.txt', "r")
w = open("../datas.txt", "a")

def generateAndWrite(r, w):
    for line in r:
        for element in line.split(" "):
            if element.strip() == 'a':
                w.write("1\n")
            elif element.strip() == 'c':
                w.write("0\n")
            else:
                v = getRandom(float(element))
                w.write(str(v) + " ")

generateAndWrite(r,w)

r.close()
w.close()
