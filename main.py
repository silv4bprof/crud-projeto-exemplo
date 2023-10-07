from utils import contar_contatos
from utils import ultimo_contato_cadastrado
from utils import cadastrar_contato
from utils import listar_contato
from utils import deletar_contato_por_id
from utils import buscar_contato_pelo_pome
from utils import atualizar_contato
from utils import resetar_arquivo
from utils import sair


def menu():
    voltar_menu_principal: str = 's'

    while voltar_menu_principal == 's':
        opcao = input(f'''
        {'=' * 64}
                    PROJETO AGENDA EM PYTHON (ARQUIVOS) - v.1           

        {contar_contatos()} CONTATOS CADASTRADOS\n
        ÚLTIMO CADASTRO:\n {ultimo_contato_cadastrado()}
        MENU:

        [1] CADASTRAR CONTATO       \t[5] ATUALIZAR CONTATO
        [2] LISTAR CONTATO          \t[6] RESETAR ARQUIVO
        [3] DELETAR CONTATO         \t[0] SAIR
        [4] BUSCAR CONTATO PELO NOME
        {'=' * 64}

        ESCOLHA UMA OPÇÃO: ''')

        if opcao == '1':
            cadastrar_contato()
        elif opcao == '2':
            listar_contato()
        elif opcao == '3':
            deletar_contato_por_id()
        elif opcao == '4':
            buscar_contato_pelo_pome()
        elif opcao == '5':
            atualizar_contato()
        elif opcao == '6':
            resetar_arquivo()
        elif opcao == '0':
            sair()
        else:
            print('\t\tOpção inválida!')
            voltar_menu_principal = input('\t\tDeseja voltar so menu principal? (s/n)').lower()


if __name__ == '__main__':
    menu()
