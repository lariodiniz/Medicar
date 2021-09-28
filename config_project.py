from os import path, system, remove, mkdir
from os.path import isfile, isdir
import sys

def help():
    print('Ação não definida.')
    print('')
    print('Para usar esse script faça: python config_project.py AÇÃO')
    print('')
    print('Ações possiveis:')
    print('    - create_app')
    print('    - create_model')


def _cria_arquivo(arquivo):
    if not isfile(arquivo):
        criado = open(arquivo, 'w')
        criado.close()

def remove_arquivo(app, arq):
    print(f'   |--> Apagando arquivo {arq}.py')
    arquivo = f'{app}\\{arq}.py'
    if isfile(arquivo):
        remove(arquivo)

def cria_arquivos(path):
    arquivos = ['__init__.py']
    for arq in arquivos:
        arquivo = f'{path}\\{arq}'
        _cria_arquivo(arquivo)

def cria_pasta(app, arq):
    print(f'   |--> Criando a pasta {arq}')
    pasta = f'{app}\\{arq}'
    if not isdir(pasta):
        mkdir(pasta)
    cria_arquivos(pasta)
    
    

def config_arquivos(app, arq):
    print(f'  |--> Configurando {arq}.')
    remove_arquivo(app, arq)
    cria_pasta(app, arq)

def config_app(app):
    print(f'--> configurando as pastas de: {app}')
    arquivos = ['models','views','serializers', 'forms']
    if not 'tests' in app:
        arquivos.append('tests')

    for arquivo in arquivos:
        config_arquivos(app, arquivo)

def create_app(app):
    print(f'--> criando a aplicação: {app}')
    if not isdir(app):
        system(f'python manage.py startapp {app}')
    print(f'--> aplicação {app} criada.')
    
    config_app(app)
    
    #configurando teste
    config_app(f'{app}\\tests')


if __name__ in ('__main__'):
    if len(sys.argv) == 1:
        help()
    else:
        action = sys.argv[1]
        action = action.lower()
        if action == 'help':
            help()
        elif action == 'create_app':
            if len(sys.argv) != 3:
                print('Informe como segundo argumento o nome da aplicação')
            else:
                create_app(sys.argv[2])
        else:
            help()