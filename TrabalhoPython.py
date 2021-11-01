def geraPadrao():
    n = int(input("Digite um numero inteiro:(2-12):"))
    letra = input("digite uma letra(A-Z):")
    letra = letra.upper()
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    def posicoes():
        for a in range(0,26):
            if alfabeto[a] == letra:
                pos = a
                return pos

    if n < 2 or n > 12:
        print("Número inválido")
    else:
        for i in range(1, n+ 1):
            for j in range(1, n - i + 1):
                print(end=".")
            for j in range(1,i+1):
                print(alfabeto[posicoes()+j-1],end="")
            for j in range(i-1,0,-1):
                print(alfabeto[posicoes()+j-1],end="")
            for j in range(1, n - i + 1):
                print(end=".")
            print()
        for i in range(1, n):
            for j in range(n, n +i):
                print(end=".")
            for j in range(n-i):
                print(alfabeto[posicoes()+j],end="")
            for j in range(n-i-1,0,-1):
                print(alfabeto[posicoes()+j-1],end="")
            for j in range(n, n +i):
                print(end=".")

            print()

geraPadrao()