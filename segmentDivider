from numpy import linspace, array

length = 8006

overlap = 3  # seconds

cutSize = 10*60  # seconds

ar = linspace(0, length, (int(length/cutSize)+1))

x = 0

ar2 = [[0, int(ar[1])]]

x = 1

while x <= (len(ar)-2):
    ar2.append([int(ar[x]-overlap), int(ar[x+1])])
    x = x+1


print(ar)
print(ar2)
