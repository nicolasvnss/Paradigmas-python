#formas de criar listas
lst = ["a,b,c,d,e"]
print(lst)
#vários tipos
lst2 = [4,3,2,"1",False]
print(lst2)
#lista com lista
lst3 = [12,["a,b,c,d,e"],"X"]
print(lst3)
#criando lista com range
lst4 = list(range(0,5))
print(lst4)
#comprimento da lista
print(len(lst))
#acessando elemento
print(lst[0])
#posiçõo 1 é uma lista
print(lst3[1])
#alterando posição
lst[0] = 4
print(lst)
#percorrendo lista
for n in range(0, len(lst4)):
    print(lst4[n]+1)