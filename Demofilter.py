lst=[10,20,30]
iterL=filter(None,lst)
for item in iterL:
    print("item:{0}".format(item))

def getBiggerThan20(i):
    return i>20
iterL=filter(getBiggerThan20,lst)
for item in iterL:
    print("item:{0}".format(item))
iterL=filter(lambda x:x>20,lst)
for item in iterL:
    print("item:{0}".format(item))
