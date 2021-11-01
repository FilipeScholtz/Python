asOpcoes = "------PRODUTOS------\n1 - MOSTRAR ESTOQUE\n2 - INSERIR PRODUTO\n3 - REMOVER PRODUTO\n------FABRICANTES------\n4 - INSERIR FABRICANTE\n5 - REMOVER FABRICANTE\n6 - MOSTRAR FABRICANTES\n------CLIENTES------\n7 - INSERIR CLIENTES\n8 - REMOVER CLIENTES\n9 - MOSTRAR CLIENTES\n------VENDAS------\n10 - REALIZAR VENDA\n11 - MOSTRAR VENDAS\n20.SAIR\n\nEscolha:"

asOpcoesFiltradas = "\nEscolha a opção que deseja filtrar:\n1 - Por faixa preço\n2 - Por preço de unidade\n9 - Voltar\n\nEscolha:"

resp = "\nDigite como deseja visualizar o estoque:\n1 - Inteiro\n2 - Filtrado\n9 - Voltar\n\nEscolha:"

respo = "\n1 - Deletar por nome\n2 - Deletar por código\n9 - Voltar\n\nEscolha:"

# listas para os diferentes tipos de item
produtos = []
fabricantes = []
vendas = []
produtosvendidos = []
clientes = []

# listas para os conjuntos (cadastros) de itens
cadProdutos = []
cadFabricantes = []
listaProdutosVendidos = []
listaVendas = []
listaClientes = []


def mostraEstoque():
    cadProdutos.sort()
    sair = False
    while (not sair):
        opção = int(input(resp))
        if (opção == 2):
            mostraEstoqueFiltrado()
        elif (opção == 1):
            if (cadProdutos == []):
                print("ESTOQUE VÁZIO!")
            else:
                print("ESTOQUE:")
                for umProduto in cadProdutos:
                    print("Código:", umProduto[0])
                    print("Nome :", umProduto[1])
                    print("Preço:", umProduto[2])
                    print("Quantidade:", umProduto[3])
                    print("Código do Fabricante:", umProduto[4])
                    print("-------")
        elif (opção < 1 or opção > 9):
            print("Opção inválida...")
        elif (opção == 9):
            sair = True


def mostraEstoqueFiltrado():
    sair = False
    while (not sair):
        opcao = int(input(asOpcoesFiltradas))
        if (opcao < 1 or opcao > 9):
            print("Opção inválida...")
        elif opcao == 1:
            nexist = 0
            detanto = []
            atanto = []
            detanto = int(input("Escolha a faixa de preço\nDe:"))
            atanto = int(input("a:"))
            if (cadProdutos == []):
                print("ESTOQUE VÁZIO!")
            else:
                print("ESTOQUE:")
                for umProduto in cadProdutos:
                    if (umProduto[2] >= detanto):
                        if (umProduto[2] <= atanto):
                            nexist = 0
                            print("Código:", umProduto[0])
                            print("Nome:", umProduto[1])
                            print("Preço:", umProduto[2])
                            print("-------")
                        else:
                            nexist = 1
                    else:
                        nexist = 1
            if (nexist == 1):
                print("NÃO EXISTE PRODUTO NESTA FAIXA DE PREÇO!")
        elif opcao == 2:
            if (cadProdutos == []):
                print("ESTOQUE VÁZIO!")
            else:
                print("ESTOQUE:")
                cadProdutos.sort()
                for umProduto in cadProdutos:
                    print("Código:", umProduto[0])
                    print("Nome:", umProduto[1])
                    print("Preço:", umProduto[2])
                    print("-------")
        elif opcao == 9:
            sair = True


def insereProduto():
    # acrescenta na lista produtos as informacoes de 1 produto~
    if cadFabricantes == []:
        print("NÃO HÁ FABRICANTES! CADASTRE UM FABRICANTE PRIMEIRO.")
    else:
        japossui = False
        cad = False
        procurator = False
        procuratorCod = False
        i = 0
        j = 0
        if cadProdutos == []:
            cod = int(input("Código do produto?"))
            nome = str(input("Nome?"))
            preço = float(input("Preço?"))
            qnt = int(input("Quantidade?"))
            print("\nFABRICANTES:\n")
            for umFabricante in cadFabricantes:
                print("Código:", umFabricante[0])
                print("Nome:", umFabricante[1])
                print("-------")
            codf = int(input("Código do fabricante?"))
            for umProcura in cadFabricantes:
                if codf == cadFabricantes[i][0]:
                    produtos.append(cod)
                    produtos.append(nome)
                    produtos.append(preço)
                    produtos.append(qnt)
                    produtos.append(codf)
                    cadProdutos.append(produtos.copy())
                    procurator = True
                i += 1
            if procurator == False:
                print("NÃO POSSUI FABRICANTE COM ESTE CÓDIGO!")
            else:
                print("PRODUTO CADASTRADO!")

        else:
           per = str(input("Deseja Repor ou Cadastrar? (r/c)"))
           if per == "r":
             procurador = False
             posi = 0
             vaoli = int
             totalzin = int
             print("Qual produto quer repor quantidade?")
             print("\nESTOQUE:")
             cadProdutos.sort()
             for umProduto in cadProdutos:
                 print("Código:", umProduto[0])
                 print("Nome:", umProduto[1])
                 print("Quantidade:", umProduto[3])
                 print("-------")
             escolha = int(input("Digite o código do produto:"))
             for procuraProd in cadProdutos:
                  if escolha == cadProdutos[j][0]:
                      vaoli = procuraProd[3]
                      posi = j
                      procurador = True
                  j += 1
             if procurador == True:
               reporQnt = int(input("Qual quantidade deseja acrescentar?"))
               totalzin = vaoli + reporQnt
               cadProdutos[posi][3] = totalzin
               print("Pronto! foi adicionado sua quantia ao estoque!")
             else:
               print("Não achamos este produto")
           elif per == "c":
              cod = int(input("Código do produto?"))
              nome = str(input("Nome?"))
              preço = float(input("Preço?"))
              qnt = int(input("Quantidade?"))
              print("\nFABRICANTES:\n")
              for umFabricante in cadFabricantes:
                  print("Código:", umFabricante[0])
                  print("Nome:", umFabricante[1])
                  print("-------")
              codf = int(input("Código do fabricante?"))
              for procuraProd in cadProdutos:
                  if cod == cadProdutos[j][0]:
                      procuratorCod = True
                  j += 1
              if procuratorCod == False:
                  for umProcura in cadFabricantes:
                      if codf == cadFabricantes[i][0]:
                          produtos.append(cod)
                          produtos.append(nome)
                          produtos.append(preço)
                          produtos.append(qnt)
                          produtos.append(codf)
                          cadProdutos.append(produtos.copy())
                          procurator = True
                      i += 1
                  if procurator == True:
                      print("PRODUTO CADASTRADO!")
                      cad = True

              if cad == False and procuratorCod == True:
                      print("JÁ POSSUI PRODUTO COM ESTE CÓDIGO")
                      japossui = True
              if procurator == False and japossui == False:
                  print("NÃO EXISTE FABRICANTE COM ESTE CÓDIGO!")
           else:
             print("OPÇÃO INVÁLIDA!")
    # acrescenta na lista cadprodutos uma copia da lista produtos (que contem
    # as informacoes de 1 produto

    produtos.clear()
    # clear limpa (esvazia) a lista produto, o que vai permitir que quando a funcao insereProduto
    # for novamente chamada, possa-se usar novamente a lista produto para inserir as informacoes de
    # um novo produto


def insereFabricante():
    procuratoFabri = False
    codi = int(input("Código do fabricante?"))
    nome = str(input("Nome do fabricante?"))
    z = 0
    for procuraFabrican in cadFabricantes:
        if codi == cadFabricantes[z][0]:
            procuratoFabri = True
        z += 1
    if procuratoFabri == False:
        fabricantes.append(codi)
        fabricantes.append(nome)
        cadFabricantes.append(fabricantes.copy())
        fabricantes.clear()
        print("FABRICANTE CADASTRADO!")
    else:
        print("JÁ POSSUI FABRICANTE COM ESTE CÓDIGO!")


def removerProduto():
    print("REMOVER PRODUTO")
    removedorProdutos = input("\nDigite o nome do produto à remover: ")
    i = 0
    produtoEcontrado = False
    for book in cadProdutos:
        if removedorProdutos == cadProdutos[i][1]:
            cadProdutos.pop(i)
            produtoEcontrado = True
        i += 1
    if produtoEcontrado == False:
        print("\nPRODUTO NÃO ENCONTRADO!")
    else:
        print("\nPRODUTO REMOVIDO!")


def removeFabricante():
    print("REMOVER FABRICANTE")
    removeFabricante = input("\nDigite o nome do fabricante à remover: ")
    i = 0
    fabricanteEcontrado = False
    for book in cadFabricantes:
        if removeFabricante == cadFabricantes[i][1]:
            cadFabricantes.pop(i)
            fabricanteEcontrado = True
        i += 1
    if fabricanteEcontrado == False:
        print("\nFABRICANTE NÃO ENCONTRADO")
    else:
        print("\nFABRICANTE REMOVIDO!")


def removerProdutoNovo():
    sair = False
    while (not sair):
        opcao = int(input(respo))
        if (opcao < 1 or opcao > 9):
            print("Opção inválida...")
        elif opcao == 1:
            i = 0
            print("REMOVENDO POR NOME")
            removedorProdutos = input("\nDigite o nome do produto à remover: ")
            produtoEcontrado = False
            for book in cadProdutos:
                if removedorProdutos == cadProdutos[i][1]:
                    cadProdutos.pop(i)
                    produtoEcontrado = True
                i += 1
            if produtoEcontrado == False:
                print("\nPRODUTO NÃO ENCONTRADO!")
            else:
                print("\nPRODUTO REMOVIDO!")
        elif opcao == 2:
            removedorProdutos = []
            print("REMOVENDO POR CÓDIGO")
            removedorProdutos = int(input("\nDigite o código do produto à remover: "))
            i = 0
            produtoEcontrado = False
            for book in cadProdutos:
                if removedorProdutos == cadProdutos[i][0]:
                    cadProdutos.pop(i)
                    produtoEcontrado = True
                i += 1
            if produtoEcontrado == False:
                print("\nPRODUTO NÃO ENCONTRADO!")
            else:
                print("\nPRODUTO REMOVIDO!")
        elif opcao == 9:
            sair = True


def mostrarFabricante():
    cadFabricantes.sort()
    if (cadFabricantes == []):
        print("Não há fabricantes cadastrados!")
    else:
        print("\nFABRICANTES:\n")
        for umFabricante in cadFabricantes:
            print("Código:", umFabricante[0])
            print("Nome:", umFabricante[1])
            print("-------")

def insereCliente():
    procuratocliente = False
    codic = int(input("Código do cliente?"))
    nomec = str(input("Nome do cliente?"))
    b = 0
    for procuraClien in listaClientes:
        if codic == listaClientes[b][0]:
            procuratocliente = True
        b += 1
    if codic < 0:
        print("VOCÊ DIGITOU UM NÚMERO NEGATIVO!")
    else:
        if procuratocliente == False:
            clientes.append(codic)
            clientes.append(nomec)
            listaClientes.append(clientes.copy())
            clientes.clear()
            print("CLIENTE CADASTRADO!")
        else:
            print("JÁ POSSUI CLIENTE COM ESTE CÓDIGO!")

def mostrarCliente():
    listaClientes.sort()
    if (listaClientes == []):
        print("NÃO HÁ CLIENTES CADASTRADOS!")
    else:
        print("\nCLIENTES:\n")
        for umClient in listaClientes:
            print("Código:", umClient[0])
            print("Nome:", umClient[1])
            print("-------")

def removeCliente():
    print("REMOVER CLIENTE")
    removeCliente = input("\nDigite o nome do cliente à remover: ")
    i = 0
    clienteEcontrado = False
    for book in listaClientes:
        if removeCliente == listaClientes[i][1]:
            listaClientes.pop(i)
            clienteEcontrado = True
        i += 1
    if clienteEcontrado == False:
        print("\nCLIENTE NÃO ENCONTRADO")
    else:
        print("\nCLIENTE REMOVIDO!")
    clientes.clear()



def fazerVenda():
    clienteEncontrad = False
    print("\nCLIENTES:\n")
    for umClient in listaClientes:
          print("Código:", umClient[0])
          print("Nome:", umClient[1])
          print("-------")
    codCli = int(input("Código do cliente:"))
    cliente = []
    confirm = ""
    c = 0
    dia = int
    mes = int
    ano = int
    for clientss in listaClientes:
        if codCli == listaClientes[c][0]:
            clienteEncontrad = True
            cliente = clientss[1]
        c += 1
    if (clienteEncontrad == True):
        print("Cliente encontrado, Sr.(a)",cliente)
        print("Digite a Data:")
        dia = int(input("Dia:"))
        if dia < 1 or dia > 31:
            print("DIA INVÁLIDO!")
        else:
            mes = int(input("Mês:"))
            if mes < 1 or mes > 12:
                print("MÊS INVÁLIDO")
            else:
                ano = int(input("Ano:"))
                if ano < 1500 or ano > 2021:
                    print("ANO INVÁLIDO")
                else:
                    print("Data:", dia,"/",mes,"/",ano)
                    confirm = input("Confirmar Data (s/n):")
                    if confirm == "s":
                        o = 0
                        pos = int
                        cod = int
                        qntPro = int
                        sub = int
                        nomeProduto = []
                        produEcontrado = False
                        print("\nESTOQUE:\n")
                        for umProduto in cadProdutos:
                            print("Código:", umProduto[0])
                            print("Nome :", umProduto[1])
                            print("-------")
                        verificProdutos = int(input("Digite o código do produto:"))
                        print("ESTOQUE:")
                        for procuranProdut in cadProdutos:
                            if verificProdutos == cadProdutos[o][0]:
                                produEcontrado = True
                                pos = o
                                cod = procuranProdut[0]
                                nomeProduto = procuranProdut[1]
                                qntPro = procuranProdut[3]
                            o += 1
                        if produEcontrado == False:
                            print("\nPRODUTO NÃO ENCONTRADO!")
                        else:
                            print("Temos ", qntPro, " unidades de: ", nomeProduto)
                            qnt = int(input("Qual a quantidade deste produto você deseja?"))
                            produQnt = False
                            if qnt <= cadProdutos[pos][3] and qnt > 0:
                                produQnt = True
                            if produQnt == False:
                                print("Desculpe! não possui esta quantidade no momento!")
                            else:
                                sub = (qntPro - qnt)
                                cadProdutos[pos][3] = sub
                                valor = cadProdutos[pos][2] * qnt
                                produtosvendidos.append(cod)
                                produtosvendidos.append(qnt)
                                vendas.append(cod)
                                vendas.append(codCli)
                                vendas.append(cliente)
                                vendas.append(dia)
                                vendas.append(mes)
                                vendas.append(ano)
                                vendas.append(nomeProduto)
                                vendas.append(qnt)
                                vendas.append(valor)
                                listaProdutosVendidos.append(produtosvendidos.copy())
                                listaVendas.append(vendas.copy())
                                print("Venda realizada")
                                print("Agora possui", cadProdutos[pos][3], " unidades de ", cadProdutos[pos][1])
                                vendas.clear()
                                produtos.clear()
                                mais = input("Gostaria de comprar mais produtos? (s/n):")
                            if mais == "s":
                                  fazerVenda()
                            elif mais == "n":
                              print("Ok, voltando...")
                            else:
                              print("OPÇÃO INVÁLIDA!")
                    elif confirm == "n":
                        print("Ok, voltando...")
                    else:
                      print("OPÇÃO INVÁLIDA!")
    else:
        print("Não foi encontrado este cliente")
    clientes.clear()

def mostrarVendas():
    i = 0
    soma = 0
    valor = 0
    listaVendas.sort()
    if (listaVendas == []):
        print("NÃO HÁ VENDAS AINDA!")
    else:
        print("\nVENDAS:\n")
        for umaVenda in listaVendas:
            if umaVenda[8] >= 0:
                valor = umaVenda[8]
                soma = soma + valor
            print("Código de produto:", umaVenda[0])
            print("Código do cliente:", umaVenda[1])
            print("Cliente:", umaVenda[2])
            print("Data:", umaVenda[3],"/",umaVenda[4],"/",umaVenda[5])
            print("Produto: ",umaVenda[6])
            print("Quantidade de produtos vendidos: ",umaVenda[7])
            print("Valor total: ",umaVenda[8])
            print("-------")
        print("\nO valor total das vendas é:",soma)

def mostraLeOpcoes():
    sair = False
    while (not sair):
        opcao = int(input(asOpcoes))
        if (opcao < 1 or opcao > 20):
            print("Opção inválida...")
        elif opcao == 1:
            mostraEstoque()
        elif opcao == 2:
            insereProduto()
        elif opcao == 4:
            insereFabricante()
        elif opcao == 5:
            removeFabricante()
        elif opcao == 3:
            removerProdutoNovo()
        elif opcao == 6:
            mostrarFabricante()
        elif opcao == 7:
            insereCliente()
        elif opcao == 9:
            mostrarCliente()
        elif opcao == 8:
            removeCliente()
        elif opcao == 10:
            fazerVenda()
        elif opcao == 11:
            mostrarVendas()
        elif opcao == 20:
            sair = True


# execucao comeca por aqui...
print("Sistema de mercadorias:")

mostraLeOpcoes()

print("Saindo...")
