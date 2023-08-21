import binascii
result1 = []
result2 = []

print("===================")
print("ASCII TO HEX")
print("===================")
print("INPUT : ", end="")
inputString = input()
print("===================")
print("OUTPUT : ")

inputStringLen = len(inputString)
inputString = binascii.hexlify(inputString.encode())

for i in range(inputStringLen):
    result1.append(inputString[-2:])
    inputString = inputString[:-2]
#print(result1)

cnt = 0;
jumpPoint = len(result1) % 8
for i in range(len(result1)):
        if i == 0:
            print("0x", end="")
        if cnt == jumpPoint & jumpPoint != 0:
            cnt = 0
            jumpPoint = -1
            print("")
            print("0x", end="")
        elif cnt == 8:
            cnt = 0
            print("")
            print("0x", end="")
        print(result1[i].decode('utf-8'), end="")
        cnt = cnt+1
print("")
print("===================")

