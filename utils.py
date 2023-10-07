from time import sleep
from classes.contato import Contato
from classes.arquivo import Arquivo


def atualizar_contato():
    id_contato = int(input('\t\tDigite o id contato que vai ser atualizado: '))
    deletar_contato_por_id(id_contato)
    listar_contato()

    agenda = open('agenda.txt', 'r', encoding='utf-8')
    aux, aux2 = [], []

    for i in agenda:
        aux.append(i)

    for i in range(0, len(aux)):
        id_temp = int(aux[i].split(";")[0])

        if id_contato != id_temp:
            aux2.append(aux[i])

    agenda.close()
    agenda = open('agenda.txt', 'w', encoding='utf-8')

    for i in aux2:
        agenda.write(i)

    # transformar essas atribuições em um objeto
    id_contato = id_contato
    nome = input('\t\tEscreva o novo nome do contato: ')
    telefone = input('\t\tEscreva o novo telefone do contato: ')
    email = input('\t\tEscreva o novo email do contato: ')

    try:
        agenda = open('agenda.txt', 'a', encoding='utf-8')
        dados = f'{id_contato};{nome};{telefone};{email}'
        agenda.write(dados)
        agenda.close()
        print('\t\tContato atualizado com sucesso')
    except FileNotFoundError as e:
        print(f'\t\tOcorreu um erro ao salvar contato!\n{e}')


def cadastrar_contato():
    id_contato = contar_contatos() + 1
    print(f'\t\tIdentificador do novo contato: {id_contato}')
    nome = input('\t\tEscreva o nome do contato: ')
    telefone = input('\t\tEscreva o telefone do contato: ')
    email = input('\t\tEscreva o email do contato: ')

    novo_contato = Contato(
        id_contato,
        nome,
        telefone,
        email
    )

    # transformar este bloco de código em um método a parte que receberá como parâmetro
    # um objeto do tipo Contato

    try:
        arquivo = Arquivo('agenda.txt', 'a')
        agenda = arquivo.abrir_arquivo()
        dados = (f'{novo_contato.get_id_contato()};{novo_contato.get_nome()};'
                 f'{novo_contato.get_telefone()};{novo_contato.get_email()}\n')

        agenda.write(dados)
        arquivo.fechar_arquivo(agenda)
    except FileNotFoundError as e:
        print(f'\t\tArquivo de agenda não foi encontrado!\n{e}')
    except IOError as e:
        print(f'\t\tOcorreu um erro de entrada de dados!\n{e}')
    except Exception as e:
        print(f'\t\tOcorreu um erro ao salvar contato!\n{e}')
    else:
        print('\t\tContato cadastrado com sucesso\n')


def listar_contato():
    agenda = open('agenda.txt', 'r', encoding='utf-8')

    if contar_contatos() > 0:
        print('\n\t\tListando contatos:\n'.upper())
        for contato in agenda:
            exibe_contato(contato)
    else:
        print('\t\tNão existem contatos cadastrados')

    agenda.close()


def deletar_contato():
    nome_deletado = input('\t\tDigite o nome para ser deletado: ').lower()
    agenda = open('agenda.txt', 'r', encoding='utf-8')
    aux, aux2 = [], []

    for i in agenda:
        aux.append(i)

    for i in range(0, len(aux)):
        if nome_deletado not in aux[i].lower():
            aux2.append(aux[i])

    agenda.close()
    agenda = open('agenda.txt', 'w', encoding='utf-8')

    for i in aux2:
        agenda.write(aux[i])

    agenda.close()

    print('\t\tContato removido com sucesso!')
    listar_contato()


def deletar_contato_por_id(id_deletado=-1):
    if id_deletado == -1:
        id_deletado = input('\t\tDigite o ID para ser deletado: ')
    else:
        id_deletado = id_deletado

    agenda = open('agenda.txt', 'r', encoding='utf-8')
    aux, aux2 = [], []

    for i in agenda:
        aux.append(i)

    for i in range(0, len(aux)):
        id_temp = aux[i].split(";")[0]

        if id_deletado != id_temp:
            aux2.append(aux[i])

    agenda.close()
    agenda = open('agenda.txt', 'w', encoding='utf-8')

    for j in aux2:
        agenda.write(j)

    agenda.close()

    print('\t\tContato removido com sucesso!')


def buscar_contato_pelo_pome():
    nome = input('\t\tDigite o nome a ser procurado: ')
    agenda = open('agenda.txt', 'r', encoding='utf-8')

    for elemento in agenda:
        if nome.lower() in elemento.split(';')[1].lower():
            exibe_contato(elemento)

    agenda.close()


def ultimo_contato_cadastrado():
    try:
        with(open('agenda.txt', 'r', encoding='utf-8')) as contatos:
            ultimo_contato = contatos.readlines()[-1]
            ultimo_contato_txt = f'\t\tId: {ultimo_contato.split(";")[0]}' \
                                 f'\n\t\tNome: {ultimo_contato.split(";")[1]}' \
                                 f'\n\t\tTelefone: {ultimo_contato.split(";")[2]}' \
                                 f'\n\t\tEmail: {ultimo_contato.split(";")[3]}'
            return ultimo_contato_txt
    except IndexError:
        return '\t\tNenhum contato cadastrado até o momento'


def contar_contatos() -> int:
    if verifica_arquivo_existente('agenda.txt'):
        num_contatos = 0

        with(open('agenda.txt', 'r', encoding='utf-8')) as contatos:
            linhas = contatos.readlines()

        # Se a variável de iteração do for (i) não for ser usada na iteração, usar um underscore ao invés.
        for _ in linhas:
            num_contatos += 1

        return num_contatos
    else:
        print('\t\tNão existem contatos ...')
        return 0


def verifica_arquivo_existente(arquivo: str) -> bool:
    # se arquivo não existir, retorne False
    # caso contrário, retorne True

    try:
        agenda = open('agenda.txt', encoding='utf-8')  # 'r' pé o modo padrão de abertura de arquivo
        agenda.close()
        return True

    except FileNotFoundError:
        print(f'Arquivo {arquivo} não existe :/')
        return False


def exibe_contato(contato):
    print(f'\t\tId: {contato.split(";")[0]} '
          f'Nome: {contato.split(";")[1]} '
          f'Telefone: {contato.split(";")[2]} '
          f'Email: {contato.split(";")[3]}', end=''
          )


def resetar_arquivo():
    f = open('agenda.txt', 'r+', encoding='utf-8')
    f.truncate(0)  # need '0' when using r+


def sair():
    print('\t\tSaindo ...')
    sleep(1)
    exit()
