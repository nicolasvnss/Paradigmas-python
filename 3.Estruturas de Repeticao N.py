#while
count = 1
while count <= 5:
    print(count)
    count += 1
#range(0, 10, 1):
#range(inicio, parada, incremento)
#O incremento pode ser negativo

#for normal
for n in range(0, 5):
    print(n+1)
    
for n in range(1, 5):
    print(n)
#for decrescente
for n in range(5, 0,-1):
    print(n)
#exemplo com break
#vai parar no >>4<<
for n in range(0, 8):
    if n==5:
        break
    print(n)
#exemplo com continue
#vai pular o numero >>4<<
for n in range(0, 5):
    if n==3:
        continue
    print(n)