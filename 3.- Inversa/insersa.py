p = input("Digita alguna palabra: ")

for i in range(len(p) -1, -1, -1):
    print(p[i], end='')
    
print("\nsegunda manera")
print(p[::-1])