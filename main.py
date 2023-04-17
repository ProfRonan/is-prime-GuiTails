print("Digite o número que quer testa")
N = int(input("> "))
i = 1
while True:
    i = i + 1
    if N ==1:
        print("Não primo")
        break
    if N <=0:
        print("Número inválido")
        break
    if N % i ==0 and N !=i:
        print("Não primo")
        break
    if N % i !=0 and i > 10000000000000000000000000000000000:
        if i < 10000000000000000000000000000000000:
            print("Primo")
            break
