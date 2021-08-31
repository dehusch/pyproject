from lib.interface import *
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        print('Opcao 2')
    elif resposta == 3:
        print('Saindo do programa')
        break
    else:
        print('Erro! Digite uma opção valida!')
