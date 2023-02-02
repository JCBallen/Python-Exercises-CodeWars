import os

os.system("cls")

lista=[0,1,2,3,4,5,0,0,0,0]

print(lista)

lista2=[x for x in lista if x!=0] # list comprenhension al reves no necesita else

print(lista2)


listaxd=[1,2,3,4,[7,0,2,5],0]
print(len(listaxd))