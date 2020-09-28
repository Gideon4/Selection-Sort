import random

def sort(listo):
    for i in range(len(listo)-1):
        num=[listo[i],i]
        for j in range(i+1,len(listo)):
            if listo[j]<num[0]:
                num=[listo[j],j]
        listo.pop(num[1])
        listo.insert(i,num[0])
    print(listo)

def generatelist(length,rangeo):
    return [random.randint(0,rangeo) for i in range(length)]
    
sort(generatelist(4096,65536))
