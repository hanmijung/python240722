# DomoStrList.py

strA="python is very powerful"
strB="파이션은 강력해"
x=100
y=3.14


print(len(strA))
print(len(strB))
#  슬라이싱 연습
print(strA[0])
print((strA[0:6]))
print(strA[:6])
print(strA[-3:])
#  리스트 형식
colors=["red","blue","green"]
print(colors)
print(type(colors))
colors.append("yellow")
colors.insert(1,"pink")
print(colors)
colors.remove("blue")
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)

t=(1,2,3)
type(t)



print("id:%s, name:%s"%("kim","김유신"))
args=(4,5)

# 형식변환
a=set((1,2,3))
type(a)
print(type(a))
b=list(a)
print(type(b))
b.append(4)
print(b)

def calc(a,b):
    return a+b, a*b
result=calc(5,6)
print(result)

print("id:%s, name:%s" %("kim","김유신"))

# 디셔너리
device={"아이폰":5,"맥북":10,"아이패스":15}
print(type(device))
device["맥북1"]=12
device["아이패스"]=115
print(device)
del device["맥북1"]
print(device)

for item in device.items():
    print(item)
