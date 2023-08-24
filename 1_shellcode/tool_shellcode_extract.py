print("===============================")
print("RUS_SH SHELL CODE EXTRACT")
print("need to have '/shellcode' file")
print("===============================")
print("OUTPUT : ")

f = open('./2_shellcode', 'r')
result = []
while True:
    s1 = f.readline()
    if s1 == '':
        break
    result.append(s1)
    result = s1.split()
    for i in range(len(result)):
        print("\\x"+result[i], end="")

print("")
print("===============================")
