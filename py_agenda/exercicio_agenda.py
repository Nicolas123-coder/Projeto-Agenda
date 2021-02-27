#exercicio_agenda

lista_nomes = []

def menu ():
    print('inserir um nome na lista ........... 1')
    print('buscar um nome ..................... 2')
    print('remover um nome .................... 3')
    print('listar nomes em ordem crescente..... 4')
    print('listar nomes em ordem decrescente... 5')
    print('SAIR................................ 6')
    
    escolha = int(input('Digite sua escolha = '))
    
    while escolha < 1 or escolha > 6 :
        escolha = int(input('Digite sua escolha = '))
    
    return escolha
    
def inserirNome ():                                                                                    #add um nome na lista
    print()
    
    nome = str(input('Digite o nome a ser inserido na agenda = '))
    lista_nomes.append(nome)
    print(lista_nomes)
    print()

def buscarNome ():                                                                                          #ve se tem um nome na lista
    print()
    global nome_busca
    
    nome_busca = str(input('Digite o nome a ser procurado na agenda = '))
    print()
    flag_nome = 0
    for i in range (len(lista_nomes)) :
        if lista_nomes [i] == nome_busca :
            flag_nome = 1
            break
        
    return flag_nome


def removerNome ():                                                                                     #remove um nome da lista 
    print()
    
    nome_remover = str(input('Digite o nome para ser removido da lista = '))
    if nome_remover in lista_nomes : 
        indice = lista_nomes.index(nome_remover)
        del lista_nomes[indice]
        print('*'*30)
        print('Nome removido = ', nome_remover)
        print('*'*30)

    else :
        print('Digite um nome válido ! ')
        print('-'*30)
        print()

def listarOrdemCrescente ():                                     #listar de A a Z
    print()
    lista_nomes.sort()
    print(lista_nomes)

def listarOrdemDecrescente ():                                   #listar de Z a A 
    print()
    lista_nomes.sort(reverse=True)
    print(lista_nomes)

def main ():   
    opcao = 0
    
    while opcao != 6 :
        
        opcao = menu()
        
        if opcao == 1 :
            inserirNome()
        
        elif opcao == 2 :
            encontrou_flag = buscarNome()
            
            print('*' *30)

            if encontrou_flag == 1 :
                print('Nome encontrado na lista = ', nome_busca)
            
            else :
                print('Nome não encontrado na lista = ', nome_busca)
            
            print('*' *30)

        elif opcao == 3 :
            removerNome()
        
        elif opcao == 4 :
            listarOrdemCrescente()
        
        elif opcao == 5 :
            listarOrdemDecrescente()
        
        
main() 